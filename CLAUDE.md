# CLAUDE.md — Mekanizma Kitabı İşletim Kılavuzu

Bu dosya her oturumda otomatik yüklenir. Amacı: bu projede **nasıl çalışacağımı** kalıcı kılmak, böylece kullanıcının her seferinde standartları yeniden anlatmasına gerek kalmaması.

---

## 1. Proje kimliği

- **Ürün:** "Genetik Hastalık Mekanizmaları" — kapsamlı bir **akademik ders kitabı (textbook)**, özet değil.
- **Hedef kitle:** Çocuk genetik uzmanları/yandal asistanları, genel pediatri hekimleri, genomik analiz yapan klinisyenler **ve tıp öğrencileri**.
- **Dil:** Türkçe (akademik ama öğretici; gereksiz basitleştirme yok, ama kavramlar anlaşılır).
- **Çekirdek pedagoji:** Her konu şu zinciri öğretmeli →
  **mekanizma → varyant tipi → hücresel sonuç → klinik fenotip → tanısal test → varyant yorumu (ACMG/ClinGen)**.

---

## 1B. Yayım standardı ve doğrulama (KARAR VERİLDİ — yeniden tartışma)

Kitap **hekimlere yönelik yayımlanacaktır**. Bu nedenle:

- **"Bu kitapta hata yok" iddiası ASLA kullanılmaz.** Savunulan şey hatasızlık değil **denetlenebilirliktir**.
- Her iddia beş türden birine ayrılır (T1 normatif · T2 çalışma bulgusu · T3 gen/varyant/dozaj · T4 ders bilgisi · T5 kitabın özgün sentezi) ve **türüne uygun otoriteyle** doğrulanır.
- **T5 (kitabın özgün pedagojik çerçeveleri) doğrulanmaz, ETİKETLENİR** — yerleşik sınıflama gibi sunulamaz.
- ⛔ **Doğrulama, veriyi bir modele okutarak yapılamaz.** `WebFetch` uydurabilir (kanıtlandı: ClinGen'de olmayan bir geni "HI = 3" diye bildirdi). Veri tabanı kanıtı **`curl` ile indirilir + Python ile tam eşleştirilir**. WebFetch yalnız keşif içindir.
- Uzman insan değerlendirmesi **yayım ön koşuludur**; model bunun yerine geçemez.

> **Tam protokol:** `00_Şablonlar/Dogrulama_Protokolu.md` — işlem sırası, sabit veri kaynakları, ClinGen skor kodları ve gen/bölge tuzağı orada. **Uygulama kaydı:** `Dogrulama_Kutugu.md`.

## 2. Altın kurallar (asla ihlal etme)

1. **Anlatı (paragraf) önce gelir — bu en kritik kuraldır.** Bölümler **akıcı, öğretici paragraflarla** yazılır; madde listesi ancak gerçekten liste olan içerik için (kaynakça, hızlı referans) kullanılır. Bir kavramı madde madde sıralamak ONU AÇIKLAMAK DEĞİLDİR. Her zor kavram, okuyucunun (özellikle tıp öğrencisinin) "ne olduğunu, neden önemli olduğunu, nasıl yorumlandığını" anlayacağı şekilde **paragraf içinde, örnek/benzetmeyle** anlatılır. Tablolar açıklayıcı paragrafın yerini almaz; onu özetler.
2. **Textbook derinliği, özet değil.** Her bölüm derin anlatım + deep-dive kutuları + bol görsel + çok sayıda algoritma içerir.
3. **Atıf doğal olmalı — cümleyi "Based on articles retrieved from PubMed" ile BAŞLATMA.** Bir textbook bu şekilde yazılmaz. Metin içinde **yazar-yıl** biçimi kullanılır (ör. "… (Richards ve ark., 2015)"); DOI linkleri **kaynakça bölümünde** verilir; PubMed atıf yükümlülüğü her bölümün Kaynaklar bölümündeki **tek bir doğrulama/atıf notu** + her kaynaktaki DOI linki ile karşılanır. Akış bozulmaz.
4. **Kaynak uydurma YASAK.** Her mekanizma/yorum iddiası, **kaynak türüne uygun kalıcı kimliği bizzat doğrulanmış** bir kaynağa dayanır: hakemli makalede PubMed MCP ile teyit edilmiş **PMID + DOI**; kılavuz/uzman panel spesifikasyonunda (HGVS, ClinGen SVI, VCEP/CSpec, ACMG teknik standardı, ACGS, EMQN) **kurum + belge + sürüm + tarih + kalıcı bağlantı + erişim tarihi**; veri tabanında **veri sürümü + sorgu tarihi**. ⚠️ *01.08.2026'da güncellendi:* eski "PMID/DOI veremediğin kaynağı çıkar" kuralı, alanın en yetkili PMID'siz kaynaklarını dışladığı için terk edildi — **titizlik değil, kimlik biçimi** esnedi. Bkz. `00_Şablonlar/Kaynak_Protokolü.md` §1.
5. **Doğrulanamayan iddiayı** "⚠️ kaynak doğrulaması gerekli" diye işaretle veya çıkar. Spekülasyonu açıkça etiketle. **Bibliyografik doğrulama ile iddia-düzeyi doğrulama ayrı denetimlerdir**: "X/X kaynağın künyesi doğrulandı" cümlesi, metindeki her iddianın o kaynaklarca desteklendiğini göstermez ve öyleymiş gibi yazılamaz.
6. **Görsel bol olmalı (üst sınır yok).** Her bölümde **en az ≥3 SVG + ≥2 Mermaid**; konu gerektiriyorsa **daha fazlasını yap** — sayı tavanı yoktur. Anlamayı kolaylaştıran her yere görsel ekle.
7. **Standart 10-başlık formatı** (aşağıda) her bölümde eksiksiz uygulanır.
8. **İkincil kaynaklar** (GeneReviews/OMIM/ClinVar/gnomAD) yalnızca destekleyici; ana mekanizma kaynağı olamaz.

---

## 3. Dosya yapısı ve adlandırma

```
Mekanizma_Kitabı/
├── CLAUDE.md                              # bu dosya (işletim kılavuzu)
├── Bölüm_00_İçindekiler_ve_İlerleme.md    # master TOC + ilerleme + KAYNAK KÜTÜĞÜ
├── 00_Şablonlar/
│   ├── Bölüm_Şablonu.md                   # kopyalanacak bölüm iskeleti
│   ├── Stil_Rehberi.md                    # ton, biçim, kutular, görsel standardı
│   └── Kaynak_Protokolü.md                # PubMed doğrulama iş akışı
├── .claude/skills/bolum-yaz/SKILL.md      # /bolum-yaz skill'i
├── assets/                                # tüm SVG görseller (sekil_XX_*.svg)
└── Bölüm_NN_<Konu>.md                     # bölüm dosyaları
```

- **Bölüm dosyası:** `Bölüm_NN_<Konu>.md` (NN = iki haneli sıra).
- **Görsel:** `assets/sekil_NN_<kısa_ad>.svg`; bölüm içinde `![Şekil N — başlık](assets/sekil_NN_*.svg)` ile referanslanır.
- Yeni bölüm/görsel ekleyince **Bölüm_00** indeksini ve kaynak kütüğünü güncelle.

---

## 4. Her bölümün zorunlu yapısı

Başlık bloğu: **çekirdek tez** (blockquote) + **📘 Okuma katmanları** (① Temel · ② Klinik · ③ İleri düzey — zorunlu; bkz. `kitap/07_Terminoloji_ve_Yazim_Kurallari.md` §12) + **Öğrenme hedefleri** + görsel/render notu.

Ardından 10 standart başlık:
1. **Kavramsal tanım** (gerekirse gruplu sözlük; her terim tanım+benzetme+klinik not)
2. **Moleküler mekanizma** (derin anlatım + deep-dive kutuları + SVG)
3. **Varyant tipleri**
4. **Klinik fenotipe dönüşüm** (bölümün anahtar sorularını yanıtla)
5. **Tanısal testlerle ilişkisi** (standart test tablosu — aşağıda)
6. **Varyant yorumlama açısından önemi** (ACMG/ClinGen bağlantısı; ilgili karar ağacı)
7. **Pediatrik genetikten klinik örnekler** (kaynaklı, somut genler)
8. **Sık yapılan hatalar** (🔴 kutu) + **Klinikte dikkat** (🟦 kutu)
9. **Klinik pratikte karar algoritması** (Mermaid)
10. **Kaynaklar** (her biri: Yazar, Yıl, Başlık, Dergi, PMID, DOI-link, kullanım amacı)

Bölüm sonu: **✅ öz-denetim tablosu** (10 kriter) + **🔎 kaynak doğrulama komutu** durumu.

**Standart test tablosu satırları:** WES · Short-read WGS · Long-read WGS · Array-CGH/SNP array · MLPA · RNA-seq · Methylation array · Karyotip. Sütunlar: "Bu mekanizmayı yakalar mı?" / "Sınırlılığı".

> Tam iskelet için: `00_Şablonlar/Bölüm_Şablonu.md`. Ton/biçim için: `00_Şablonlar/Stil_Rehberi.md`.

---

## 5. Görsel standardı

- **SVG (assets/):** Beyaz zemin (`fill="#ffffff"`), açık renk paleti, Türkçe etiketler, başlık + alt-not. CSS değişkeni KULLANMA (img olarak izole render edilir). Mekanizma şemaları, anatomiler, eğriler, pedigriler için.
- **Mermaid (kod bloğu):** Karar ağaçları, akış/algoritmalar, sınıflandırma için. Etiketleri `"..."` içine al; satır sonu `<br/>`.
- Her bölümde en az: 1 mekanizma SVG'si + 1 karar/algoritma Mermaid'i + konuya özgü ek görseller.

---

## 6. Kaynak protokolü (özet — ayrıntı: Kaynak_Protokolü.md)

1. Bölüm için 5–8 **çekirdek** kaynak belirle (landmark mekanizma + guideline + klinik örnek).
2. PubMed MCP ile **doğrula:** `search_articles` → `lookup_article_by_citation` → `get_article_metadata` (PMID + DOI + başlık teyidi).
3. Önce **Bölüm_00 kaynak kütüğüne** bak; daha önce doğrulanmış kaynağı **yeniden doğrulama**, tekrar kullan.
4. Metinde her iddiayı kaynağa bağla; PubMed atıf + DOI linki ver.
5. Bölüm sonunda doğrulama durumunu **iki satırda** raporla: (a) bibliyografik — X/X kaynağın künyesi, türlerine göre; (b) iddia düzeyi — hangi tarihte turdan geçtiği ve işaretlenen iddialar. Doğrulanamayan → işaretle/çıkar.
6. Yeni doğrulanan kaynakları **Bölüm_00 kütüğüne ekle**.

---

## 7. Bölüm yazım iş akışı (agentik döngü)

Her bölüm için sırayla:
1. **Plan:** Bölümün öğrenme hedefleri, anahtar sorular, gerekli görseller/algoritmalar, örnek genler.
2. **Kaynak:** Kütüğü kontrol et → eksikleri PubMed'den doğrula (madde 6).
3. **Görseller:** Gerekli SVG'leri `assets/`'e üret.
4. **Yaz:** Standart 10-başlık formatında, textbook derinliğinde, görselleri ve Mermaid'i gömerek.
5. **Öz-denetim:** Öz-denetim tablosu + kaynak doğrulama durumu.
6. **İndeks:** Bölüm_00'da durumu "✅ tamam" yap, kaynak kütüğünü güncelle.
7. **Rapor:** Kullanıcıya kısa özet + dosya linkleri; bir sonraki bölüm için onay/iste.

> **Varsayılan ilerleme:** Kullanıcı aksini belirtmedikçe bölümleri **plandaki sırayla** yaz. Her bölüm sonunda dur, kısa rapor ver, devam onayı al (kullanıcı "devam"/"hepsini yaz" derse onay beklemeden ilerle).

---

## 8. Bölüm listesi ve sıra

1. Genetik hastalık mekanizması nedir? ✅
2. Loss-of-function ✅
3. Haploinsufficiency
4. Gain-of-function
5. Dominant-negatif
6. Neomorfik aleller (antimorf = dominant-negatifin tarihsel adı; mekanizma Bölüm 5'tedir)
7. Splicing
8. CNV / yapısal varyantlar
9. Repeat expansion
10. İmprinting, UPD, epigenetik
11. Mitokondriyal genetik
12. Mozaiklik
13. Noncoding / regülatör varyantlar
14. Digenik / oligogenik / modifier
15. Aynı gen → farklı hastalık (allelik seri)
16. Mekanizma → varyant yorumu (ACMG/ClinGen)
17. Klinik senaryolarla sentez
+ **Final pass:** birleştirme, tekrar azaltma, terminoloji standardizasyonu, global kaynakça.

Güncel ilerleme **Bölüm_00_İçindekiler_ve_İlerleme.md** dosyasındadır.

---

## 9. Kullanıcı tercihleri (kalıcı kararlar — tekrar sorma)

- Format: **ayrı `.md` dosyaları** + `assets/` SVG'ler.
- Derinlik: **maksimum / textbook** (özet asla).
- Kaynak: **doğrulanmış çekirdek** kaynaklar; her biri PMID+DOI.
- Görsel: **bol** (SVG + Mermaid).
- Dil: **Türkçe**.
- Önce mekanizma, sonra klinik, sonra test, sonra yorum.

---

## 10. Araç notları

- **PubMed MCP** mevcut: `search_articles`, `lookup_article_by_citation`, `get_article_metadata`, `convert_article_ids`, `get_full_text_article`. Kaynak doğrulamasının tek meşru yolu budur (eğitim verisinden PMID "hatırlama" → uydurma riski; YAPMA).
- Görseller `assets/`'e **SVG dosyası** olarak yazılır (sohbet widget'ı değil), çünkü kalıcı kitap dosyasına gömülecek.
- **SVG'lerde `&` doğrudan KULLANMA → `&amp;` yaz** (kaçırılmamış `&` SVG'yi bozar, render edilmez). Yeni SVG ekledikten sonra geçerliliği `xmllint --noout assets/*.svg` ile kontrol et.

