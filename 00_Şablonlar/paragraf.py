# -*- coding: utf-8 -*-
"""Verilen çapa ifadesini içeren paragrafı, bölüm/başlık/satır bilgisiyle döndürür."""
import re, sys, os, glob, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def dosya_bul(no):
    g = glob.glob(os.path.join(ROOT, f"Bölüm_{no}_*.md"))
    if not g:
        raise SystemExit(f"Bölüm {no} bulunamadı")
    return g[0]


def paragraf_bul(no, capa):
    yol = dosya_bul(no)
    satirlar = open(yol, encoding="utf-8").read().split("\n")
    # çapayı içeren satırı bul
    hit = None
    for i, s in enumerate(satirlar):
        if capa in s:
            hit = i
            break
    if hit is None:
        return None
    # paragraf sınırları: boş satırlar
    bas = hit
    while bas > 0 and satirlar[bas - 1].strip():
        bas -= 1
    son = hit
    while son < len(satirlar) - 1 and satirlar[son + 1].strip():
        son += 1
    # en yakın üst başlık
    baslik = ""
    for j in range(bas, -1, -1):
        m = re.match(r"^(#{2,4})\s+(.*)", satirlar[j])
        if m:
            baslik = m.group(2).strip()
            break
    return dict(dosya=os.path.basename(yol), satir=hit + 1, baslik=baslik,
                metin="\n".join(satirlar[bas:son + 1]).strip())


if __name__ == "__main__":
    if sys.argv[1] == "--json":
        items = json.load(open(sys.argv[2], encoding="utf-8"))
        eksik = []
        for it in items:
            r = paragraf_bul(it["b"], it["capa"])
            if r is None:
                eksik.append(it["id"])
            else:
                it["bulundu"] = r
        json.dump(items, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("EKSİK:", eksik if eksik else "yok")
    else:
        r = paragraf_bul(sys.argv[1], sys.argv[2])
        print(json.dumps(r, ensure_ascii=False, indent=1) if r else "BULUNAMADI")
