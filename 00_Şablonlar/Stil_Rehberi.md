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

## 3. Görsel standardı (v2 — editöryal textbook standardı)

> **Felsefe:** Görsel bir "şema" değil, bir **ders sayfasıdır**: sakin, editöryal, anlatıyı taşıyan. Renk dekorasyon değil **anlam** taşır (semantik). Az sayıda renk, tutarlı anlamla — gökkuşağı palet yok. Her figür tek başına okunabilir: başlık + panel yapısı + bir "öğreti" satırı.

### 3.1 Renk paleti (v2 — tek kaynak; eski doygun palet emekli)
**Nötr/yapı (slate ölçeği):** mürekkep/başlık `#1A2B4A`, gövde metin `#2E3440`, ikincil `#475569`/`#64748B`, çizgi/kenar `#CBD5E1`/`#94A3B8`, dolgu `#E2E8F0`/`#F1F5F9`/`#F8FAFC`.

**Semantik renkler (sabit anlam — değiştirme):**
| Renk | Ana / dolgu / koyu | Anlam |
|---|---|---|
| 🔵 Mavi | `#2563EB` / `#DBEAFE` / `#1D4ED8` | LoF, normal-kontrollü, "Senaryo 1", yapı/protein |
| 🔴 Kırmızı | `#B91C1C` / `#FEE2E2` / `#FEF6F5` | GoF, patojen/ağır, "Senaryo 2", aşırı aktivite |
| 🟠 Amber | `#D97706` / `#FEF3C7` / `#B45309` | Vurgu, klinik dikkat, fosforilasyon (P), öğreti kutusu |
| 🟡 Sarı yıldız | `#FCD34D` + kenar `#92400E` | "varyant burada" işareti (★) |

> Eski palet (#e74c3c, #27ae60, #2980b9, #8e44ad …) artık KULLANILMAZ.

### 3.2 Tipografi
`font-family="Inter, 'Source Sans 3', 'Helvetica Neue', Arial, sans-serif"`. Hiyerarşi: panel başlığı ~14px/700, etiket ~11–12px/600-700, alt-not/öğreti ~9.5–10.5px, italik kaynak/nüans notu `#64748B`/`#94A3B8`.

### 3.3 Okunurluk ve çakışma YASAĞI (zorunlu kalite kuralı)
- **Hiçbir metin başka metnin, çizginin veya kutunun üzerine binmez.** Öğeleri yerleştirmeden önce koordinatları/boyutları hesapla; metin kutusunun içine sığdığını doğrula.
- **Metin daima okunur:** görselde minimum yazı **≥9px** (tercihen ≥10px); kritik etiketler daha büyük. Düşük kontrastlı metni açık zemine koyma.
- **Uzun metni böl:** tek satıra sığmayan ifadeyi `<tspan>` ile alt satıra al; kutu genişliğini metne göre ayarla (taşma yok).
- **Ferah boşluk:** kutular/oklar arası nefes payı bırak; sıkışık yığma yok. `text-anchor` (start/middle/end) ile hizala.
- **Doğrulama (zorunlu — gözle bak):** `xmllint` yalnız XML geçerliliğini test eder, görsel çakışmayı GÖSTERMEZ. Her SVG yazıldıktan sonra **PNG'ye render edilip gözle denetlenir:** `qlmanage -t -s 1300 -o /tmp/svgcheck assets/sekil_NN_*.svg` → PNG'yi aç ve bak. Çakışma/taşma/metnin şekil arkasında kaybolması varsa düzelt, yeniden render et, tekrar bak. Körlemesine bırakma.

### 3.4 Zorunlu yapısal iskelet
- **Panel rozeti:** köşeye `#1A2B4A` yuvarlatılmış kare + beyaz harf (A, B, C…) — çok panelli figürlerde.
- **Panel başlığı:** her panel üstünde semantik renkli, 700 ağırlık başlık.
- **Karşılaştırma figürü:** sol = mavi (normal/LoF), sağ = kırmızı (patojen/GoF); ortada kesik dikey ayraç.
- **"Mekanizma → test → yorum" şeridi** (uygun figürlerde alt bant) — kitabın çekirdek pedagojisini tekrarlar.
- **Öğreti satırı (footer):** en altta tek cümlelik ders.
- **Kaynak notu:** kaynaklı figürde alt köşede küçük `#64748B` "Kaynaklar: Yazar (yıl)…".

### 3.5 İnce işçilik
- `<defs>` içinde **yumuşak gölge** (`feDropShadow dy=1.5 stdDeviation=2 opacity=0.10`) ve **ok-uçları (marker)**; ok renkleri semantik (mavi/kırmızı ayrı).
- Yuvarlatılmış kutular (`rx≈8–14`), hizalı grid, nicel gösterim (az P vs çok P, ★ varyant).

### 3.6 Teknik kurallar (kırılmaz)
- `viewBox` ile ölçeklenir; ilk eleman `<rect ... fill="#ffffff"/>` (beyaz zemin).
- **CSS değişkeni kullanma** (img olarak izole render edilir → renkler sabit verilir).
- **`&` asla doğrudan → `&amp;`** (kaçırılmamış `&` SVG'yi bozar).
- Türkçe etiketler; her şekilde başlık + öğreti satırı.
- Çizimden sonra `xmllint --noout assets/*.svg` ile doğrula.
- Mekanizma şeması, anatomi, eğri, pedigri, spektrum için kullanılır.

### Mermaid (kod bloğu)
- Karar ağaçları/algoritmalar/sınıflandırma için.
- Etiketleri `"..."` içine al; satır sonu `<br/>`; parantez/özel karakterleri tırnak içinde kullan.
- `flowchart TD` (yukarıdan aşağı) varsayılan.

### Minimum sayı
- Bölüm başına **≥3 SVG** + **≥2 Mermaid**.

## 4. Atıf biçimi (final pass'te standardize edildi — bu biçim bağlayıcıdır)
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
- Tüm kaynaklar PMID+DOI doğrulanmış mı? Spekülasyon işaretli mi?
