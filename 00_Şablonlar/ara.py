#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ara.py — çıkarılmış doğrulama materyalinde hedefli arama.

Amaç: telifli metnin tamamını bağlama yüklemeden, yalnızca denetlenen iddiayla
ilgili paragrafı görmek.

  python3 00_Şablonlar/ara.py "nonsense-mediated decay" "50 nucleotide"
  python3 00_Şablonlar/ara.py -c 600 haploinsufficiency      # daha geniş bağlam
  python3 00_Şablonlar/ara.py -n 3 "PMP22"                   # en fazla 3 eşleşme

Birden çok terim verilirse HEPSİNİN aynı paragrafta geçtiği yerler öncelenir.
Her sonuç, kaynak dosya ve konum (sayfa/bölüm) işaretiyle birlikte basılır —
bulunan alıntı doğrudan Dogrulama_Kutugu.md'ye kaydedilebilir.
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MET = os.path.join(ROOT, "_metin")


def main():
    args = sys.argv[1:]
    ctx, limit = 320, 8
    while args and args[0] in ("-c", "-n"):
        flag = args.pop(0)
        val = int(args.pop(0))
        if flag == "-c":
            ctx = val
        else:
            limit = val
    if not args:
        sys.exit(__doc__)
    terms = [a.lower() for a in args]

    files = sorted(glob.glob(os.path.join(MET, "*.txt")))
    if not files:
        sys.exit("_metin/ boş. Önce: python3 00_Şablonlar/kaynak_cikar.py")

    hits = []
    for f in files:
        txt = open(f, encoding="utf-8").read()
        # konum işaretlerinin indeksini çıkar
        marks = [(m.start(), m.group(1)) for m in re.finditer(r"\[\[([^\]]+)\]\]", txt)]

        def where(pos):
            loc = "?"
            for s, lab in marks:
                if s <= pos:
                    loc = lab
                else:
                    break
            return loc

        low = txt.lower()
        for m in re.finditer(re.escape(terms[0]), low):
            a, b = max(0, m.start() - ctx), min(len(txt), m.end() + ctx)
            frag = txt[a:b]
            score = sum(1 for t in terms if t in frag.lower())
            hits.append((score, where(m.start()), frag.replace("\n", " ").strip()))

    if not hits:
        print(f"'{args[0]}' için eşleşme yok.")
        return
    hits.sort(key=lambda x: -x[0])
    print(f"{len(hits)} eşleşme; en ilgili {min(limit, len(hits))} tanesi:\n")
    for score, loc, frag in hits[:limit]:
        tag = f"[{score}/{len(terms)} terim]" if len(terms) > 1 else ""
        print(f"── {loc} {tag}\n   …{frag}…\n")


if __name__ == "__main__":
    main()
