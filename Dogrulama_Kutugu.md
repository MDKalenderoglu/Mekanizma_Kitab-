# Doğrulama Kütüğü

Bu dosya, kitaptaki iddiaların **hangi otoriteye karşı, nasıl ve ne sonuçla** denetlendiğini kaydeder. Amacı hatasızlık iddiası değil, **denetlenebilirliktir**. Tamamlandığında kitabın "Doğrulama Yöntemi" ekine dönüşecektir.

## İddia türleri ve otoriteleri

| Tür | İçerik | Otorite | Doğrulanabilir mi? |
|---|---|---|---|
| **T1** | Normatif/kılavuz kuralı | ClinGen rehber belgeleri + kılavuz makaleleri | Evet, kesin |
| **T2** | Spesifik çalışma bulgusu (sayı, oran, kohort) | Kaynağın özeti/tam metni | Evet, ikili |
| **T3** | Gen–varyant–hastalık eşleşmesi | ClinGen Dosage/Gene-Disease Validity, ClinVar, gnomAD, MITOMAP | Evet |
| **T4** | Mekanizma ders bilgisi | Tek otorite yok — atıf denetimi + uzman değerlendirmesi | Kısmen |
| **T5** | Kitabın özgün pedagojik sentezi | Yok — **doğrulanmaz, etiketlenir** | Hayır |

## Durum kodları

✅ doğrulandı · ⚠️ düzeltme/ekleme gerekli · ❌ yanlış, düzeltildi · 🔲 doğrulanamadı (işaretlenecek) · 🏷️ etiketlenmeli

---

# Bölüm 3 — Haploinsufficiency (pilot, tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Denetlenen iddia:** 19 · **Kullanılan otorite:** PubMed özet/tam metin, ClinGen Dosage Sensitivity Map (gen ve bölge listeleri)

## T2 — Çalışma bulguları

| # | İddia (kitapta) | Kaynak | Otoriteden gelen | Durum |
|---|---|---|---|---|
| 3.1 | "Yaklaşık bir milyon bireyin nadir CNV'lerini birleştiren meta-analiz" | Collins 2022 | *"rCNVs from nearly one million individuals"* | ✅ |
| 3.2 | "her otozomal gen için pHaplo/pTriplo skorları" | Collins 2022 | *"for all autosomal genes"* | ✅ |
| 3.3 | **"pHaplo ≥0,86 → HI"** | Collins 2022 | Tam metin: *"2,987 haploinsufficient (pHaplo≥0.86) and 1,559 triplosensitive (pTriplo≥0.94)"* | ✅ **tam metinden teyitli** |
| 3.4 | HI genleri daha uzun, kodlayan dizi ve promotörleri daha korunmuş | Huang 2010 | *"HI genes are typically longer and have more conserved coding sequences and promoters"* | ✅ |
| 3.5 | Erken gelişimde daha yüksek ifade, daha doku-özgü | Huang 2010 | *"higher levels of expression during early development and greater tissue specificity"* | ✅ |
| 3.6 | "protein-etkileşim ağında daha merkezi düğümler" | Huang 2010 | Makale *"functional interaction network"* diyor — protein-protein değil **işlevsel** etkileşim ağı | ⚠️ terim düzeltilecek |
| 3.7 | Tbx5 haploinsufficiency'si *ANF* ve *connexin 40* transkripsiyonunu azaltır | Bruneau 2001 | *"markedly decreased atrial natriuretic factor (ANF) and connexin 40 (cx40) transcription… 50% reduction"* | ✅ |
| 3.8 | Aile içi değişken ekspresivite (Holt-Oram) | Bruneau 2001 | *"suggest mechanisms for intrafamilial phenotypic variability"* | ✅ |
| 3.9 | CNV çerçevesi beş kademeli sınıflama + "uncoupling" | Riggs 2020 | *"five-tier classification system"; "recommends 'uncoupling' the evidence-based classification… from its potential implications for a particular individual"* | ✅ |
| 3.10 | PAX6'da 500'den fazla varyant tanımlanmış | Lima Cunha 2019 | *"more than 500 different mutations described"* | ✅ |
| 3.11 | Seidman & Seidman'ın TF HI'yi kavramsallaştırması | Seidman 2002 | Tam metin: *"half-normal levels of many transcription factors are simply not enough"*; TBX5, NKX2-1, FOXC2, PAX3, TBX1 örnekleri; **30'dan fazla sendrom** | ✅ ama **yazı türü** "commentary/editorial" — metinde belirtilmeli; "30+ sendrom" verisi eklenebilir |

