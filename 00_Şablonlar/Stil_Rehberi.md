# Stil Rehberi — Mekanizma Kitabı

Bu rehber, tüm bölümlerde tutarlı ton, biçim ve görsel standardını sağlar.

## 1. Ton ve dil
- **Türkçe**, akademik ama öğretici. Hedef: hem tıp öğrencisi hem uzman okuyabilsin.
- Gereksiz basitleştirme yok; ama her zor kavram **örnek/benzetme** ile desteklenir.
- Özet değil **textbook**: kavramlar nüanslarıyla, "neden böyle" açıklanarak verilir.
- Cümleler net; her iddia ya temel ders bilgisi ya da kaynaklı.

## 1B. Yazım üslubu — ANLATI ÖNCE (en kritik kural)
- Bölümler **akıcı paragraflarla** yazılır. Madde listesi bir kavramı *açıklamaz*, yalnızca *sıralar*; bu yüzden anlatımın ana taşıyıcısı **paragraf**tır.
- **Madde listesi yalnızca şunlar için:** kaynakça, hızlı-referans/özet, gerçek adım listeleri, karşılaştırma maddeleri. Bir terimi/mekanizmayı tanıtırken **paragraf kullan**, madde değil.
- **Her zor kavram için "öğretme döngüsü":** (1) sezgisel giriş/benzetme → (2) tanım → (3) nasıl ölçülür/işler → (4) **neden klinik olarak önemli** → (5) somut örnek. Örnek: pLI/LOEUF/HI anlatılırken önce "bir genin hata kaldırıp kaldıramadığını popülasyondan nasıl anlarız?" sezgisi verilir, sonra metrik tanımlanır.
- **Terimleri akış içinde tanıt:** ilk geçişte **kalın** yaz ve cümle içinde tanımla; ayrı bir sözlük maddesi yapma (gerekiyorsa paragrafların ardından kısa özet tablo eklenebilir).
- Tablolar ve görseller **paragrafı destekler/özetler**, yerini almaz. Her tablo/şekil öncesinde veya sonrasında onu yorumlayan metin bulunur.
- Okuyucuyu yormadan ama **eksiksiz** anlat; bir uzmanın "yüzeysel" demeyeceği, bir öğrencinin "anlamadım" demeyeceği denge hedeflenir.

## 1C. Atıf üslubu (textbook tarzı)
- **Cümleyi "Based on articles retrieved from PubMed" ile başlatma.** Bu ifade textbook akışını bozar; yalnızca her bölümün **Kaynaklar** bölümündeki tek bir doğrulama/atıf notunda yer alır.
- Metin içinde **yazar-yıl** kullan: "… (Karczewski ve ark., 2020)". Çok sık tekrarlanan kaynaklarda bir kez bağla, sonra akışı sürdür.
- **DOI linkleri kaynakçada** verilir (her madde sonunda). Gerektiğinde metinde de DOI linki verilebilir ama cümle akışını bozmadan.
- PubMed MCP atıf yükümlülüğü: Kaynaklar bölümünde "Bu bölümün bibliyografik verileri PubMed üzerinden doğrulanmıştır" notu + her kaynakta DOI linki ile karşılanır.

## 2. Biçim ögeleri (her bölümde)
- **Çekirdek tez** (başta, blockquote).
- **Öğrenme hedefleri** (numaralı, ölçülebilir fiiller).
- **Deep-dive kutusu:** `> **🔬 Deep-dive — başlık:** …` (mekanizma nüansı için, bölümde ≥1).
- **Klinikte dikkat kutusu:** `> **🟦 Klinikte dikkat — …**`
- **Sık yapılan hata kutusu:** `> **🔴 Sık yapılan hata kutusu**`
- **Hatırlatıcı / mnemonik:** `> **🧠 …**` (uygun olduğunda).
- Bol **yayın tablosu**: kavram tabloları, varyant-tipi tabloları, test tablosu ve karşılaştırma tabloları. Kaynak Markdown'daki iç öz-denetim tablosu korunur ancak derlenen HTML/PDF'ye ve Tablolar Listesi'ne girmez.

## 3. Görsel standardı (v2)

