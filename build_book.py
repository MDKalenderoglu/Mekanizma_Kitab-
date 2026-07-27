#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_book.py — Mekanizma Kitabı tek-dosya HTML kitap üreticisi.

Kitap mimarisi (akademik textbook düzeni):
  DIŞ KAPAK · İÇ KAPAK · KÜNYE · İTHAF · ÖNSÖZ · TEŞEKKÜR · YAZAR
  İÇİNDEKİLER · ŞEKİLLER · ALGORİTMALAR · TABLOLAR LİSTESİ
  KISALTMALAR · TERMİNOLOJİ VE YAZIM KURALLARI
  KISIM I–VI (17 bölüm)
  EKLER · SÖZLÜK · TOPLU KAYNAKÇA · GEN DİZİNİ · HASTALIK DİZİNİ
  ÖZGEÇMİŞ · ARKA KAPAK

Ne yapar:
  • kitap/ klasöründeki ön/arka madde dosyalarını sırayla gömer.
  • Bölüm_NN_*.md dosyalarını (Bölüm_00 hariç) KISIM ayraçlarıyla sıralar.
  • Şekil / Algoritma / Tablo listelerini ve toplu kaynakçayı OTOMATİK üretir.
  • Mermaid kod bloklarını offline render eder; assets/*.svg'leri inline gömer.
  • Kapak + içindekiler + textbook CSS + yazdır→PDF desteği ekler.

Kullanım:  python3 build_book.py
Çıktı:     Genetik_Hastalık_Mekanizmaları.html
"""
import re
import sys
import html
import glob
import os
import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")
KITAP = os.path.join(ROOT, "kitap")
MERMAID_JS = os.path.join(ROOT, "build_assets", "mermaid.min.js")
OUT = os.path.join(ROOT, "Genetik_Hastalık_Mekanizmaları.html")

BOOK_TITLE = "Genetik Hastalık Mekanizmaları"
BOOK_SUBTITLE = "Mekanizmadan Varyant Yorumuna — Kapsamlı Akademik Ders Kitabı"

# KISIM yapısı: (roma, ad, alt başlık, bölüm numaraları)
PARTS = [
    ("I", "Çerçeve", "Mekanizma nedir ve neden merkeze alınır?", [1]),
    ("II", "Protein Düzeyinde Mekanizmalar",
     "Ürünün yokluğu, azlığı, fazlalığı, bozulması ve yeni işlev kazanması", [2, 3, 4, 5, 6]),
    ("III", "Transkript ve Genom Yapısı",
     "Kırpılma kusurları, yapısal varyantlar ve tekrar dizileri", [7, 8, 9]),
    ("IV", "Epigenetik, Organel ve Mozaiklik",
     "Dizide olmayan kusurlar: damga, ikinci genom ve hücre soyları", [10, 11, 12]),
    ("V", "Genomik Bağlam ve Karmaşık Mimari",
     "Kodlamayan genom, çok-lokuslu kalıtım ve allelik seriler", [13, 14, 15]),
    ("VI", "Yorum ve Klinik Sentez",
     "Mekanizmadan varyant sınıflandırmasına, oradan hastanın başına", [16, 17]),
]

FRONT = [
    ("01_Kunye.md", "Künye ve Telif"),
    ("02_Ithaf.md", "İthaf"),
    ("03_Onsoz.md", "Önsöz"),
    ("04_Tesekkur.md", "Teşekkür"),
    ("05_Yazar.md", "Yazar ve Editörler"),
]
FRONT_AFTER_TOC = [
    ("06_Kisaltmalar.md", "Kısaltmalar"),
    ("07_Terminoloji_ve_Yazim_Kurallari.md", "Terminoloji ve Yazım Kuralları"),
]
BACK = [
    ("20_Ekler.md", "Ekler"),
    ("21_Sozluk.md", "Sözlük"),
]
BACK_AFTER_BIB = [
    ("22_Gen_Dizini.md", "Gen Dizini"),
    ("23_Hastalik_Dizini.md", "Hastalık Dizini"),
    ("24_Ozgecmis.md", "Yazar Özgeçmişi"),
]

try:
    import markdown
except ImportError:
    sys.exit("HATA: 'markdown' kurulu değil. Çalıştır: python3 -m pip install --user markdown")


def chapter_files():
    out = []
    for f in glob.glob(os.path.join(ROOT, "Bölüm_*.md")):
        m = re.match(r"Bölüm_(\d+)_", os.path.basename(f))
        if not m:
            continue
        n = int(m.group(1))
        if n == 0:  # Bölüm_00 = ilerleme/kütük dosyası; kitaba girmez
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
    """Mermaid bloklarını ve SVG görsellerini token'la koru."""
    placeholders = {}

    def repl_mermaid(m):
        key = f"@@MERMAID_{len(placeholders)}@@"
        placeholders[key] = (
            f'<div class="mermaid-wrap"><pre class="mermaid">{html.escape(m.group(1))}</pre></div>'
        )
        return key

    md_text = re.sub(r"```mermaid\s*\n(.*?)```", repl_mermaid, md_text, flags=re.DOTALL)

    def repl_img(m):
        alt, path = m.group(1).strip(), m.group(2).strip()
        svg_path = os.path.join(ROOT, path)
        key = f"@@FIG_{len(placeholders)}@@"
        if os.path.exists(svg_path):
            with open(svg_path, encoding="utf-8") as fh:
                svg = re.sub(r"<\?xml.*?\?>", "", fh.read(), flags=re.DOTALL).strip()
            placeholders[key] = (f'<figure class="svg-fig">{svg}'
                                 f'<figcaption>{html.escape(alt)}</figcaption></figure>')
        else:
            placeholders[key] = f'<p class="missing">[Görsel bulunamadı: {html.escape(path)}]</p>'
        return key

    md_text = re.sub(r"!\[([^\]]*)\]\((assets/[^)]+\.svg)\)", repl_img, md_text)
    return md_text, placeholders


def restore_blocks(html_text, placeholders):
    for key, val in placeholders.items():
        html_text = html_text.replace(f"<p>{key}</p>", val)
        html_text = html_text.replace(key, val)
    return html_text


def convert(md_text):
    md_text, ph = protect_blocks(md_text)
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "footnotes"],
        output_format="html5",
    )
    return restore_blocks(md.convert(md_text), ph)


def read_kitap(fname):
    p = os.path.join(KITAP, fname)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as fh:
        return fh.read()


# ---------------------------------------------------------------- listeler
def collect_lists(chapters):
    figs, algos, tabs = [], [], []
    for n, f in chapters:
        with open(f, encoding="utf-8") as fh:
            txt = fh.read()
        for no, cap in re.findall(r"!\[Şekil (\d+\.\d+) — ([^\]]+)\]\(assets/", txt):
            figs.append((no, cap.strip(), n))
        for no, cap in re.findall(r"\*\*Algoritma (\d+\.\d+) — ([^*]+)\*\*", txt):
            algos.append((no, cap.strip(), n))
        for no, cap in re.findall(r"\*\*Tablo (\d+\.\d+) — ([^*]+)\*\*", txt):
            tabs.append((no, cap.strip(), n))
    key = lambda x: tuple(int(p) for p in x[0].split("."))
    return sorted(figs, key=key), sorted(algos, key=key), sorted(tabs, key=key)


def list_section(anchor, title, rows, label, intro):
    items = "".join(
        f'<li><span class="lno">{label} {no}</span>'
        f'<span class="lcap">{html.escape(cap)}</span>'
        f'<span class="lch"><a href="#bolum-{ch}">Bölüm {ch}</a></span></li>'
        for no, cap, ch in rows
    )
    return (f'<section class="chapter listpage" id="{anchor}"><h1>{title}</h1>'
            f'<p class="intro">{intro}</p><ul class="figlist">{items}</ul></section>')


def collect_bibliography(chapters):
    seen, used = {}, {}
    for n, f in chapters:
        with open(f, encoding="utf-8") as fh:
            for line in fh.read().splitlines():
                m = re.match(r"^\d+\.\s+\*\*(.+?)\*\*\s*(.*?\*\*PMID:\s*(\d+)\*\*[^—]*)", line)
                if not m:
                    continue
                au, rest, pmid = m.group(1).strip(), m.group(2).strip().rstrip(" —"), m.group(3)
                seen.setdefault(pmid, (au, rest))
                used.setdefault(pmid, set()).add(n)
    rows = []
    for i, pmid in enumerate(sorted(seen, key=lambda p: seen[p][0].split()[0].lower()), 1):
        au, rest = seen[pmid]
        chs = ", ".join(str(x) for x in sorted(used[pmid]))
        rows.append(f"{i}. **{au}** {rest} · *Bölüm: {chs}*")
    return rows, len(seen)


CSS = r"""
:root{
  --ink:#1a2b4a; --body:#222; --muted:#5b6675; --rule:#d8dee6;
  --accent:#2471a3; --accent-soft:#eef6fb; --gold:#b8860b;
}
*{box-sizing:border-box}
html{font-size:16px}
body{font-family:"Iowan Old Style","Palatino Linotype",Georgia,"Times New Roman",serif;
  color:var(--body);line-height:1.62;margin:0;background:#f4f6f9;}
.page{max-width:860px;margin:0 auto;padding:48px 56px;background:#fff;box-shadow:0 1px 4px rgba(0,0,0,.06);}
h1,h2,h3,h4{font-family:"Helvetica Neue",Arial,sans-serif;color:var(--ink);line-height:1.25;}
h1{font-size:2rem;border-bottom:3px solid var(--accent);padding-bottom:.3em;margin-top:0;}
h2{font-size:1.45rem;margin-top:1.8em;border-bottom:1px solid var(--rule);padding-bottom:.2em;}
h3{font-size:1.15rem;margin-top:1.4em;color:var(--accent);}
h4{font-size:1.02rem;margin-top:1.1em;}
p{margin:.7em 0;} a{color:var(--accent);text-decoration:none;} a:hover{text-decoration:underline;}
code{font-family:"SF Mono",Menlo,Consolas,monospace;font-size:.86em;background:#f1f3f6;padding:.1em .35em;border-radius:4px;}
pre code{background:none;padding:0;}
table{border-collapse:collapse;width:100%;margin:1.1em 0;font-size:.92rem;font-family:"Helvetica Neue",Arial,sans-serif;}
th,td{border:1px solid var(--rule);padding:.5em .65em;text-align:left;vertical-align:top;}
thead th{background:var(--ink);color:#fff;font-weight:600;}
tbody tr:nth-child(even){background:#f7f9fb;}
blockquote{margin:1.1em 0;padding:.8em 1.1em;border-left:5px solid var(--accent);
  background:var(--accent-soft);border-radius:0 6px 6px 0;}
blockquote p:first-child{margin-top:0;} blockquote p:last-child{margin-bottom:0;}
figure.svg-fig{margin:1.4em 0;text-align:center;page-break-inside:avoid;}
figure.svg-fig svg{max-width:100%;height:auto;border:1px solid var(--rule);border-radius:6px;}
figure.svg-fig figcaption{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.85rem;
  color:var(--muted);margin-top:.5em;font-style:italic;}
.mermaid-wrap{margin:1.4em 0;text-align:center;page-break-inside:avoid;}
pre.mermaid{background:#fff;}
.missing{color:#c0392b;font-style:italic;}
hr{border:none;border-top:1px solid var(--rule);margin:2em 0;}
/* Kapaklar */
.cover,.titlepage,.backcover{min-height:92vh;display:flex;flex-direction:column;justify-content:center;
  text-align:center;page-break-after:always;}
