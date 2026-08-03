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

# Bölüm 1 — Genetik hastalık mekanizması nedir? (tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Denetlenen iddia:** 14 · **Kullanılan otorite:** PubMed künye/özet; ders kitabı çapraz kontrolü (Emery & Rimoin 2019 böl. 4, 7, 9; Gardner & Sutherland 2018)

## T2 — Kaynak künyesi ve içerik uyumu

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 1.1 | Richards 2015 künyesi (*Genet Med* 17(5):405–424, PMID 25741868) | PubMed künyesiyle birebir; beş kademeli terminoloji özet düzeyinde teyitli | ✅ |
| 1.2 | MacArthur 2014 künyesi (*Nature* 508(7497):469–476, PMID 24759409) | Birebir; *"risk an acceleration of false-positive reports of causality"* — kitabın "yanlış-pozitif nedensellik" cümlesini doğrudan destekler | ✅ |
| 1.3 | Karczewski 2020 künyesi (*Nature* 581(7809):434–443, PMID 32461654) | Birebir; 125.748 ekzom + 15.708 genom = 141.456 birey | ✅ |
| 1.4 | Cooper 2013 künyesi (*Hum Genet* 132(10):1077–1130, PMID 23820649) | Birebir; özet, kitabın saydığı eksik penetrans nedenlerini (allel dozu, diferansiyel allelik ekspresyon, CNV, cis/trans modifiye ediciler, yaş, cinsiyet, epigenetik) tek tek içeriyor | ✅ |

## T4 — Atıfsız iddiaların çapraz kontrolü

| # | İddia | Çapraz kontrol | Sonuç |
|---|---|---|---|
| 1.5 | "Genom yaklaşık **3,2 milyar** bp" | Emery & Rimoin böl. 4, s.1: *"approximately 3.1 billion bp"* | ⚠️→✅ **3,1 milyar** olarak düzeltildi |
| 1.6 | "Nükleozom: ~147 bp DNA, sekiz histonluk oktamer" | Emery & Rimoin böl. 9, s.1: *"147 bp of DNA wrapped around"*, dört çekirdek histondan ikişer molekül | ✅ T4-(a) yerleşik |
| 1.7 | Penetrans = taşıyıcıların kaçı hastalanır; ekspresivite = tablonun şiddeti | Emery & Rimoin böl. 7, §7.5.3: *"the degree to which a particular phenotype is expressed"*; aynı ailede aynı varyantın değişken şiddeti | ✅ T4-(a) yerleşik |
| 1.8 | Karyotip çözünürlüğü "~5–10 Mb" | Gardner & Sutherland, s.57: 3–5 Mb'lik del/dup'lar **yüksek çözünürlüklü bantlama** gerektirmiştir | ⚠️→✅ satır rutin/yüksek çözünürlük ayrımıyla yeniden yazıldı |
| 1.9 | "Mitokondriyal kalıtımda varyant babadan hiçbir çocuğa geçmez" | Emery & Rimoin böl. 10, s.5: *"exclusively maternally inherited"* — ders kitabıyla uyumlu | ✅ ders kitabı düzeyinde doğru; 🔲 *nadir biparental aktarım tartışması Bölüm 11 turunda ele alınacak* |
| 1.10 | Nondisjunction → trizomi; telomer koruyucu başlık; X-inaktivasyonu doz dengeleme | Yerleşik ders bilgisi | ✅ T4-(a) |

## T1 — Normatif iddialar

| # | İddia | Durum |
|---|---|---|
| 1.11 | "PVS1 yalnızca LoF'un o gen için bilinen mekanizma olduğu durumlarda anlamlıdır" — §6'da **kaynaksız** öne sürülmüştü | ⚠️→✅ ClinGen SVI PVS1 iyileştirmesine bağlandı (**Abou Tayoun ve ark., 2018**, PMID 30192042) |
| 1.12 | pLI ve LOEUF'un birlikte **Karczewski 2020**'ye atfı | ⚠️→✅ pLI'nin kökeni **ExAC (Lek ve ark., 2016**, PMID 27535533); atıf ayrıştırıldı. *Bölüm 3 bulgusu 3.20 ile aynı kusur — kitap genelinde tarandı* |

## T5 — Etiketlenen özgün çerçeveler

| # | Çerçeve | Eylem |
|---|---|---|
| 1.13 | "Rezerv ve eşik" birleştirici deep-dive'ı | 🏷️ etiketlendi — bileşenleri kaynaklı, gruplama editöryal |
| 1.14 | "Penetrans = Presence / Ekspresivite = Extent" bellek desteği | 🏷️ etiketlendi — kitabın kendi anlatım aracı |

## Bölüm 1 özeti

| Sonuç | Sayı |
|---|---|
| ✅ Doğrulandı (değişiklik gerekmez) | **8** |
| ⚠️ Düzeltildi | **4** (3,2→3,1 milyar bp · karyotip çözünürlüğü · PVS1 atfı · pLI atfı) |
| 🏷️ Etiketlenen özgün sentez | **2** |
| ❌ **Olgusal yanlış** | **0** |

**Yorum:** İki atıf kusuru (1.11, 1.12) olgusal yanlış değil ama **izlenebilirlik kusurudur**: okuyucu, kitabın normatif bir kuralı hangi belgeye dayandırdığını göremiyordu. pLI atfı, Bölüm 3'te de çıkan aynı hatanın tekrarıdır — bu, kusurun tek bir bölüme özgü olmadığını, kitap genelinde taranması gerektiğini gösterir.

---

# Bölüm 2 — Loss-of-function (tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Denetlenen iddia:** 13 · **Kullanılan otorite:** PubMed künye/özet; ders kitabı çapraz kontrolü

## T2 — Çalışma bulguları

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 2.1 | NMD, PTC'li transkriptleri yıkar; kaçış → DN/GoF etkili toksik protein; NMD bilgisi genotip-fenotip için gerekli | Khajavi 2006 özeti: *"Failure to eliminate these mRNAs with PTCs may result in the synthesis of abnormal proteins that can be toxic to cells through dominant-negative or gain-of-function effects"* — kitabın cümlesi özetin birebir karşılığı | ✅ |
| 2.2 | DMD: out-of-frame → Duchenne; in-frame → Becker; aynı mekanizma splice varyantlarına da uygulanır | Monaco 1988 özeti: üç DMD hastasında ORF kayması → *"truncated, abnormal protein"*; üç BMD hastasında ORF korunmuş → *"presumed to be semifunctional"*; *"same ORF mechanism is also applicable to potential 5′ and 3′ intron splice mutations"* | ✅ |
| 2.3 | CFTR'de "çok sayıda varyant tanımlı ama yalnız bir kısmı hastalık nedeni" | Sosnay 2013: 39.696 birey; AF ≥%0,01 olan 159 varyanttan **127'si (%80)** hem klinik hem işlevsel ölçütü karşıladı; 12'si nötr, 20'si belirsiz | ⚠️→✅ **sayılar metne eklendi** (iddia doğruydu, kanıtı görünmüyordu) |
| 2.4 | PKU: klasik → hafif PKU → hafif HPA spektrumu; genotip veritabanları fenotip ve BH4 yanıtını öngörür | Hillert 2020: küresel dağılım %62 klasik / %22 hafif PKU / %16 hafif HPA; genotip temelli fenotip öngörüsü **%88**, BH4 yanıtı **%83** | ✅ |
| 2.5 | Richards 2015, Abou Tayoun 2018, Karczewski 2020 künyeleri | PubMed künyeleriyle birebir | ✅ |

## T4 — Atıfsız mekanizma iddiaları

| # | İddia | Değerlendirme | Eylem |
|---|---|---|---|
| 2.6 | "Yüksek rezervli genler (birçok metabolik enzim) resesif davranır" — mekanizmanın **neden**i kaynaksızdı | T4-(b): kaynaklanabilir. Kacser & Burns 1981 özeti bunu doğrudan söylüyor: akı kontrolü çok sayıda enzime dağılır, duyarlılık katsayıları küçüktür, *"A reduction to 50% activity in the heterozygote… is therefore not expected to be detectable in the phenotype. The mutant would therefore be described as 'recessive'"* | ⚠️→✅ **kaynak eklendi** (§4.3 + Bölüm 3 §2.1) — Bölüm 3'ün 3.17 açık kalemi de böylece kapandı |
| 2.7 | pLI ve LOEUF'un birlikte Karczewski 2020'ye atfı | Bölüm 1 ve 3'te de çıkan aynı kusur | ⚠️→✅ pLI → **Lek 2016**, LOEUF → **Karczewski 2020** olarak ayrıştırıldı |
| 2.8 | "PTC, son ekzon-ekzon bağlantısının ~50 nt yukarısındaysa NMD" | Çapraz kontrol kitaplarında bu sayısal sınır **bulunamadı** (aranan: "50-55", "nucleotides upstream"). Kitapta zaten "öğretici basitleştirme" olarak işaretli ve RNA doğrulaması öneriliyor | ✅ mevcut etiketleme yeterli; sayı **T4-(a) etiketli** kalıyor, kesin kanıt olarak sunulmuyor |
| 2.9 | "Destabilize missense fonksiyonel null olabilir" · "Compound het'te daha hafif allel fenotipi belirler" | Yerleşik; ikincisi Hillert 2020 verisiyle uyumlu | ✅ T4-(a) |

## Bölüm 2 özeti

| Sonuç | Sayı |
|---|---|
| ✅ Doğrulandı (değişiklik gerekmez) | **9** |
| ⚠️ Düzeltildi/zenginleştirildi | **3** (CFTR sayıları · Kacser & Burns kaynağı · pLI/LOEUF atıf ayrımı) |
| 🔲 Etiketli kalan basitleştirme | **1** (NMD ~50 nt) |
| ❌ **Olgusal yanlış** | **0** |

**Yorum:** Bölüm 2'nin dört çekirdek kaynağının hepsi, kitaptaki cümleyi **özet düzeyinde birebir** destekliyor — bu, kaynakların "süs" değil gerçekten okunmuş olduğunu gösteriyor. Çıkan tek yapısal kusur, pLI/LOEUF atıf karışıklığının **üçüncü kez** görülmesidir; bu artık bölüm hatası değil, kitap geneli bir kalıptır ve kalan bölümlerde özellikle aranacaktır.