## T3 — Gen/bölge dozaj iddiaları (ClinGen Dosage Sensitivity Map)

| # | İddia | ClinGen kaydı | Durum |
|---|---|---|---|
| 3.12 | PAX6 haploinsufficiency prototipi | **PAX6, ClinGen gen dozaj listesinde HİÇ YOK** (dosyada 0 eşleşme; PAX2/3/5/8/9 var). İddia birincil literatürle desteklidir (Lima Cunha 2019), ClinGen küresi yoktur | ⚠️ metne "küreleme eksikliği" notu eklendi |
| 3.13 | TBX5 HI → Holt-Oram | Gen TBX5 · **HI = 3** | ✅ |
| 3.14 | NF1 HI → NF tip 1 | Gen NF1 · **HI = 3** | ✅ |
| 3.15 | WAGR: PAX6+WT1 birlikte delesyonu | Gen WT1 · **HI = 3**; Bölge **ISCA-37401 "11p13 (WAGR syndrome) region" HI = 3** | ✅ |
| 3.16 | **PMP22: delesyon→HNPP, duplikasyon→CMT1A** | Gen PMP22 · HI = 3, **TS = 0 ("kanıt yok")**; Bölge **ISCA-37436 "17p12 recurrent (HNPP/CMT1A) region (includes PMP22)" HI = 3, TS = 3** — indirilmiş TSV'den programatik olarak teyitli | ⚠️→✅ **düzeltildi** (§4.6'ya kutu eklendi) |

### ⚠️ Bulgu 3.16 — kitabın düzeltilmesi gereken en önemli noktası

Kitap §4.6 ve §6, okuyucuya "duplikasyonu otomatik benign sayma, ClinGen dozaj skorlarına bak" diyor ve örnek olarak PMP22/CMT1A veriyor. Ancak ClinGen'de **gen düzeyinde PMP22 triplosensitivity skoru 0'dır** ("kanıt yok"); duplikasyon patojenitesi **bölge düzeyinde** (17p12 tekrarlayan bölge, ISCA-37436, TS = 3) küre edilmiştir.

Kitabın anlattığı biyoloji doğru, ama **verdiği aracı kullanan okuyucu yanlış sonuca varır**: PMP22'yi gen listesinde arayıp TS = 0 görür ve "duplikasyon kanıtlanmamış" diye düşünür — yani kitabın uyardığı hatanın tam kendisini yapar.

**Düzeltme:** ClinGen Dozaj Haritası'nın **gen** ve **bölge** olmak üzere iki ayrı küre listesi tuttuğu; tekrarlayan CNV bölgelerinin (17p12, 11p13 gibi) bölge kaydında aranması gerektiği açıkça yazılmalı.

## T4 — Atıfsız mekanizma iddiaları

| # | İddia | Değerlendirme | Eylem |
|---|---|---|---|
| 3.17 | "Enzimler substrat doygunluğu ve metabolik yedekle çalıştığı için akı %50 dozda korunur" | Bu, dominansın metabolik kontrol kuramına dayanan klasik açıklamasıdır; yerleşik ama **kaynaksız** | Kaynak eklenmeli (metabolik kontrol analizi literatürü) |
| 3.18 | "Dengeli ifade hipotezi (balance hypothesis)" | Adı verilen, gerçek bir hipotez; **kaynaksız** | Kaynak eklenmeli |
| 3.19 | Morfojen gradyanı ve eşik-bağımlı hücre kaderi | Yerleşik gelişim biyolojisi; kaynaksız | Kaynak eklenmeli ya da "yerleşik ders bilgisi" olarak etiketlenmeli |

## T1/T5 — Diğer

| # | İddia | Durum |
|---|---|---|
| 3.20 | pLI ve LOEUF'un "Karczewski 2020" kaynağına birlikte atfı | ⚠️ LOEUF bu makalenin; **pLI'nin kökeni ExAC (Lek ve ark., 2016)**. Atıf hassaslaştırılmalı |
| 3.21 | "Delesyonun önemi boyutuyla değil içerdiği HI geniyle belirlenir" → yalnız Riggs 2020'ye atfedilmiş | ⚠️ Bu bulguyu **Huang 2010 doğrudan göstermiştir** (*"better discriminate between pathogenic and benign deletions than… deletion size or numbers of genes deleted"*). Atıf eklenmeli |
| 3.22 | Şekil 3.4 "dozaj duyarlılığı spektrumu" çerçevesi | 🏷️ Kitabın pedagojik sentezi — etiketlenmeli |

