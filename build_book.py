#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_book.py — Mekanizma Kitabı tek-dosya HTML kitap üreticisi.

Ne yapar:
  • Önsöz.md varsa kitabın başına (içindekilerden sonra) koyar.
  • Bölüm_NN_*.md dosyalarını (Bölüm_00 hariç) sırayla okur.
  • Bölüm kaynakçalarından PMID'ye göre tekilleştirilmiş TOPLU KAYNAKÇA üretir.
  • Markdown → HTML (tablolar, kod, başlık id'leri, dipnotlar).
  • Mermaid kod bloklarını <pre class="mermaid"> olarak gömer (offline render).
  • assets/*.svg görsellerini doğrudan HTML içine GÖMER (img değil, inline SVG)
    → çıktı tek dosya, paylaşınca görseller kopmaz.
  • mermaid.min.js'i inline gömer → internet OLMADAN diyagramlar render olur.
  • Kapak + otomatik içindekiler + textbook CSS + yazdır→PDF desteği ekler.

Kullanım:
  python3 build_book.py
Çıktı:
  Genetik_Hastalık_Mekanizmaları.html  (çift tıkla aç; Yazdır→PDF ile kitap PDF'i)
"""
import re
import sys
import html
import glob
import os
import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")
MERMAID_JS = os.path.join(ROOT, "build_assets", "mermaid.min.js")
OUT = os.path.join(ROOT, "Genetik_Hastalık_Mekanizmaları.html")

BOOK_TITLE = "Genetik Hastalık Mekanizmaları"
BOOK_SUBTITLE = "Mekanizmadan Varyant Yorumuna — Kapsamlı Akademik Ders Kitabı"

try:
    import markdown
except ImportError:
    sys.exit("HATA: 'markdown' kurulu değil. Çalıştır: python3 -m pip install --user markdown")


def chapter_files():
    files = glob.glob(os.path.join(ROOT, "Bölüm_*.md"))
    out = []
    for f in files:
        base = os.path.basename(f)
        m = re.match(r"Bölüm_(\d+)_", base)
        if not m:
            continue
        n = int(m.group(1))
        if n == 0:  # Bölüm_00 = içindekiler/ilerleme (kitap gövdesine girmez)
            continue
        out.append((n, f))
    out.sort()
    return out


def extract_title(md_text, fallback):
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def protect_blocks(md_text):
    """Mermaid bloklarını ve SVG görsellerini token'la koru; markdown bunlara dokunmasın."""
    placeholders = {}

    # 1) Mermaid kod blokları
    def repl_mermaid(m):
        key = f"@@MERMAID_{len(placeholders)}@@"
        code = html.escape(m.group(1))  # & < > kaçışı → textContent doğru okunur
        placeholders[key] = f'<div class="mermaid-wrap"><pre class="mermaid">{code}</pre></div>'
        return key

    md_text = re.sub(r"```mermaid\s*\n(.*?)```", repl_mermaid, md_text, flags=re.DOTALL)

    # 2) SVG görselleri: ![alt](assets/x.svg)  → inline <figure><svg>…</svg><figcaption>
    def repl_img(m):
        alt = m.group(1).strip()
        path = m.group(2).strip()
        svg_path = os.path.join(ROOT, path)
        key = f"@@FIG_{len(placeholders)}@@"
        if os.path.exists(svg_path):
            with open(svg_path, encoding="utf-8") as fh:
                svg = fh.read()
            # XML bildirimi varsa temizle
            svg = re.sub(r"<\?xml.*?\?>", "", svg, flags=re.DOTALL).strip()
            cap = html.escape(alt)
            placeholders[key] = (
                f'<figure class="svg-fig">{svg}'
                f'<figcaption>{cap}</figcaption></figure>'
            )
        else:
            placeholders[key] = f'<p class="missing">[Görsel bulunamadı: {html.escape(path)}]</p>'
        return key

    md_text = re.sub(r"!\[([^\]]*)\]\((assets/[^)]+\.svg)\)", repl_img, md_text)
    return md_text, placeholders


def restore_blocks(html_text, placeholders):
    for key, val in placeholders.items():
        html_text = html_text.replace(f"<p>{key}</p>", val)  # paragrafa sarılmışsa
        html_text = html_text.replace(key, val)
    return html_text


def convert_chapter(md_text):
    md_text, ph = protect_blocks(md_text)
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc", "footnotes"],
        output_format="html5",
    )
    body = md.convert(md_text)
    body = restore_blocks(body, ph)
    return body


CSS = r"""
:root{
  --ink:#1a2b4a; --body:#222; --muted:#5b6675; --rule:#d8dee6;
  --accent:#2471a3; --accent-soft:#eef6fb;
  --dd:#8e44ad; --dd-bg:#f6eefb;       /* deep-dive */
  --warn:#c0392b; --warn-bg:#fdecea;   /* sık hata */
  --note:#2980b9; --note-bg:#eaf4fb;   /* klinikte dikkat */
}
*{box-sizing:border-box}
html{font-size:16px}
body{
  font-family:"Iowan Old Style","Palatino Linotype",Georgia,"Times New Roman",serif;
  color:var(--body); line-height:1.62; margin:0;
  background:#f4f6f9;
}
.page{max-width:860px;margin:0 auto;padding:48px 56px;background:#fff;
  box-shadow:0 1px 4px rgba(0,0,0,.06);}