---

# Bölüm 4 — Gain-of-function (tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Denetlenen iddia:** 12 · **Kullanılan otorite:** PubMed künye/özet (8 kaynağın tamamı)

## T2 — Çalışma bulguları

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 4.1 | Wilkie 1994 dominanlık mekanizmalarını sınıflar; "artmış/konstitütif aktivite", "ektopik ifade", "yeni işlev" ayrı kategorilerdir | Özet sekiz kategoriyi sayıyor; (2) artmış gen dozu, (3) ektopik/zamansal değişmiş ifade, (4) artmış veya konstitütif protein aktivitesi, (8) yeni protein işlevleri — birebir | ✅ |
| 4.2 | FGFR3 Lys650Glu kinaz aktivitesini yabanıl tipin **~100 katına** çıkarır | Webster 1996 özeti: *"approximately 100-fold above that of wild-type FGFR3"*; ayrıca *"mimic the conformational changes… normally initiated by ligand binding"* — kitabın ikinci cümlesi de birebir | ✅ **sayı tam** |
| 4.3 | RET: GoF → MEN2 (kanser), LoF → Hirschsprung | Edery 1997 özeti: *"the two 'faces' of RET, gain of function and loss of function, each lead to a different syndrome"* | ✅ |
| 4.4 | "Noonan olgularının **yarısından fazlası** PTPN11'den kaynaklanır" | Tartaglia 2001: *"account for more than 50% of the cases **that we examined**"* — bu, seçilmiş bir seriye ait orandır, genel popülasyon oranı değil | ⚠️→✅ "yaklaşık yarısı; ilk seride %50'den fazlası" olarak **hassaslaştırıldı** |
| 4.5 | "Enerjik analiz … gain-of-function olduğunu **göstermiştir**" | Kaynak daha temkinli: *"indicates that… there **may be** a significant shift"*, *"**implies** that they are gain-of-function"* | ⚠️→✅ "işaret etmiştir" olarak yumuşatıldı |
| 4.6 | SCN2A: GoF <3 ay başlangıç + sodyum kanal blokerine iyi yanıt | Brunklaus 2020 özeti: GoF missense veya CNV duplikasyonu olanlar *"most frequently present with early onset epilepsy (<3 months), and demonstrate good response to sodium channel blockers"* | ✅ **birebir** |
| 4.7 | Brnich 2019'un dört adımlı çerçevesinin ilk adımı "mekanizmayı tanımla" | Özet: *"(1) define the disease mechanism"* | ✅ |

## ❗ Bulgu 4.8 — bölümün en önemli düzeltmesi: Berecki 2018'e ait olmayan iddia

Kitap iki yerde (§4.5 ve §7.4) şunu söylüyordu: *"LoF varyantları (örn. Arg853) daha geç başlangıçlı tablo ve **otizm spektrum bozukluğuyla** ilişkilidir"* — ve bunu **Berecki ve ark. (2018)**'e atfediyordu.

Berecki 2018 özeti R853Q için **otizmden hiç söz etmez**; söylediği şudur: *"infantile spasms is the dominant seizure type seen in R853Q cases, presenting at a median age of 8 months."* Yani kaynak bir **nöbet tipi ve başlangıç yaşı** bildiriyor, bir nörogelişimsel tanı değil.

İddianın kendisi doğrudur (SCN2A işlev kaybı gerçekten OSB/entelektüel yetersizlikle ilişkilidir) ama **kaynağı yanlıştı**. Bu, kütüğün en çok aradığı hata türüdür: *doğru bilgi + yanlış çapa*. Okuyucu kaynağa gittiğinde iddiayı bulamaz ve kitabın atıflarına olan güveni haklı olarak sarsılır.

**Düzeltme:** Berecki 2018'e yalnızca elektrofizyolojik ayrım ve başlangıç yaşı/nöbet tipi atfedildi; OSB/EY ilişkisi için **Sanders ve ark. (2018)**, *Trends Neurosci* 41(7):442–456, PMID 29691040 eklendi (özet: *"SCN2A dysfunction as a leading cause of infantile seizures, autism spectrum disorder, and intellectual disability"*).

| # | İddia | Durum |
|---|---|---|
| 4.9 | "GoF'ta LoF olgularında aynı ilaçlar **zararlı olabilir**" — Brunklaus'a atfedilmişti | ⚠️→✅ Brunklaus özeti yalnızca GoF'ta **yarar** bildiriyor; "kötüleşme" ifadesi SCN1A/Dravet bağlamına taşındı ve **yerleşik klinik bilgi** olarak, kaynağa yüklenmeden yazıldı |
| 4.10 | "Delesyon fenotipi kopyalıyorsa LoF, kopyalamıyorsa GoF/DN" pratik testi | 🏷️ Kitabın pedagojik formülasyonu; bileşenleri Wilkie 1994 çerçevesinde mevcut | ✅ kaynağa uyumlu, etiket gerekmedi |

## Bölüm 4 özeti

| Sonuç | Sayı |
|---|---|
| ✅ Doğrulandı (değişiklik gerekmez) | **7** |
| ⚠️ Düzeltildi | **4** (PTPN11 oranı · "göstermiştir"→"işaret etmiştir" · SCN2A/OSB atfı · SCB kötüleşme atfı) |
| ❌ **Olgusal yanlış** | **0** (ancak 1 **atıf yanlışı**: 4.8) |

**Yorum:** Bu bölümün sayısal iddiaları (FGFR3 ~100 kat, <3 ay) kaynak özetlerinde birebir çıktı — kitabın sayı disiplini iyi. Buna karşılık 4.8, **kaynağın söylemediği bir şeyi kaynağa yüklemenin** ilk örneğidir; olgusal olarak doğru bir cümle olduğu için hiçbir "bilgi denetimi" onu yakalayamazdı. Yalnızca kaynak-cümle karşılaştırması yakaladı.

---

# Bölüm 5 — Dominant-negatif (tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Denetlenen iddia:** 11 · **Kullanılan otorite:** PubMed künye/özet (7 kaynak); ClinGen gen dozaj listesi (**yeniden indirildi**, 1.526 satır, programatik eşleştirme)

## T2 — Çalışma bulguları

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 5.1 | Herskowitz DN'i "aşırı ifade edildiğinde yabanıl-tip etkinliğini bozan mutant polipeptit" olarak tanımladı; doğal örnekler (onkogenler) öngördü | Özet birebir: *"mutant polypeptides that when overexpressed disrupt the activity of the wild-type gene"*; *"some oncogenes might be examples of naturally occurring dominant negative mutations"* | ✅ |
| 5.2 | DN varyantlar protein arayüzlerinde zenginleşir, kararlılığı LoF'tan çok daha az bozar; tahmin araçları DN'de zayıftır | Gerasimavicius 2022 özeti: *"dominant, non-LOF disease mutations having much milder effects on protein structure, and DN mutations being highly enriched at protein interfaces"*; *"nearly all computational variant effect predictors… underperform on non-LOF mutations"* | ✅ **birebir** |
| 5.3 | OI bir "dominant-negatif bağ dokusu hastalığı"dır; niceliksel kusur (null *COL1A1*) hafif, yapısal kusur (glisin) ağır formlarla ilişkilidir | Forlino & Marini özeti: *"OI is a dominant negative disorder of connective tissue"*; *"Quantitative and structural mutations are associated with the milder and more severe forms of OI, respectively"* — **null COL1A1 allelleri** örneği açıkça geçiyor | ✅ **birebir** |
| 5.4 | "Arg337 varyantları… hetero-tetramerde transkripsiyon aktivitesi %50'den fazla azalır" | Kamada 2025: **%50'den fazla azalma R337C'ye özgü**; R337H hetero-tetrameri normale yakın kurar ama aktiviteyi belirgin bozar. Ayrıca kayıp, *bax* (düşük afinite) hedefinde *CDKN1A*'dan daha belirgin | ⚠️→✅ iki varyant **ayrı ayrı** yazıldı; "kompleks kuruluyor ama çalışmıyor" ayrımı eklendi |

## T3 — Gen dozaj (ClinGen, bugün yeniden indirildi)

