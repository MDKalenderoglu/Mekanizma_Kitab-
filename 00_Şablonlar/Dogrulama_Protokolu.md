# Doğrulama Protokolü — bağlayıcı kurallar

Bu belge, Mekanizma Kitabı'nın **yayımlanabilirlik** standardını tanımlar. Bir kez karar verilmiştir; her oturumda yeniden tartışılmaz. Uygulama kaydı `Dogrulama_Kutugu.md` dosyasındadır.

---

## 0. Temel ilke

**Kitap "hatasızlık" iddia etmez; "denetlenebilirlik" iddia eder.**

Yayımlanabilir savunma cümlesi şudur ve bundan fazlası yazılmaz:

> "Her mekanizma ve yorumlama iddiası kaynaklıdır. Birincil kaynakların bibliyografik verisi PubMed üzerinden doğrulanmıştır. Normatif (kılavuz) iddiaları ClinGen'in *[tarih]* itibarıyla yürürlükteki rehber belgeleriyle karşılaştırılmıştır. Metin *[N]* alan uzmanı tarafından değerlendirilmiştir. Doğrulanamayan iddialar ⚠️ ile işaretlenmiştir."

"Bu kitapta hata yoktur" cümlesi **hiçbir koşulda** kullanılmaz.

---

## 1. İddia türleri ve otoriteleri

Kitaptaki her iddia beş türden birine girer. **Tür belirlenmeden doğrulama yapılmaz.**

| Tür | İçerik | Otorite | Yöntem |
|---|---|---|---|
| **T1** | Normatif/kılavuz kuralı (kriter, eşik, güç düzeyi) | ClinGen rehber belgeleri + kılavuz makaleleri | Belge indirilir, kural cümlesi karşılaştırılır |
| **T2** | Spesifik çalışma bulgusu (sayı, oran, kohort, kat) | Kaynağın özeti veya tam metni | Cümle düzeyinde karşılaştırma; özette yoksa tam metin |
| **T3** | Gen–varyant–hastalık–dozaj eşleşmesi | ClinGen Dosage/Gene-Disease Validity, ClinVar, gnomAD, MITOMAP, HGNC | **Dosya indirilir, programatik eşleştirilir** |
| **T4** | Mekanizma ders bilgisi | Tek otorite yok | Atıf denetimi + üçe ayırma + uzman değerlendirmesi |
| **T5** | Kitabın özgün pedagojik sentezi | Yok | **Doğrulanmaz — etiketlenir** |

### T4 üçe ayırma kuralı
Atıfsız her mekanistik önerme şu üçünden birine konur:
- **(a)** gerçekten yerleşik ders bilgisi → kaynak gerekmez, kütükte öyle işaretlenir
- **(b)** kaynaklanabilir → kaynak bulunur ve eklenir
- **(c)** aslında çıkarım → **yumuşatılır veya çıkarılır**

Hatalar (c) grubunda saklanır. Kaynaksız, kulağa doğru gelen cümle en riskli cümledir.

### T5 etiketleme kuralı
Kitabın özgün çerçeveleri (allelik serinin altı ekseni, mekanizma × kriter matrisi, ekzomun altı kör noktası, "kanıt tartılır sayılmaz", zincirin kırıldığı üç yer vb.) **yerleşik sınıflama değildir** ve öyle sunulamaz. Her birinin yanına şu anlamda bir not konur:

> *"Bu çerçeve kitabın pedagojik sentezidir; literatürde bu adla yerleşik bir sınıflandırma değildir. Bileşenlerin her biri kaynaklıdır, gruplama editöryaldir."*

---

## 2. ⛔ Kanıt toplama kuralı (ihlal edilemez)

**Doğrulama, veriyi bir modele okutarak yapılamaz.**

`WebFetch` bir sayfayı küçük bir modele okutup özet döndürür ve **uydurabilir**. Bu, 27.07.2026 turunda somut olarak gerçekleşti: ClinGen gen listesi WebFetch ile sorgulandığında model "PAX6: HI = 3" yanıtı verdi; dosya `curl` ile indirilip programatik arandığında **PAX6'nın listede hiç bulunmadığı** görüldü.

| Kullanım | Araç | Kanıt değeri |
|---|---|---|
| Veri tabanı sorgusu (ClinGen, gnomAD, ClinVar…) | **`curl` ile indir + Python ile tam eşleştir** | ✅ Kanıt |
| Kaynak künyesi ve özet | PubMed MCP `get_article_metadata` | ✅ Kanıt |
| Özette olmayan sayı/detay | PMC tam metin (alıntı çıkarılır) | ✅ Kanıt |
| Keşif, yön bulma, belge listesi | `WebFetch` / `WebSearch` | ⚠️ Yalnız keşif — **kanıt değil** |

WebFetch'ten gelen her sayı, kanıt sayılmadan önce programatik olarak teyit edilir.

---

## 3. Kaynak künyesi standardı

Ayrıntı: `Stil_Rehberi.md` §4. Özet:
- 4 veya az yazar → hepsi; 5+ → ilk üç + "ve ark."
- Dergi **tam adı** (kısaltma yok); sayfa aralığı **en-dash**; başlık PubMed'deki tam hâli
- Aynı kaynak birden çok bölümde geçerse **künye birebir aynı** olur
- Her künyede PMID + DOI bağlantısı + kullanım amacı