h1,h2,h3,h4{font-family:"Helvetica Neue",Arial,sans-serif;color:var(--ink);line-height:1.25;}
h1{font-size:2rem;border-bottom:3px solid var(--accent);padding-bottom:.3em;margin-top:0;}
h2{font-size:1.45rem;margin-top:1.8em;border-bottom:1px solid var(--rule);padding-bottom:.2em;}
h3{font-size:1.15rem;margin-top:1.4em;color:var(--accent);}
h4{font-size:1.02rem;margin-top:1.1em;}
p{margin:.7em 0;}
a{color:var(--accent);text-decoration:none;}
a:hover{text-decoration:underline;}
code{font-family:"SF Mono",Menlo,Consolas,monospace;font-size:.86em;
  background:#f1f3f6;padding:.1em .35em;border-radius:4px;}
pre code{background:none;padding:0;}
/* Tablolar */
table{border-collapse:collapse;width:100%;margin:1.1em 0;font-size:.92rem;
  font-family:"Helvetica Neue",Arial,sans-serif;}
th,td{border:1px solid var(--rule);padding:.5em .65em;text-align:left;vertical-align:top;}
thead th{background:var(--ink);color:#fff;font-weight:600;}
tbody tr:nth-child(even){background:#f7f9fb;}
/* Blockquote tabanlı kutular */
blockquote{margin:1.1em 0;padding:.8em 1.1em;border-left:5px solid var(--accent);
  background:var(--accent-soft);border-radius:0 6px 6px 0;}
blockquote p:first-child{margin-top:0;} blockquote p:last-child{margin-bottom:0;}
/* Kutu renk varyantları (emoji ipucuyla) */
blockquote:has(strong:first-child){}
/* Görseller */
figure.svg-fig{margin:1.4em 0;text-align:center;page-break-inside:avoid;}
figure.svg-fig svg{max-width:100%;height:auto;border:1px solid var(--rule);border-radius:6px;}
figure.svg-fig figcaption{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.85rem;
  color:var(--muted);margin-top:.5em;font-style:italic;}
.mermaid-wrap{margin:1.4em 0;text-align:center;page-break-inside:avoid;}
pre.mermaid{background:#fff;}
.missing{color:var(--warn);font-style:italic;}
hr{border:none;border-top:1px solid var(--rule);margin:2em 0;}
/* Kapak */
.cover{min-height:88vh;display:flex;flex-direction:column;justify-content:center;
  text-align:center;page-break-after:always;}
.cover .big{font-family:"Helvetica Neue",Arial,sans-serif;font-size:3rem;font-weight:800;
  color:var(--ink);line-height:1.1;margin:0 0 .3em;}
.cover .sub{font-size:1.2rem;color:var(--muted);max-width:620px;margin:0 auto 2em;}
.cover .meta{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.95rem;color:var(--muted);}
.cover .rule{width:80px;height:4px;background:var(--accent);margin:1.4em auto;}
/* İçindekiler */
.toc{page-break-after:always;}
.toc h2{border:none;}
.toc ol{font-family:"Helvetica Neue",Arial,sans-serif;font-size:1.02rem;line-height:2;
  list-style:none;padding-left:0;counter-reset:ch;}
.toc ol li{border-bottom:1px dotted var(--rule);padding:.1em 0;}
.toc ol li.plain{font-weight:700;}
.toc ol.front{margin-bottom:.6em;}
.toc ol.back{margin-top:.6em;}
.chapter{page-break-before:always;}
/* Yazdırma / PDF */
@media print{
  body{background:#fff;}
  .page{box-shadow:none;max-width:none;padding:0 12mm;}
  h2,h3,h4{page-break-after:avoid;}
  table,figure,blockquote,.mermaid-wrap{page-break-inside:avoid;}
  @page{margin:18mm 14mm;}
}
"""


def collect_bibliography(chapters):
    """Bölüm kaynakçalarını PMID'ye göre tekilleştirip toplu kaynakça üretir."""
    seen = {}  # pmid -> (authors, rest)
    used = {}  # pmid -> set(bölüm no)
    for n, f in chapters:
        with open(f, encoding="utf-8") as fh:
            txt = fh.read()
        for line in txt.splitlines():
            m = re.match(r"^\d+\.\s+\*\*(.+?)\*\*\s*(.*?\*\*PMID:\s*(\d+)\*\*[^—]*)", line)
            if not m:
                continue
            au, rest, pmid = m.group(1).strip(), m.group(2).strip().rstrip(" —"), m.group(3)
            seen.setdefault(pmid, (au, rest))
            used.setdefault(pmid, set()).add(n)

    def sortkey(pmid):
        au = seen[pmid][0]
        return (au.split()[0].lower(), au)

    rows = []
    for i, pmid in enumerate(sorted(seen, key=sortkey), 1):
        au, rest = seen[pmid]
        chs = ", ".join(str(x) for x in sorted(used[pmid]))
        rows.append(f"{i}. **{au}** {rest} · *Bölüm: {chs}*")
    return rows, len(seen)


def build():
    chapters = chapter_files()
    if not chapters:
        sys.exit("HATA: Bölüm_NN_*.md bulunamadı.")

    with open(MERMAID_JS, encoding="utf-8") as fh:
        mermaid_js = fh.read()

    today = datetime.date.today().strftime("%d.%m.%Y")
    toc_items, bodies = [], []
    for n, f in chapters:
        with open(f, encoding="utf-8") as fh:
            md_text = fh.read()
        title = extract_title(md_text, os.path.basename(f))
        anchor = f"bolum-{n}"
        toc_items.append(f'<li><a href="#{anchor}">{html.escape(title)}</a></li>')
        body = convert_chapter(md_text)
        bodies.append(f'<section class="chapter" id="{anchor}">{body}</section>')

    # Toplu kaynakça
    bib_rows, bib_n = collect_bibliography(chapters)
    bib_md = (
        "# Toplu Kaynakça\n\n"
        "> Bu liste, bölüm kaynakçalarının PMID'ye göre tekilleştirilmiş birleşimidir; "
        "her kaynağın sonunda kullanıldığı bölümler belirtilmiştir. "
        "Bibliyografik veriler PubMed üzerinden doğrulanmıştır.\n\n" + "\n\n".join(bib_rows) + "\n"
    )
    bodies.append(f'<section class="chapter" id="toplu-kaynakca">{convert_chapter(bib_md)}</section>')

    # Önsöz (varsa)
    front = ""
    onsoz_path = os.path.join(ROOT, "Önsöz.md")
    if os.path.exists(onsoz_path):
        with open(onsoz_path, encoding="utf-8") as fh:
            front = f'<section class="chapter" id="onsoz">{convert_chapter(fh.read())}</section>'

    n_fig = len(glob.glob(os.path.join(ASSETS, "*.svg")))
    cover = f"""
    <section class="cover">
      <div class="big">{html.escape(BOOK_TITLE)}</div>
      <div class="rule"></div>
      <div class="sub">{html.escape(BOOK_SUBTITLE)}</div>
      <div class="meta">{len(chapters)} bölüm · {n_fig} şekil · {bib_n} doğrulanmış kaynak<br>
      Sürüm taslağı · {today}</div>
    </section>"""

    toc_extra = ('<li class="plain"><a href="#onsoz">Önsöz — Bu kitap neden yazıldı, nasıl okunmalı?</a></li>'
                 if front else "")
    toc = f"""
    <section class="toc">
      <h2>İçindekiler</h2>
      <ol class="front">{toc_extra}</ol>
      <ol>{''.join(toc_items)}</ol>
      <ol class="back"><li class="plain"><a href="#toplu-kaynakca">Toplu Kaynakça ({bib_n} kaynak)</a></li></ol>
    </section>"""

    doc = f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(BOOK_TITLE)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="page">
{cover}
{toc}
{front}
{''.join(bodies)}
</div>
<script>{mermaid_js}</script>
<script>
  mermaid.initialize({{ startOnLoad: true, theme: "neutral", securityLevel: "loose",
    flowchart: {{ htmlLabels: true, useMaxWidth: true }} }});
</script>
</body>
</html>"""

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(doc)

    size = os.path.getsize(OUT) / (1024 * 1024)
    print(f"✅ Kitap üretildi: {os.path.basename(OUT)} ({size:.1f} MB)")
    print(f"   {len(chapters)} bölüm gömüldü: " + ", ".join(str(n) for n, _ in chapters))
    print("   Çift tıkla tarayıcıda aç; Yazdır → 'PDF olarak kaydet' ile kitap PDF'i çıkar.")


if __name__ == "__main__":
    build()
