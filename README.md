# Genetik Hastalık Mekanizmaları — Mekanizma Kitabı

Türkçe, akademik bir **ders kitabı (textbook)** projesi: genetik hastalık mekanizmalarını
*mekanizma → varyant tipi → hücresel sonuç → klinik fenotip → tanısal test → varyant yorumu (ACMG/ClinGen)*
zinciriyle öğreten, bol görselli (SVG + Mermaid) ve **PubMed ile doğrulanmış kaynaklı** bir eser.

> **Bu dosya, projeyi başka bir bilgisayarda kaldığı yerden sürdürmek içindir.**
> Amaç: yeni bir Claude Code oturumu açıldığında bağlamın **hiç kaybolmaması**.

---

## 📍 Şu an neredeyiz? (canlı ilerleme)

Güncel durumun **tek doğ­ru kaynağı**: [`Bölüm_00_İçindekiler_ve_İlerleme.md`](Bölüm_00_İçindekiler_ve_İlerleme.md)
(içindekiler + bölüm durumları + doğrulanmış kaynak kütüğü + görsel kütüğü + "sonraki adım").

- **Tamamlanan:** Bölüm 1–10 (textbook derinliğinde).
- **Sıradaki:** Bölüm 11 — Mitokondriyal genetik.
- Bir sonraki bölümün planı `Bölüm_00`'ın **"4. Sonraki adım"** kısmındadır.

---

## 🔄 Başka bir PC'de nasıl devam edilir? (adım adım)

1. **Depoyu indir:**
   ```bash
   git clone <repo-URL>
   cd Mekanizma_Kitabı
   ```
2. **Bağımlılıkları kur** (kitap derlemek için):
   ```bash
   python3 -m pip install --user markdown
   ```
   (Mermaid.js zaten `build_assets/mermaid.min.js` içinde repoda; ayrıca indirmeye gerek yok.)
3. **PubMed MCP'yi bağla — KRİTİK.** Kaynak doğrulaması (`search_articles`, `get_article_metadata`,
   `lookup_article_by_citation`) bu bağlantı olmadan çalışmaz ve projenin **altın kuralı** (kaynak
   uydurma yasağı) ihlal edilir. Yeni PC'de Claude Code'da bio-research/PubMed MCP sunucusunun
   bağlı ve yetkili olduğundan emin ol.
4. **Claude Code'u proje klasöründe aç.** `CLAUDE.md` her oturumda **otomatik yüklenir** — işletim
   kılavuzu, kurallar ve stil oradan gelir.
5. **İlk mesajın olarak şunu yaz** (bağlamı hızla kurar):
   > "Bölüm_00_İçindekiler_ve_İlerleme.md'yi oku, neredeyiz özetle, sonra `/bolum-yaz` ile sıradaki bölüme devam et."

Bu kadar. `CLAUDE.md` + `Bölüm_00` + `00_Şablonlar/` üçlüsü, yeni oturumun projeyi **aynı olgunlukta**
sürdürmesi için gereken her şeyi taşır.

---

## 🗂️ Dosya haritası

| Yol | Ne işe yarar |
|-----|--------------|
| `CLAUDE.md` | **İşletim kılavuzu** — her oturum otomatik yüklenir; kurallar, format, iş akışı |
| `Bölüm_00_İçindekiler_ve_İlerleme.md` | Canlı içindekiler + ilerleme + **kaynak kütüğü** + görsel kütüğü + sonraki adım |
| `Bölüm_NN_<Konu>.md` | Bölüm dosyaları (NN = 01, 02, …) |
| `assets/sekil_NN_*.svg` | Tüm SVG görseller |
| `00_Şablonlar/Bölüm_Şablonu.md` | Kopyalanacak bölüm iskeleti (10 başlık) |
| `00_Şablonlar/Stil_Rehberi.md` | Ton, biçim, kutular, görsel standardı |
| `00_Şablonlar/Görsel_Doktrini_v2.md` | **SVG çizim doktrini** (palet, çakışma-yasağı, marker tuzağı, gözle-denetim kuralı) |
| `00_Şablonlar/Kaynak_Protokolü.md` | PubMed doğrulama iş akışı |
| `.claude/skills/bolum-yaz/SKILL.md` | `/bolum-yaz` skill'i (bölüm üretim adımları) |
| `build_book.py` | Tek dosyalık HTML kitabı üretir |
| `build_assets/mermaid.min.js` | Offline Mermaid render (repoda gömülü) |
| `Genetik_Hastalık_Mekanizmaları.html` | **Derlenmiş kitap** (paylaşılabilir çıktı) |

---

## 🏗️ Kitabı derleme (build)

Kaynak `.md` dosyaları **asıldır**; paylaşılacak çıktı bunlardan üretilir:
```bash
python3 build_book.py
```
Kök dizinde tek dosyalık, kendi kendine yeten `Genetik_Hastalık_Mekanizmaları.html` üretir
(tüm SVG'ler inline, Mermaid'ler offline render, kapak + otomatik içindekiler + textbook CSS dahil).
**PDF için:** HTML'i tarayıcıda aç → Yazdır → "PDF olarak kaydet".

> Her bölüm bitiminde: öz-denetim + `Bölüm_00` güncelle + `python3 build_book.py` çalıştır.

---

## ⚠️ Bozulmadan devam için altın kurallar (özet — tamamı `CLAUDE.md`'de)

1. **Anlatı (paragraf) önce** — madde listesi bir kavramı açıklamaz.
2. **Textbook derinliği**, özet değil.
3. **Kaynak uydurma YASAK** — her iddia PubMed MCP ile doğrulanmış PMID + DOI'ye dayanır.
4. **Görsel bol** — bölüm başına ≥3 SVG + ≥2 Mermaid; v2 doktrini (`Görsel_Doktrini_v2.md`).
5. **Standart 10-başlık formatı** her bölümde eksiksiz.
6. Her bölüm sonunda `Bölüm_00`'ı güncelle + kitabı yeniden derle.

---

## 💾 Yedekleme / senkron alışkanlığı

Her önemli ilerlemeden sonra (yeni bölüm, düzeltme) değişiklikleri GitHub'a gönder:
```bash
git add -A
git commit -m "Bölüm NN tamamlandı"
git push
```
Böylece hangi PC'de çalışırsan çalış, `git pull` ile en güncel hâli alırsın ve hiçbir emek kaybolmaz.