.cover{background:linear-gradient(160deg,#f8fafc 0%,#eef4fa 100%);margin:-48px -56px 0;padding:56px;}
.cover .big{font-family:"Helvetica Neue",Arial,sans-serif;font-size:3.1rem;font-weight:800;
  color:var(--ink);line-height:1.08;margin:0 0 .3em;letter-spacing:-.5px;}
.cover .sub{font-size:1.18rem;color:var(--muted);max-width:640px;margin:0 auto 2em;}
.cover .meta,.titlepage .meta{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.95rem;color:var(--muted);}
.cover .rule,.titlepage .rule{width:84px;height:4px;background:var(--accent);margin:1.4em auto;}
.cover .author{font-family:"Helvetica Neue",Arial,sans-serif;font-size:1.15rem;color:var(--ink);
  font-weight:600;margin-top:2.2em;}
.titlepage .big{font-family:"Helvetica Neue",Arial,sans-serif;font-size:2.4rem;font-weight:700;color:var(--ink);}
.titlepage .sub{font-size:1.05rem;color:var(--muted);max-width:560px;margin:.6em auto 1.4em;}
.backcover{justify-content:flex-start;padding-top:3em;text-align:left;}
.backcover h1{border-bottom:none;}
/* KISIM ayraç */
.part{page-break-before:always;min-height:52vh;display:flex;flex-direction:column;justify-content:center;
  text-align:center;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);margin:2em 0;}
.part .kicker{font-family:"Helvetica Neue",Arial,sans-serif;letter-spacing:.28em;font-size:.85rem;
  color:var(--gold);text-transform:uppercase;font-weight:700;}
.part .pname{font-family:"Helvetica Neue",Arial,sans-serif;font-size:2.1rem;font-weight:800;
  color:var(--ink);margin:.35em 0 .25em;}
.part .pdesc{color:var(--muted);font-size:1.02rem;max-width:600px;margin:0 auto 1em;}
.part .plist{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.9rem;color:var(--muted);}
/* İçindekiler ve listeler */
.toc{page-break-after:always;} .toc h1{border-bottom:3px solid var(--accent);}
.toc ul{font-family:"Helvetica Neue",Arial,sans-serif;font-size:1rem;line-height:1.9;
  list-style:none;padding-left:0;margin:.4em 0;}
.toc li{border-bottom:1px dotted var(--rule);padding:.12em 0;}
.toc li.plain{font-weight:700;}
.toc li.partline{font-weight:800;color:var(--gold);border-bottom:none;padding-top:.9em;
  letter-spacing:.06em;font-size:.92rem;text-transform:uppercase;}
.toc li.chline{padding-left:1.2em;}
.listpage ul.figlist{list-style:none;padding-left:0;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.93rem;}
.listpage ul.figlist li{display:flex;gap:.7em;align-items:baseline;border-bottom:1px dotted var(--rule);padding:.28em 0;}
.listpage .lno{flex:0 0 8.5em;font-weight:700;color:var(--ink);}
.listpage .lcap{flex:1 1 auto;}
.listpage .lch{flex:0 0 5.5em;text-align:right;color:var(--muted);font-size:.86em;}
.listpage .intro{color:var(--muted);font-size:.92rem;}
.chapter{page-break-before:always;}
@media print{
  body{background:#fff;} .page{box-shadow:none;max-width:none;padding:0 12mm;}
  .cover{margin:0;padding:0;background:none;}
  h2,h3,h4{page-break-after:avoid;}
  table,figure,blockquote,.mermaid-wrap{page-break-inside:avoid;}
  @page{margin:18mm 14mm;}
}
"""


def build():
    chapters = chapter_files()
    if not chapters:
        sys.exit("HATA: Bölüm_NN_*.md bulunamadı.")
    with open(MERMAID_JS, encoding="utf-8") as fh:
        mermaid_js = fh.read()

    today = datetime.date.today().strftime("%d.%m.%Y")
    cmap = dict(chapters)
    titles = {}
    for n, f in chapters:
        with open(f, encoding="utf-8") as fh:
            titles[n] = extract_title(fh.read(), os.path.basename(f))

    figs, algos, tabs = collect_lists(chapters)
    bib_rows, bib_n = collect_bibliography(chapters)

    bodies, toc_lines, used = [], [], []

    def add_files(items):
        for fname, label in items:
            md = read_kitap(fname)
            if md is None:
                continue
            anchor = fname.split("_", 1)[1].replace(".md", "").lower().replace("_", "-")
            bodies.append(f'<section class="chapter" id="{anchor}">{convert(md)}</section>')
            toc_lines.append(f'<li class="plain"><a href="#{anchor}">{html.escape(label)}</a></li>')
            used.append(fname)

    add_files(FRONT)
    add_files(FRONT_AFTER_TOC)

    toc_lines.append(f'<li class="plain"><a href="#sekiller">Şekiller Listesi ({len(figs)})</a></li>')
    toc_lines.append(f'<li class="plain"><a href="#algoritmalar">Algoritmalar Listesi ({len(algos)})</a></li>')
    toc_lines.append(f'<li class="plain"><a href="#tablolar">Tablolar Listesi ({len(tabs)})</a></li>')
    bodies.append(list_section("sekiller", "Şekiller Listesi", figs, "Şekil",
                               "Kitaptaki tüm çizimler; her biri ilgili bölüme bağlantılıdır."))
    bodies.append(list_section("algoritmalar", "Algoritmalar Listesi", algos, "Algoritma",
                               "Karar ağaçları ve klinik akış şemaları."))
    bodies.append(list_section("tablolar", "Tablolar Listesi", tabs, "Tablo",
                               "Kavram, varyant tipi, test ve öz-denetim tabloları."))

    for roma, pname, pdesc, nums in PARTS:
        chs = " · ".join(f"Bölüm {n}" for n in nums)
        bodies.append(
            f'<section class="part" id="kisim-{roma.lower()}">'
            f'<div class="kicker">Kısım {roma}</div><div class="pname">{html.escape(pname)}</div>'
            f'<div class="pdesc">{html.escape(pdesc)}</div><div class="plist">{chs}</div></section>'
        )
        toc_lines.append(f'<li class="partline"><a href="#kisim-{roma.lower()}">'
                         f'Kısım {roma} — {html.escape(pname)}</a></li>')
        for n in nums:
            with open(cmap[n], encoding="utf-8") as fh:
                bodies.append(f'<section class="chapter" id="bolum-{n}">{convert(fh.read())}</section>')
            toc_lines.append(f'<li class="chline"><a href="#bolum-{n}">{html.escape(titles[n])}</a></li>')

    add_files(BACK)
    bib_md = ("# Toplu Kaynakça\n\n> Bölüm kaynakçalarının PMID'ye göre tekilleştirilmiş birleşimidir; "
              "her kaynağın sonunda kullanıldığı bölümler belirtilmiştir. Bibliyografik veriler PubMed "
              "üzerinden doğrulanmıştır.\n\n" + "\n\n".join(bib_rows) + "\n")
    bodies.append(f'<section class="chapter" id="toplu-kaynakca">{convert(bib_md)}</section>')
    toc_lines.append(f'<li class="plain"><a href="#toplu-kaynakca">Toplu Kaynakça ({bib_n})</a></li>')
    add_files(BACK_AFTER_BIB)

    back_md = read_kitap("25_Arka_Kapak.md")
    backcover = f'<section class="backcover" id="arka-kapak">{convert(back_md)}</section>' if back_md else ""
    if back_md:
        used.append("25_Arka_Kapak.md")

    n_fig = len(glob.glob(os.path.join(ASSETS, "*.svg")))
    author_line = ""
    yz = read_kitap("05_Yazar.md")
    if yz:
        m = re.search(r"^\*\*(.+?)\*\*", yz, re.M)
        if m and "DOLDURULACAK" not in m.group(1):
            author_line = f'<div class="author">{html.escape(m.group(1))}</div>'

    cover = f"""<section class="cover">
      <div class="big">{html.escape(BOOK_TITLE)}</div>
      <div class="rule"></div>
      <div class="sub">{html.escape(BOOK_SUBTITLE)}</div>
      {author_line}
      <div class="meta" style="margin-top:2.4em">{len(chapters)} bölüm · {n_fig} şekil · {len(algos)} algoritma · {len(tabs)} tablo · {bib_n} doğrulanmış kaynak</div>
    </section>"""

    titlepage = f"""<section class="titlepage">
      <div class="big">{html.escape(BOOK_TITLE)}</div>
      <div class="sub">{html.escape(BOOK_SUBTITLE)}</div>
      <div class="rule"></div>
      {author_line}
      <div class="meta">Sürüm taslağı · {today}</div>
    </section>"""

    toc = f'<section class="toc" id="icindekiler"><h1>İçindekiler</h1><ul>{"".join(toc_lines)}</ul></section>'

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
{titlepage}
{toc}
{''.join(bodies)}
{backcover}
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
    allf = [f for f, _ in FRONT + FRONT_AFTER_TOC + BACK + BACK_AFTER_BIB] + ["25_Arka_Kapak.md"]
    missing = [f for f in allf if f not in used]
    print(f"✅ Kitap üretildi: {os.path.basename(OUT)} ({size:.1f} MB)")
    print(f"   {len(chapters)} bölüm · {len(PARTS)} kısım · {len(figs)} şekil · "
          f"{len(algos)} algoritma · {len(tabs)} tablo · {bib_n} kaynak")
    if missing:
        print("   ⚠️ Henüz yazılmamış ön/arka madde: " + ", ".join(missing))
    print("   Çift tıkla tarayıcıda aç; Yazdır → 'PDF olarak kaydet' ile kitap PDF'i çıkar.")


if __name__ == "__main__":
    build()
