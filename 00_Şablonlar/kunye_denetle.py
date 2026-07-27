#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kunye_denetle.py — bölüm kaynakçalarındaki künyeleri NCBI'dan indirip programatik eşleştirir.

Amaç: "kaynak uydurma" ve künye kayması riskini modele okutmadan, **veriyi indirip
karşılaştırarak** denetlemek (Dogrulama_Protokolu.md §2).

  python3 00_Şablonlar/kunye_denetle.py Bölüm_11_*.md Bölüm_12_*.md
  python3 00_Şablonlar/kunye_denetle.py            # tüm bölümler

Her kaynak satırından PMID, yıl, dergi cilt(sayı):sayfa çıkarılır; NCBI esummary
ile karşılaştırılır. Uyuşmazlıklar ⚠️ ile listelenir.
"""
import os
import re
import sys
import glob
import json
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id="


def esummary(pmids):
    """PMID listesi için NCBI esummary kayıtlarını indirir (200'lük gruplar)."""
    kayit = {}
    for i in range(0, len(pmids), 200):
        grup = pmids[i:i + 200]
        with urllib.request.urlopen(API + ",".join(grup), timeout=60) as r:
            veri = json.load(r)
        kayit.update({k: v for k, v in veri.get("result", {}).items() if k != "uids"})
        time.sleep(0.4)
    return kayit


def sayfa_normalize(s):
    """'405-24' ve '405–424' aynı sayılsın diye son sayfayı tam hâle getirir."""
    s = (s or "").replace("–", "-").replace("—", "-").strip()
    m = re.match(r"^(\d+)-(\d+)$", s)
    if not m:
        return s
    bas, son = m.groups()
    if len(son) < len(bas):
        son = bas[:len(bas) - len(son)] + son
    return f"{bas}-{son}"


def bolum_kaynaklari(yol):
    """Kaynakça satırlarından (PMID, yıl, cilt, sayı, sayfa) çıkarır."""
    out = []
    for satir in open(yol, encoding="utf-8"):
        m = re.search(r"PMID:\s*\*{0,2}\s*(\d+)", satir)
        if not m:
            continue
        pmid = m.group(1)
        yil = re.search(r"\((\d{4})\)", satir)
        cilt = sayi = sayfa = None
        # Karşılaşılan biçimler: 17(5):405–424 · 61:437–455 · 12(1):3 · 97(3–4):639–666
        # 6(10):e1001154 · 115(24):E5516–E5525 · 26(22):e202500330 · 7(7) [sayfasız]
        kalip = (r"(?<![\d.])(\d{1,4}[A-Z]?)"                  # cilt (167A gibi harfli olabilir)
                 r"(?:\(([A-Za-z]?\d+(?:[–\-]\d+)?)\))?"       # (sayı) — D1 / 3–4 olabilir
                 r"(?::([A-Za-z]?\d+(?:[–\-][A-Za-z]?\d+)?(?:\.e\d+)?))?")  # :sayfa/madde no
        for mm in re.finditer(kalip, satir.split("**PMID")[0]):
            if mm.group(2) or mm.group(3):                    # en az biri varsa künye sayılır
                cilt, sayi, sayfa = mm.group(1), mm.group(2), mm.group(3)
        out.append(dict(pmid=pmid, yil=yil.group(1) if yil else None,
                        cilt=cilt, sayi=sayi, sayfa=sayfa, satir=satir.strip()))
    return out


def main():
    dosyalar = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "Bölüm_[0-9]*.md")))
    kaynaklar = []
    for f in dosyalar:
        for k in bolum_kaynaklari(f):
            k["dosya"] = os.path.basename(f)
            kaynaklar.append(k)
    if not kaynaklar:
        sys.exit("PMID içeren kaynak satırı bulunamadı.")

    pmidler = sorted({k["pmid"] for k in kaynaklar})
    print(f"{len(kaynaklar)} kaynak satırı · {len(pmidler)} benzersiz PMID indiriliyor…\n")
    kayit = esummary(pmidler)

    uyusmaz, eksik = [], []
    for k in kaynaklar:
        r = kayit.get(k["pmid"])
        if not r or r.get("error"):
            eksik.append(k)
            continue
        sorun = []
        # yıl: esummary pubdate ya da epubdate
        yillar = {y for y in re.findall(r"\d{4}", (r.get("pubdate", "") + " " + r.get("epubdate", "")))}
        if k["yil"] and yillar and k["yil"] not in yillar:
            sorun.append(f"yıl {k['yil']} ≠ NCBI {sorted(yillar)}")
        if k["cilt"] and r.get("volume") and k["cilt"] != r["volume"]:
            sorun.append(f"cilt {k['cilt']} ≠ {r['volume']}")
        if k["sayi"] and r.get("issue") and k["sayi"].replace("–","-") != r["issue"].replace("–","-"):
            sorun.append(f"sayı {k['sayi']} ≠ {r['issue']}")
        if k["sayfa"] and r.get("pages"):
            a, b = sayfa_normalize(k["sayfa"]), sayfa_normalize(r["pages"])
            if a != b:
                sorun.append(f"sayfa {k['sayfa']} ≠ {r['pages']}")
        if sorun:
            uyusmaz.append((k, r, sorun))

    print(f"✅ Sorunsuz: {len(kaynaklar) - len(uyusmaz) - len(eksik)}")
    if eksik:
        print(f"\n❌ NCBI'da BULUNAMAYAN PMID ({len(eksik)}):")
        for k in eksik:
            print(f"   {k['dosya']} · PMID {k['pmid']}\n     {k['satir'][:150]}")
    if uyusmaz:
        print(f"\n⚠️  KÜNYE UYUŞMAZLIĞI ({len(uyusmaz)}):")
        for k, r, sorun in uyusmaz:
            print(f"   {k['dosya']} · PMID {k['pmid']} — {'; '.join(sorun)}")
            print(f"     NCBI: {r.get('source')} {r.get('volume')}({r.get('issue')}):{r.get('pages')} · {r.get('pubdate')}")
            print(f"     kitap: {k['satir'][:150]}")
    if not uyusmaz and not eksik:
        print("Tüm künyeler NCBI kayıtlarıyla uyumlu.")


if __name__ == "__main__":
    main()