---

## 4. Bölüm doğrulama turu — işlem sırası

Her bölüm için sırayla:

1. **İddia çıkarımı** — bölüm okunur, doğrulanabilir iddialar numaralanır ve T1–T5 türlerine ayrılır.
2. **T3 taraması** — bölümdeki gen/bölge iddiaları indirilmiş ClinGen dosyalarıyla eşleştirilir.
3. **T2 taraması** — her sayısal iddia kaynağın özetiyle karşılaştırılır; özette yoksa PMC tam metninden alıntı çıkarılır.
4. **T1 taraması** — kriter/kural cümleleri ilgili ClinGen rehber belgesiyle karşılaştırılır.
5. **T4 taraması** — atıfsız mekanistik önermeler (a)/(b)/(c) olarak ayrılır.
6. **T5 etiketleme** — özgün çerçeveler işaretlenir.
7. **Düzeltmeler uygulanır**, kaynakça güncellenir, numaralar yeniden sıralanır.
8. **Kütüğe yazılır** (`Dogrulama_Kutugu.md`), bölüm sonu doğrulama notu güncellenir.
9. **Build alınır**, kaynak sayısı ve bağlantılar kontrol edilir.

---

## 5. Sabit veri kaynakları

Bunlar her turda yeniden aranmaz; adresleri buradadır.

| Kaynak | Adres | Kullanım |
|---|---|---|
| ClinGen gen dozaj listesi | `https://ftp.clinicalgenome.org/ClinGen_gene_curation_list_GRCh38.tsv` | T3 gen düzeyi HI/TS |
| ClinGen bölge dozaj listesi | `https://ftp.clinicalgenome.org/ClinGen_region_curation_list_GRCh38.tsv` | T3 **tekrarlayan bölgeler** |
| ClinGen varyant sınıflandırma rehberleri | `https://www.clinicalgenome.org/tools/clingen-variant-classification-guidance/` | T1 belge listesi |
| PubMed | MCP `search_articles` / `get_article_metadata` | T2 künye ve özet |
| PMC tam metin | `https://pmc.ncbi.nlm.nih.gov/articles/PMC…/` | T2 özette olmayan sayılar |
| Telifli ders kitabı (EPUB/PDF) | `kaynak_pdf/` (git dışı) → `kaynak_cikar.py` → `_metin/` → `ara.py` | **T4** kaynaksız mekanizma cümleleri |

### Telifli materyal iş akışı
1. Dosyalar `kaynak_pdf/` içine konur — bu klasör `.gitignore`'dadır, depoya girmez.
2. `python3 00_Şablonlar/kaynak_cikar.py` → `_metin/*.txt` (EPUB: stdlib; PDF: pypdf; taranmış dosyada uyarı verir, OCR yok).
3. `python3 00_Şablonlar/ara.py "terim" "ikinci terim"` → yalnız ilgili paragraf bağlama girer; her sonuç kaynak + konum işaretiyle döner.
4. **Telifli metin kitaba kopyalanmaz.** Bulunan pasaj yalnızca kütüğe kanıt olarak, kısa alıntı hâlinde kaydedilir.

**Dozaj skoru kodları:** 0 = kanıt yok · 1 = az kanıt · 2 = bir miktar kanıt · 3 = yeterli kanıt · 30 = otozomal resesif fenotiple ilişkili gen · 40 = doz duyarlılığı olası değil.

**Kritik uyarı:** ClinGen dozaj küreleri **gen** ve **bölge** olmak üzere iki ayrı listede tutulur. Tekrarlayan CNV bölgeleri (17p12, 11p13, 15q11-q13, 22q11.2…) ve imprintli lokuslar (SNRPN, NDN, H19, IGF2…) için **gen düzeyi skor yanıltıcıdır**; bölge kaydına bakılır. Ayrıca **bir genin listede olmaması, doza duyarlı olmadığı anlamına gelmez** (ör. PAX6 listede yoktur).

---

## 6. Bilinen ve kabul edilen sınır

**Model, bilmediği bir hatayı yakalayamaz.** Eğitim verisinde ince bir yanlış varsa, iddia kaynaksızsa ve kulağa doğru geliyorsa T4-(a) diye işaretlenip geçilir. Bu kategori hiçbir otomatik denetimle sıfırlanmaz.

**Bu yüzden uzman değerlendirmesi vazgeçilmezdir** — "iyi olur" değil, yayım ön koşuludur. En az 2–3 alan uzmanı (klinik genetik uzmanı, moleküler genetik laboratuvar sorumlusu, genetik danışman), bölüm bölüm, imzalı değerlendirme.

---

## 7. İlerleme

| Bölüm | Durum | Tarih |
|---|---|---|
| 3 | ✅ Tamamlandı (19 iddia; 0 olgusal yanlış, 6 iyileştirme) | 27.07.2026 |
| Kitap geneli T3 gen taraması | ✅ Tamamlandı (79 gen; 0 çelişki) | 27.07.2026 |
| 1, 2, 4–17 | 🔲 Bekliyor | — |
| T1 ClinGen rehber taraması (Böl. 7, 12, 15, 16) | 🔲 Bekliyor | — |
| T4/T5 kitap geneli | 🔲 Bekliyor | — |
| Uzman değerlendirmesi | 🔲 Bekliyor — **kullanıcı organize edecek** | — |
