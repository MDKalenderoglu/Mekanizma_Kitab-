# -*- coding: utf-8 -*-
import sys, re, os, glob
sys.path.insert(0, ".")
from maddeler import MADDELER
from paragraf import paragraf_bul, ROOT

BASLIK = {}
for y in glob.glob(os.path.join(ROOT, "Bölüm_[0-9][0-9]_*.md")):
    ad = os.path.basename(y)
    no = ad[6:8]
    with open(y, encoding="utf-8") as f:
        for s in f:
            if s.startswith("# "):
                BASLIK[no] = s[2:].strip().replace("Bölüm %s — " % int(no), "")
                break

KATEGORI = {
 "A": ("A. Test ve doku seçimi yönlendirmeleri",
       "Yanlışsa okuyucu yanlış test ister — kitabın klinik riski en yüksek kategorisi."),
 "B": ("B. Sayısal eşikler, oranlar ve öğretici basitleştirmeler",
       "Okuyucunun ezberleyip alıntılayacağı sayılar. Bir kısmı kitapta zaten \"temsilî\" diye etiketli — etiketin yeterli olup olmadığı da sorudur."),
 "C": ("C. Kaynaksız mekanizma ve ders bilgisi (T4-a)",
       "Programatik denetimin kapatamadığı asıl kategori: kaynaksız, kulağa doğru gelen, \"yerleşik ders bilgisi\" sayılıp geçilen cümleler."),
 "D": ("D. Kitabın özgün pedagojik çerçeveleri (T5)",
       "Bunlar doğrulanamaz — yalnızca \"iyi öğretiyor mu, yanıltıyor mu\" diye değerlendirilebilir. Dördü de kitapta 🏷️ ile \"yerleşik sınıflama değildir\" diye etiketli."),
}

def isaretle(metin, isaret):
    temiz = isaret.replace("**", "").replace("*", "")
    return metin.replace(isaret, "***" + temiz + "***", 1)

def alintila(metin):
    out = []
    for s in metin.split("\n"):
        s = re.sub(r"^>\s?", "", s)
        out.append("> " + s if s.strip() else ">")
    return "\n".join(out)

parca = []
son_kat = None
for mid, b, capa, isaret, soru in MADDELER:
    kat = mid[0]
    if kat != son_kat:
        bas, alt = KATEGORI[kat]
        parca.append(f"\n---\n\n## {bas}\n\n*{alt}*\n")
        son_kat = kat
    r = paragraf_bul(b, capa)
    metin = isaretle(r["metin"], isaret)
    parca.append(
        f"\n### {mid} · Bölüm {int(b)} — {BASLIK.get(b,'')}\n\n"
        f"**Yer:** `{r['dosya']}` · {r['baslik']} · satır {r['satir']}\n\n"
        f"{alintila(metin)}\n\n"
        f"**Sorulan:** {soru}\n\n"
        f"**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → \n\n"
        f"<br>\n"
    )

print("".join(parca))