| # | İddia | ClinGen kaydı | Durum |
|---|---|---|---|
| 5.5 | "Null allel → hafif tip I OI" kuralının kapsamı | **COL1A1 HI = 3** ("yeterli kanıt"), **COL1A2 HI = 0** ("kanıt yok") — dosyadan programatik eşleştirme | ⚠️→✅ **kural COL1A1'e özgüdür**; §7.1'e 🟦 kutu eklendi (Bölüm 3'ün açık kalemi kapandı) |
| 5.6 | TP53 DN örneği | TP53 HI = 3 — kitabın TP53'ü hem doz-duyarlı hem DN etkili sunmasıyla çelişmiyor | ✅ |

## T4/T5

| # | İddia | Durum |
|---|---|---|
| 5.7 | Multimer matematiği: (½)ⁿ ile tümü-sağlam kompleks oranı (dimer ¼, trimer ⅛, tetramer 1/16) | ✅ Kitapta zaten "rastgele birleşme + eşit üretim" varsayımıyla **temsilî** olarak etiketli; Kamada 2025 verisi bu modelin basitleştirme olduğunu destekliyor (R337C'de tetramer oluşumu neredeyse normal, kayıp işlevde) |
| 5.8 | "Delesyon/null testi" ile mekanizma ayrımı | ✅ Wilkie 1994 + Forlino 2000 ile uyumlu; kitabın en güçlü pedagojik aracı |
| 5.9 | "Antimorfik = DN" eşleştirmesi (Müller) | ✅ yerleşik terminoloji; kitap tercih ettiği terimi açıkça belirtiyor |

## Bölüm 5 özeti

| Sonuç | Sayı |
|---|---|
| ✅ Doğrulandı (değişiklik gerekmez) | **9** |
| ⚠️ Düzeltildi/hassaslaştırıldı | **2** (Kamada R337C/R337H ayrımı · COL1A2 sınırı) |
| ❌ **Olgusal yanlış** | **0** |

**Yorum:** Bölüm 5'in kavramsal iddiaları kaynaklarla olağanüstü iyi örtüşüyor (5.2 ve 5.3 özet cümleleriyle birebir). Buna karşılık 5.5, kitabın **başka bir bölümün taramasından gelen** bir uyarıyı ilk kez kullanışlı bir klinik nota çevirmesidir: ClinGen'de COL1A2'nin haploinsufficiency skoru 0'dır ve "null → hafif OI" kuralı bu gene taşınamaz. Bu, tek başına okunduğunda hatalı klinik yoruma yol açabilecek bir genellemeydi.

---

# Bölüm 6 — Neomorfik ve antimorfik alleller (tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Denetlenen iddia:** 10 · **Kullanılan otorite:** PubMed künye/özet (7 kaynak)

## T2 — Çalışma bulguları

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 6.1 | IDH1 mutantı yabanıl işlevini kaybeder **ve** α-KG'yi 2-HG'ye indirgeyen yeni aktivite kazanır; 2-HG tümörde birikir | Dang 2009 özeti birebir: *"new ability of the enzyme to catalyse the NADPH-dependent reduction of alpha-ketoglutarate to R(-)-2-hydroxyglutarate"*; *"markedly elevated levels of 2HG"* | ✅ (NADPH ayrıntısı eklendi) |
| 6.2 | H3 K27M, PRC2'yi EZH2 alt birimi üzerinden inhibe eder; H3K27me3 genel olarak düşer | Lewis 2013 özeti birebir: *"H3K27M inhibits the enzymatic activity of the Polycomb repressive complex 2 through interaction with the EZH2 subunit"* | ✅ |
| 6.3 | **"Ollier/Maffucci bireylerinin %90'ından fazlası mozaik IDH1/IDH2 ile açıklanır"** | Amary 2011: **40 bireyin 37'sinde** *en az bir tümörde* mutasyon (≈%92,5) — bu bir **tümör düzeyi** saptama oranıdır. Mozaiklik kanıtı ayrıdır ve daha ölçülüdür: 19 bireyin 18'inde tüm tümörler aynı Arg132 mutasyonunu paylaşıyor; **12 kişinin yalnız 2'sinde** tümör dışı dokuda mutant DNA saptanabilmiş. Yazarlar *"compatible with a model"* diyor | ⚠️→✅ ham sayılar yazıldı; "göstermiştir" → yazarların kendi temkinli ifadesine çevrildi |

## T4 — Terminoloji

| # | İddia | Değerlendirme | Eylem |
|---|---|---|---|
| 6.4 | **"Müller allel serisi"** (kitap genelinde 16 yerde) | Allel serisini tanımlayan genetikçi **Hermann Joseph Muller**'dir (1890–1967, ABD); adında umlaut **yoktur**. "Müller" yazımı, aynı bölümde kaynak yazarı olarak geçen *Manuel M. Müller* (Lewis 2013 ortak yazarı) ile karışma riski de yaratıyordu | ⚠️→✅ Bölüm 5, 6, 15 ve Bölüm_00'da **Muller** olarak düzeltildi; yazar adı *Müller MM* korundu |
| 6.5 | "Neomorf, hipermorf ve toksik kazanım keskin sınırlarla ayrılmaz" | Kitap bunu zaten spektrum olarak ve etiketleyerek sunuyor | ✅ |
| 6.6 | K→M ikamesinin genellenebilirliği | Lewis 2013 özeti H3K9 ve H3K36 için de aynı etkiyi bildiriyor — kitapta **yoktu** | ➕ eklendi (pedagojik değeri yüksek: mekanizma tek hastalığa özgü değil) |
| 6.7 | Neomorfta PVS1 uygulanmaz; PM1/PS3 öne çıkar | Richards 2015 + Gerasimavicius 2022 ile uyumlu | ✅ |

## Bölüm 6 özeti

| Sonuç | Sayı |
|---|---|
| ✅ Doğrulandı | **7** |
| ⚠️ Düzeltildi | **2** (Amary oranı/ifadesi · Muller yazımı) |
| ➕ Kaynaktan eklenen içerik | **2** (NADPH ayrıntısı · K→M genellemesi) |
| ❌ **Olgusal yanlış** | **0** |

**Yorum:** 6.3, 4.8'e benzer bir kalıbın daha yumuşak biçimidir: sayı doğru (%92,5 ≈ ">%90") ama **neyin ölçüldüğü** kaymıştı — "bireylerin %90'ı mozaik mutasyonla açıklanır" ile "40 bireyin 37'sinde en az bir tümörde mutasyon var" aynı şey değildir; ikincisi mozaikliği *dolaylı* olarak destekler. 6.4 ise bir ders kitabı için beklenenden daha önemlidir: kavramın adı yanlış yazıldığında okuyucu kaynağı arayamaz.

---

# Bölüm 7 — Splicing (tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Denetlenen iddia:** 12 · **Kullanılan otorite:** PubMed künye/özet (7 kaynak; T1 için ClinGen SVI Splice Alt Grubu belgesi)

## ❗ Bulgu 7.1 — bölümün en önemli düzeltmesi: RNA-splicing kanıtı **PS3 ile kodlanmaz**

Kitap §6'da RNA kanıtını "**PS3/BP7**" başlığı altında topluyor, §5'te "splice yorumunda PS3/BP7'nin neden bu kadar değerli olduğunu açıklar" diyor, öğrenme hedefi 6 ve iki Mermaid algoritması da PS3'ü RNA kanıtının kodu olarak gösteriyordu.

ClinGen SVI Splice Alt Grubu bunun tersini söylüyor (Walker ve ark., 2023, özetten):

> *"We propose repurposing the **PVS1_Strength** code to capture splicing assay data that provide experimental evidence for variants resulting in RNA transcript(s) with loss of function… We propose that the **PS3/BS3 codes are applied only for well-established assays that measure functional impact not directly captured by RNA-splicing assays**."*

Yani RNA'nın gösterdiği "ekzon atlandı → işlev kaybı yapan transkript" bulgusu **PVS1_Strength** ile; PS3/BS3 ise RNA-splicing testinin ölçmediği işlevsel etkiyi ölçen testler için kullanılır. Kitabın söylediği, kılavuzun ayırmak için özel çaba harcadığı iki kodu birleştiriyordu.

**Neden önemli:** Bu bir terminoloji inceliği değil, **uygulama farkı**dır. Aynı RNA bulgusunu PS3 (güçlü) yerine PVS1_Strength ile kodlamak, kanıtın hem adını hem birleştirme kurallarındaki davranışını değiştirir; iki kodun aynı varyantta ayrı ayrı sayılması **kanıtın çift sayılmasına** ve yanlış sınıflandırmaya yol açabilir.

**Düzeltme:** §5, §6, öğrenme hedefi 6, Algoritma 7.2, Algoritma 7.3, hata kutusu (yeni madde 4) ve öz-denetim tablosu güncellendi.

## T2 — Çalışma bulguları

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 7.2 | "Nadir genetik hastalıkların patojen varyantlarının ~%9–11'i splice-değiştirici sessiz/intronik sınıftandır"; bunlar RNA-seq'te yüksek oranda doğrulanır ve popülasyonda güçlü biçimde elenir | Jaganathan 2019 özeti birebir: *"We estimate that 9%-11% of pathogenic mutations in patients with rare genetic disorders are caused by this previously underappreciated class"*; *"validate at a high rate on RNA-seq and are strongly deleterious in the human population"* | ✅ **birebir** |
| 7.3 | SMN2 ekzon 7'deki sessiz C→T (kodon 280) bir ESE'yi zayıflatarak ekzon 7 atlanmasına yol açar | Lorson 1999 özeti birebir: *"the exon 7 C-to-T transition at codon 280, a translationally silent variance, was necessary and sufficient to dictate exon 7 alternative splicing"*; *"attenuates activity of an exonic enhancer"* | ✅ (SMN1/SMN2 arasındaki **beş nükleotid farkı** ve "gerekli ve yeterli" ayrıntısı eklendi) |
| 7.4 | PS1'in "aynı öngörülen RNA-splicing etkisi" için kullanılması | Walker 2023 özeti birebir | ✅ |
| 7.5 | BP7'nin intronik/sessiz varyantta "etki yok" kanıtı olarak kullanılması | Walker 2023 özeti birebir | ✅ |

## T4 — Künye tutarlılığı

| # | Sorun | Durum |
|---|---|---|
| 7.6 | **Scotti & Swanson yıl tutarsızlığı:** metin içinde "(2015)", kaynakçada ve Bölüm_00 kütüğünde "(2016)" | ⚠️→✅ Sayı/sayfa bilgisiyle (Nat Rev Genet **17(1):19–32**) uyumlu olan **2016** biçiminde birleştirildi. (PubMed elektronik yayın tarihi 23.11.2015; basılı sayı 2016.) Protokol §3: aynı kaynak her yerde **birebir aynı künye** |

## Bölüm 7 özeti

| Sonuç | Sayı |
|---|---|
| ✅ Doğrulandı | **9** |
| ⚠️ Düzeltildi | **3** (RNA kanıt kodu · Scotti yılı · Lorson ayrıntısı zenginleştirildi) |
| ❌ **Olgusal yanlış** | **0** |
| ⚠️ **Normatif (T1) yanlış** | **1** — bulgu 7.1 |

**Yorum:** 7.1, denetimin şimdiye kadarki en somut kazancıdır. Kitabın anlattığı biyoloji doğruydu; yanlış olan, kılavuzun **kod atama kuralıydı**. Bu tür hatalar bilgi denetimiyle değil, yalnızca **kılavuz belgesinin kendi cümlesiyle karşılaştırmayla** yakalanır — protokolün T1 kategorisini ayrı tutmasının nedeni tam olarak budur.

---

# Bölüm 8 — CNV ve yapısal varyantlar (tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Denetlenen iddia:** 11 · **Kullanılan otorite:** PubMed künye/özet (6 kaynak); ders kitabı çapraz kontrolü (Strachan & Read 5e; Lupski, *Genomic Disorders*)

## T2 — Çalışma bulguları

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 8.1 | CNV'ler toplam nükleotid olarak SNP'leri aşar; "genomik bozukluk" kavramı; rekombinasyon + replikasyon temelli oluşum | Stankiewicz & Lupski 2010 özeti birebir: *"CNVs encompass more total nucleotides and arise more frequently than SNPs"*; *"such conditions have been referred to as genomic disorders"* | ✅ ("daha sık ortaya çıkar" ifadesi eklendi) |
| 8.2 | CMA getirisi %15–20; karyotip ~%3 | Miller 2010 özeti: 33 çalışma, **21.698 hasta**; CMA %15–20; karyotip *"approximately 3%, **excluding Down syndrome and other recognizable chromosomal syndromes**"* | ⚠️→✅ **koşul eklendi** — bu koşul olmadan karşılaştırma karyotipi haksız biçimde küçük gösterir |
| 8.3 | "CMA dengeli SV ve düşük mozaikliği göremez" | Doğru; ancak aynı özet bunu **oransal** olarak bağlama oturtuyor: *"these are relatively infrequent causes of abnormal phenotypes in this population (<1%)"* — kitapta yoktu | ➕ eklendi (§5 ve hata kutusu 4) |
| 8.4 | TAD sınırı bozulması → enhancer hijacking → ekstremite malformasyonu; yalnız CTCF sınırı bozulduğunda | Lupiáñez 2015 özeti birebir: *"This rewiring occurred only if the variant disrupted a CTCF-associated boundary domain"* | ✅ (lokus *WNT6/IHH/EPHA4/PAX3*, CRISPR fare modeli ve hasta fibroblastı ayrıntısı eklendi) |
| 8.5 | Lupski 1991: 17p duplikasyonu → CMT1A | Özet birebir; kanıtlar: polimorfik lokusta üç allel, RFLP doz farkı, iki-renkli FISH | ✅ (kanıt yöntemleri metne eklendi) |

## T4 — Atıf sınırı

| # | Sorun | Değerlendirme | Eylem |
|---|---|---|---|
| 8.6 | "~1,4 Mb bölge + CMT1A-REP + NAHR hotspot" bilgisi, paragraf sonundaki **Lupski 1991** atfının kapsamındaymış gibi duruyordu | 1991 özetinde bu ayrıntılar **yok** (orada 500 kb'lik yeni bir SacII fragmanından söz edilir); 1,4 Mb ve CMT1A-REP sonraki literatürün bilgisidir. Ders kitabı çapraz kontrolü: Strachan & Read 5e *"a 1.4 Mb duplication that spans multiple genes, but the disease arises because of dosage-sensitivity in one gene, PMP22"*; Lupski *Genomic Disorders* aynı bölge için 1,5 Mb ve CMT1A-REP misalignment mekanizmasını anlatıyor | ⚠️→✅ paragraf ikiye ayrıldı: 1991'e **yalnız duplikasyon keşfi** atfedildi, bölge boyutu/REP bilgisi "sonraki çalışmalar" olarak verildi |
| 8.7 | 17p12 dozaj iddiası | Bölüm 3 turunda ClinGen bölge listesinden programatik teyitli (ISCA-37436, HI = 3, TS = 3) | ✅ tutarlı |

## Bölüm 8 özeti

| Sonuç | Sayı |
|---|---|
| ✅ Doğrulandı | **8** |
| ⚠️ Düzeltildi/koşullandırıldı | **2** (CMA %3 karşılaştırmasının koşulu · 1991 atfının kapsamı) |
| ➕ Kaynaktan eklenen içerik | **3** (<%1 bağlamı · Lupiáñez lokus/yöntem · Lupski kanıt yöntemleri) |
| ❌ **Olgusal yanlış** | **0** |

**Yorum:** 8.2 ince ama önemli bir örnektir: "%15–20'ye karşı %3" doğru bir alıntıdır, ama **koşulu düşürülmüş** bir alıntıdır. Koşul yazılmadığında okuyucu karyotipin genel tanısal değerini olduğundan düşük sanır. 8.6 ise 4.8'in bir akrabasıdır — atfın *kapsamı* kaymış; kaynak doğru, ama o kaynağın söylemediği ayrıntılar onun şemsiyesi altına girmiş.

---

# Bölüm 8 — Sayısal ve yapısal kromozom anomalileri (yeniden yapılandırma)

**Uygulama tarihi:** 03.08.2026 · **Kapsam:** 18 iddia kümesi · **Kanıt standardı:** 27 PubMed kaydının programatik künye doğrulaması + resmî PMC ana metinleri + ISCN 2024/ACGS resmî PDF'leri + Gardner & Amor 5e T4 çapraz kontrolü.

Önceki 27.07.2026 turu yalnız yedi kaynak ve altı özet üzerinden yürütülmüştü. Bu kayıt onun yerini silmez; yeni bölümde kullanılan bilimsel iddialar için özetler kanıt sayılmamış, ana metinler yeniden incelenmiştir.

## Kanıt haritası sonucu

| Küme | Kapsam | Sonuç |
|---|---|---|
| 8-A–D | Ayrımlar; normal mayoz/mitoz; nondisjunction dışı yollar; kinetokor/SAC | ✅ İki bağımsız hat; insan–hayvan tür sınırı metinde açık |
| 8-E–F | Postzigotik anöploidi, rescue/UPD, triploidi–diandri/digini | ✅ İki bağımsız hat; gebelik evresi/ascertainment koşulu korundu |
| 8-G–J | DSB/telomer, NAHR/NHEJ/MMEJ, FoSTeS/MMBIR, chromothripsis/chromoanasynthesis | ✅ İki bağımsız hat; mikrohomoloji ve mekanizma kesinliği sınırlandı |
| 8-K–O | Kromozomal ürünler, fenotip yolları, testler, ISCN ve geriye çıkarım | ✅ ISCN + normatif belgeler + tam metin çalışmalar |
| 8-P–Q | Parental taşıyıcılık, segregasyon ve yineleme | ✅ Translokasyonlarda iki hat; inversiyon halkası nitel ve yüzdesiz |
| 8-R | Düşük düzey/gonadal mozaiklik ve parental kan sınırı | ✅ İki birincil hat; gonadal mozaiklik kesin kanıtlanmış gibi yazılmadı |

## Bağlayıcı bilimsel kararlar

1. Her anöploidi nondisjunction değildir; predivision ve reverse segregation ana metinde insan verisiyle ayrıldı.
2. Karyotipten ebeveyn kökeni veya mayoz evresi üretilmedi.
3. “Dengeli” benign/moleküler kayıpsız kabul edilmedi; Redin ve Ordulu kohortlarının seçilmişliği açıklandı.
4. Breakpoint mikrohomolojisi kesin mekanizma kanıtı yapılmadı; FoSTeS/MMBIR'ın her zaman ayrılamadığı belirtildi.
5. Chromothripsis için “duplikasyon olmaz” mutlak ifadesi reddedildi.
6. Teorik gamet/embriyo ürünleri canlı doğum olasılığına çevrilmedi; genel yineleme yüzdesi verilmedi.
7. Normal parental kanın düşük düzey veya gonadal mozaikliği tümüyle dışlamadığı, örnekleme/duyarlılık sınırı olarak yazıldı.
8. ISCN örneklerinin tamamı ISCN 2024 ana metninden ve basılı sayfalarıyla doğrulandı; ISCN mekanizma kaynağı yapılmadı.

## Erişim ve belge sorunları

- İnversiyon halkasına özgü ikinci bağımsız birincil tam metin erişimi bulunmadı; alt başlık Gardner & Amor + ISCN düzeyinde nitel tutuldu, ampirik yüzde çıkarıldı.
- Lee 2007 FoSTeS ana metni erişilebilir olmadığı için kaynak setine alınmadı; ilgili sınır Burssed 2022 + Hastings 2009 + Liu 2011 ile kapatıldı.
- ACGS WGS-SV PDF dosya adı `v1.2`, iç sürüm geçmişi `2026 v0.1, 1 Mayıs 2026` göstermektedir; iki bilgi birlikte kaydedildi.
- ACGS array v2.00 (2011) güncel normatif temel yapılmadı.
- OGM validasyonunun Robertsonian/sentromerik yapılar, bazı LCR breakpointleri ve düşük mozaiklik dışlamaları metne taşındı.

## Uygulama sonucu

- Bölüm yeni adla 10 ana başlık altında yeniden yazıldı.
- 3 yeni SVG ve 3 Mermaid; 9 numaralı tablo; 8 çözümlü rapor örneği oluşturuldu.
- 27/27 PubMed kaydı programatik doğrulandı; ISCN 2024, ACGS KA/TCA, QF-PCR ve WGS-SV belgeleri ana metinden kontrol edildi.
- Tam build başarıyla tamamlandı: 17 bölüm · 64 şekil · 49 algoritma · 78 tablo · 172 benzersiz PMID; 191 doğrudan nesne hedefi doğrulandı.
- Stage, commit ve push bu pakete dahil edilmedi.

---

# Bölüm 9 — Tekrar dizisi genişlemesi (tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Denetlenen iddia:** 14 · **Kullanılan otorite:** PubMed künye/özet (10 kaynağın tamamı); ders kitabı çapraz kontrolü (Thompson & Thompson 2023)

## ❗ Bulgu 9.1 — teknik kusur: iki Mermaid algoritması yayımlanan kitapta bozuk render oluyordu

Bölüm 9, kitapta **tek başına** Mermaid etiketlerinde satır sonu için `\n` kullanıyordu (diğer 16 bölüm `<br/>` kullanıyor; CLAUDE.md §5 de `<br/>` diyor). Kitabın gömdüğü mermaid sürümü **11.15.0**'dır ve bu sürümde tırnak içindeki `\n` satır sonu üretmez, **düz metin olarak basılır**. Yani Algoritma 9.1 ve 9.2'nin düğüm etiketleri yayımlanmış HTML'de `\n` karakterleriyle birlikte görünüyordu.

Bu, içerik denetimiyle bulunamayacak, yalnız **biçim tutarlılığı taramasıyla** çıkan bir kusurdur. Düzeltildi (blok içi tüm `\n` → `<br/>`).

## T2 — Çalışma bulguları

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 9.2 | "40'tan fazla hastalık; tri-, tetra-, penta-, hekzanükleotid" | Paulson 2018 özeti: *"More than 40 diseases, most of which primarily affect the nervous system"*; *"tetra-, penta-, hexa-, and even **dodeca**-nucleotide"* | ✅ (dodeka- ve "çoğunlukla sinir sistemi" eklendi) |
| 9.3 | DM1: MBNL sekestrasyonu + CELF1 artışı → fetal splicing izoformları | Chau & Kalsotra 2015 özeti birebir | ✅ |
| 9.4 | CDM1'de CUG foci'nin gelişen korteksi etkilemesi | De Serres-Bérard 2021 özeti birebir: *"may affect the developing cortex in utero"* | ✅ |
| 9.5 | FRDA: GAA → heterokromatin → transkripsiyonel susturma; mitokondriyal demir birikimi; HDAC inhibitörleri | Marmolino & Acquaviva 2009 özeti birebir | ✅ |
| 9.6 | C9orf72: beş DPR (GA, GR, PA, PR, GP); arginin-zenginleri nükleolar kalite kontrolü bozar | Schmitz 2021 özeti birebir | ✅ |
| 9.7 | SCA1'de CAT/histidin kesintileri aleli stabilize eder | Kraus-Perrotta & Lagalwar 2016 özeti birebir | ✅ |

## T4 — Atıf kapsamı ve çapa değişiklikleri

| # | Sorun | Değerlendirme | Eylem |
|---|---|---|---|
| 9.8 | "FMRP sinapslarda mRNA'ların dendritik taşınmasını ve çevrilmesini düzenler" → **Hoogeveen & Oostra 1997**'ye atfedilmişti | 1997 derlemesi bunu söylemez; orada öne sürülen model FMRP'nin **çekirdek–sitoplazma taşınmasında** rol oynadığıdır. Sinaptik/dendritik yerel çevrim modeli sonraki literatürün bilgisidir | ⚠️→✅ 1997'ye yalnız **metilasyon → susturma → FMRP yokluğu** atfedildi; sinaptik işlev "sonraki çalışmalar / yerleşik ders bilgisi" olarak ayrıldı |
| 9.9 | "60 CAG → genç erişkin, 40 CAG → 50–60 yaş" → **Jimenez-Sanchez 2017**'ye atfedilmişti | Bu sayılar o özette yok. Ders kitabı çapraz kontrolü doğruluyor: Thompson & Thompson 2023 — *"Normal range ≤35 · Reduced penetrance range 36–39 · Fully penetrant range ≥40"*; *"adult-onset disease usually have 40 to 55 repeats; juvenile-onset usually more than 60"* | ⚠️→✅ sayılar **yerleşik ders bilgisi** olarak yeniden yazıldı; ayrıca T&T'nin önemli uyarısı eklendi: *"The number of repeats does not correlate with features of HD other than age at onset"* |
| 9.10 | Paternal aktarımda büyük genişleme eğilimi — kaynaksızdı | Kraus-Perrotta & Lagalwar 2016 özeti bunun **moleküler nedenini** veriyor: spermatid→sperm geçişinde boşluk onarımı başarısızlığı; *"Equivalent failures were not detected in female gametic cells"* | ➕ kaynak eklendi |
| 9.11 | FXTAS yalnız premutasyona özgü sunuluyordu | Hagerman & Hagerman 2015: gri zon (45–54) ve **metillenmemiş** tam mutasyon allellerinde de bildirilmiş; değişmeyen koşul *FMR1*'in ifade edilmesi | ➕ eklendi (mekanizma mantığını güçlendiriyor: FXS susturma ister, FXTAS ifade ister) |

## Biçim/yazım kusurları (bu bölüme özgü)

| # | Kusur | Eylem |
|---|---|---|
| 9.12 | **Kiril harf bulaşması:** "İndirg**ен**miş" (5 yerde; `ен` Kiril) — arama ve dizin oluşturmayı bozar | ✅ düzeltildi |
| 9.13 | "bradik**e**zi" → bradikinezi; "CG**A**-zengini RNA" → CGG; "histon**e** deasetilaz" → histon | ✅ düzeltildi |

## Bölüm 9 özeti

| Sonuç | Sayı |
|---|---|
| ✅ Doğrulandı | **8** |
| ⚠️ Atıf çapası düzeltildi | **2** (9.8, 9.9) |
| ➕ Kaynaktan eklenen içerik | **3** |
| 🔧 Teknik/yazım kusuru giderildi | **3** (Mermaid `\n`, Kiril harfler, yazım) |
| ❌ **Olgusal yanlış** | **0** |

**Yorum:** Bu bölüm, denetimin **içerik dışı** boyutunun neden gerekli olduğunu gösterdi: 9.1 bir bilgi hatası değil, yayımlanan üründe **görünen** bir kusurdu ve 16 bölümde doğru yapılan bir şeyin bir bölümde atlanmasından doğmuştu. 9.8/9.9 ise artık tanıdık kalıp: doğru bilgi, yanlış çapa.

---

# Bölüm 10 — İmprinting, UPD, epigenetik (tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Denetlenen iddia:** 12 · **Kullanılan otorite:** PubMed künye/özet (9 kaynağın tamamı); ClinGen gen dozaj listesi (indirilmiş, programatik)

## T2 — Çalışma bulguları

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 10.1 | PWS: metilasyon analizi >%99 tanı; delesyon %65–75, matUPD15 %20–30, ID %1–3 | Cassidy 2012 özeti birebir (*"paternal deletion of this region (65-75%), maternal uniparental disomy 15 (20-30%), or an imprinting defect (1-3%)"*; *"will detect >99%"*) | ✅ **birebir** — kitabın sayı disiplini burada örnek düzeyde |
| 10.2 | PWS kardeş tekrarlanma riski | Cassidy: *"Sibling recurrence risk is typically <1%, but higher risks may pertain in certain cases"* — kitapta yoktu | ➕ eklendi |
| 10.3 | *UBE3A*: beyinde ağırlıklı maternal ifade; AS'nin dört nedeni; antisens transkriptle susturma | Lalande & Calciano 2007 özeti birebir | ✅ |
| 10.4 | **"ICR1 hipermetilasyonu *ve paternal UPD11* en yüksek Wilms riskini taşır"** | Eggermann & Prawitt 2022: upd(11)pat, moleküler doğrulanmış BWSp olgularının **%20'ye varan** kısmıdır ve tümör riski bakımından **"the second highest"** alt gruptur | ⚠️→✅ sıralama düzeltildi: en yüksek risk ICR1 hipermetilasyonunda; upd(11)pat **ikinci** sırada |
| 10.5 | "Trizomi kurtarma kaynaklı UPD **tipik olarak** heterodizomiktir" → Mergenthaler 2000 | Mergenthaler'in verisi bunu mutlaklaştırmıyor: maternal UPD7'de izodizomi (n = 11) ve tam/kısmi heterodizomi (n = 12) **hemen hemen eşit**; olguların ~%50'si post-zigotik mitotik segregasyon hatası | ⚠️→✅ "tipik olarak" ifadesi yumuşatıldı, ham sayılar eklendi |
| 10.6 | Segmental/kompleks UPD mekanizmaları; "kromozom segregasyonu sanılandan karmaşık" | Kotzot 2001 özeti birebir (*"chromosomal segregation is more complex than previously thought"*) | ✅ |
| 10.7 | İmprintli genlerin bir **ağ** olarak davranması; MLID | Eggermann 2021 özeti birebir (*"imprinted gene network"*; paternal ifadeli genler büyümeyi artırır, maternal olanlar baskılar) | ✅ |
| 10.8 | Reik & Walter: ebeveyn çatışması; imprintli genlerin büyüme ve doğum sonrası davranışı etkilemesi | Özet birebir | ✅ |

## T3 — İmprintli lokuslarda ClinGen gen skoru (Bölüm 3'ün açık kalemi)

| # | Bulgu | Eylem |
|---|---|---|
| 10.9 | *SNRPN*, *NDN*, *H19*, *IGF2* — ClinGen **gen düzeyi HI skoru = 0**. Bu, "doza duyarlı değil" demek değildir; patojenite **bölge ve damgalama düzeyinde** tanımlanır | ✅ §6'ya 🟦 kutu eklendi; *PMP22* (Bölüm 3, bulgu 3.16) ile aynı ders açıkça bağlandı. **Bölüm 3'ün ikinci açık kalemi kapandı** |

## Bölüm 10 özeti

| Sonuç | Sayı |
|---|---|
| ✅ Doğrulandı | **9** |
| ⚠️ Düzeltildi | **2** (BWS tümör riski sıralaması · UPD7 izo/hetero genellemesi) |
| ➕ Kaynaktan eklenen içerik | **2** |
| ❌ **Olgusal yanlış** | **0** |

**Yorum:** Bu bölüm, kitabın **en iyi kaynaklanmış** bölümlerinden biri çıktı: PWS alt-tip yüzdeleri kaynak özetiyle rakam rakam örtüşüyor. Çıkan iki düzeltme de aynı türden: kaynağın **derecelendirmesini** (ikinci en yüksek → en yüksek) ve **belirsizliğini** (yarı yarıya → tipik olarak) sıkılaştırma eğilimi. Bu eğilim, denetimin kalan bölümlerde özellikle arayacağı kalıptır.

---

# Kitap geneli — künye denetimi (tamamlandı, programatik)

**Tarih:** 27.07.2026 · **Yöntem:** `00_Şablonlar/kunye_denetle.py` — kaynakça satırlarından PMID/yıl/cilt(sayı):sayfa ayrıştırılır, NCBI **esummary** kayıtları `urllib` ile indirilir ve alan alan karşılaştırılır. Model okuması yoktur (Protokol §2).

| Ölçüt | Sonuç |
|---|---|
| Taranan kaynak satırı | **194** (17 bölümün tamamı) |
| Benzersiz PMID | **118** |
| NCBI'da **bulunamayan** PMID (uydurma göstergesi) | **0** |
| Yıl uyuşmazlığı | **0** |
| Cilt / sayı / sayfa uyuşmazlığı | **0** |

**Neden önemli:** Kitabın en büyük yayım riski olarak tanımlanan **"kaynak uydurma"**, artık bir güven beyanı değil, **tekrarlanabilir bir ölçüm** ile kapatılmıştır. Herhangi bir okuyucu ya da hakem, aynı komutu çalıştırıp aynı sonucu üretebilir:

```bash
python3 00_Şablonlar/kunye_denetle.py
```

**Sınır:** Bu denetim künyenin *bibliyografik* doğruluğunu gösterir — makalenin **var olduğunu ve doğru künyeyle anıldığını**. Kitabın o kaynağa yüklediği **iddianın** kaynakta gerçekten bulunup bulunmadığı ayrı bir sorudur ve bölüm bölüm T2 taramasıyla denetlenir (bkz. bulgu 4.8, 8.6, 9.8, 9.9 — hepsi künyesi kusursuz kaynaklarda çıkan **atıf kapsamı** hatalarıdır).

---

# Bölüm 11 — Mitokondriyal genetik (tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Kullanılan otorite:** PubMed künye/özet; ders kitabı çapraz kontrolü (Thompson & Thompson 2023)

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 11.1 | ClinGen mtDNA spesifikasyonunun getirdiği uyarlamalar: frekans/haplogrup, heteroplazmi, PS3 (tek-lif), PM1 (tRNA yapısal alanı) | McCormick 2020 özeti: spesifikasyonlar *"mtDNA genome composition and structure, haplogroups and phylogeny, maternal inheritance, heteroplasmy, and functional analyses unique to mtDNA"* ile *"mtDNA genomic databases and computational algorithms"*a değiniyor — kitabın dört maddesi birebir örtüşüyor | ✅ |
| 11.2 | — | Aynı özetin saydığı özellikler arasında **"absence of splicing"** var; kitapta yoktu. Bunun pratik sonucu büyük: **Bölüm 7'nin tüm kriter seti mtDNA'da uygulanamaz** | ➕ eklendi (§6, beşinci fark) |
| 11.3 | "Kompleks II tümüyle nükleer kodludur; izole Kompleks II eksikliği maternal kalıtılmaz" | Thompson & Thompson 2023, s.534: *"Except for complex II, each complex has some components encoded in mtDNA and some in the nuclear genome. MtDNA encodes 13 of the polypeptides…"* | ✅ ders kitabıyla teyitli |
| 11.4 | "Kompleks I'in ~45 alt biriminden yalnız 7'si mtDNA kaynaklı" | mtDNA'nın kodladığı 13 polipeptidin dağılımıyla aritmetik olarak tutarlı (7 CI + 1 CIII + 3 CIV + 2 CV = 13) | ✅ |
| 11.5 | Paternal mtDNA geçişi | Bölüm zaten ⚠️ ile "tartışmalı; klinik danışmada esas alınmaz" diye etiketlemiş | ✅ **Bölüm 1'in açık kalemi (1.9) kapandı** |
| 11.6 | Eşik yüzdeleri (%60–90), hücre başına kopya sayısı | Bölüm zaten "temsilî" olarak etiketlemiş | ✅ T5/etiketli |

**Yorum:** Bölüm 11, normatif katmanı en özenli işlenmiş bölümlerden biri: mtDNA'nın ACMG çerçevesini neden kırdığını kaynağın kendi gerekçe listesiyle aynı sırada anlatıyor. Tek eksik (11.2) bir hata değil, **kaynakta olup kitaba geçmemiş** güçlü bir argümandı.

---

# Bölüm 12 — Mozaiklik (tamamlandı)

**Denetim tarihi:** 27.07.2026 · **Kullanılan otorite:** PubMed künye/özet (sayısal iddia taşıyan kaynaklar)

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 12.1 | 100 aile tarandı, **4** ailede ebeveyn kanında düşük düzeyli mozaiklik | Campbell 2014 özeti birebir (*"prospectively screened 100 families… identified four cases"*) | ✅ |
| 12.2 | — | Aynı özet iki güçlü noktayı daha veriyor: kanda saptanan mozaiklik, germline ile sınırlı mozaikliğe göre riski **belirgin biçimde** artırır; gametogenezdeki cinsiyet farkı nedeniyle somatik mozaik aktarıcıların çoğu **anne**dir ve bu, X'e bağlı resesif hastalıklardaki beklenmedik yinelemelerin bir kısmını açıklayabilir. Kitapta yoktu | ➕ eklendi |
| 12.3 | FCD tip II: üç çocuk, **33 elektrottan 4'ü** mutasyon-pozitif | Checri 2023 özeti birebir | ✅ |
| 12.4 | PROS şemsiyesi (makrodaktili, FAO, HHML, CLOVES, megalensefali tabloları) | Keppler-Noreuil 2015 özeti birebir | ✅ |
| 12.5 | PS2/PM6'nın mozaiklikte zayıflaması; VAF + doku raporlama zorunluluğu; klonal hematopoez tuzağı (*DNMT3A*, *TET2*, *ASXL1*) | Richards 2015 çerçevesiyle tutarlı; klonal hematopoez uyarısı yerleşik | ✅ |

**Yorum:** Bölüm 12, sayısal iddialarını kaynak özetleriyle birebir örtüşür biçimde vermiş — denetimde tek bir sayı bile kaymamıştır. Eklenen tek şey (12.2), kaynağın kitabın anlattığı derse **doğrudan hizmet eden** ama alınmamış bir bulgusuydu.

---

# Bölüm 13 — Kodlamayan / regülatör varyantlar (tamamlandı)

**Denetim tarihi:** 27.07.2026

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 13.1 | *PTF1A*'nın 25 kb aşağısında ~400 bp'lik tanımlanmamış bölge; **on ailede altı** resesif varyant; izole pankreas agenezisinin **en sık nedeni** | Weedon 2014 özeti birebir: *"six different recessive mutations in a previously uncharacterized ~400-bp sequence located 25 kb downstream of PTF1A… in ten families"*; *"These mutations are the most common cause of isolated pancreatic agenesis"* | ✅ **birebir** |
| 13.2 | *FTO* intronik bölgesi megabaz uzaklıktaki *IRX3* promotörüyle temas eder; insan beyninde varyantlar *IRX3* ifadesiyle ilişkili, *FTO* ile değil; *Irx3* eksik farede ağırlık **%25–30** azalır | Smemo 2014 özeti birebir (insan/fare/zebra balığı; *"reduction in body weight of 25 to 30%… primarily through the loss of fat mass and increase in basal metabolic rate"*) | ✅ **birebir** |
| 13.3 | Kodlamayan varyantta **PVS1 uygulanmaz**, **PS3 ağırlık kazanır** (reporter/MPRA) | Bölüm 7'deki düzeltmeyle **çelişmiyor**: orada yasaklanan, RNA-*splicing* bulgusunun PS3 ile kodlanmasıydı; burada söz konusu olan gerçek işlevsel (transkripsiyonel) testtir — Walker 2023'ün PS3/BS3 için ayırdığı alanın ta kendisi. Ayrıca bölüm, derin intronik/kriptik splice'ı açıkça Bölüm 7 çerçevesine havale ediyor | ✅ tutarlı |

**Yorum:** Bölüm 13, sayısal iddiaları kaynak özetleriyle kelime kelime örtüşen ikinci bölüm (12'den sonra). Denetimde **düzeltme gerektiren hiçbir bulgu çıkmadı**.

---

# Bölüm 15 — Digenik / oligogenik / modifier (tamamlandı)

**Denetim tarihi:** 27.07.2026

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 15.1 | *RET* intron 1 enhancer varyantı: riske katkısı nadir kodlayan alellerden **~20 kat** büyük; *in vitro* enhancer aktivitesini azaltır; düşük penetrans; **cinsiyete göre farklı** etki | Emison 2005 özeti birebir (*"makes a 20-fold greater contribution to risk than rare alleles do"*; *"reduces in vitro enhancer activity markedly, has low penetrance, has different genetic effects in males and females"*) | ✅ **birebir** |
| 15.2 | Digenik RP: *RDS/ROM1* — yalnız **çift heterozigotlar** hastalanır | Kajiwara 1994 özeti birebir (*"only double heterozygotes develop retinitis pigmentosa"*; üç aile) | ✅ |
| 15.3 | "Digenik hastalıkta risk %25 değildir; iki lokusun birlikte aktarılma olasılığından hesaplanır" | Kalıtım mantığıyla doğru; kitabın hata kutusunda ve algoritmasında tutarlı | ✅ |
| 15.4 | Oligogenik/modifier tablolarda **kesin oran verilmemesi** gerektiği | Kitabın kendi normatif duruşu; kaynaklarla çelişmiyor ve dürüst belirsizlik beyanı olarak doğru konumlanmış | ✅ T5 uygun |

**Yorum:** Bölüm 15, sayı vermekten kaçınması gereken yerde kaçınıyor, sayı verdiği tek yerde (15.1) kaynağıyla birebir örtüşüyor. Düzeltme gerekmedi.

---

# Bölüm 14 — Aynı gen → farklı hastalık (tamamlandı)

**Denetim tarihi:** 27.07.2026

| # | Bulgu | Eylem |
|---|---|---|
| 14.1 | **Bulgu 4.8'in tekrarı:** "*SCN2A*'da işlev kaybı … **otizm spektrum** tablolarıyla ilişkilidir (Berecki ve ark., 2018)" | ⚠️→✅ Berecki'ye yalnız elektrofizyoloji ve başlangıç yaşı/nöbet tipi bırakıldı; OSB/EY için **Sanders ve ark., 2018** eklendi (bölümün 22. kaynağı). Bölüm 4 turunda öngörülen "izlenecek" kalem böylece kapandı |
| 14.2 | **"Allelik serinin altı ekseni"** çerçevesi — kitabın en görünür özgün sentezi, **etiketsizdi** | 🏷️→✅ §2 girişine ve bölüm sonu işaretli-iddialar notuna etiket eklendi: bileşenler kaynaklı, gruplama editöryal, literatürde bu adla yerleşik sınıflandırma yok (Protokol §1 T5 kuralı) |
| 14.3 | Bölüm 16 ve 17'de aynı Berecki atfı | ✅ kontrol edildi — oralarda yalnız R1882Q işlev kazanımı bağlamında kullanılmış, OSB iddiası yok |

# Bölüm 16 — Mekanizmadan varyant yorumuna (tamamlandı)

**Denetim tarihi:** 27.07.2026 · Kitabın **en normatif** bölümü olduğu için T1 odaklı denetlendi.

| # | Bulgu | Eylem |
|---|---|---|
| 16.1 | **Bulgu 7.1'in tekrarı — üç ayrı yerde.** Bölüm 16, RNA-splicing kanıtını **PS3** ile eşleştiriyordu: (a) varyant-tipi tablosunda "Kanonik splice → PVS1 → **PS3 (RNA)**", (b) aynı tabloda "Derin intronik/sessiz → PP3 → **PS3 (RNA)**", (c) test tablosunda "RNA-seq **PS3 ve PVS1 için** doğrudan kanıt üretir", (d) uzman-panel özetinde "**PS3'ün RNA verisiyle ilişkilendirilmesi**" | ⚠️→✅ dördü de düzeltildi: RNA-splicing bulgusu → **PVS1_Strength**; etkisizlik → **BP7**; PS3/BS3 → RNA-splicing testinin ölçmediği işlevsel etki (Walker ve ark., 2023) |
| 16.2 | **Mekanizma × kriter matrisi** (Şekil 16.3) — kitabın ikinci büyük özgün çerçevesi | ✅ **zaten etiketliydi**: metinde, öz-denetim tablosunda ve bölüm sonu notunda "pedagojik özet, normatif değil" uyarısı mevcut. Düzeltme gerekmedi |
| 16.3 | PM2'nin günümüzde **destekleyici** güce indirilmesi | ✅ ClinGen SVI uygulamasıyla uyumlu; kitap bunu açıkça yazıyor |
| 16.4 | CNV, mtDNA, splice ve kodlamayan varyantlar için **ayrı spesifikasyonlar** olduğunun listelenmesi (Riggs 2020, McCormick 2020, Walker 2023, Ellingford 2022) | ✅ dördü de doğru kaynağa bağlı |

**Yorum:** 16.1, denetimin en değerli tekrar bulgusudur. Bölüm 7'de düzeltilen kural, kitabın **özet/sentez** bölümünde dört ayrı yerde eski hâliyle duruyordu. Bu, tek bir bölümü düzeltmenin yetmediğini gösterir: normatif bir kural değiştiğinde kitap **genelinde** aranmalıdır. (Aynı ders pLI/Karczewski kalıbında da çıkmıştı.)

---

# Bölüm 17 — Klinik senaryolarla sentez (tamamlandı)

**Denetim tarihi:** 27.07.2026

| # | İddia (kitapta) | Otoriteden gelen | Durum |
|---|---|---|---|
| 17.1 | 100.000 Genom pilotu: **2.183 aileden 4.660 katılımcı**; HPO ile fenotipleme; sanal panel + otomatik önceliklendirme; probandların **%25'inde** tanı; monogenik %35 ↔ kompleks %11; EY/işitme/görme **%40–55**; tanıların **%14'ü** araştırma+otomatik birleşimiyle (kodlamayan, yapısal, mitokondriyal ve ekzomun kötü kapsadığı kodlayan varyantlar); tanıların dörtte biri **anında** klinik sonuç doğurdu | Smedley 2021 (NEJM) özeti — **yedi sayının yedisi de birebir** | ✅ |
| 17.2 | DDD yeniden analizi: 2014'te **1.133** çocukta %27; iyileştirilmiş varyant çağırma, yeni algoritmalar, güncel anotasyon, kanıta dayalı filtreleme ve **yeni hastalık genleri** ile 182 ek tanı → **454/1.133 (%40)**; 43 kişide (%4) belirsiz bulgu | Wright 2018 özeti — beş yöntem kalemi ve tüm sayılar **birebir** | ✅ |
| 17.3 | **Bulgu 7.1'in üçüncü tekrarı:** "Yanlış dokudan yapılan RNA analizi **PS3** üretmez" ve Algoritma'da "Splice → **PS3** + PVS1 basamağı" | ⚠️→✅ ikisi de düzeltildi (RNA-splicing → **PVS1_Strength**; etkisizlik → BP7). §7'deki "İşlev kazanımı/DN → PM1 + PS3" kullanımı ise **doğru** ve korundu (gerçek işlevsel test) |

**Yorum:** Bölüm 17, sayısal disiplin bakımından kitabın en iyi bölümü: iki ulusal ölçekli çalışmadan alınan **on iki ayrı sayının tamamı** kaynak özetleriyle birebir örtüştü. Buna karşılık aynı bölümde PS3/splice kalıbı üçüncü kez göründü — bu kusurun bir "dikkatsizlik" değil, kitabın yazıldığı dönemde **yerleşmiş yanlış bir alışkanlık** olduğunu gösteriyor.

---

# 📊 Doğrulama turu — genel sonuç (27.07.2026)

**Kapsam:** 17 bölümün tamamı + Bölüm 0 kütüğü. Bölüm 3 daha önce (pilot) denetlenmişti; bu turda kalan 16 bölüm denetlendi ve Bölüm 3'ün iki açık kalemi kapatıldı.

| Sonuç | Sayı |
|---|---|
| Denetlenen bölüm | **17/17** |
| Programatik olarak doğrulanan künye satırı | **194/194** (118 benzersiz PMID; 0 uydurma, 0 sapma) |
| ❌ **Olgusal (bilgi) yanlışı** | **0** |
| ⚠️ **Normatif (T1) yanlış** | **1 kural, 3 bölümde 7 ayrı yerde** — RNA-splicing kanıtının PS3 ile kodlanması (Böl. 7, 16, 17) |
| ⚠️ **Atıf kapsamı hatası** (doğru bilgi, yanlış çapa) | **6** (4.8 · 8.6 · 9.8 · 9.9 · 15.1 · 10.5) |
| ⚠️ Sayı/derece hassaslaştırması | **7** (1.5 · 1.8 · 4.4 · 4.5 · 6.3 · 8.2 · 10.4) |
| ➕ Kaynakta olup kitaba geçmemiş, eklenen içerik | **12** |
| 🏷️ Etiketlenen özgün çerçeve (T5) | **4** (rezerv-ve-eşik · Presence/Extent · altı eksen · mekanizma×kriter matrisi — sonuncusu zaten etiketliydi) |
| 🔧 Teknik/biçim kusuru | **3** (Bölüm 9 Mermaid `\n` render hatası · Kiril harf bulaşması · yazım) |
| 🆕 Turda eklenen doğrulanmış kaynak | **5** (Lek 2016, Kacser & Burns 1981, Abou Tayoun 2018→Böl. 1, Sanders 2018, Kacser→Böl. 3) |

## Üç kalıp

Denetim, birbirinden bağımsız üç hata kalıbı ortaya çıkardı; üçü de "yanlış bilgi" değildir ve hiçbiri bir bilgi denetimiyle yakalanamazdı:

1. **Atıf kapsamının kayması.** Cümle doğru, kaynak var, künye kusursuz — ama o cümle o kaynakta yok. En net örnek 4.8: *SCN2A* işlev kaybının otizmle ilişkisi Berecki 2018'e atfedilmişti; o makale otizmden hiç söz etmez. Yalnız **kaynak-cümle karşılaştırması** yakalar.
2. **Belirsizliğin sıkılaştırılması.** Kaynak "ikinci en yüksek" derken kitap "en yüksek", kaynak "yarı yarıya" derken kitap "tipik olarak", kaynak "işaret ediyor" derken kitap "göstermiştir" diyor. Tek tek küçük, toplamda kitabın kesinlik tonunu kaynaklarının üstüne çıkarıyor.
3. **Düzeltmenin tek bölümde kalması.** Bölüm 7'de bulunan normatif hata, Bölüm 16'da dört, Bölüm 17'de iki yerde daha duruyordu; pLI/Karczewski atfı üç bölümde birden vardı. **Bir kural düzeltildiğinde kitap genelinde aranmalıdır.**

## Ne iddia edilebilir, ne edilemez

Bu tur sonunda savunulabilir cümle şudur:

> "Kitaptaki 194 kaynak künyesinin tamamı NCBI kayıtlarıyla programatik olarak eşleştirilmiştir (tekrarlanabilir: `kunye_denetle.py`). On yedi bölümün tamamı iddia düzeyinde denetlenmiş; sayısal ve normatif iddialar kaynak özetleriyle cümle düzeyinde karşılaştırılmıştır. Bu turda bir normatif kural hatası (RNA-splicing kanıtının kodlanması) ve altı atıf-kapsamı hatası bulunup düzeltilmiştir. Kitabın özgün pedagojik çerçeveleri, yerleşik sınıflandırma olmadıkları belirtilerek etiketlenmiştir."

Savunulamayacak cümle ise değişmemiştir: **"Bu kitapta hata yoktur" denemez.** Özellikle T4-(a) kategorisi — kaynaksız, kulağa doğru gelen, yerleşik ders bilgisi sayılıp geçilen mekanizma cümleleri — hiçbir otomatik denetimle kapanmaz. **Uzman insan değerlendirmesi hâlâ yayım ön koşuludur.**
✅ *Kapandı:* Bölüm 3'ün "imprintli lokuslarda gen skoru yanıltıcı" açık kalemi (bulgu 10.9).
✅ *Kapandı:* Bölüm 3'ün "%50 dozda akı korunur" açık kalemi — Kacser &amp; Burns (1981) eklendi.

---

# 🔒 Kapanış turu (28.07.2026)

Doğrulama turundan kalan beş "izlenecek" kalemin tamamı kitap geneli taramayla kapatıldı.

| # | İzlenen kalem | Yöntem | Sonuç |
|---|---|---|---|
| K1 | Mermaid etiketlerinde `\n` kullanımı | Tüm `Bölüm_*.md` üzerinde düz metin taraması | ✅ **0 eşleşme** — Bölüm 9 düzeltmesi dışında hiç yokmuş |
| K2 | Kiril / karışık alfabe bulaşması | Tüm `Bölüm_*.md` + `kitap/*.md` üzerinde `[\x{0400}-\x{04FF}]` taraması | ✅ **0 eşleşme** |
| K3 | PS3'ün splice bağlamında kullanımı (Böl. 13, 16, 17) | Bölümlerde tüm `PS3` geçişlerinin bağlam okuması | ✅ Splicing kanıtı **PVS1_Strength**, etkisizlik **BP7** olarak kodlanmış (Böl. 16 §hızlı-referans ve §özet). Böl. 13'teki PS3 kullanımı **kodlamayan** varyantların reporter/MPRA kanıtı içindir — doğru. Böl. 17'deki PS3 kullanımları GoF/DN yön testi içindir — doğru |
| K4 | Berecki 2018'in kapsam dışı kullanımı (Böl. 15, 16, 17) | Üç bölümdeki tüm geçişlerin okunması | ✅ Üçünde de yalnızca **elektrofizyolojik yön ayrımı** için kullanılmış; OSB/EY iddiası Böl. 15'te ayrıca **Sanders 2018**'e bağlanmış ve künyede "Berecki 2018'in kapsamı dışındadır" notu düşülmüş |
| K5 | pLI'nin Karczewski 2020'ye atfı (doğrusu Lek 2016) | Böl. 16'da `pLI` taraması | ⚠️→✅ **Bulundu ve düzeltildi.** §PM2 klinik kutusunda "pLI/LOEUF; Karczewski ve ark., 2020" duruyordu; metin pLI → **Lek 2016**, LOEUF → Karczewski 2020 olarak ayrıştırıldı, Lek 2016 künyesi Böl. 16 kaynakçasına (no. 25) eklendi ve Bölüm 0 kütüğünde bölüm listesi güncellendi |

**Ek düzeltme (biçim):** Bölüm 0 indeksinde Bölüm 16 için "3 Mermaid" yazıyordu; dosyada 2 Mermaid var — indeks düzeltildi.

**Programatik yeniden doğrulama (28.07.2026):** `python3 00_Şablonlar/kunye_denetle.py` → **196/196 kaynak satırı · 118 benzersiz PMID · 0 uyuşmazlık, 0 eksik.** (Turdaki 194 sayısı, sonradan eklenen künyelerle 196'ya çıkmıştır.)

## Kapanış turundan çıkan ders

K5, doğrulama turunun üçüncü kalıbını (*"düzeltmenin tek bölümde kalması"*) bir kez daha doğruladı: hata Bölüm 1, 2 ve 3'te düzeltilmiş, Bölüm 16'da kalmıştı — ve orada da metnin gövdesinde değil, bir **klinik kutusunun içinde** duruyordu. Bu, kitap-geneli taramanın yalnızca ana metni değil kutuları, tablo hücrelerini ve künye "kullanım amacı" notlarını da kapsaması gerektiğini gösterir.

Buna karşılık K1–K4'ün temiz çıkması, turda yapılan düzeltmelerin **tek seferde ve tutarlı** biçimde uygulandığını gösteriyor. Kitabın denetlenebilirlik iddiası bu turla birlikte tamamlanmıştır.

**Değişmeyen sınır:** Bu tur bir biçim ve tutarlılık turudur; T4-(a) kategorisini (kaynaksız, yerleşik sayılıp geçilen mekanizma cümleleri) kapatmaz. **Uzman insan değerlendirmesi hâlâ yayım ön koşuludur.**

---

# Teknik temizlik ve build güvenliği turu (02.08.2026)

**Kapsam:** Bu tur bilimsel revizyon değildir. Mekanizma iddiaları, klinik eşikler, tablo hücreleri ve kaynak künyeleri değiştirilmemiştir. Bölüm 9 ve 12'de yalnız tablo numaraları, dilbilgisel çekim ekleri ve bunlara bağlı çapraz göndermeler güncellenmiştir; normalize edilmiş diff ile iki bölümün bilimsel içeriğinin değişmediği doğrulanmıştır.

| Denetim | Sonuç |
|---|---|
| Dinamik envanter | ✅ 17 bölüm · 64 şekil · 49 algoritma · 73 tablo · 153 benzersiz PMID |
| Tablo numaraları | ✅ Bölüm 9: 9.1–9.5 · Bölüm 12: 12.1–12.5; mükerrer/liste dışı numara yok |
| SVG terminolojisi | ✅ Aktif 12 SVG'de Türkçe `alel/alelik/bialelik`, `Muller`, `dizileme` standardı uygulandı |
| Karışık alfabe | ✅ Aktif SVG'lerde Kiril karakteri kalmadı |
| SVG yapısal geçerliliği | ✅ `xmllint`: 64/64 geçerli XML |
| Eksik SVG davranışı | ✅ Yapay eksik referans testi `BuildError` ile derlemeyi durdurdu |
| Mükerrer tablo davranışı | ✅ Yapay mükerrer numara testi `BuildError` ile derlemeyi durdurdu |
| Taşınabilir yardımcı betik | ✅ `00_Şablonlar/paragraf.py` proje dışı çalışma dizininden çalıştı |
| HTML build | ✅ 4,9 MB tek dosyalık HTML başarıyla üretildi; eksik ön/arka madde uyarısı yok |

**Terminoloji otoritesi:** `CSpec`, ClinGen'in resmî **Criteria Specification Registry** adlandırmasıyla; `pLoF`, gnomAD'ın resmî **predicted loss-of-function** kullanımıyla karşılaştırıldı (erişim: 02.08.2026). Bunlar kısaltma açılımı doğrulamasıdır; yeni bir mekanistik veya normatif iddia değildir.

**Kaynak raporlama düzeltmesi:** `153` sayısı “153 birincil kaynak” olarak değil, derleyicinin PMID'ye göre tekilleştirdiği **153 benzersiz PMID kaydı** olarak raporlanır. DOI'si olmayan geçerli kayıtlar bulunabildiğinden “her kaydın PMID ve DOI'si vardır” ifadesi kaldırılmış; “bibliyografik veriler PubMed üzerinden doğrulanmış, DOI'si bulunan kayıtlarda bağlantı verilmiştir” biçimine çekilmiştir. Yeni kaynak eklenmedi; kaynak sayısı değişmedi.

**Kalıcı resmî bağlantılar:** ClinGen CSpec Registry — `https://erepo.clinicalgenome.org/cspec/`; gnomAD LoF curations — `https://gnomad.broadinstitute.org/news/2020-10-loss-of-function-curations-in-gnomad/`.

---

# Nesne bağlantıları ve terminoloji/HGVS denetimi (02.08.2026)

**Kapsam:** Bu paket yeni mekanizma iddiası, klinik eşik veya kaynak künyesi eklemedi. Şekil/algoritma/tablo listelerinin doğrudan nesneye gitmesi sağlandı; kısaltmalar, seçili hastalık adları, HGVS/HGNC kuralları, NaV1.2 açıklaması, hedef kitle ve okuyucuya sızan iç karar kodları denetlendi. Terim düzeltmeleri aktif kitap metni, sözlük, hastalık dizini ve ilgili SVG'lerde kitap geneline yayıldı.

| Denetim | Sonuç |
|---|---|
| Nesne envanteri | ✅ 64 şekil · 49 algoritma · 73 tablo = **186 benzersiz hedef** |
| Doğrudan bağlantılar | ✅ Her nesne için görünür bağlantı + baskı sayfa sayacı bağlantısı; toplam **372 hedef bağlantısı**, tüm hedefler mevcut ve tekil |
| Numaralandırma | ✅ Şekil, algoritma ve tablo numaraları bölüm içinde kesintisiz; mükerrer numara yok |
| Build güvenliği | ✅ Eksik/mükerrer nesne hedefinde ve geçersiz/mükerrer/kesintili nesne numarasında `BuildError` ile durur |
| Okuyucu metnindeki iç kodlar | ✅ `E5 kararı`, `F6 kararı` ve `G2.2` üretilen HTML'de yok |
| VUS ve hastalık adları | ✅ `klinik önemi belirsiz varyant`; Kistik fibrozis, Osteogenezis imperfekta, Herediter basınca duyarlı nöropati ve Charcot–Marie–Tooth biçimleri aktif Türkçe metinde tutarlı |
| NaV1.2 | ✅ Gen sembolü olmadığı ve *SCN2A*'nın kodladığı kanal/protein adı olduğu açıklandı |
| HGVS/HGNC | ✅ Normatif kural ile kitabın editöryal tercihi ayrıldı; referans dizi/sürüm, protein parantezi, `Ter`/`*`, çerçeve kayması ve faz gösterimi resmî kaynaklara bağlandı |
| SVG/XML | ✅ 64/64 aktif SVG `xmllint` doğrulamasından geçti |
| HTML build | ✅ 4,9 MB tek dosyalık HTML; 17 bölüm · 153 benzersiz PMID |
| Diff biçimi | ✅ `git diff --check` temiz |

**Türkçe kaynak denetimi:** Tıbbi Genetik Derneği, T.C. Sağlık Bakanlığı, Türk Nöroloji Dergisi, üniversite kayıtları ve Türkçe hakemli tıp yayınları karşılaştırıldı. Uluslararası adlandırmada HGVS 21.1.4, HGNC, NCBI ve IUPHAR/BPS kullanıldı. Önce/sonra tablosu, tercih gerekçeleri ve kalıcı bağlantılar `Terminoloji_Kaynak_Denetimi.md` içindedir.

**Sayfa numarası sınırı:** Akışkan HTML'nin sabit sayfası yoktur. Baskı CSS'sine `target-counter(attr(href), page)` altyapısı eklendi; ancak bu özellik sıradan tarayıcı PDF'inde garanti edilmez. Nihai sabit PDF, uyumlu bir sayfalama motoruyla üretildikten sonra nesne listelerindeki numaralar ile gerçek hedef sayfalar görsel olarak doğrulanmadan bu kalem “yayın kapanışı tamamlandı” sayılmayacaktır.

**Git durumu:** Paket kullanıcı onayıyla uygulandı; Git geçmişi commit düzeyinde korunur, push kullanıcı tarafından yapılır.