> **⚠️ Bağlayıcı tanım burada değil:** görsel standardının **tek source-of-truth'u** `00_Şablonlar/Görsel_Doktrini_v2.md` dosyasıdır. Palet hex değerleri, tipografi ölçüleri, zorunlu yapısal iskelet, ince işçilik, ok-ucu (`markerUnits`) tuzağı, render + gözle denetim yordamı ve kırılmaz teknik kurallar **orada** tanımlıdır. Bu bölüm o ayrıntıyı **tekrarlamaz**; yalnız yönlendirir. Bir uyuşmazlık görürsen doktrin geçerlidir.

**Felsefe:** Görsel bir "şema" değil, bir **ders sayfasıdır**: sakin, editöryal, anlatıyı taşıyan. Renk dekorasyon değil **anlam** taşır (semantik). Az sayıda renk, tutarlı anlamla — gökkuşağı palet yok. Her figür tek başına okunabilir: başlık + panel yapısı + bir "öğreti" satırı.

### 3.1 Nereye bakılır

| Konu | Bağlayıcı kaynak |
|---|---|
| Semantik palet (tam hex listesi) ve emekli eski palet | `Görsel_Doktrini_v2.md` → "Palet" |
| Tipografi ve punto hiyerarşisi | aynı → "Tipografi" |
| Okunurluk ve **çakışma yasağı** | aynı → "OKUNURLUK + ÇAKIŞMA YASAĞI" |
| Zorunlu yapısal iskelet (panel rozeti, başlık, öğreti footer'ı, kaynak notu) | aynı → "Yapısal iskelet" |
| Ok-ucu / `markerUnits` tuzağı | aynı → "OK-UCU (marker) TUZAĞI" |
| **Render + gözle denetim yordamı** | aynı → "RENDER + GÖZLE DENETİM ZORUNLU" |
| Teknik kurallar (`viewBox`, beyaz zemin, CSS değişkeni yasağı, `&amp;`) | aynı → "Teknik kurallar" |

### 3.2 Yönelim için kısa özet (ayrıntı doktrinde)

- **Renk anlam taşır:** nötr/yapı = slate · mavi = LoF / normal-kontrollü / yapı · kırmızı = GoF / patojen / aşırı aktivite · amber = vurgu ve klinik dikkat · sarı yıldız (★) = "varyant burada". Eski doygun web paleti **kullanılmaz.** Tam hex değerleri doktrinde.
- **Hiçbir metin başka metnin, çizginin veya kutunun üzerine binmez**; minimum punto ≥9px. Bu bir zevk kuralı değil, kalite kapısıdır.
- **Beyaz zemin + `viewBox` + CSS değişkeni yok + `&` yerine `&amp;`** — figürler `img` olarak izole render edilir.
- **Bitirmeden önce zorunlu üç adım:** `xmllint --noout` → en-boy oranını koruyan proje renderer'ı → **PNG'ye gözle bak.** Yordam, tek render standardı ve `qlmanage` yasağının gerekçesi doktrindedir.

### 3.3 Mermaid (kod bloğu) — bu bölümde tanımlı

- Karar ağaçları / algoritmalar / sınıflandırma için kullanılır; mekanizma şeması, anatomi, eğri, pedigri ve spektrum için SVG kullanılır.
- Etiketleri `"..."` içine al; satır sonu `<br/>`; parantez ve özel karakterleri tırnak içinde kullan.
- `flowchart TD` (yukarıdan aşağı) varsayılan.

### 3.4 Minimum sayı — bu bölümde tanımlı

Bölüm başına **≥3 SVG** + **≥2 Mermaid**. Üst sınır yoktur; konu gerektiriyorsa daha fazlası yapılır (CLAUDE.md §2.6).

## 4. Atıf biçimi (final pass'te standardize edildi — bu biçim bağlayıcıdır)
> **Kaynak türü makale değilse:** kılavuz / uzman panel spesifikasyonu (HGVS, ClinGen SVI, VCEP/CSpec, ACMG teknik standardı, ACGS, EMQN) **kurum + belge + sürüm + tarih + kalıcı bağlantı + erişim tarihi** ile; veri tabanı kaydı **veri sürümü + sorgu tarihi** ile künyelenir. Aşağıdaki biçim dergi makalesi içindir; diğer türler için bağlayıcı tanım `Kaynak_Protokolü.md` §1 ve CLAUDE.md §2.4'tedir (PMID/DOI verilemeyen kaynak bu yüzden **çıkarılmaz** — kimlik biçimi esner, titizlik esnemez).

- **Metin içi:** yazar-yıl → "… (Richards ve ark., 2015)". Cümleyi "Based on articles retrieved from PubMed" ile BAŞLATMA; bu yükümlülük Kaynaklar bölümündeki doğrulama notu + her maddedeki DOI linki ile karşılanır.
- **Kaynakça maddesi (tek biçim):**
  `N. **Yazar1 XX, Yazar2 YY, Yazar3 ZZ, ve ark. (Yıl).** Tam başlık. *Derginin tam adı* cilt(sayı):sayfa–sayfa. **PMID: …** · DOI: [10.xxxx/…](https://doi.org/10.xxxx/…) — *Kullanım amacı: …*`
- **Yazar listesi:** 4 veya daha az yazar → hepsi yazılır; 5+ → ilk üç yazar + "ve ark.".
- **Dergi adı:** kısaltma DEĞİL, **tam ad** ("Genetics in Medicine", "American Journal of Human Genetics", "Proceedings of the National Academy of Sciences USA"). Tek istisna, resmî adı parantezli olan dergilerdir: *Genes (Basel)*.
- **Sayfa aralığı:** en-dash (`405–424`), kısa çizgi değil. Elektronik sayfa ekleri korunur (`535–548.e24`).
- **Başlık:** PubMed'deki tam başlık; kısaltma/üç nokta kullanılmaz.
- Aynı kaynak birden çok bölümde geçiyorsa **künye birebir aynı** olmalıdır (yalnız "Kullanım amacı" bölüme göre değişir). Toplu kaynakça bu künyelerden otomatik üretilir.

## 5. Terminoloji tutarlılığı (final pass kararları)
- "Varyant" (nötr) tercih; "mutasyon"u yalnız yerleşik adlandırmalarda kullan (*tam mutasyon*, *premutasyon*, *gsp mutasyonu* gibi).
- İngilizce teknik terimi ilk geçişte parantezle Türkçeleştir: "haploinsufficiency (yetersiz doz)"; sonrasında tek biçimde devam et.
- Kısaltmalar ilk geçişte açılır (NMD, LoF, GoF, DN, CNV, UPD, VUS…).
- **Sabitlenen tercihler:** `nonsense` (nonsens değil) · `hotspot` (ilk geçişte "hotspot (sıcak nokta)", sonra hotspot) · `eksik penetrans` (azalmış penetrans değil) · `dizileme` (sekanslama değil) · `dominant-negatif` (tireli).
- **Latince ifadeler:** `de novo` **düz** yazılır (Türkçe klinik genetikte yerleşiktir); `*in vitro*`, `*in silico*`, `*in cis*`, `*in trans*` **italik** yazılır.
- Gen adları italik (*LMNA*), protein adları düz (lamin A/C).

## 6. Kalite çıtası (her bölüm bunu geçmeli)
- Mekanizma → varyant → hücre → fenotip → test → yorum zinciri kurulmuş mu?
- En az 2-3 somut, kaynaklı pediatrik örnek var mı?
- Görsel ve algoritma minimumları karşılanmış mı?
- **Bibliyografik doğrulama:** her künye kaynak türüne uygun kalıcı kimliğiyle doğrulandı mı (makale: PMID+DOI; kılavuz: belge+sürüm+tarih; veri tabanı: sürüm+sorgu tarihi)?
- **İddia düzeyi doğrulama (ayrı denetim):** her iddia T1–T5 türüne göre kendi otoritesiyle karşılaştırıldı mı? "X/X künye doğrulandı" cümlesi bunun yerine **geçmez** (`Dogrulama_Protokolu.md` §0 · CLAUDE.md §2.5).
- Spekülasyon ⚠️ ile, kitabın özgün pedagojik çerçeveleri 🏷️ ile işaretli mi?