---

## 11. Yayım / kitap üretimi (build)

Kaynak `.md` dosyaları **düzenlenebilir asıldır**; paylaşılacak çıktı bunlardan **üretilir**. Pipeline:

- **Komut:** `python3 build_book.py` → kök dizinde **`Genetik_Hastalık_Mekanizmaları.html`** üretir.
- Bu, **tek dosyalık, kendi kendine yeten** bir HTML kitaptır: tüm SVG'ler inline gömülür, Mermaid'ler **offline** render olur (mermaid.js `build_assets/mermaid.min.js`'ten inline gömülür), kapak + otomatik içindekiler + textbook CSS dahildir.
- **PDF için:** HTML'i tarayıcıda aç → **Yazdır → "PDF olarak kaydet"** (CSS'te sayfa-sonu/print kuralları hazır).
- Betik bölümleri otomatik toplar: `Bölüm_NN_*.md` (NN≥01), sıralı; `Bölüm_00` kitap gövdesine girmez.
- **Her bölüm bitiminde** (öz-denetim + indeks güncellemesinden sonra) `python3 build_book.py` çalıştırıp kitabı tazele.
- Bağımlılık: `python3 -m pip install --user markdown` (bir kez); mermaid.js bir kez `build_assets/`'e indirilmiştir.