---

## Bölüm 3 özeti

| Sonuç | Sayı |
|---|---|
| ✅ Doğrulandı (değişiklik gerekmez) | **10** |
| ⚠️ Düzeltme/ekleme gerekli | **6** |
| Kaynak eklenmesi gereken atıfsız iddia | **3** |
| 🏷️ Etiketlenecek özgün sentez | **1** |
| ❌ **Olgusal yanlış** | **0** |

**Yorum:** Doğrulanabilir iddiaların hiçbirinde olgusal hata çıkmadı. Buna karşılık **altı iyileştirme** gerekli ve bunlardan biri (3.16 — PMP22 gen/bölge ayrımı) okuyucuyu pratikte yanlış sonuca götürebilecek gerçek bir öğretim kusurudur. Bu, denetimin neden gerekli olduğunun somut kanıtıdır: hata "yanlış bilgi"de değil, **bilginin eksik bağlamında** çıktı.

---

## ⛔ Yöntem dersi — WebFetch uydurabilir

Bu turda **kritik bir metodolojik bulgu** çıktı. ClinGen gen listesi önce `WebFetch` ile (sayfayı küçük bir modele okutarak) sorgulandı; model **"PAX6: HI = 3"** yanıtını verdi. Aynı dosya sonradan `curl` ile indirilip programatik olarak arandığında **PAX6'nın dosyada hiç bulunmadığı** görüldü (0 eşleşme). Aynı çağrıdaki bölge kayıtları (ISCA-37436, ISCA-37401) ise **doğru** çıktı.

**Kural:** Doğrulama, veriyi bir modele okutarak yapılamaz. Birincil veri dosyası **indirilir ve programatik olarak (tam eşleşme ile) sorgulanır**. `WebFetch` yalnızca keşif/yön bulma için kullanılır, kanıt olarak kullanılmaz.

---

# Kitap geneli — T3 gen dozaj taraması (tamamlandı)

**Kaynak:** ClinGen Gene Curation List GRCh38 (26.07.2026, 1.520 gen) + Region Curation List (519 bölge), doğrudan indirildi ve programatik eşleştirildi.
**Kapsam:** Gen Dizini'ndeki 79 genin tamamı.

| Sonuç | Sayı | Not |
|---|---|---|
| ClinGen'de kayıtlı ve kitapla **uyumlu** | 43 | HI/TS skorları kitabın mekanizma iddialarıyla çelişmiyor |
| ClinGen'de **kaydı yok** | 36 | Küreleme eksikliği; kitabın iddiası birincil literatüre dayanıyor — hata değil |
| **Çelişki** | **0** | |
| **Bağlam eksikliği (düzeltildi)** | 1 | PMP22 gen/bölge ayrımı |

**Dikkat çeken kayıtlar (kitapla uyumlu, bilgi amaçlı):**

- `CFTR`, `PAH`, `RYR1`, `COL4A3`, `LMBR1`, `DGUOK`, `NDUFS4`, `NDUFV1`, `SUCLG1`, `SURF1`, `TYMP` → **HI = 30 "otozomal resesif fenotiple ilişkili gen"**. Kitap bu genleri haploinsufficiency örneği olarak sunmuyor; uyumlu.
- `FGFR3` → HI = 0, TS = 0. Kitap FGFR3'ü işlev **kazanımı** geni olarak işliyor; uyumlu ve destekleyici.
- `COL1A1` HI = 3 ama `COL1A2` HI = 0 → Bölüm 5/15'te "null alel → hafif tip I" iddiası **COL1A1'e özgüdür**; metin bunu genelleştirmemeli. 🔲 *Bölüm 5 turunda kontrol edilecek.*
- `SNRPN`, `NDN`, `H19`, `IGF2` → gen düzeyi HI = 0. Bunlar **imprintli** lokuslardır; mekanizma bölge/damgalama düzeyindedir. PMP22 ile aynı ders: 🔲 *Bölüm 10 turunda "gen skoru yanıltıcı olabilir" notu eklenecek.*

---

# Kalan bölümler

🔲 Bölüm 1, 2, 4–17 — iddia düzeyinde denetlenmedi.
🔲 Açık kalem: §2.1'deki "enzimler substrat doygunluğu ve metabolik yedekle çalışır → akı korunur" iddiası kaynaksız (yerleşik ders bilgisi). Metabolik kontrol/dominans literatüründen kaynak aranacak.
