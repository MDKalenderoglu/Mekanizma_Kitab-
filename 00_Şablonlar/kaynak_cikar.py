#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kaynak_cikar.py — doğrulama materyalinden aranabilir metin çıkarır.

EPUB ve PDF'i düz metne çevirip `_metin/` altına yazar. Amaç bağlama tümünü
yüklemek DEĞİL, `ara.py` ile hedefli arama yapabilmektir.

  python3 00_Şablonlar/kaynak_cikar.py            # kaynak_pdf/ altındaki her şeyi işler
  python3 00_Şablonlar/kaynak_cikar.py dosya.epub # tek dosya

Çıktı: _metin/<dosya>.txt  — her parçanın başına `[[kaynak | konum]]` işareti
konur; böylece bulunan bir alıntı kütüğe sayfa/bölüm bilgisiyle kaydedilebilir.

Bağımlılık: EPUB için yok (stdlib). PDF için `pypdf`.
İkisi de telifli olabilir → `_metin/` ve `kaynak_pdf/` .gitignore'dadır.
"""
import os
import re
import sys
import glob
import html
import zipfile
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "kaynak_pdf")
OUT = os.path.join(ROOT, "_metin")

SKIP_TAGS = {"script", "style", "head", "svg"}


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.buf = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self._skip += 1
        elif tag in ("p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"):
            self.buf.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS and self._skip:
            self._skip -= 1

    def handle_data(self, d):
        if not self._skip:
            self.buf.append(d)

    def text(self):
        t = "".join(self.buf)
        t = re.sub(r"[ \t\xa0]+", " ", t)
        t = re.sub(r"\n\s*\n\s*\n+", "\n\n", t)
        return "\n".join(ln.strip() for ln in t.splitlines()).strip()


def read_epub(path):
    """EPUB = ZIP + XHTML. Okuma sırası spine'dan alınır."""
    parts = []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        # OPF dosyasını bul (spine sırası için)
        opf = next((n for n in names if n.lower().endswith(".opf")), None)
        order = []
        if opf:
            raw = z.read(opf).decode("utf-8", "ignore")
            base = os.path.dirname(opf)
            ids = dict(re.findall(r'<item\b[^>]*id="([^"]+)"[^>]*href="([^"]+)"', raw))
            ids.update({k: v for v, k in re.findall(r'<item\b[^>]*href="([^"]+)"[^>]*id="([^"]+)"', raw)})
            for idref in re.findall(r'<itemref\b[^>]*idref="([^"]+)"', raw):
                href = ids.get(idref)
                if href:
                    p = os.path.normpath(os.path.join(base, html.unescape(href))).replace("\\", "/")
                    if p in names:
                        order.append(p)
        if not order:
            order = [n for n in names if n.lower().endswith((".xhtml", ".html", ".htm"))]
        for n in order:
            try:
                t = Text()
                t.feed(z.read(n).decode("utf-8", "ignore"))
                body = t.text()
            except Exception as e:
                body = f"[ÇÖZÜMLENEMEDİ: {e}]"
            if body.strip():
                parts.append((n, body))
    return parts


def read_pdf(path):
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("HATA: PDF için pypdf gerekli → python3 -m pip install --user pypdf")
    r = PdfReader(path)
    out = []
    for i, page in enumerate(r.pages, 1):
        try:
            body = page.extract_text() or ""
        except Exception as e:
            body = f"[ÇÖZÜMLENEMEDİ: {e}]"
        if body.strip():
            out.append((f"s.{i}", body.strip()))
    return out


def process(path):
    name = os.path.basename(path)
    ext = os.path.splitext(name)[1].lower()
    if ext == ".epub":
        parts = read_epub(path)
    elif ext == ".pdf":
        parts = read_pdf(path)
    else:
        print(f"  ⏭  atlandı (desteklenmeyen tür): {name}")
        return None
    if not parts:
        print(f"  ⚠️  METİN ÇIKMADI: {name} — büyük olasılıkla TARANMIŞ (görüntü) dosya; OCR gerekir.")
        return None
    os.makedirs(OUT, exist_ok=True)
    dst = os.path.join(OUT, os.path.splitext(name)[0] + ".txt")
    with open(dst, "w", encoding="utf-8") as fh:
        for loc, body in parts:
            fh.write(f"\n[[{name} | {loc}]]\n{body}\n")
    chars = sum(len(b) for _, b in parts)
    print(f"  ✓ {name}: {len(parts)} parça · {chars:,} karakter → {os.path.relpath(dst, ROOT)}")
    return dst


def main():
    args = sys.argv[1:]
    files = args if args else sorted(
        glob.glob(os.path.join(SRC, "*.epub")) + glob.glob(os.path.join(SRC, "*.pdf"))
    )
    if not files:
        sys.exit(f"kaynak_pdf/ içinde .epub veya .pdf yok.\nDosyaları şuraya koy: {SRC}")
    print(f"{len(files)} dosya işleniyor…")
    for f in files:
        process(f)
    print("\nArama için:  python3 00_Şablonlar/ara.py \"aranacak ifade\"")


if __name__ == "__main__":
    main()
