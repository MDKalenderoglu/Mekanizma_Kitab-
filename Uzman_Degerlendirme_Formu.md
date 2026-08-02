# Uzman Değerlendirme Formu

**Değerlendirilen sürüm:** 28.07.2026 · 17 bölüm · 196 kaynak künyesi · 64 şekil · 49 algoritma

---

## Bu form ne için?

Kitabın künye doğrulaması tamamlandı (196/196 kaynak NCBI kayıtlarıyla programatik olarak eşleştirildi), sayısal iddialar kaynak özetleriyle cümle düzeyinde karşılaştırıldı, normatif kurallar kılavuz belgelerine karşı denetlendi. Bu formdaki maddeler o denetimlerin **yakalayamayacağı** türdendir:

- kaynaksız ama kesin dille yazılmış mekanizma cümleleri,
- klinik yönlendirmeler (hangi test, hangi doku, hangi sıra),
- öğretici basitleştirmeler ve temsilî sayılar,
- kitabın kendi ürettiği pedagojik çerçeveler.

Bunlar ancak alanın uzmanı tarafından değerlendirilebilir. **Uzman değerlendirmesi yayım ön koşuludur; hiçbir otomatik denetim onun yerine geçmez.**

## Nasıl doldurulur?

Her madde, kitaptaki **paragrafın tamamıyla** birlikte verilmiştir; sorulan yer paragrafın içinde ***koyu italik*** olarak işaretlidir. Paragrafın geri kalanı bağlam içindir — onu da yanlış buluyorsanız belirtin.

Her maddenin altındaki satırda:

- **D** — doğru, olduğu gibi kalsın
- **Y** — yanlış (kısaca doğrusunu yazın)
- **A** — doğru ama eksik/yanıltıcı; alternatif öneriniz varsa yazın

Boş bırakılan maddeler "değerlendirilmedi" olarak raporlanacaktır.

**Yer bilgisi:** Her maddede kaynak dosya, bölüm içi başlık ve satır numarası verilmiştir. Kitap tek dosyalık HTML olarak üretildiği için sabit sayfa numarası yoktur; satır numarası kaynak `.md` dosyasındaki yeri gösterir ve düzeltmeyi doğrudan oraya uygulamamı sağlar.

## Öncelik

Zamanınız kısıtlıysa **A → B → D** sırasını izleyin. A bölümü klinik kararı doğrudan değiştirir; B bölümü okuyucunun ezberleyeceği sayıları içerir; D bölümü kitabın özgün iddialarıdır. C bölümü en uzun olanıdır ama tek tek riski daha düşüktür.

| Bölüm | Konu | Madde |
|---|---|---|
| **A** | Test ve doku seçimi yönlendirmeleri | 24 |
| **B** | Sayısal eşikler ve öğretici basitleştirmeler | 26 |
| **C** | Kaynaksız mekanizma ve ders bilgisi (T4-a) | 23 |
| **D** | Kitabın özgün pedagojik çerçeveleri (T5) | 5 |
| **E** | Terminoloji kararları | 7 |
| **F** | Kapsam ve yapı kararları | 7 |
| **G** | Serbest kanaat | 5 soru |

---

## A. Test ve doku seçimi yönlendirmeleri

*Yanlışsa okuyucu yanlış test ister — kitabın klinik riski en yüksek kategorisi.*

### A1 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · 5. Tanısal testlerle ilişkisi · satır 177

> **Bu mekanizmayı hangi test yakalar? (özet):** Haploinsufficiency'de **tek test yeterli değildir**. Nokta LoF varyantları için **dizileme (WES/WGS)**, alleli silen delesyonlar için **doz analizi (MLPA / array-CGH / WGS-CNV)** gerekir; ***ikisi birlikte istenmelidir***. Yalnız WES yapılan bir HI gende negatif sonuç, büyük bir delesyonu kaçırdığı için tanıyı dışlamaz — array/MLPA ile tamamlanmalıdır (Şekil 3.3'deki "tanısal sonuç" kutusu).

**Sorulan:** Haploinsufficiency geninde dizileme ve doz analizinin *birlikte* istenmesi kuralı — pratikte her zaman geçerli mi, yoksa gen/test menüsüne göre kademelendirilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → günümüzde artık yeterli ve uygun örneklem var ise  WES ve WGS analizleriyle de CNV bakılabilmekte, bu nedenle tek seferede her iki test istemeye gerek yoktur. Eğer bakılamayan durumla karşı karşıya isek bu durumda da basamak yaklaşımı veya eş zamanlı test istemleri ülkeye laboratuvara maddi durumlara costefektiviteye fenotipe vs gibi etkenlere bağlı olarak tercih edilmelidir. 

<br>

### A2 · Bölüm 8 — CNV ve Yapısal Varyantlar

**Yer:** `Bölüm_08_CNV_Yapisal_Varyantlar.md` · 5. Tanısal testlerle ilişkisi · satır 127

> CNV/SV'lerde test seçimi, varyantın **tipine ve boyutuna** göre değişir. Kopya-sayısı değişimleri için altın standart **kromozomal mikroarray (CMA)**'dır. Miller ve ark. (2010), 33 çalışmayı ve CMA ile test edilmiş **21.698 hastayı** kapsayan bir derlemeye dayanarak, gelişimsel gerilik/zihinsel yetersizlik, otizm spektrum bozukluğu veya çoklu konjenital anomalisi olan bireylerde CMA'nın tanısal getirisinin **%15–20** olduğunu, G-bantlı karyotipin getirisinin ise **yaklaşık %3** düzeyinde kaldığını göstermiştir. Bu %3'lük rakamın nasıl hesaplandığı önemlidir: **Down sendromu ve diğer klinik olarak tanınabilen kromozomal sendromlar dışlanarak** verilmiştir — yani karyotipin "zaten klinikle tanınan" olguları yakalaması bu karşılaştırmaya dâhil edilmemiştir. Aradaki farkın kaynağı, CMA'nın submikroskopik delesyon ve duplikasyonlara çok daha duyarlı olmasıdır. Bu nedenle CMA **birinci-basamak sitogenetik test** olarak önerilir; ***karyotip ise belirgin kromozomal sendrom düşünülen olgular, ailede dengeli yeniden düzenlenme öyküsü veya tekrarlayan düşük öyküsü için saklanır*** (Miller ve ark., 2010, *Am J Hum Genet*; [DOI](https://doi.org/10.1016/j.ajhg.2010.04.006)). Önemli sınır: CMA **gerçekten dengeli** yeniden düzenlenmeleri (translokasyon/inversiyon) ve **düşük düzey mozaikliği** göremez. Yine de bu sınırı orantılı görmek gerekir: aynı derleme, bu iki durumun bu hasta grubunda anormal fenotipin görece seyrek nedeni olduğunu (**<%1**) belirtir — yani CMA'yı birinci basamağa taşıyan gerekçeyi ortadan kaldırmaz, yalnızca negatif bir CMA'dan sonra klinik şüphe sürüyorsa ne aranacağını söyler.

**Sorulan:** Karyotipin hangi durumlar için saklanacağı listesi eksiksiz mi? Türkiye pratiğinde bu öneri uygulanabilir mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → günümüzde artık karyotip analizinin tercih edilme sıklığı azalmış ancak tamamen test dışına alınamaz. karyotip istemleri endikasyonlarını:
## En güncel kaynak

**NHS England – National Genomic Test Directory, Rare and Inherited Disease Eligibility Criteria, v9.1; 20 Mayıs 2026.** Bu belge doğrudan hangi klinik durumda karyotip veya hedefli kromozom analizinin seçileceğini tanımlar. NHS sayfasında halen güncel nadir hastalık test uygunluk belgesi olarak v9.1 gösterilmektedir. ([NHS İngiltere][1])

Laboratuvar uygulaması ve analiz standartları için tamamlayıcı kaynak:

**ACGS Best Practice Guidelines for Constitutional Karyotype Analysis and Targeted Chromosome Analysis, v1.0; 2024.** Öneriler 20 Ağustos 2024’te onaylanmıştır ve postnatal, prenatal, gebelik kaybı ve solid doku kromozom analizlerini kapsar. ([acgs.uk.com][2])

### Terminoloji düzeltmesi

**“Kromozom analizi” ile “karyotip” tam eş anlamlı değildir.**

* **Karyotype analysis, KA:** Bütün metafaz kromozomlarının incelenmesi.
* **Targeted chromosome analysis, TCA:** Yalnızca belirli kromozomların veya beklenen anomalinin incelenmesi.
* **Chromosome analysis:** KA ve TCA’yı kapsayan üst terimdir.

Güncel belgelerde birçok eski “karyotip endikasyonu” artık TCA veya hızlı anöploidi testi olarak yürütülmektedir. ([acgs.uk.com][2])

# Güncel karyotip/TCA seçim endikasyonları

## 1. Görülebilir yapısal kromozom yeniden düzenlenmesi

Karyotipin en net endikasyonudur:

* Robertsonian translokasyon
* Resiprokal translokasyon
* Ring kromozom
* Büyük inversiyon
* Marker kromozom
* Derivatif kromozom
* Mikroskopik olarak görülebilecek diğer yapısal değişiklikler
* CMA, WGS, anöploidi testi veya başka bir yöntemle saptanan anomalinin kromozomal mimarisinin belirlenmesi

Bu grup güncel NHS dizininde **R463 – Cytogenetic characterisation of a genomic abnormality** olarak tanımlanmıştır. ([NHS İngiltere][3])

Örnek:

> CMA’da 14q ve 21q materyalini içeren dengesizlik bulundu. Bunun Robertsonian translokasyon mu, resiprokal translokasyon mu veya kompleks yeniden düzenlenme mi olduğunu belirlemek için karyotip gerekir.

CMA kopya sayısını gösterir; dengeli translokasyon mimarisini ve materyalin hangi kromozoma yerleştiğini çoğu durumda göstermez.

## 2. Ailede bilinen kromozomal yeniden düzenlenme

* Ailede dengeli translokasyon taşıyıcılığı
* Bilinen inversiyon
* Robertsonian translokasyon
* Marker veya ring kromozom
* Probandda saptanan yapısal anomalinin ebeveyn çalışması
* Aile içi kaskad tarama
* Dengesiz bir anomalinin ebeveynlerden dengeli formda taşınıp taşınmadığının araştırılması

Güncel kod **R465 – Familial cytogenetic rearrangement** olarak verilmiştir. Analiz, beklenen değişikliğe göre tam karyotip veya TCA şeklinde yapılabilir. ([NHS İngiltere][3])

## 3. Kromozomal mozaisizm şüphesi

Karyotip/TCA şu durumlarda seçilebilir:

* CMA, WGS, QF-PCR veya önceki karyotipte mozaisizm işareti bulunması
* Klinik fenotipin belirli bir mozaik kromozom bozukluğunu kuvvetle düşündürmesi ancak standart testin negatif olması
* Mozaik Turner sendromu
* Mozaik trisomi 21
* Ring kromozom mozaisizmi
* Pallister–Killian sendromunda dokuya özgü `+i(12p)`
* Düşük düzeyli hücre hattının metafaz sayımıyla araştırılması
* Anormal hücre hattının yapısal niteliğinin belirlenmesi

Bu grup **R265 – Chromosomal mosaicism: karyotype/TCA** olarak tanımlanmıştır. ([NHS İngiltere][3])

Ancak önemli ayrım şudur: **Mozaisizm şüphesinde otomatik olarak yalnızca karyotip seçilmez.** SNP-array, heterojen hücre popülasyonundan DNA kullanılması ve B-allele frequency profili sağlaması nedeniyle bazı olgularda daha uygun ilk test olabilir. Dokuya özgü mozaisizm düşünülüyorsa kan yerine fibroblast, bukkal hücre veya ilgili dokunun incelenmesi gerekebilir. 

## 4. Seks kromozomu anöploidisi veya yapısal anomalisi şüphesi

Örnekler:

* Turner sendromu
* Mozaik Turner sendromu
* Klinefelter sendromu
* Primer amenore
* Prematür over yetmezliği
* Gecikmiş puberte
* Seks kromozomu yapısal anomalisi
* DSD olguları
* `45,X/46,XY`, `45,X/46,XX`, `46,XX/47,XXX` gibi mozaik durumlar

Güncel NHS yaklaşımında bu grup çoğunlukla **tam karyotip yerine TCA** altında yer alır: **R468 – Possible sex chromosome aneuploidy or structural rearrangement**. ([NHS İngiltere][3])

Buna karşılık fenotip, seks kromozomlarına ek olarak otozomal bir yeniden düzenlenmeyi düşündürüyorsa tam karyotip gerekir. Örneğin erkek infertilitesinde Robertsonian translokasyon olasılığı yalnızca seks kromozomu TCA’sı ile dışlanamaz. 

## 5. Klinik olarak belirgin yaygın anöploidi şüphesi

Postnatal dönemde:

* Trizomi 21
* Trizomi 18
* Trizomi 13
* Turner sendromu
* Diğer seks kromozomu anöploidileri

Güncel dizinde bunlar önce **common aneuploidy testing** başlığı altında değerlendirilir. Karyotip/TCA özellikle:

* Serbest trizomi ile translokasyon trizomisinin ayrılması,
* Rekürrens riskinin belirlenmesi,
* Mozaik hücre hattının araştırılması,
* Yapısal seks kromozomu anomalisi olasılığı

için kullanılır. ([NHS İngiltere][3])

Dolayısıyla “Down sendromu düşünüyorum, doğrudan yalnızca karyotip göndereyim” yaklaşımı güncel test mimarisini tam yansıtmaz. Hızlı anöploidi testi tanıyı hızlandırabilir; kromozom analizi mekanizmayı ve rekürrens riskini belirler.

## 6. Tekrarlayan gebelik kaybı

Güncel NHS kriterleri ebeveyn karyotipini şu durumlarla sınırlar:

* **Üç veya daha fazla düşük:** Gebelik materyali uygun olmadığı, maternal kontaminasyon bulunduğu veya analiz başarısız olduğu için test edilememişse ve önceki kayıplardan hiçbirinde başarılı sonuç yoksa.
* **Beş veya daha fazla gebelik kaybı:** Önceki kayıpların hiçbirinde test edilebilir gebelik materyali bulunmamışsa.

Belge ayrıca ebeveyn karyotipinin sınırlı bilgi sağladığını ve mümkünse sonraki gebelik kaybı materyalinin doğrudan test edilmesinin daha bilgilendirici olduğunu açıkça belirtir. ([NHS İngiltere][3])

Gebelik kaybı materyali mevcutsa rutin genom çapında karyotip artık ilk tercih değildir; yaygın anöploidi testi ve CMA tercih edilir. 

## 7. İnfertilite

Güncel NHS dizininde **R466 – Unexplained infertility before infertility treatment** doğrudan karyotip endikasyonu olarak tanımlanmıştır. ([NHS İngiltere][3])

Klinikte özellikle:

* Non-obstrüktif azospermi
* Şiddetli oligozoospermi
* Hipergonadotropik hipogonadizm
* Prematür over yetmezliği
* Primer amenore
* Turner/Klinefelter şüphesi
* Robertsonian veya resiprokal translokasyon olasılığı

karyotip açısından daha yüksek önceliklidir.

## 8. Prenatal tanıda anormal test sonucunun karakterizasyonu

ACGS 2024 yaklaşımına göre prenatal örneklerde rutin tam karyotip kullanımı sınırlandırılmıştır. Kromozom analizi esas olarak:

* Anormal QF-PCR sonucunun takibi
* Anormal CMA sonucunun kromozomal yapısının belirlenmesi
* Dengesizliğin translokasyon, ring veya diğer yapısal yeniden düzenlenmeden kaynaklanıp kaynaklanmadığının gösterilmesi
* Rekürrens riskinin değerlendirilmesi
* Mozaik prenatal bulgunun araştırılması

için uygulanır. 

Ebeveynlerden biri dengeli translokasyon taşıyıcısıysa fetüste öncelikli soru çoğunlukla **dengesiz materyal bulunup bulunmadığıdır**; bu nedenle prenatal CMA yeterli olabilir. Fetüsün dengeli taşıyıcı olup olmadığını belirlemek rutin olarak gerekli değildir; kırılma noktası gen bozuyorsa veya X kromozomu tutulumu gibi klinik gerekçe varsa ayrıca değerlendirilir. 

# Pediatrik genetik pratiği için kısa karar kuralı

**Karyotip/TCA seç:**

* Dengeli veya büyük yapısal yeniden düzenlenme aranıyorsa
* Kromozomal anomalinin fiziksel mimarisi gerekli ise
* Ailede bilinen translokasyon/inversiyon varsa
* Mozaik hücre hattı ve hücre sayımı gerekiyorsa
* Seks kromozomu anöploidisi/yapısal bozukluğu düşünülüyorsa
* CMA/WGS/QF-PCR bulgusunun sitogenetik karakterizasyonu gerekiyorsa

**Karyotipi tek başına ilk test seçme:**

* Nonspesifik gelişimsel gecikme/entelektüel yetersizlik
* İzole otizm
* Belirli kromozomal fenotip göstermeyen çoklu konjenital anomali
* Submikroskopik delesyon/duplikasyon şüphesi
* Tek gen hastalığı şüphesi
* Gebelik kaybı materyalinin genom çapında değerlendirilmesi

Bu durumlarda klinik soruya göre CMA, hızlı anöploidi testi, panel, ES veya GS daha uygun olabilir. Karyotipin güncel ana alanı **kromozomun sayısal veya fiziksel yapısının hücresel düzeyde gösterilmesidir**; nonspefisik sendrom taraması değildir. ([acgs.uk.com][2])

[1]: https://www.england.nhs.uk/publication/national-genomic-test-directories/ "NHS England » National genomic test directory"
[2]: https://www.acgs.uk.com/media/12611/acgs-best-practice-guidelines-for-constitutional-karyotype-analysis-and-targeted-chromosome-analysis-v10.pdf "Purpose and Scope:"
[3]: https://www.england.nhs.uk/wp-content/uploads/2018/08/rare-and-inherited-disease-eligibility-criteria-v9.1.pdf "National Genomic Test Directory - Testing Criteria for Rare and Inherited Disease"
ÖZELLİKLE: https://www.acgs.uk.com/media/12611/acgs-best-practice-guidelines-for-constitutional-karyotype-analysis-and-targeted-chromosome-analysis-v10.pdf BURAYA DA BAKABİLİRSİN. 

<br>

### A3 · Bölüm 8 — CNV ve Yapısal Varyantlar

**Yer:** `Bölüm_08_CNV_Yapisal_Varyantlar.md` · 8. Sık yapılan hatalar · satır 193

> **🔴 Sık yapılan hata kutusu**
> 1. **CNV'yi boyutuna göre yorumlamak.** Büyük ama gen-fakir CNV iyi huylu, küçük ama HI geni silen CNV patojen olabilir. İçeriğe bakın.
> 2. **Duplikasyonu otomatik "delesyondan hafif" saymak.** PMP22'de duplikasyon (CMT1A) belirgin hastalık yapar; triplosensitiviteyi unutmayın.
> 3. **Dengeli SV'yi "zararsız" saymak.** Kırılma noktası bir geni bölebilir veya TAD sınırını bozabilir (pozisyon etkisi).
> 4. **CMA negatif diye dengeli/mozaik varyantı dışlamak.** CMA dengeli yeniden düzenlenmeleri ve düşük mozaikliği göremez; klinik şüphede WGS/karyotip düşünün. (Ancak bunu abartmayın: ***bu iki durum bu hasta grubunda anormal fenotipin <%1'ini açıklar — CMA'yı birinci basamaktan indirmenin gerekçesi değildir***.)
> 5. **Duyarlılık CNV'sini kesin tanı gibi raporlamak.** Penetransı ve aile segregasyonunu belirtin.

**Sorulan:** "<%1" oranı ve buradan çıkarılan pratik sonuç doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → bu iki durum bu hasta grubunda anormal fenotipin <%1'ini açıklar — CMA'yı birinci basamaktan indirmenin gerekçesi değildir. BU İFADEYİ: bu iki durum bu hasta grubunda anormal fenotipi YİNE DE TAM OLARAK AÇIKLAMAYABİLİR. OLARAK DEĞİŞTİR. ORAN VERME.

<br>

### A4 · Bölüm 9 — Tekrar Dizisi Genişlemesi (Repeat Expansion)

**Yer:** `Bölüm_09_Repeat_Expansion.md` · 5. Tanısal testlerle ilişkisi · satır 142

> **🟦 Klinikte dikkat — WES negatifliği tekrar hastalığını ekarte etmez:** Ataksi, miyotoni, entelektüel yetersizlik veya nörodejenerasyon ile başvuran bir hastada WES negatif çıksa bile, klinik tablo tekrar genişlemesi hastalıklarıyla uyumluysa ***hedefli PCR veya long-read WGS yapılmalıdır***. Tekrar genişlemesi WES'in "kör noktasıdır."

**Sorulan:** Hedefli PCR mı, long-read WGS mi önce gelmeli? Listelenen klinik tablolar (ataksi, miyotoni, EY, nörodejenerasyon) yeterli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → YAPILMALDIR DEE YAPILABİLİR OLARAK DÜZELT. SIRALAMA BELİRTME. ÖNCELİK BELİRTME.
Tekrar genişlemesi WES'in "kör noktalarından biridir." olarak düzelt.
<br>

### A5 · Bölüm 9 — Tekrar Dizisi Genişlemesi (Repeat Expansion)

**Yer:** `Bölüm_09_Repeat_Expansion.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 174

> **🟦 Klinikte dikkat — Presemptomatik test ve etik boyutlar:** Huntington gibi tam penetranslı, tedavisi olmayan hastalıklarda presemptomatik genetik testler özel etik değerlendirme gerektirir. Pek çok uluslararası kılavuz, HD için presemptomatik test öncesinde kapsamlı genetik danışmanlık seanslarını zorunlu kılmaktadır. ***Çocuklara rutin presemptomatik HD testi yapılması önerilmez***.

**Sorulan:** Bu normatif ifade, ulusal/uluslararası kılavuzlarla uyumlu mu? İstisnaları (semptomatik çocuk, juvenil HD şüphesi) belirtilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → doğru

<br>

### A6 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 5. Tanısal testlerle ilişkisi · satır 146

> **Bu mekanizmayı hangi test yakalar? (özet):** ***İlk basamak daima metilasyon-duyarlı bir testtir*** (PWS/AS ve BWS/SRS için MS-MLPA veya metilasyon-spesifik PCR); bu test delesyon, UPD ve ID'nin üçünü birden yakalar. Metilasyon anormalse alt-tip belirlenir: **kopya sayısı** (delesyon?) MS-MLPA/array ile, **UPD** SNP array veya mikrosatellit/trio analiziyle, **ID** ise ne delesyon ne UPD bulunduğunda dışlamayla konur. İmprintli gen tek gense ve metilasyon normalse, sıra **dizilemeye** (nokta varyantı) gelir.

**Sorulan:** "Daima" ifadesi doğru mu? Klinik tablo çok tipikse doğrudan alt-tip testine gidilebilir mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → daima ifadesini sil. 

<br>

### A7 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 8. Sık yapılan hatalar ve klinikte dikkat · satır 199

> **🔴 Sık yapılan hata kutusu**
> 1. **"Ekzom normalse imprinting bozukluğu dışlanır" sanmak.** Standart WES metilasyonu ve çoğu UPD'yi okumaz; PWS/AS/BWS/SRS'yi kaçırır. İmprinting bozukluğu şüphesinde **metilasyon testi** ayrıca istenmelidir.
> 2. **"İki sağlam alel var, o hâlde hastalık olmaz" varsaymak.** İmprintli lokusta işlevsel doz zaten tek alelden gelir; UPD'de "iki kopya" olması normal işlevi garanti etmez.
> 3. **Metilasyon anormalliğini alt-tiple karıştırmak.** "Metilasyon PWS paterni" tanıyı koyar ama delesyon/UPD/ID ayrımını yapmaz; ***tekrarlanma riski için alt-tip şarttır***.
> 4. **İmprinting defektini otomatik "sporadik/düşük risk" saymak.** ID'lerin bir kısmı ailevi ICR mikrodelesyonundan kaynaklanır (%50 risk); danışmadan önce dışlanmalıdır.
> 5. **İzodizomiyi yalnızca imprint sorunu sanmak.** İzodizomi resesif bir varyantı homozigotlaştırarak, ebeveyn taşıyıcılığıyla açıklanamayan resesif hastalık da yapabilir.
> 6. **BWS'de tüm alt-tipleri aynı tümör riskiyle izlemek.** Tarama yoğunluğu moleküler alt-tipe göre ayarlanmalıdır (ICR1 hipermetilasyon / UPD11 en yüksek risk).

**Sorulan:** Alt-tip belirlemenin danışma için şart olduğu ifadesi ve önerilen sıralama doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → şarttır deme yapılması önerilir de.

<br>

### A8 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 158

> **🟦 Klinikte dikkat — ClinGen'in *gen düzeyi* dozaj skorları imprintli lokuslarda yanıltıcıdır.** Bölüm 8'de tanıtılan haploinsufficiency (HI) skorunu imprintli bir gende sorguladığınızda beklediğinizi bulamazsınız: ClinGen gen dozaj listesinde *SNRPN*, *NDN*, *H19* ve *IGF2*'nin HI skoru **0**'dır ("kanıt yok"). Bu, bu genlerin doza duyarlı olmadığı anlamına **gelmez**; anlamı, patojenitenin **gen düzeyinde tek kopya kaybıyla** değil, **bölge ve damgalama düzeyinde** — yani hangi ebeveyn kopyasının kaybedildiğiyle — tanımlanmasıdır. Aynı tuzağın CNV'lerdeki karşılığını Bölüm 3'te *PMP22* üzerinden görmüştük: gen kaydı ile bölge kaydı farklı şeyler söyler. İmprintli bir lokusta refleks, **gen skoruna değil bölge kaydına ve metilasyon paternine** bakmaktır.
>
> **🟦 Klinikte dikkat — De novo ≠ düşük risk (her zaman değil):** İmprinting defektlerinin çoğu sporadik (primer epimutasyon) olup düşük tekrarlanma riski taşır. Ancak ID'lerin bir alt-kümesi, ICR içindeki küçük bir **mikrodelesyondan** kaynaklanır; bu genetik lezyon ebeveynden aktarılabilir ve %50'ye varan tekrarlanma riski yaratır. Bu yüzden "imprinting defekti" tanısı, danışmadan önce mutlaka **ICR mikrodelesyonu açısından incelenmelidir** — ***"epigenetik = sporadik" varsayımı tehlikelidir***.

**Sorulan:** "Mutlaka incelenmelidir" ifadesi pratikte uygulanabilir mi (test erişimi)? Hangi lokuslarda öncelikli?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → mutlaka ifadesine gerek yok.

<br>

### A9 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 156

> **🟦 Klinikte dikkat — ClinGen'in *gen düzeyi* dozaj skorları imprintli lokuslarda yanıltıcıdır.** Bölüm 8'de tanıtılan haploinsufficiency (HI) skorunu imprintli bir gende sorguladığınızda beklediğinizi bulamazsınız: ClinGen gen dozaj listesinde *SNRPN*, *NDN*, *H19* ve *IGF2*'nin HI skoru **0**'dır ("kanıt yok"). Bu, bu genlerin doza duyarlı olmadığı anlamına **gelmez**; anlamı, patojenitenin **gen düzeyinde tek kopya kaybıyla** değil, **bölge ve damgalama düzeyinde** — yani hangi ebeveyn kopyasının kaybedildiğiyle — tanımlanmasıdır. Aynı tuzağın CNV'lerdeki karşılığını Bölüm 3'te *PMP22* üzerinden görmüştük: gen kaydı ile bölge kaydı farklı şeyler söyler. ***İmprintli bir lokusta refleks, gen skoruna değil bölge kaydına ve metilasyon paternine bakmaktır***.
>
> **🟦 Klinikte dikkat — De novo ≠ düşük risk (her zaman değil):** İmprinting defektlerinin çoğu sporadik (primer epimutasyon) olup düşük tekrarlanma riski taşır. Ancak ID'lerin bir alt-kümesi, ICR içindeki küçük bir **mikrodelesyondan** kaynaklanır; bu genetik lezyon ebeveynden aktarılabilir ve %50'ye varan tekrarlanma riski yaratır. Bu yüzden "imprinting defekti" tanısı, danışmadan önce mutlaka **ICR mikrodelesyonu açısından incelenmelidir** — "epigenetik = sporadik" varsayımı tehlikelidir.

**Sorulan:** Bu refleks doğru formüle edilmiş mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → gen skorunun dışında. DMR ve metilasyon paternine bakmaktır.

<br>

### A10 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 5. Tanısal testlerle ilişkisi · satır 181

> **Bu mekanizmayı hangi test yakalar? (özet):** mtDNA lezyonları için hedefli **mtDNA dizileme + delesyon/kopya sayısı analizi**, doğru dokuda (***çocukta kan sıklıkla yeterlidir; erişkinde ve şüphe sürüyorsa idrar epiteli veya kas***) yapılmalıdır. Nükleer nedenler için **WES/WGS** gerekir. Pratikte iki genom birlikte değerlendirilmelidir; giderek artan biçimde **WGS**, her ikisini tek testte kapsadığı için tercih edilmektedir.

**Sorulan:** Doku sıralaması ve yaş ayrımı doğru mu? Kas biyopsisinin yeri günümüzde nerede?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → kan yeterli olabilmektedir, ancak şüphe devam ediyor ve sonuç uygun gelmedi sie idrar epiteli veya kas kullanımı yapılabilir. Erişkin ayrımını belirtmeye gerek yok.

<br>

### A11 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 8. Sık yapılan hatalar ve klinikte dikkat · satır 254

> **🔴 Sık yapılan hata kutusu**
> 1. **"Kanda mtDNA analizi negatif geldi, mitokondriyal hastalık dışlandı."** Mitotik segregasyon nedeniyle kan, özellikle erişkinlerde ve m.3243A>G gibi varyantlarda yanlış negatif verebilir. Şüphe sürüyorsa idrar epiteli veya kas örneklenmelidir.
> 2. **"Ailede maternal geçiş yok, o hâlde mitokondriyal hastalık değil."** Mitokondriyal hastalıkların çoğu nükleer kaynaklıdır ve otozomal resesif kalıtılır; ayrıca tek büyük mtDNA delesyonları tipik olarak sporadiktir. Maternal kalıtımın yokluğu tanıyı dışlamaz.
> 3. **"Heteroplazmi %30, demek ki hafif hastalık olur."** Yüzde–fenotip ilişkisi doku bağımlıdır; kanda %30 olan bir varyant kasta veya beyinde çok daha yüksek olabilir. Tek bir dokudan alınan yüzde, klinik ağırlığın doğrudan ölçüsü değildir.
> 4. **"Laktat normal, mitokondriyal hastalık düşünmedim."** Normal laktat mitokondriyal hastalığı dışlamaz; laktat duyarlı ama özgül olmayan bir destekleyici bulgudur.
> 5. **"WES yaptık, mtDNA da bakılmış olur."** Standart WES mtDNA'yı güvenilir biçimde kapsamaz; heteroplazmi ölçümü ve büyük delesyon saptaması için uygun değildir. ***mtDNA hedefli analiz veya WGS gerekir***.
> 6. **"Homoplazmik varyant, mutlaka patojendir."** Homoplazmik değişikliklerin çoğu haplogrup polimorfizmidir. Homoplazmi bir yük göstergesidir, patojenite kanıtı değildir.
> 7. **"Anneye tekrarlanma riski %50 dedik."** mtDNA varyantı taşıyan bir anneden **tüm** çocuklara varyant geçer; belirsiz olan geçip geçmeyeceği değil, **hangi yükte** geçeceğidir. Bu yüzden risk bir Mendel oranıyla ifade edilemez.
> 8. **"Standart ACMG kriterlerini uyguladık."** mtDNA varyantları için ClinGen'in mtDNA'ya özgü spesifikasyonu kullanılmalıdır (McCormick ve ark., 2020); nükleer frekans eşikleri ve de novo mantığı doğrudan aktarılamaz.

**Sorulan:** Modern WES protokollerinde mtDNA kapsaması arttı mı? Bu uyarı hâlâ geçerli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → her wes protokolünde mtDNA bakılmıyor, özellikle seçilmeli ve ona göre wetlab ve drylab tercihleri sağlanmalı.

<br>

### A12 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 8. Sık yapılan hatalar ve klinikte dikkat · satır 250

> **🔴 Sık yapılan hata kutusu**
> 1. **"Kanda mtDNA analizi negatif geldi, mitokondriyal hastalık dışlandı."** Mitotik segregasyon nedeniyle kan, özellikle erişkinlerde ve m.3243A>G gibi varyantlarda yanlış negatif verebilir. ***Şüphe sürüyorsa idrar epiteli veya kas örneklenmelidir***.
> 2. **"Ailede maternal geçiş yok, o hâlde mitokondriyal hastalık değil."** Mitokondriyal hastalıkların çoğu nükleer kaynaklıdır ve otozomal resesif kalıtılır; ayrıca tek büyük mtDNA delesyonları tipik olarak sporadiktir. Maternal kalıtımın yokluğu tanıyı dışlamaz.
> 3. **"Heteroplazmi %30, demek ki hafif hastalık olur."** Yüzde–fenotip ilişkisi doku bağımlıdır; kanda %30 olan bir varyant kasta veya beyinde çok daha yüksek olabilir. Tek bir dokudan alınan yüzde, klinik ağırlığın doğrudan ölçüsü değildir.
> 4. **"Laktat normal, mitokondriyal hastalık düşünmedim."** Normal laktat mitokondriyal hastalığı dışlamaz; laktat duyarlı ama özgül olmayan bir destekleyici bulgudur.
> 5. **"WES yaptık, mtDNA da bakılmış olur."** Standart WES mtDNA'yı güvenilir biçimde kapsamaz; heteroplazmi ölçümü ve büyük delesyon saptaması için uygun değildir. mtDNA hedefli analiz veya WGS gerekir.
> 6. **"Homoplazmik varyant, mutlaka patojendir."** Homoplazmik değişikliklerin çoğu haplogrup polimorfizmidir. Homoplazmi bir yük göstergesidir, patojenite kanıtı değildir.
> 7. **"Anneye tekrarlanma riski %50 dedik."** mtDNA varyantı taşıyan bir anneden **tüm** çocuklara varyant geçer; belirsiz olan geçip geçmeyeceği değil, **hangi yükte** geçeceğidir. Bu yüzden risk bir Mendel oranıyla ifade edilemez.
> 8. **"Standart ACMG kriterlerini uyguladık."** mtDNA varyantları için ClinGen'in mtDNA'ya özgü spesifikasyonu kullanılmalıdır (McCormick ve ark., 2020); nükleer frekans eşikleri ve de novo mantığı doğrudan aktarılamaz.

**Sorulan:** m.3243A>G özelinde verilen bu uyarı diğer varyantlara genellenebilir mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → özellikle spesifik bir varyant belirtmemelisin.

<br>

### A13 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 7. Pediatrik genetikten klinik örnekler · satır 239

> **Pearson ve Kearns-Sayre sendromları — tek büyük delesyon.** Holt ve arkadaşlarının 1988'de mitokondriyal miyopatili hastaların kasında büyük mtDNA delesyonlarını göstermesi, mtDNA'nın insan hastalığındaki rolünü kanıtlayan ilk bulgulardandır (Holt ve ark., 1988). Pediatride bu delesyonlar iki uçta karşımıza çıkar: süt çocukluğunda **Pearson sendromu** (sideroblastik anemi, pansitopeni, ekzokrin pankreas yetmezliği) ve daha ileri yaşlarda **Kearns-Sayre sendromu** (20 yaş öncesi başlayan progresif eksternal oftalmoplejı, pigmenter retinopati ve kardiyak ileti bozukluğu). Aynı lezyon tipi, delesyonun doku dağılımına göre kemik iliği ağırlıklı veya kas/göz ağırlıklı bir tablo yapar; Pearson'dan sağ kalan çocuklar zamanla Kearns-Sayre fenotipine kayabilir. **Öğreti:** tek büyük delesyonlar genellikle sporadiktir; bu, kardeş tekrarlanma riskini maternal kalıtımlı nokta varyantlarından ayıran kritik bir bilgidir. Ayrıca KSS'de ***kardiyak ileti bozukluğu ani ölüm riski taşıdığı için düzenli EKG izlemi zorunludur***.

**Sorulan:** İzlem sıklığı belirtilmeli mi? Holter/pacemaker eşiği eklenmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → EKG ve kardiyak izlemi ilgili kliniklerce yapılmalıdır demen yereli 

<br>

### A14 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 195

> Birincisi, **popülasyon frekansı kriterleri (BA1/BS1/PM2) yeniden kalibre edilmiştir.** mtDNA'da bir varyantın sık görülmesi, çoğu zaman patojenite yokluğunun değil, o varyantın bir **haplogrup belirteci** olmasının işaretidir. İnsan popülasyonları farklı mtDNA haplogruplarına ayrılır ve her haplogrup, tanımı gereği bir dizi homoplazmik varyantla karakterizedir. Bu nedenle frekans değerlendirmesi, MITOMAP ve HelixMTdb gibi mtDNA-özgü veri tabanları üzerinden ve haplogrup bağlamı gözetilerek yapılmalıdır; ***genel nükleer frekans eşikleri doğrudan aktarılamaz***.

**Sorulan:** Veri tabanı seçimi ve haplogrup uyarısı yeterli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → yeterli

<br>

### A15 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 2.4 Letal-mozaik hipotezi: neden bu sendromlar hiç kalıtılmaz? · satır 108

> **Blaschko çizgileri**, bu mozaikliğin deri üzerindeki görünür haritasıdır. Bu çizgiler ne sinir dağılımını ne damar dağılımını ne de dermatomları izler; embriyogenez sırasında deri hücre soylarının **göç yollarını** yansıtırlar. Sırtta V, gövde yanlarında S, ekstremitelerde çizgisel bir örüntü oluştururlar. Klinik değeri doğrudandır: bir deri lezyonu bu çizgileri izliyorsa, altta neredeyse kesinlikle mozaik bir varyant vardır ve ***test için kan değil, lezyonlu deri istenmelidir***.

**Sorulan:** "Neredeyse kesinlikle mozaik varyant vardır" ifadesinin kesinlik derecesi uygun mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → uygun

<br>

### A16 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 2.1 Zamanlama dağılımı, dağılım her şeyi belirler · satır 68

> Bu üçlüden çıkan pratik kural, bölümün en çok kullanılacak cümlesidir: **varyant ne kadar erken oluşursa o kadar çok hücre soyuna dağılır ve germline'a ulaşma olasılığı o kadar artar.** Klinikte bu kural iki yönde birden çalışır. İleri yönde: erken bir mozaik varyant beklediğinizden daha yaygın tutulum yapar. Geri yönde — ve tanısal olarak daha yararlı biçimde: yaygın tutulumlu bir hastada varyantı kanda bulma şansınız yüksekken, ***tek bir deri lezyonuyla sınırlı bir tabloda kan kesinlikle yanlış dokudur***.

**Sorulan:** "Kesinlikle" sözcüğü burada gerekli mi, yoksa yumuşatılmalı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → kesinlikle ifadesini kullanma! kan uygun doku olmayabilir demen daha uygun

<br>

### A17 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 8. Sık yapılan hatalar ve klinikte dikkat · satır 262

> **🔴 Sık yapılan hata kutusu**
> 1. **"Kanda saptanmadı, mozaiklik yok."** Kan, geç oluşmuş veya doku-sınırlı bir mozaik varyantı hiç taşımayabilir. Negatif kan sonucu mozaikliği dışlamaz; lezyonun bulunduğu doku örneklenmelidir.
> 2. **"Standart WES negatif geldi, genetik neden yok."** Standart derinlikte WES yaklaşık %10 VAF'ın altını göremez. ***Mozaiklik şüphesinde derin hedefli panel veya ddPCR gerekir***.
> 3. **"Ebeveynlerde saptanmadı, o hâlde de novo ve tekrar riski yok."** Ebeveyn germline mozaikliği kanda görünmez. "De novo" olgularda bile tekrarlanma riski sıfır değildir.
> 4. **"VAF %8, demek ki hücrelerin %8'i etkilenmiş."** Heterozigot bir varyantta VAF, taşıyan hücre oranının yaklaşık **yarısıdır**; %8 VAF kabaca %16 hücre demektir. Ayrıca örnek saflığı bu oranı daha da bozar.
> 5. **"Raporda varyant var, doku ve yüzde önemli değil."** Mozaik bir raporda doku adı ve VAF, varyantın kendisi kadar bilgi taşır; ikisi olmadan sonuç yorumlanamaz.
> 6. **"Karyotipte mozaiklik görülmedi."** Mozaik anöploidiyi dışlamak için yeterli sayıda hücre sayılmış olmalıdır; standart sayımda düşük oranlı mozaiklik kolayca kaçar.
> 7. **"Erişkinin kanında düşük VAF'lı somatik varyant bulundu, hastalığı bu açıklıyor."** Yaşla ilişkili klonal hematopoez ayırt edilmeden bu bağ kurulmamalıdır; ikinci bir dokuda doğrulama gerekir.
> 8. **"Aile öyküsü yok, o hâlde genetik değil."** Mozaik sendromların çoğu tanımı gereği sporadiktir; aile öyküsünün yokluğu genetik nedeni desteklemez de dışlamaz da.

**Sorulan:** Hedef derinlik değeri verilmeli mi (ör. ≥1000×)? ddPCR yerine amplikon NGS önerilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → sayısal ifade vermene gerek yok. LR WGS de yapılabileceğini eklemelisin.

<br>

### A18 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 214

> Dördüncüsü ve ters yöndeki tuzak, **klonal hematopoezdir.** Yaş ilerledikçe, kan kök hücrelerinde biriken somatik varyantlar taşıyan klonlar genişleyebilir. Erişkin bir bireyin kanında düşük VAF'lı bir somatik varyant saptanması, bu varyantın hastanın klinik tablosuyla ilgili olduğu anlamına gelmez; özellikle *DNMT3A*, *TET2*, *ASXL1* gibi genlerdeki düşük düzeyli bulgular yaşla ilişkili klonal hematopoezin işareti olabilir. Bu nedenle kanda saptanan düşük VAF'lı bir varyantın hastalıkla ilişkisi, klinik tabloyla ve mümkünse ***ikinci bir dokuyla doğrulanmadan kurulmamalıdır***.

**Sorulan:** Klonal hematopoez ayrımı için yaş eşiği/VAF eşiği verilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → örneğin diyerek başlayarak açıklama yapman iyi olur ama kesin bir dille konuşma, sadece anlaşılırlığını artırsak yeterli olur.

<br>

### A19 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 3. Varyant tipleri · satır 131

> Tablonun okunma biçimi şudur. İlk iki satır standart dizi varyantlarıdır ve tek sorun **duyarlılıktır**. Üçüncü ve dördüncü satırlar kopya sayısı/kromozom düzeyindedir; burada VAF mantığı geçerli değildir ve mozaiklik oranı farklı biçimde (hücre sayımı, alel dengesi) hesaplanır — ayrıca ***klasik karyotipte mozaikliği dışlamak için yeterli sayıda hücre sayılmış olması gerekir***. Beşinci satır, Bölüm 10'daki uniparental dizomiyle doğrudan köprü kurar: mitotik rekombinasyonla oluşan segmental UPD tipik olarak mozaiktir ve Beckwith-Wiedemann sendromunun paternal UPD11 alt tipinde bu mozaiklik kuraldır. Son satır ise bir yorum tuzağıdır ve 6. başlıkta ayrıca ele alınacaktır.

**Sorulan:** Sayı verilmeli mi (ör. 30–50 metafaz, düşük mozaiklikte daha fazla)?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → sayı verilirse güzel olur, ama kaynak bulmak lazım, kaynaksız ifade edemeyiz. eğer kayak bulmazsak yazamayız.

<br>

### A20 · Bölüm 13 — Kodlamayan (Noncoding) ve Regülatör Varyantlar

**Yer:** `Bölüm_13_Noncoding_Regulator_Varyantlar.md` ·  · satır 3

> **Bölümün çekirdek tezi:** Genomun protein kodlayan kısmı %2'den azdır; klinik genetiğin neredeyse tamamı ise on yıllardır bu %2'ye bakmıştır. Kodlamayan varyantlar, bu kör noktanın adıdır. Bu bölümün çekirdek iddiası şudur: **kodlamayan bir varyant, proteinin tek bir amino asidini bile değiştirmeden hastalık yapabilir — çünkü hedefi ürünün kendisi değil, ürünün ifade programıdır.** Bir promotör varyantı genin ne kadar üretileceğini, bir enhancer varyantı hangi dokuda üretileceğini, bir 5′UTR varyantı ne kadar verimli çevrileceğini, bir TAD sınırı varyantı ise hangi genin üretileceğini bozar. Buradan üç klinik sonuç doğar: (1) ***bu varyantları görmek için ekzom yetmez, WGS gerekir***; (2) fenotip çoğu zaman şaşırtıcı biçimde **dar ve tek organa sınırlıdır**, çünkü etkilenen düzenleyici doku-özgüdür; (3) yorumlamada **PVS1 uygulanamaz** ve kanıtın ağırlık merkezi hesaplamadan **fonksiyonel deneye** kayar. Bölüm 8'de yapısal varyant ölçeğinde gördüğümüz düzenleyici mimariyi (TAD, enhancer hijacking) bu bölüm **tek nükleotid** ölçeğine indirir.

**Sorulan:** Üç klinik sonucun tamamı doğru mu? "Dar ve tek organa sınırlı fenotip" genellemesi tutar mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → WGS gereklidir, ancak standart kısa okuma WGS lerde de kaçabilir bu nedenle LR WGS veya Optik genome analizi gibi tekniklerle de testle yapılabilr. buna rağmen tanıya gidilemeyen drumlarda HiC, spesiifk tad domian analizleri vs de yapılabilr.

<br>

### A21 · Bölüm 7 — Splicing (Kırpılma) Varyantları

**Yer:** `Bölüm_07_Splicing.md` · 5. Tanısal testlerle ilişkisi · satır 114

> Splice varyantlarında temel ayrım nettir: **DNA testleri varyantı bulur, ama splicing etkisini RNA gösterir.** Kanonik splice varyantları WES/WGS ile yakalanır; ancak **derin intronik** varyantlar yalnız WGS ile görülür (WES intronları kapsamaz). ***Etkinin kanıtı için ise RNA-seq veya hedefe yönelik cDNA/RT-PCR gerekir*** — bu, splice yorumunda RNA kanıtının (PVS1_Strength / BP7) neden bu kadar değerli olduğunu açıklar (§6).

**Sorulan:** Doğru doku şartı ve minigen assay'in yeri yeterince vurgulanmış mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → kısa WGS göremeyebilir, uzun okuma WGS görebilir.

<br>

### A22 · Bölüm 14 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_14_Ayni_Gen_Farkli_Hastalik.md` · 5. Tanısal testlerle ilişkisi · satır 195

> ***Allelik serilerde test seçiminin belirleyicisi cihaz değil, hangi hastalığın arandığı varsayımıdır.*** Aynı gen için hedefli hotspot dizilemesi bir hastalıkta yeterliyken, başka bir hastalıkta gen tamamı + delesyon/duplikasyon analizi gerekir. Aşağıdaki tablo bu bakışla okunmalıdır.

**Sorulan:** Bu ilke pratikte uygulanabilir mi, yoksa gen tamamının bakılması artık varsayılan mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → genel olarak şu an tüm gen bakılıyor, eğer aile taraması yapılackasa o durumda probandınn varyantını olduğu bölge diziliemesine bakılıyor

<br>

### A23 · Bölüm 17 — Klinik Senaryolarla Sentez: Hastadan Mekanizmaya

**Yer:** `Bölüm_17_Klinik_Senaryolarla_Sentez.md` · 7. Pediatrik genetikten klinik örnekler: sekiz senaryo · satır 251

> **Senaryo 7 — Sekiz yaşında çocuk, kas güçsüzlüğü ve yüksek kreatin kinaz; panel ve ekzom negatif.** Klinik olarak konjenital kas hastalığı düşünülüyor; geniş panel ve ekzom sonuçsuz. **Mekanizma hipotezi:** kodlayan bölge dışında kalan bir splicing kusuru (Bölüm 7, 13). **Test:** ***kas dokusundan RNA dizileme*** (± WGS). **Yorum:** genetik tanısı konmamış nadir kas hastalıkları kohortunda transkriptom dizileme, aday splice-bozucu varyantların doğrulanmasını ve hem ekzonik hem **derin intronik** bölgelerdeki splice-değiştirici varyantların saptanmasını sağlamış, genel tanı oranı **%35** olmuştur; ayrıca sık tekrarlayan bir de novo intronik varyantın, kollajen VI benzeri distrofi düşünülen ve önceki genetik analizleri negatif olan hastaların yaklaşık dörtte birini açıkladığı gösterilmiştir (Cummings ve ark., 2017). **Öğreti:** RNA analizi burada iki iş birden yapar — tanıyı koyar ve Bölüm 16'da gördüğümüz gibi öngörüyü ölçüme çevirerek PS3'ü açar.

**Sorulan:** Bu senaryoda kas biyopsisi önerisi Türkiye koşullarında gerçekçi mi? Fibroblast alternatif olabilir mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → kas dokusunda biyopsi yapılabilir, ancak öncesinde WGS yapılması daha isabetli olur hatta mümkünse uzun okuma WGS önerilir, buna rağmen hala tanı alamasıysa o durumda biyopsi ve RNASeq yapılabilir. Ancak eğer aranan gen belli veya olası ise o genin germline ekspresonu kontrol edilerek doğrudan germline bulk RNA Seq de yapılabilir, bu durum daha non invaziv olduğu için kas biyopisisin önüne geçmelidir.


<br>

### A24 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 5. Tanısal testlerle ilişkisi · satır 171

> | Test | Bu mekanizmayı yakalar mı? | Sınırlılığı |
> |------|----------------------------|-------------|
> | **WES** | Kısmen. Nükleer mitokondriyal genleri (~1500) iyi kapsar; mtDNA'yı ise ancak "off-target" okumalarla, değişken ve güvenilmez biçimde kapsar | ***mtDNA kapsaması standart değildir; heteroplazmi ölçümü güvenilir değildir***; büyük mtDNA delesyonlarını ve kopya sayısını değerlendiremez |
> | **Short-read WGS** | Evet — hem nükleer genleri hem mtDNA'yı yüksek derinlikte kapsar; heteroplazmi ve kopya sayısı tahmini yapılabilir | Düşük düzeyli heteroplazmi için doğrulama gerekir; NUMT (nükleer mtDNA kopyaları) kaynaklı yanlış pozitiflere dikkat |
> | **Long-read WGS** | Evet; büyük mtDNA delesyonlarının sınırlarını ve karmaşık yeniden düzenlenmeleri tanımlamada üstün | Maliyet ve erişim; rutin ilk basamak değil |
> | **Array-CGH / SNP array** | Hayır (mtDNA'yı hedeflemez) | Yalnız nükleer CNV'ler için; mitokondriyal tanıda rolü sınırlıdır |
> | **MLPA** | Sınırlı. Nükleer gen delesyonları için kullanılabilir | mtDNA heteroplazmisini ölçmek için uygun değildir |
> | **RNA-seq** | Dolaylı. Nükleer gendeki splice etkilerini ve ifade kaybını gösterebilir | Doku-spesifik; mtDNA varyantını doğrudan sınıflamaz |
> | **Methylation array** | Hayır | mtDNA hastalık mekanizmasında metilasyonun yerleşik tanısal rolü yoktur |
> | **Karyotip** | Hayır | Çözünürlük tümüyle yetersiz; mtDNA'yı görmez |
> | **(mito-özgü) mtDNA dizileme + delesyon/kopya sayısı analizi** | **Evet — altın standart** | Doğru doku seçilmezse yanlış negatif; yüzde mutlaka raporlanmalı |

**Sorulan:** Bu, her bölümde tekrarlanan **standart test tablosunun** bir örneğidir. Sekiz satırın (WES · short-read WGS · long-read WGS · array · MLPA · RNA-seq · metilasyon array · karyotip) "yakalar mı / sınırlılığı" değerlendirmeleri toptan doğru mu? Düzeltilmesi gereken hücre var mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → doğru

<br>

---

## B. Sayısal eşikler, oranlar ve öğretici basitleştirmeler

*Okuyucunun ezberleyip alıntılayacağı sayılar. Bir kısmı kitapta zaten "temsilî" diye etiketli — etiketin yeterli olup olmadığı da sorudur.*

### B1 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.C — Varyasyon, allel ve varyant tipleri · satır 69

> İki insan genomu birbirinden milyonlarca pozisyonda farklıdır; ama bu farkların ezici çoğunluğu zararsızdır. Klinik genetiğin asıl zorluğu da buradadır: devasa bir nötr varyasyon arka planı içinden, hastalığa gerçekten neden olan varyantı ayıklamak. Bu nedenle modern dilde, herhangi bir referans-dışı değişikliğe nötr bir terim olan **varyant** denir; eskiden yaygın olan "mutasyon" sözcüğü artık daha çok yerleşik adlandırmalarda kullanılır, "polimorfizm" ise popülasyonda yaygın (***genellikle %1'den sık***) ve çoğunlukla zararsız varyantları anlatır. Patojen olup olmama, varyantın bir başka ekseni olarak ayrıca değerlendirilir; bir varyantın yaygın olması onu otomatik olarak benign yapmaz, ama nadir bir hastalık için güçlü bir benign ipucudur. Burada önemli bir uyarı vardır: **referans dizi her zaman "sağlıklı" anlamına gelmez**; referansta da patojen aleller bulunabilir.

**Sorulan:** %1 eşiği hâlâ öğretilmeli mi, yoksa terk edilmiş bir tanım olarak mı sunulmalı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → kalabilir. 
Polimorfizm, bir genetik varyantın belirli bir popülasyonda en az %1 alel frekansına ulaşmış olmasıdır.
MAF≥0.01(%1)
Buradaki oran birey sıklığı değil, alel frekansıdır. Klasik tanımda lokustaki daha seyrek alelin, yani minor allele frequency—MAF değerinin ≥%1 olması gerekir.
| Alel frekansı | Kullanılabilecek ifade                        |
| ------------: | --------------------------------------------- |
|     **<%0,1** | Nadir varyant                                 |
|  **%0,1–<%1** | Düşük frekanslı varyant                       |
|       **≥%1** | Polimorfizm                                   |
|       **≥%5** | Yaygın/common varyant olarak adlandırılabilir |
Ancak bu alt kategorilerin sınırları kaynağa göre değişebilir. Polimorfizmin klasik ve yerleşik eşiği %1’dir; %5 değildir.
Kritik ayrım: polimorfizm ≠ benign
Bir varyantın popülasyonda ≥%1 olması, onun otomatik olarak:
benign,
fonksiyonsuz,
klinik olarak önemsiz
olduğu anlamına gelmez.
Polimorfizm yalnızca frekans temelli bir terimdir. Klinik sınıflandırma ise benign, likely benign, VUS, likely pathogenic veya pathogenic şeklinde ayrıca yapılır. Bu nedenle güncel klinik raporlamada belirsizlik yaratabilecek “polimorfizm” ifadesi yerine çoğunlukla doğrudan variant ve ACMG sınıfı kullanılır. ACMG/AMP de “mutation” ve “polymorphism” yerine nötr variant terminolojisini önermektedir.
%5 nereden geliyor?
ACMG/AMP 2015 kriterlerinde:
Hastalık için beklenenden yüksek popülasyon frekansı → BS1
Alel frekansının >%5 olması → genel durumda bağımsız benign kanıt olarak BA1
şeklinde tanımlanmıştır. Dolayısıyla %5, polimorfizm tanımı değildir; ACMG’nin genel benign sınıflandırma eşiğidir. Üstelik bazı kurucu varyantlar ve düşük penetranslı hastalık alelleri için BA1 istisnaları vardır.
sana haricen genetik terminolojileri kontrol etme için link veriyorum: https://pmc.ncbi.nlm.nih.gov/articles/PMC4450815/pdf/nihms-689203.pdf


<br>

### B2 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.E — Varyantın kökeni ve kalıtım kalıpları · satır 93

> Bir varyantın nereden geldiği, hem rekürrens riski hem de yorum açısından belirleyicidir. **Germline** (eşey hücresi) varyantları gametlerde bulunur, döllenmeyle bireyin tüm hücrelerine geçer ve sonraki kuşaklara aktarılabilir. **Somatik** varyantlar ise döllenmeden sonra tek bir hücrede ortaya çıkar ve yalnızca o hücrenin soyunda bulunur; kanserlerin ve birçok mozaik tablonun temelinde bunlar yatar. Çocukta yeni beliren ve ebeveynlerin kanında saptanamayan varyantlara *de novo* denir; bunların tipik rekürrens riski düşüktür, ancak ebeveynin eşey hücrelerinde gizli bir mozaiklik (gonadal mozaiklik) bulunabileceği için ***risk asla tam olarak sıfır değildir*** (Bölüm 12). Aynı bireyde genetik olarak farklı hücre popülasyonlarının bir arada bulunmasına ise **mozaiklik** denir ve kendi başına bir bölümü hak edecek kadar önemlidir.

**Sorulan:** Gonadal mozaiklik nedeniyle verilen bu ifade doğru mu? Sayısal bir tekrarlanma riski (%1–2 gibi) verilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → verilebilir

<br>

### B3 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 🔎 Bölüm sonu kaynak doğrulama · satır 289

> ### 🔎 Bölüm sonu kaynak doğrulama
> 6/6 kaynak PMID + DOI ile doğrulandı. "Kaynak doğrulaması gerekli" olarak işaretlenmiş açık bir iddia yoktur. Sayısal örnekler (penetrans için 6/8 gibi) ***belirli bir çalışmadan değil, kavramı göstermek için temsilî olarak verilmiştir***. Bölüm, 27.07.2026 tarihli doğrulama turundan geçmiştir (bkz. `Dogrulama_Kutugu.md`).

**Sorulan:** Temsilî sayı kullanımı öğretici mi, yoksa gerçek bir gen üzerinden gerçek penetrans verisi mi kullanılmalı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → bu şekilde kalabilir

<br>

### B4 · Bölüm 2 — Loss-of-Function (İşlev Kaybı) Mekanizmaları

**Yer:** `Bölüm_02_Loss_of_Function.md` · 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu) · satır 314

> ### 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu)
> "Bu bölümdeki tüm kaynakların PMID/DOI bilgisini kontrol et. PMID veya DOI veremediğin kaynağı çıkar. Kaynağı olmayan iddiayı 'kaynak doğrulaması gerekli' olarak işaretle."
>
> **Bu bölüm için durum:** 9/9 kaynak PMID+DOI doğrulandı. NMD eşik kuralı (son ekzon-ekzon bağlantısı ~50 nt) ***öğretici basitleştirmedir; gen/transkripte göre istisnalar olabilir*** ve RNA ile doğrulama önerilir. Bölüm, 27.07.2026 tarihli iddia-düzeyi doğrulama turundan geçmiştir (bkz. `Dogrulama_Kutugu.md`).

**Sorulan:** 50 nt kuralının bu şekilde sunulması yeterli mi? İstisnalar (son ekzon, ilk 150 nt, uzun 3'UTR) örneklenmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → istisnaları da anlatsak güzel olur ama kaynaklı olması gerekir, kafaımzdan yazamaıyız.

<br>

### B5 · Bölüm 2 — Loss-of-Function (İşlev Kaybı) Mekanizmaları

**Yer:** `Bölüm_02_Loss_of_Function.md` · 4.5. C-terminal truncation neden bazen hafif, bazen ağır? · satır 156

> "Son ekzon = her zaman hafif/benign" varsayımı ***bu nedenle yanlıştır*** (Şekil 2.1B).

**Sorulan:** Bu uyarı doğru mu? Son ekzon varyantlarının ne zaman ağır olduğu yeterince açıklanmış mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → şimdilik kalsın bu şekilde. ama burayı not et, sonra tekrar bakıcaz.

<br>

### B6 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · 2.1. Neden "yarım" bazen yetmez? Doz, eşik ve doğrusal olmayan yanıt · satır 58

> Bu çerçeve, Bölüm 2'deki "doz duyarlı genler → dominant; rezervli genler → resesif" ayrımını niceliksel bir resme oturtur. Vurgulanması gereken nokta, eğrinin **şeklinin gene özgü** olmasıdır: aynı %50 fiziksel kayıp, eğrinin dikliğine ve eşiğin yerine göre felç edici veya tamamen önemsiz olabilir. Bu yüzden ***"varyant %50 kayıp yapıyor" bilgisi tek başına fenotip hakkında hiçbir şey söylemez***; o kayıp **hangi gende** oldu sorusu belirleyicidir.

**Sorulan:** Doz–yanıt eğrisi çerçevesi öğretici olarak doğru mu? Aşırı basitleştirme riski var mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → güzel bu şekilde kalsın.

<br>

### B7 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · 2.1. Neden "yarım" bazen yetmez? Doz, eşik ve doğrusal olmayan yanıt · satır 54

> Sezgimiz genellikle doğrusaldır: "%50 protein → %50 işlev → hafif etki" diye düşünmeye eğilimliyiz. Biyoloji çoğu zaman bizi bu sezgiden kurtarır, çünkü gen dozu ile **fenotipik sonuç** arasındaki ilişki nadiren düz bir çizgidir. Birçok sistem, geniş bir doz aralığında neredeyse sabit (platolu) çalışır: enzimler genelde substrat doygunluğu ve metabolik yedekle çalıştığı için aktivite %50'ye inse bile akı (flux) büyük ölçüde korunur. Bunun kuramsal gerekçesi metabolik kontrol analizinde verilmiştir: bir yolağın akısı üzerindeki kontrol çok sayıda enzime dağılır, tek bir enzimin duyarlılık katsayısı küçüktür ve heterozigottaki %50'lik aktivite düşüşü çoğu zaman ölçülebilir bir akı değişikliği yaratmaz — ***resesifliğin yaygınlığı, seçilimle kazanılmış bir "güvenlik payı" değil, enzim ağının kinetik yapısının doğrudan sonucudur*** (Kacser & Burns, 1981, *Genetics*; [DOI](https://doi.org/10.1093/genetics/97.3-4.639)). Bu tür genlerde doz–yanıt eğrisi erken yükselip platoya oturur; **klinik eşik %50 dozun altında** kalır ve tek allel kaybı sessizdir (Şekil 3.1'daki yeşil eğri). Buna karşılık bazı genlerde sistemin işleyişi tam da o ürünün konsantrasyonuna **keskin biçimde bağlıdır**; eğri neredeyse doğrusaldır veya eşiğe yakın diktir, ve %50 doz eğriyi **eşik bandının altına** sokar (kırmızı eğri). İşte haploinsufficiency, bir genin klinik eşiğinin %50 dozun **üstünde** kaldığı bu ikinci senaryodur.

**Sorulan:** Kacser & Burns (1981) çerçevesinin bu kadar kesin sunulması doğru mu? Bu tez literatürde tartışmalı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → kalsın böyle

<br>

### B8 · Bölüm 4 — Gain-of-Function (İşlev Kazanımı)

**Yer:** `Bölüm_04_Gain_of_Function.md` · 3. Varyant tipleri · satır 90

> Aşağıdaki tablo, GoF'a yol açabilen varyant tiplerini ve her birinin ürüne "fazla/yanlış aktiviteyi nasıl kazandırdığını" özetler. Dikkat edilecek nokta, bu listenin Bölüm 2–3'teki LoF/HI tablolarının neredeyse **tersi** olmasıdır: orada baskın aktör nonsense/frameshift/delesyon iken, burada baskın aktör **missense** ve nadir **in-frame** değişiklikler ile **duplikasyonlardır**; ***nonsense/frameshift ise GoF için tipik olarak beklenmez*** (çünkü onlar ürünü yok eder, GoF için aktif ürün gerekir).

**Sorulan:** Bu genelleme doğru mu? İstisnalar (ör. son ekzon kesilmesiyle otoinhibisyon kaybı) belirtilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → kesinlikle belirtilmeli .

<br>

### B9 · Bölüm 4 — Gain-of-Function (İşlev Kazanımı)

**Yer:** `Bölüm_04_Gain_of_Function.md` · 4.3. GoF fenotipleri neden sıklıkla doğuştan ve "fazlalık" temalıdır? · satır 132

> GoF mekanizmalı genlerin büyük kısmı büyüme/sinyal yolaklarında (RTK'lar, RAS-MAPK, iyon kanalları) görev aldığından, fenotipler sıklıkla **aşırı sinyalin** sonuçlarını yansıtır: aşırı veya düzensiz büyüme, kanser yatkınlığı (kontrolsüz proliferasyon), aşırı nöronal uyarılabilirlik (epilepsi), veya gelişim programının erken/yanlış tetiklenmesiyle yapısal anomaliler. RAS-MAPK yolağının GoF'la sürekli uyarıldığı "RASopati"ler (Noonan ve ilişkili sendromlar) bu temanın iyi bir örneğidir: yüz dismorfisi, kalp defektleri, büyüme sorunları ve değişen kanser riski bir arada görülür. Önemli bir nüans: GoF'un FGFR3 örneğinde olduğu gibi aşırı sinyal bir "dur" sinyalini abartıyorsa fenotip *büyüme baskılanması* (cücelik) yönünde de olabilir — yani "fazla sinyal" her zaman "fazla büyüme" demek değildir; ***hangi yolakta fazlalık olduğu belirleyicidir***.

**Sorulan:** FGFR3 üzerinden kurulan bu ders doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → doğru, Akondroplazide FGFR3 gain-of-function varyantı büyümeyi artırmaz; normalde kemik uzamasını frenleyen FGFR3 sinyalini artırarak büyüme plağı kondrositlerinin proliferasyonunu ve hipertrofik farklılaşmasını baskılar.

<br>

### B10 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 2.2. Multimer matematiği: DN neden haploinsufficiency'den ağırdır? · satır 69

> Bu hesabı mekanizmalar arasında karşılaştırınca DN'in ağırlığı somutlaşır. **Haploinsufficiency'de** (null allel) varyant ürün hiç üretilmez; ortada zehirleyecek bir şey yoktur, sağlam allelin ürünü korunur ve işlev yaklaşık **%50** kalır. **DN dimerde** (n=2) tümü-sağlam kompleks oranı (½)² = **¼ (~%25)**; geri kalan ¾ kompleks en az bir varyant alt birim içerdiği için zehirlenir. ***DN trimerde (n=3, örneğin kollajen) oran (½)³ = ⅛ (~%12)***; **DN tetramerde** (n=4, örneğin p53) (½)⁴ = **1/16 (~%6)**. Yani aynı "tek varyant allel" durumu, protein ne kadar çok alt birimliyse o kadar az sağlam kompleks bırakır. Buradaki ders nettir: DN, haploinsufficiency'nin "yarı doz" tablosunu çok aşan, çoğu kez **ağır** bir fenotipe yol açar — çünkü bozuk ürün yalnız eksiltmez, kalanı da harcar.

**Sorulan:** Bu multimer matematiği "rastgele birleşme + ½ varyant alt birim" varsayımıyla temsilî veriliyor. Öğretici mi, yanıltıcı mı? Kollajen için gerçek oran farklı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Haploinsufficiency modelinde varyant alel işlevsel ürün sağlamaz; mutant ürün sağlam alelin ürününü doğrudan bozmaz. Eşit alelik ekspresyon varsayımı altında normal protein miktarı yaklaşık %50’dir, ancak hücresel kompansasyon ve protein kararlılığı nedeniyle gerçek düzey değişebilir.
Dominant-negatif homooligomerlerde ise temsilî bir binom modeli kullanılabilir. Alt birimler WT ve mutant alellerden eşit miktarda üretiliyor, rastgele birleşiyor ve tek bir mutant alt birim kompleksi tamamen işlevsiz kılıyorsa, tamamen WT kompleks oranı (1/2)^n olur. Buna göre dimerde %25, homotrimerde %12,5 ve tetramerde %6,25 tamamen WT kompleks beklenir.
Bu oranlar doğrudan rezidüel işlev veya fenotip ağırlığı olarak yorumlanmamalıdır. Mutant alt birimin ekspresyonu, kararlılığı, oligomerleşme verimi ve karma kompleksin rezidüel aktivitesi sonucu belirler. Kollajenlerde ayrıca trimer bileşimi dikkate alınmalıdır: homotrimerik tip II ve III kollajende teorik normal molekül oranı 1/8 iken, heterotrimerik tip I kollajende heterozigot COL1A1 yapısal varyantı için 1/4, COL1A2 varyantı için 1/2’dir.

<br>

### B11 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 4. Klinik fenotipe dönüşüm · satır 104

> **Soru 2 — DN neden çoğu kez daha ağır seyreder?** §2.2'deki multimer matematiği nedeniyle. Haploinsufficiency işlevi ~%50'ye indirirken, ***DN onu kompleks büyüklüğüne göre %25'e, %12'ye veya daha aşağıya çeker***. Bunun en çarpıcı klinik kanıtı, **aynı gende** null ve DN varyantların ürettiği şiddet farkıdır (OI'da tip I vs tip II–IV). Bu nedenle, bir genin hastalık spektrumunda hem çok hafif (null) hem çok ağır (missense) uçların bulunması, klinisyene mekanizma hakkında doğrudan bilgi verir.

**Sorulan:** "DN her zaman HI'dan ağırdır" genellemesi doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Dominant-negatif varyantlar neden sıklıkla daha ağır olabilir? Güçlü DN varyantlarda mutant ürün yalnızca kendi alelinin işlevini kaybettirmez; WT ürünle birleşerek karma komplekslerin işlevini de azaltabilir. Eşit alelik ekspresyon, rastgele birleşme ve tek mutant alt birimin kompleksi tamamen işlevsiz kılması varsayımlarında, tamamen WT kompleks oranı kompleks büyüklüğü arttıkça (1/2)^n biçiminde azalır. Bu nedenle güçlü DN mekanizma, aynı gendeki klasik haploinsufficiency’ye göre daha düşük rezidüel işlev ve daha ağır fenotip oluşturabilir.
Ancak bu evrensel bir kural değildir. Hesap yalnızca idealize tamamen WT kompleks oranını verir; doğrudan toplam işlevi veya klinik şiddeti göstermez. Mutant ürünün ekspresyonu, kararlılığı, kompleks içine katılımı ve karma kompleksin rezidüel aktivitesi sonucu değiştirir. OI’da COL1A1 null varyantlarının çoğunlukla hafif tip I, bazı yapısal kollajen varyantlarının ise tip II–IV oluşturması bu ilişkiyi iyi gösterir; fakat bütün dominant-negatif veya missense varyantlar haploinsufficiency’den daha ağır değildir.

<br>

### B12 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 2.2. Multimer matematiği: DN neden haploinsufficiency'den ağırdır? · satır 71

> **🔬 Deep-dive — Kollajenin "¾ bozuk" kuralı ve neden delesyon daha hafif?** Tip I kollajenin klasik örneği bu matematiği klinikte gösterir. Kollajen molekülü bir üçlü sarmaldır; her sarmalın düzgün örülmesi için üç zincirin de kusursuz olması ve ***özellikle sarmal boyunca her üçüncü konumdaki glisinlerin korunması gerekir*** (glisin, sarmalın iç eksenine sığabilen tek küçük amino asittir). *COL1A1* veya *COL1A2*'de bir glisini başka bir amino asitle değiştiren missense varyant, bozuk ama yine de sarmala katılmaya çalışan bir zincir üretir; bu zincir sarmalın katlanmasını yavaşlatır, aşırı modifikasyona ve yıkıma yol açar ve içine girdiği molekülü bozar — klasik bir "protein suicide" / zehirli alt birim örneği. Sonuçta sentezlenen kollajen moleküllerinin yaklaşık **¾'ü en az bir bozuk zincir** içerdiği için anormaldir. Buna karşılık, *COL1A1*'in bir kopyasını tümüyle susturan **null allel**, hiç bozuk zincir üretmez: hücre yalnızca **daha az ama normal** kollajen yapar (haploinsufficiency). İşte bu yüzden null allel **hafif osteogenesis imperfecta tip I** yaparken, glisin substitüsyonları **ağır (tip II–IV)** OI yapar (Forlino &amp; Marini, 2000, *Mol Genet Metab*; [DOI](https://doi.org/10.1006/mgme.2000.3039)). Aynı gen, iki farklı mekanizma, zıt ağırlık — ve bu, mekanizma çıkarımının en güçlü doğal deneyidir.

**Sorulan:** Kollajen glisin kuralının bu biçimde anlatımı doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Metnin ana öğretisi doğru. Fakat ¾ kuralı yalnızca COL1A1 için, “delesyon” yerine null/NMD oluşturan varyant, “üç zincir de kusursuz olmalı” yerine tek mutant zincir çoğu durumda molekülü bozabilir denmelidir.

<br>

### B13 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 168

> **🟦 Klinikte dikkat — "Kısaltıcı varyant her zaman en kötü" değildir:** ***Sezgi, protein üretimini erken durduran (nonsense/frameshift) varyantların missense'ten daha ağır olacağını söyler***. DN genlerde bu **tersine dönebilir**: kısaltıcı/null varyant ürünü yok ettiği için *zehirleyemez* ve daha hafif (haploinsufficiency) tablo yapabilirken, ürünü ayakta tutan **missense** varyant kompleksi zehirleyip **daha ağır** hastalık yapabilir. Bu yüzden DN gende varyant tipinden şiddete doğrudan atlamayın; mekanizmayı sorun.

**Sorulan:** OI üzerinden kurulan bu ters-sezgi dersi doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → doğru

<br>

### B14 · Bölüm 6 — Neomorfik ve Antimorfik Alleller

**Yer:** `Bölüm_06_Neomorfik_Antimorfik.md` · 2.2. Neden tekrarlayan hotspot missense? · satır 63

> Neomorfik (ve çoğu antimorfik) varyantın çarpıcı bir ortak özelliği vardır: gen boyunca rastgele dağılmazlar, **belirli kodonlarda tekrar tekrar** ortaya çıkarlar. Bunun nedeni doğrudan mekanizmadan gelir. Yeni bir aktivite kazanmak, işlev kaybetmekten çok daha "zor"dur: bir proteini bozmanın binlerce yolu vardır (herhangi bir kritik kalıntıyı bozan herhangi bir LoF varyant işe yarar), ama ona **belirli yeni bir iş** kazandıracak değişiklik genellikle **çok özel, sayılı** kalıntılarda olur. Bu yüzden neomorfik varyantlar **hotspot** desenler çizer: ***IDH1'de neredeyse daima Arg132, IDH2'de Arg172/Arg140; histon H3'te Lys27***. Bu desen hem mekanizmanın bir sonucudur hem de varyant yorumunda güçlü bir araçtır (PM1 kriteri; §6). Gerasimavicius ve ark.'nın (2022) gösterdiği gibi, LoF dışı (DN/GoF/neomorf) varyantlar üç boyutlu uzayda kümelenme eğilimindedir ve standart tahmin araçları onları sıklıkla kaçırır — bu da hotspot bilgisinin önemini artırır (Gerasimavicius ve ark., 2022, *Nat Commun*; [DOI](https://doi.org/10.1038/s41467-022-31686-6)).

**Sorulan:** Hotspot listesi doğru ve güncel mi? H3K27M için gen adı (H3-3A/H3C2) belirtilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Düzeltilmiş metin
Neomorfik ve birçok dominant-negatif missense varyant, gen boyunca rastgele dağılmak yerine belirli kodonlarda, fonksiyonel motiflerde, protein etkileşim yüzeylerinde veya üç boyutlu yapısal kümelerde yoğunlaşabilir. Bunun nedeni mekanizmadan kaynaklanır: bir proteinin işlevini bozmanın çok sayıda yolu bulunurken, ona belirli bir yeni aktivite, substrat özgüllüğü veya patolojik etkileşim kazandırabilecek değişiklikler çoğu zaman sınırlı sayıdaki kalıntıda mümkündür. Klasik örnekler, neomorfik D-2-hidroksiglutarat üretimine yol açan IDH1 p.Arg132 ile IDH2 p.Arg140/p.Arg172 varyantlarıdır. Bir diğer örnek, en sık H3-3A tarafından kodlanan H3.3 proteininde, daha seyrek H3C2, H3C3 veya H3C11 tarafından kodlanan H3.1 proteinlerinde görülen H3 K27M onkohiston varyantıdır; HGVS terminolojisinde bu değişiklik p.Lys28Met olarak gösterilir. Gerasimavicius ve arkadaşları, DN ve GOF varyantların LoF varyantlara göre üç boyutlu protein yapısında daha fazla kümelendiğini ve standart varyant etki tahmin araçlarının bu mekanizmaları daha düşük başarıyla saptadığını göstermiştir. Bununla birlikte hotspot veya 3D kümelenme tek başına patojeniteyi kanıtlamaz; PM1 yalnızca ilgili gen–hastalık mekanizması için doğrulanmış hotspot veya kritik fonksiyonel bölge bulunduğunda uygulanmalıdır.
Gerasimavicius makalesinin doğru DOI’si: 10.1038/s41467-022-31686-6.

<br>

### B15 · Bölüm 9 — Tekrar Dizisi Genişlemesi (Repeat Expansion)

**Yer:** `Bölüm_09_Repeat_Expansion.md` · 🔎 Bölüm sonu kaynak doğrulama komutu · satır 303

> **Bu bölüm için durum:** 10/10 kaynak PMID + DOI doğrulandı. İşaretlenen spekülatif iddia: DPR toksisitesinin hastalıktaki rölatif ağırlığı "aktif araştırma alanı" olarak etiketlendi. Tüm tekrar eşiği sayısal değerleri literatür konsensusu kaynaklı olup ***"temsilî" olarak verilmiştir; klinik kullanımda güncel gen-spesifik lab kılavuzları tercih edilmelidir***. Bölüm, 27.07.2026 tarihli iddia-düzeyi doğrulama turundan geçmiştir; turda *HTT* eşik aralıkları ve FMRP işlevi ders kitabı çapraz kontrolüyle (Thompson & Thompson 2023) yeniden çapalanmış, iki Mermaid algoritmasındaki satır sonları proje standardına (`<br/>`) çevrilmiş ve metindeki Kiril harf bulaşması giderilmiştir (bkz. `Dogrulama_Kutugu.md`).

**Sorulan:** Eşikleri temsilî bırakıp kılavuza yönlendirmek doğru bir tercih mi, yoksa net bir tablo mu verilmeli?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Neredeyse her zaman anneden” doğru bir epidemiyolojik ifadedir. “Genellikle >1.000 CTG” de tipik dağılımı doğru anlatır; fakat zorunlu eşik veya tanı kriteri değildir.

<br>

### B16 · Bölüm 9 — Tekrar Dizisi Genişlemesi (Repeat Expansion)

**Yer:** `Bölüm_09_Repeat_Expansion.md` · Miyotonik Distrofi — Konjenital form: yenidoğan tuzağı · satır 190

> Konjenital DM1 (CDM1), neredeyse her zaman etkilenmiş anneden çok büyük CTG tekrar sayısı (***genellikle >1000***) miras alan yenidoğanlarda görülür. Ciddi hipotoni ("floppy infant"), solunum yetmezliği ve beslenme güçlükleriyle yoğun bakım başvurusuna yol açar. Annede bilinen DM1 yoksa (çünkü anne hafif etkilenmiş ve farkında olmayabilir), yenidoğanda açıklanamayan hipotoni varlığında anne değerlendirmesi ve DM1 PCR testi hayat kurtarabilir. CDM1, annenin miyotonisine bakılarak anlaşılabilecek bir durumdur (De Serres-Bérard ve ark., 2021; Chau ve Kalsotra, 2015).

**Sorulan:** CDM1 için verilen "neredeyse her zaman anneden" ve ">1000 CTG" ifadeleri doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → “Neredeyse her zaman anneden” doğru bir epidemiyolojik ifadedir. “Genellikle >1.000 CTG” de tipik dağılımı doğru anlatır; fakat zorunlu eşik veya tanı kriteri değildir.

<br>

### B17 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 2.4 Çift genom: mitokondriyal fenotip ≠ mitokondriyal kalıtım · satır 95

> Bunun klinik sonucu belirleyicidir. ***Kompleks II tümüyle nükleer kodludur; dolayısıyla izole Kompleks II eksikliği hiçbir zaman maternal kalıtılmaz***. Kompleks I'in 45 civarındaki alt biriminin yalnızca 7'si mtDNA kaynaklıdır; geri kalanındaki bir varyant otozomal resesif bir hastalık üretir. Aynı klinik tablo — örneğin Leigh sendromu — hem *MT-ATP6*'daki bir mtDNA varyantından hem de *SURF1* gibi bir nükleer genden kaynaklanabilir; ilkinde risk maternaldir ve tüm çocuklara geçer, ikincisinde her gebelikte %25'tir. **Fenotip aynıdır, mekanizmanın son yolu aynıdır, ama kalıtım ve dolayısıyla aileye verilecek risk tümüyle farklıdır.**

**Sorulan:** Kompleks II ve Kompleks I alt birim sayıları (45 alt birimin 7'si mtDNA) doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Düzeltilmiş metin
Kompleks II, SDHA, SDHB, SDHC ve SDHD olmak üzere dört yapısal alt birimden oluşur ve bu alt birimlerin tamamı nükleer genom tarafından kodlanır. Montaj faktörleri de nükleer kodlu olduğundan primer izole Kompleks II eksikliği, mtDNA’ya özgü maternal kalıtım göstermez.
Memeli Kompleks I’i 45 alt birim kopyasından oluşur: yedi alt birim mtDNA tarafından, kalan 38 alt birim kopyası nükleer genom tarafından kodlanır. NDUFAB1 kompleks içinde iki kopya bulunduğundan bu 45 alt birim 44 farklı gene karşılık gelir. Nükleer Kompleks I hastalıklarının çoğu otozomal resesiftir; ancak NDUFA1 ilişkili X’e bağlı hastalık gibi istisnalar vardır.
Leigh sendromu, MT-ATP6 gibi mtDNA varyantlarından veya SURF1 gibi nükleer genlerdeki biallelik varyantlardan kaynaklanabilir. MT-ATP6 ilişkili hastalıkta annenin tüm çocukları varyantı alma açısından risk altındadır; heteroplazmi ve klinik şiddet çocuklar arasında değişebilir. SURF1 ilişkili otozomal resesif hastalıkta ise her iki ebeveyn taşıyıcıysa etkilenme riski her gebelik için %25’tir.
Sonuç: “Kompleks II tamamen nükleer kodludur” ve “Kompleks I’in 45 alt biriminin 7’si mtDNA kökenlidir” doğrudur. Hatalı bölüm, nükleer Kompleks I hastalıklarının tamamını otozomal resesif saymak ve mtDNA varyantının bütün çocuklarda zorunlu olarak aynı sonucu oluşturacağını söylemektir.

<br>

### B19 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 2.2 Poliplazmiden eşiğe: dozun sürekli hâle gelmesi · satır 73

> Eşiğin sayısal değeri varyant tipine ve dokuya göre değişir; nokta varyantları için tipik olarak yüksek oranlar (temsilî olarak %60–90 aralığı), tek büyük delesyonlar için ise daha düşük oranlar bildirilmiştir (Gorman ve ark., 2016). Ancak klinisyen için ezberlenmesi gereken sayı değil, **ilkedir**: eşik, dokunun oksidatif enerji talebiyle ters orantılıdır. Sürekli ve yüksek ATP tüketen dokular — merkezî sinir sistemi, kalp kası, iskelet kası, retina ve optik sinir, böbrek tübülü, iç kulak — düşük eşiklidir ve erken etkilenir. Fibroblast gibi düşük talepli dokular yüksek mutant yüklerini bile tolere edebilir. Mitokondriyal hastalıkların neden ***neredeyse her zaman çok sistemli ama nörolojik ve kardiyak ağırlıklı*** seyrettiğinin cevabı budur.

**Sorulan:** Bu genelleme doğru mu? İzole organ tutulumlu tablolar (LHON, izole miyopati) bu ifadeyi zayıflatıyor mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Düzeltilmiş metin
Heteroplazmi eşiğinin sayısal değeri varyanta, etkilenen OXPHOS işlevine, hücre tipine ve ölçülen sonlanıma göre değişir. Heteroplazmik mtDNA varyantları için %60–90 aralığı sıklıkla kullanılan temsilî bir çerçevedir; bazı tek büyük mtDNA delesyonlarında daha düşük, bazı tek nükleotid veya mt-tRNA varyantlarında daha yüksek eşikler bildirilmiştir. Bununla birlikte güncel veriler evrensel bir eşik olmadığını ve bazı dokularda %60’ın altında biyokimyasal bozukluk gelişebildiğini göstermektedir.
Yüksek OXPHOS bağımlılığı ve sınırlı metabolik rezerv; merkezî sinir sistemi, kalp, iskelet kası, retina, iç kulak ve böbrek tübülleri gibi dokuları mitokondriyal işlev kaybına duyarlı hâle getirir. Ancak heteroplazmi eşiği enerji talebiyle basit bir ters orantı göstermez. Mutant mtDNA’nın doku ve hücreler arasındaki dağılımı, sağlam mtDNA kopya sayısı, mitokondriyal biyogenez, hücresel metabolik esneklik, yaş ve nükleer değiştiriciler de fenotipi belirler. Fibroblastlar bazı varyantların etkisini kültür koşullarında maskeleyebilir; bu nedenle normal fibroblast biyokimyası hastalıkla ilişkili dokudaki bozukluğu dışlamaz.
Mitokondriyal hastalıklar sıklıkla multisistemiktir ve nörolojik, kas ve kardiyak bulgularla zenginleşir; ancak LHON, izole sağırlık, izole miyopati ve CPEO gibi organ-seçici fenotipler iyi tanımlanmıştır. Bu tablolar eşik ilkesine aykırı değildir; dokuya özgü mutant dağılımın ve hücre tipine özgü biyolojik duyarlılığın enerji talebi kadar belirleyici olduğunu gösterir.
Net sonuç: İzole organ fenotipleri mekanizmayı zayıflatmaz. Fakat “mitokondriyal hastalıklar neredeyse her zaman multisistemiktir” ve “eşik enerji talebiyle ters orantılıdır” cümleleri çıkarılmalıdır. Bunların yerine doku dağılımı + hücresel duyarlılık + metabolik rezerv modeli kullanılmalıdır.

<br>

### B20 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 2.3 Yüzde neden sabit değil: darboğaz ve mitotik segregasyon · satır 87

> **🔬 Deep-dive — mtDNA neden babadan geçmez, ve "hiç" mi geçmez?** Paternal mtDNA'nın elenmesi tek bir mekanizmaya değil, üst üste binen birkaç güvenceye dayanır. Birincisi basit bir **seyreltme** sorunudur: olgun bir oosit yüz binler mertebesinde mtDNA taşırken, sperm yalnızca birkaç yüz mitokondri getirir; oran baştan binde birler düzeyindedir. İkincisi **etkin yıkımdır**: döllenmeden sonra sperm kaynaklı mitokondriler işaretlenerek otofajik yolaklarla ortadan kaldırılır. Bu iki katmanın birlikte çalışması, insan pedigrilerinde ***maternal kalıtımın neden istisnasız görünen bir kural gibi davrandığını açıklar***. Literatürde çok az sayıda **paternal mtDNA geçişi** bildirimi bulunmakla birlikte, bunlar son derece nadirdir, bir kısmı tartışmalıdır ve klinik danışmanlık pratiğini değiştirmez. ⚠️ Bu istisnaların sıklığı ve mekanizması hâlâ tartışmalıdır; genetik danışmada maternal kalıtım kuralı esas alınmalı, paternal geçiş rutin bir olasılık olarak sunulmamalıdır.

**Sorulan:** Paternal mtDNA geçişi bildirimleri karşısında bu ifade nasıl konumlandırılmalı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Düzeltilmiş metin
Deep-dive — mtDNA neden babadan geçmez; gerçekten “hiç” mi geçmez?
İnsanlarda mtDNA kalıtımı klinik olarak maternal kabul edilir. Bu tek bir bariyere değil, üst üste binen mekanizmalara dayanır. Olgun oosit yüz binler mertebesinde mtDNA molekülü taşırken sperm yalnızca sınırlı sayıda mitokondri içerir ve mtDNA içeriği son derece düşüktür. Güncel insan verileri, sperm mitokondrilerindeki intakt mtDNA’nın spermatogenez sırasında büyük ölçüde veya tamamen elimine edilebildiğini; TFAM’ın mitokondriden uzaklaştırılmasının bu süreçle ilişkili olduğunu göstermektedir. Döllenmeden sonra paternal mitokondrilerin otofajik ve lizozomal yollarla uzaklaştırılması da memeli modellerinde gösterilmiş ek bir güvence mekanizmasıdır.
İnsanlarda paternal veya biparental mtDNA kalıtımıyla uyumlu az sayıda bildirim vardır. Bununla birlikte daha geniş genomik çalışmalar, bu görünümün babadan otozomal olarak aktarılan mega-NUMT’lar tarafından taklit edilebildiğini göstermiştir. Bu nedenle gerçek paternal mtDNA aktarımının varlığı ve sıklığı kesinleşmiş değildir; varsa bile olağanüstü istisnai görünmektedir.
Genetik danışmanlıkta maternal kalıtım kuralı korunmalıdır. mtDNA patojenik varyantı taşıyan erkeklerin çocukları için paternal aktarım rutin bir risk olarak sunulmaz. Şüpheli bir baba–çocuk aktarımında paternal kalıtım sonucuna varmadan önce kontaminasyon, örnek kimliği, NUMT/mega-NUMT ve analiz artefaktları kapsamlı biçimde dışlanmalıdır.
Net düzeltme: Metninizin klinik mesajı doğru, fakat “seyreltme + döllenme sonrası otofaji” modeli insanlarda tek ve kesin açıklama gibi sunulmamalıdır. Spermatogenez sırasında mtDNA eliminasyonu güncel anlatıya eklenmelidir.

<br>

### B21 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 2.3 VAF: mozaikliğin sayısı ve tuzakları · satır 94

> **🔬 Deep-dive — VAF ne zaman hücre oranının yarısı DEĞİLDİR?** Dört durumda bu dönüşüm bozulur ve her biri klinikte karşımıza çıkar. **(1) Kopya sayısı değişimleri:** Mozaik bir delesyonda varyant "alel" kaybolmuş durumdadır; VAF yerine kopya sayısı oranı (veya alel dengesi) değerlendirilir ve yarıya bölme mantığı geçerli değildir. **(2) X kromozomu ve hemizigotluk:** Erkekte X'teki bir varyant hemizigottur; taşıyan hücrede tek alel vardır ve o alel varyanttır, dolayısıyla VAF doğrudan hücre oranına eşittir — yarıya bölmek yanlış olur. **(3) Homozigot veya bileşik heterozigot bağlam:** İkinci vuruşun eklendiği hücrelerde alel dengesi değişir. **(4) Örnek saflığı:** Bir doku örneği asla tek tip hücreden oluşmaz; lezyonlu deriden alınan bir biyopside lezyon hücreleri örneğin yalnızca %30'unu oluşturuyorsa, ***ölçülen VAF gerçek klonal yükü olduğundan çok daha düşük gösterir***. Bu son madde, cerrahi örneklerde patologla birlikte "lezyon-zengin" bölge seçmenin neden tanısal başarıyı artırdığını açıklar.

**Sorulan:** Örnek saflığı anlatımı doğru mu? Düzeltme yapılabileceği (lezyon oranına bölme) belirtilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Metnin düzeltilmiş biçimi
Örnek saflığı: Bir doku örneği çoğunlukla mutant ve mutasyonsuz hücrelerin karışımıdır. Kopya-nötr, diploid bir lokusta heterozigot varyant için ölçülen VAF, tüm örnekte varyant taşıyan hücre oranının yaklaşık yarısıdır. Ancak lezyon hücreleri örneğin yalnızca belirli bir kısmını oluşturuyorsa VAF, varyantın lezyon içindeki klonal oranını doğrudan göstermez. Lezyon hücrelerinin DNA’ya katkısı ρ, bunlar içinde varyant taşıyan hücre oranı f ise ideal modelde VAF≈ρf/2 olur. Buna göre lezyon içindeki hücresel oran yaklaşık f≈2×VAF/ρ formülüyle tahmin edilebilir. Örneğin lezyon saflığı %30 olan bir örnekte bütün lezyon hücrelerinde heterozigot bulunan bir varyantın beklenen VAF’ı yaklaşık %15’tir.
Bu düzeltme yalnızca temsilîdir. Lokal kopya sayısı değişikliği, LOH, anöploidi, mutant alel multiplicity’si, hücresel heterojenite ve teknik alel yanlılığı varsa basit bölme işlemi geçerli değildir. Ayrıca histolojik olarak tahmin edilen lezyon oranı, DNA havuzundaki gerçek lezyon katkısıyla aynı olmayabilir. Bu nedenle patolojik değerlendirme ve makrodiseksiyon tanısal duyarlılığı artırır; fakat VAF’tan hücre oranı hesaplanırken saflık, lokal kopya sayısı ve hedef hücre tipi birlikte değerlendirilmelidir.
Net düzeltme: “Lezyon oranına bölme yapılabilir” denmelidir; fakat hücre oranı için doğru basit formül 2 × VAF / lezyon saflığıdır. Ayrıca bunun yalnızca diploid, heterozigot, kopya-nötr modelde geçerli olduğu açıkça yazılmalıdır.

<br>

### B22 · Bölüm 15 — Digenik, Oligogenik Kalıtım ve Modifiye Edici Lokuslar

**Yer:** `Bölüm_15_Digenik_Oligogenik_Modifier.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 229

> **🟦 Klinikte dikkat — "İki gende varyant bulduk" bir gözlemdir, sonuç değildir:** Her sağlıklı bireyin genomunda çok sayıda nadir varyant bulunur; herhangi iki aday gende birer nadir varyantın rastlantısal olarak bir arada bulunması kaçınılmazdır. Digenik iddiayı kurmak için en az şu üçü gerekir: ***(1) iki ürün arasında gösterilebilir biyolojik bağ*** (aynı kompleks/yolak; protein–protein etkileşimi), **(2)** ailede **birlikte ayrışma** — yalnız çift-taşıyıcılar hasta, **(3)** **bağımsız ailelerde tekrarlanma**. Bunlara fonksiyonel birlikte-etki gösterimi eklenirse iddia güçlenir. Schäffer'in derlemesi, yayımlanmış insan digenik kalıtım örneklerinde en çok işe yarayan iki bilgi kaynağının **aday gen bilgisi** ve **protein–protein etkileşim bilgisi** olduğunu; buna karşılık pozisyonel bağlantı analizinin bu alanda büyük ölçüde başarısız kaldığını göstermiştir (Schäffer, 2013).

**Sorulan:** Üç koşul yeterli mi? Fonksiyonel model (hücre/hayvan) dördüncü koşul olarak eklenmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Metnin düzeltilmiş biçimi
Klinikte dikkat — “İki gende varyant bulduk” bir gözlemdir, digenik tanı değildir. Her bireyin genomunda çok sayıda nadir varyant bulunduğundan, iki aday gendeki varyantların aynı kişide saptanması rastlantısal olabilir. Digenik bir model öne sürülmeden önce gerçek digenik kalıtım, monogenik hastalık artı modifier etkisi ve iki bağımsız moleküler tanının birleşmesi birbirinden ayrılmalıdır.
Güçlü bir digenik iddia; monogenik açıklamaların kapsamlı biçimde dışlanmasını, iki gen arasında hastalıkla ilgili biyolojik ilişki bulunmasını, kombinasyonla uyumlu aile segregasyonunu, varyant çiftinin sağlıklı kontrol popülasyonlarında bulunmamasını veya beklenenden az bulunmasını ve tercihen bağımsız aile ya da kohortlarda tekrarlanmasını gerektirir. Gerçek digenik modelde tek varyant taşıyan bireylerin etkilenmemesi beklenirken, monogenik artı modifier modelinde primer varyantı taşıyan bireyler daha hafif veya farklı fenotip gösterebilir.
En güçlü kanıt, iki genin ve mümkünse iki spesifik varyantın ortak etkisini tek tek etkileriyle karşılaştıran kombinatoryal fonksiyonel modeldir. Deney yalnız çift mutantı değil, WT, yalnız A, yalnız B ve A+B koşullarını içermelidir. Hayvan modeli şart değildir; izogenik hücre, hasta hücresi, iPSC/organoid veya uygun biyokimyasal sistem kullanılabilir. Fonksiyonel ortak-etki gösterimi bulunmayan yeni iddialar kesin digenik tanı yerine aday veya olası digenik model olarak raporlanmalıdır.
Net cevap: Üç koşul yeterli değildir. Fonksiyonel ortak-etki modeli dördüncü bir süsleyici unsur değil, özellikle yeni ve küçük olgu sayılı digenik iddialarda nedenselliği kuran ana kanıt alanlarından biridir.

<br>

### B23 · Bölüm 15 — Digenik, Oligogenik Kalıtım ve Modifiye Edici Lokuslar

**Yer:** `Bölüm_15_Digenik_Oligogenik_Modifier.md` · 2.2 Trialelik kalıtım: kalıtım modelinin kendisi sorgulanınca · satır 73

> Bu bulgunun kavramsal ağırlığı, tek bir hastalığın ötesindedir. Burada sorgulanan şey bir genin patojenitesi değil, **kalıtım modelinin kendisidir**: aynı lokusta iki patojen alel taşıyan bir bireyin sağlıklı kalabilmesi, "resesif" etiketinin her zaman yeterli olmadığını gösterir. ⚠️ Trialelik kalıtımın BBS'deki kapsamı ve genelleştirilebilirliği literatürde tartışılmıştır; ***bu modelin her ailede geçerli olduğu varsayılmamalı***, ancak kalıtım modelinin sorgulanabilir olduğu ilkesi korunmalıdır.

**Sorulan:** Trialelik kalıtım uyarısı yeterince güçlü mü? Model bugün büyük ölçüde terk edildi mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Düzeltilmiş metin
Bardet–Biedl sendromunda trialelik kalıtım tarihsel olarak önemli fakat günümüzde ciddi biçimde tartışmalı bir modeldir. İlk çalışmalarda, bir BBS geninde iki varyant taşıdığı hâlde belirgin fenotip göstermeyen bazı bireylerin, ikinci bir BBS genindeki üçüncü varyant bulunmadığında sağlıklı kaldığı bildirilmiş ve üç alelin hastalık için birlikte gerekli olabileceği öne sürülmüştür. Daha sonraki geniş genetik çalışmalar bu zorunlu trialelik modeli tutarlı biçimde doğrulamamıştır. Güncel konsensüs BBS’yi, aynı gendeki bialelik patojenik veya olası patojenik varyantlarla oluşan otozomal resesif bir hastalık olarak kabul eder.
Bununla birlikte ikinci BBS genindeki ek varyantların fenotip şiddetini, organ tutulumunu veya ekspresiviteyi değiştirebileceğine ilişkin veriler vardır. Bu nedenle “zorunlu üçüncü alel” ile “ikinci-lokus modifier etkisi” birbirinden ayrılmalıdır. Birincisi günümüzde rutin tanı veya rekürrens hesabında kullanılmamakta; ikincisi ise araştırılmaya devam eden, fakat klinik yorum standardı henüz oluşmamış bir mekanizma olarak kabul edilmektedir.
Bir BBS geninde trans yerleşimli iki gerçek patojenik varyant taşıdığı bildirilen sağlıklı birey, doğrudan trialelizm kanıtı sayılmamalıdır. Önce varyant sınıflandırması, faz, yaşa bağlı fenotip, hipomorfik etki, CNV ve intronik varyantlar ile eksik klinik değerlendirme yeniden incelenmelidir.
Net cevap: Zorunlu trialelik BBS modeli bugün büyük ölçüde klinik kullanımdan çıkmıştır. Ancak BBS genleri arasındaki modifier etkiler ve toplam varyant yükü bütünüyle terk edilmiş değildir. Metin bu iki kavramı kesin biçimde ayırmalıdır.

<br>

### B24 · Bölüm 16 — Mekanizmadan Varyant Yorumuna: ACMG/ClinGen Sentezi

**Yer:** `Bölüm_16_Mekanizmadan_Varyant_Yorumuna.md` · 1. Kavramsal tanım · satır 45

> **İkincisi, tek bir kriter nadiren yeter.** En güçlü kriter olan PVS1 bile tek başına patojenik sınıfa ulaştırmaz; ***yanına en az bir destekleyici kanıt gerekir***. Bu, çerçevenin muhafazakârlığının kasıtlı bir özelliğidir.

**Sorulan:** Bu ifade nokta puanlama sisteminde doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**İfade nokta sisteminde kısmen doğru, fakat “en az bir destekleyici kanıt” bölümü hatalıdır.**

PVS1’in **Very Strong** düzeyinde uygulanması:

[
\text{PVS1}_{VS}=+8\ \text{puan}
]

Nokta sistemindeki eşikler:

| Toplam puan | Sınıf           |
| ----------: | --------------- |
|         ≥10 | Patojenik       |
|         6–9 | Olası patojenik |
|         0–5 | VUS             |
|   −1 ila −6 | Olası benign    |
|         ≤−7 | Benign          |

Dolayısıyla:

[
PVS1_{VS}=8
]

tek başına **patojenik sınıfa ulaşmaz**. Saf puan hesabına göre **olası patojenik** aralığındadır. ([erepo.clinicalgenome.org][1])

Ancak bir adet formal **Supporting** kriter yalnızca `+1` puandır:

[
8+1=9
]

Bu da hâlâ **olası patojenik** sınıftır, patojenik değildir.

Patojenik sınıfa geçmek için en az iki ek puan gerekir:

[
8+2=10
]

Bu şu kombinasyonlardan biri olabilir:

* `PVS1_VeryStrong + 1 Moderate`
* `PVS1_VeryStrong + 2 Supporting`
* Daha güçlü başka bir bağımsız kanıt

## Kritik ayrım: saf nokta sistemi ve ACGS uygulaması

Saf Tavtigian nokta modelinde:

> `PVS1_VeryStrong` tek başına 8 puanla **likely pathogenic** aralığındadır.

Buna karşılık ACGS 2024, BA1 istisnası dışında `(likely) pathogenic` veya `(likely) benign` sınıflandırma için **en az iki bağımsız kanıt kriteri** bulunmasını ister. Bu ek güvenlik kuralında yalnız PVS1 bulunan varyant, ikinci doğrulayıcı kanıt elde edilene kadar **VUS** olarak tutulur. Bir Supporting kriter eklenirse toplam 9 olur ve **likely pathogenic** sınıfına çıkabilir; yine patojenik olmaz. ([Genomics Education Programme][2])

## Metindeki ikinci sorun: “PVS1” her zaman 8 puan değildir

Şöyle yazılmalıdır:

> **PVS1 kriterinin Very Strong düzeyinde uygulanması 8 puandır.**

Çünkü PVS1 karar ağacına göre:

* PVS1_VeryStrong = 8
* PVS1_Strong = 4
* PVS1_Moderate = 2
* PVS1_Supporting = 1

olarak düşürülebilir. Örneğin NMD’den kaçan, biyolojik olarak önemli olmayan bir transkripti etkileyen veya proteinin sınırlı bir bölümünü kaybettiren varyantta tam PVS1 kullanılamaz. ClinGen’in güncel kılavuz sayfası PVS1 karar ağacını ve kriter gücü modifikasyonlarını temel referans olarak göstermektedir. ([ClinGen][3])

## Düzeltilmiş metin

> **Very Strong düzeyinde uygulanan PVS1, nokta sisteminde 8 puan sağlar ve tek başına patojenik sınıf için gereken 10 puana ulaşmaz. Patojenik sınıfa geçmek için en az iki ek puan gerekir; bu, bir Moderate veya iki bağımsız Supporting kriterle sağlanabilir. Bir Supporting kriter eklenmesi toplamı yalnızca 9 puana çıkarır ve sınıflandırma olası patojenik düzeyinde kalır. Bazı klinik uygulama kılavuzları ayrıca, tek bir güçlü kriterin sınıflandırmayı tek başına belirlememesi için en az iki bağımsız kanıt şartı uygular.**

**Net düzeltme:**
“PVS1 tek başına patojenik yapmaz” → doğru.
“Patojenik olması için yanına bir Supporting yeterlidir” → yanlış.
**Patojenik için `+2` ek puan gerekir.**

[1]: https://erepo.clinicalgenome.org/cspec/ui/svi/doc/1570648177?utm_source=chatgpt.com "Criteria Specification Registry"
[2]: https://www.genomicseducation.hee.nhs.uk/wp-content/uploads/2024/08/ACGS-2024_UK-practice-guidelines-for-variant-classification.pdf "Microsoft Word - UK Practice Guidelines for Variant Classification v1.2 2024 (002)"
[3]: https://clinicalgenome.org/tools/clingen-variant-classification-guidance/ "ClinGen Variant Classification Guidance - ClinGen | Clinical Genome Resource"


<br>

### B25 · Bölüm 16 — Mekanizmadan Varyant Yorumuna: ACMG/ClinGen Sentezi

**Yer:** `Bölüm_16_Mekanizmadan_Varyant_Yorumuna.md` · 2.1 Popülasyon kanıtı: "nadir" hastalığa göre tanımlanır · satır 77

> **🟦 Klinikte dikkat — Bir varyantın "gnomAD'de yok" olması ne kadar kanıttır?** Yokluk, PM2'yi (***orta güçte değil, günümüzde çoğu uzman grubunda destekleyici güce indirilmiş biçimde***) destekler; ama tek başına patojenite kanıtı değildir. Her insan genomunda çok sayıda nadir, işlevsel olarak zararsız varyant vardır. Gen düzeyinde kısıt ölçütleri bu kanıtı bağlamlandırır — **pLI** ExAC veri kümesiyle tanımlanmış (Lek ve ark., 2016), **LOEUF** ise gnomAD ile getirilmiştir (Karczewski ve ark., 2020): kısıtlı bir gende nadir bir kesici varyant anlamlıyken, kısıtsız bir gende aynı bulgu çok daha zayıftır.

**Sorulan:** PM2'nin destekleyiciye indirilmesi genel geçer mi, yoksa VCEP'e göre değişiyor mu diye sunulmalı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**İki katmanlı sunulmalı:**

> **ClinGen SVI’nin genel önerisi, PM2’nin Moderate düzeyden Supporting düzeye indirilmesidir. Ancak ilgili gen–hastalık ilişkisi için onaylanmış VCEP spesifikasyonu varsa PM2’nin uygulanma koşulu, frekans eşiği ve kanıt gücü o spesifikasyona göre belirlenir.**

Dolayısıyla metindeki **“günümüzde çoğu uzman grubunda destekleyici güce indirilmiştir”** ifadesi belirsiz kalıyor. Daha kesin olan:

> **ClinGen SVI’nin genel çerçevesinde PM2_Supporting olarak uygulanır; gen ve hastalığa özgü VCEP kuralları farklı bir eşik veya güç tanımlayabilir.**

ClinGen SVI, 2020’de popülasyon yokluğunun 2015 ACMG/AMP sisteminde gereğinden fazla ağırlıklandırıldığını ve tek başına Moderate kanıtın öngörülen odds değerini karşılamadığını belirterek PM2’yi Supporting düzeye indirdi. Bu öneri ClinGen’in Temmuz 2025’te güncellenen genel varyant sınıflandırma rehberinde hâlen yer alıyor. 

## VCEP’e göre ne değişebilir?

VCEP spesifikasyonları üç bileşeni değiştirebilir:

1. **Kanıt gücü:** Supporting, Moderate veya uygulanamaz.
2. **Frekans eşiği:** “Tamamen yok” yerine hastalığa özgü çok düşük bir PopMax/FAF eşiği kullanılabilir.
3. **Teknik koşullar:** Kalıtım biçimi, penetrans, hastalık prevalansı, kurucu varyantlar, cinsiyet ve değerlendirilecek popülasyon alt grubu tanımlanabilir.

Örneğin GALT ve F9 spesifikasyonları PM2’yi Supporting düzeyinde kullanırken, bazı VCEP spesifikasyonları ve önceki onaylı uygulamalar PM2_Moderate kullanımını korumuştur. Bu nedenle bütün genler için tek bir kuvvet düzeyi dayatılmamalıdır. ([Evrensel Veri Deposytosu][1])

### Uygulama sırası

| Durum                                                 | Yaklaşım                                                |
| ----------------------------------------------------- | ------------------------------------------------------- |
| Güncel ve onaylı gen–hastalık VCEP spesifikasyonu var | **VCEP kuralını uygula**                                |
| VCEP spesifikasyonu yok                               | **ClinGen SVI genel varsayılanı: PM2_Supporting**       |
| Eski bir VCEP sürümü kullanılıyor                     | Güncel CSpec sürümünü ve değişiklik tarihini kontrol et |
| Yalnız laboratuvar içi kriter mevcut                  | Hangi rehberden sapıldığı açıkça belgelenmeli           |

ClinGen CSpec Registry’nin amacı, VCEP’lerin gen ve hastalığa özgü ACMG/AMP spesifikasyonlarını yayımlamaktır; bu spesifikasyonlar ayrıca ClinGen VCEP Review Committee tarafından değerlendirilir. ([Kriteri Belirleme Kaynağı][2])

## “gnomAD’de yok” otomatik PM2 değildir

Önce şu sorular yanıtlanmalıdır:

* Pozisyon gnomAD’de yeterli kapsam ve callability gösteriyor mu?
* Varyant tipi kullanılan veri setinde güvenilir saptanabiliyor mu?
* İlgili atasal popülasyon yeterince temsil edilmiş mi?
* gnomAD sürümü ve genom yapısı nedir?
* Hastalığın prevalansı, penetransı ve genetik/allelik heterojenitesi hangi maksimum güvenilir frekansa izin veriyor?
* Varyant gerçekten yok mu, yoksa filtrelenmiş veya düşük kaliteli mi?

ClinGen’in güncel gnomAD v4 rehberinin Haziran 2025 sürümü, VCEP’lerin popülasyon verisi kullanımını ayrıca güncellemiştir. Bu nedenle yalnız “0 allele count” görerek PM2 vermek doğru değildir. ([ClinGen][3])

## pLI ve LOEUF cümlesindeki nüans

Şu cümle fazla doğrusal:

> “Kısıtlı bir gende nadir bir kesici varyant anlamlıyken, kısıtsız bir gende aynı bulgu çok daha zayıftır.”

Yön olarak doğru olsa da **pLI veya LOEUF, PM2’nin gücünü yükselten ACMG kriterleri değildir.** Bunlar gen düzeyinde popülasyonel LoF intoleransını gösterir. Şunları tek başına kanıtlamaz:

* genin belirli bir hastalıkla ilişkili olduğunu,
* haploinsufficiency’nin hastalık mekanizması olduğunu,
* incelenen pLoF varyantının gerçekten işlev kaybı oluşturduğunu,
* varyantın patojenik olduğunu.

Lek ve arkadaşları pLI’nin yüksek olmasının otomatik olarak “hastalık geni” anlamına gelmediğini özellikle belirtmiştir. LOEUF da sürekli ve daha iyi kalibre edilmiş bir kısıt ölçütüdür; ancak gen uzunluğu ve istatistiksel güçten etkilenir. ([Nature][4])

Daha doğru ifade:

> **Gen düzeyindeki pLI ve LOEUF ölçütleri, popülasyon yokluğunu doğrudan güçlendirmez; varyantın bulunduğu genin heterozigot LoF’a toleransını bağlamlandırır. Nadir bir kesici varyant ancak ilgili gen–hastalık ilişkisinde LoF mekanizması gösterilmişse, transkript ve NMD değerlendirmesi PVS1 ile uyumluysa anlamlı patojenik kanıta dönüşür.**

## Düzeltilmiş metin

> **Klinikte dikkat — Bir varyantın “gnomAD’de yok” olması ne kadar kanıttır?** Popülasyon veri tabanlarında yokluk veya hastalık için beklenenden daha düşük frekans, PM2 kriterini destekleyebilir; ancak tek başına patojeniteyi göstermez. ClinGen SVI’nin genel önerisinde PM2, Moderate yerine Supporting güçte uygulanır. Bununla birlikte ilgili gen–hastalık ilişkisi için onaylanmış bir VCEP spesifikasyonu varsa frekans eşiği ve kriter gücü o spesifikasyona göre belirlenmelidir.
>
> PM2 uygulanmadan önce varyant pozisyonunun yeterli kapsam ve callability’ye sahip olduğu, ilgili varyant tipinin veri tabanında güvenilir biçimde saptanabildiği ve hastalıkla ilişkili popülasyonların yeterince temsil edildiği doğrulanmalıdır. Her insan genomunda çok sayıda özel veya son derece nadir benign varyant bulunduğundan, yalnızca yokluk zayıf pozitif kanıttır.
>
> pLI ve LOEUF gibi gen düzeyindeki kısıt ölçütleri bu bilgiyi bağlamlandırabilir; ancak bağımsız ACMG kanıtı veya PM2 güç artırıcısı değildir. Yüksek LoF intoleransı, genin heterozigot protein-kesici varyantlara karşı seçilim altında olduğunu düşündürür. Klinik yorum için ayrıca gen–hastalık geçerliliği, hastalık mekanizması ve varyantın gerçekten LoF oluşturup oluşturmadığı gösterilmelidir.

**Net ifade:** PM2_Supporting, genel ClinGen SVI varsayılanıdır; **evrensel ve VCEP’ten bağımsız sabit bir kural değildir.**

[1]: https://erepo.clinicalgenome.org/cspec/ui/svi/doc/1624749084 "Criteria Specification Registry"
[2]: https://cspec.clinicalgenome.org/cspec/ui/svi/doc/GN150?utm_source=chatgpt.com "Criteria Specification Registry"
[3]: https://clinicalgenome.org/docs/clingen-guidance-to-vceps-regarding-the-use-of-gnomad-v4-march-2024/ "ClinGen Guidance to VCEPs regarding the use of gnomAD v4 - ClinGen | Clinical Genome Resource"
[4]: https://www.nature.com/articles/nature19057?utm_source=chatgpt.com "Analysis of protein-coding genetic variation in 60,706 humans | Nature"


<br>

### B26 · Bölüm 16 — Mekanizmadan Varyant Yorumuna: ACMG/ClinGen Sentezi

**Yer:** `Bölüm_16_Mekanizmadan_Varyant_Yorumuna.md` · 7. Pediatrik genetikten klinik örnekler (çözümlü) · satır 267

> **Örnek 1 — Yenidoğanda dirençli nöbet; *SCN2A* p.Arg1882Gln (de novo).** Doğumun ilk gününde fokal nöbetlerle başvuran bebekte trio WES ile de novo bir missense varyant saptanır. Kanıt zinciri şöyle kurulur: ebeveynlik doğrulanmış de novo (PS2, +4); popülasyonda yok (PM2, +1); bu kodon *SCN2A*'nın bilinen tekrarlayan varyant konumlarındandır (PM1, +2); elektrofizyolojik çalışmalar bu varyantın **işlev kazanımı** yönünde olduğunu ve dinamik aksiyon potansiyeli çalışmasında ateşlemede dramatik artış öngördüğünü göstermiştir (PS3, +4) (Berecki ve ark., 2018). ***Toplam +11 → patojenik***. **Öğreti:** mekanizma yönü burada yalnız sınıfı değil tedaviyi de belirler; erken başlangıçlı, işlev kazanımı yönündeki sodyum kanalı tablolarında sodyum kanal blokerleri yararlı olabilirken, işlev kaybı tablolarında aynı yaklaşım uygun değildir (Brunklaus ve ark., 2020). Ayrıca dikkat: PS3 burada "fonksiyon bozulmuş" dediği için değil, **yönü gösterdiği** için bu kadar değerlidir.

**Sorulan:** Bu çözümlü örneğin puanlaması doğru mu? PS3'ün tam güçte (+4) kullanılması bu veriyle savunulabilir mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Varyantın patojenik olduğu sonucu doğru; fakat verilen `+11` puanlık kanıt zinciri mevcut hâliyle doğru değil.** En belirgin hata, **tek bir doğrulanmış de novo olguya PS2_Strong `(+4)` verilmesi**. Güncel SCN2A VCEP v2.0 kurallarında tek doğrulanmış de novo kompleks nörogelişimsel bozukluk olgusu **PS2_Moderate `(+2)`** eder. ([Evrensel Veri Deposytosu][1])

## Kriter denetimi

| Kriter | Metindeki kullanım | Güncel değerlendirme                     |
| ------ | -----------------: | ---------------------------------------- |
| PS2    |               `+4` | **Tek doğrulanmış trio için +2**         |
| PM2    |               `+1` | Uygun                                    |
| PM1    |               `+2` | Koşullu; gerekçe yanlış kurulmuş         |
| PS3    |               `+4` | **Savunulabilir**                        |
| Toplam |               `11` | **PM1 doğrulanırsa 9 → olası patojenik** |

### 1. PS2: tek trio `+4` değildir

SCN2A VCEP, doğrulanmış anne-babalıkla saptanan her bağımsız kompleks nörogelişimsel bozukluk olgusuna **1 de novo puanı** verir:

* 1 de novo puanı → `PS2_Moderate` → ACMG nokta sisteminde `+2`
* 2 de novo puanı → `PS2_Strong` → `+4`
* 4 de novo puanı → `PS2_VeryStrong` → `+8`

Dolayısıyla senaryoda yalnızca bu yenidoğan kullanılıyorsa:

[
PS2_{\text{Moderate}}=+2
]

olmalıdır. Trio WES’te varyantın anne ve babada görülmemesi de tek başına yeterli değildir; PS2 için biyolojik anne-baba ilişkilerinin doğrulanmış olması gerekir. Aksi durumda PM6 kullanılır. ([Evrensel Veri Deposytosu][1])

---

## 2. PS3_Strong `(+4)` savunulabilir mi?

**Evet. Hatta Berecki 2018 verileri güncel SCN2A VCEP eşiklerini açık biçimde karşılıyor.**

Ancak PS3’ü yalnızca:

> “Dinamik aksiyon potansiyeli modelinde ateşleme arttı.”

diye vermek yerine, **kalibre edilmiş patch-clamp parametrelerine** dayandırmak gerekir.

Berecki ve arkadaşlarının R1882Q sonuçları:

### Persistan akım

[
WT=1.18%,\qquad R1882Q=2.92%
]

[
\frac{2.92}{1.18}=2.47
]

Yani mutant persistan akım yaklaşık **WT’nin %247’si**. SCN2A VCEP’nin PS3_Strong eşiği:

[
\text{Persistan akım}\geq%135\ WT
]

olduğundan güçlü kriter karşılanır.

### Aktivasyon voltajı

[
V_{0.5,\ activation}:
-17.06\ \text{mV}\rightarrow-23.08\ \text{mV}
]

Mutlak kayma:

[
6.02\ \text{mV}
]

PS3_Strong eşiği `≥2.2 mV` olduğundan bu da güçlü düzeydedir.

### İnaktivasyon voltajı

[
V_{0.5,\ inactivation}:
-48.60\ \text{mV}\rightarrow-44.23\ \text{mV}
]

Mutlak kayma:

[
4.37\ \text{mV}
]

PS3_Strong eşiği `≥4.1 mV` olduğundan bu parametre de güçlü düzeyi karşılar.

VCEP, bir varyant birden fazla fonksiyonel ölçütte farklı güç düzeylerini karşılıyorsa **en yüksek düzeyin kullanılmasını ve toplamın Strong düzeyinde sınırlandırılmasını** söyler. Bu nedenle:

[
PS3_{\text{Strong}}=+4
]

uygundur. ([Cspec][2])

R1882Q’nun artmış persistan akım, yavaşlamış inaktivasyon ve artmış eksitabilite etkileri bağımsız HEK-hücreli elektrofizyoloji çalışmasında da yeniden gösterilmiştir. Bu replikasyon PS3’ü iki kez saydırmaz, fakat deneysel sonucun güvenilirliğini artırır. ([PubMed Central (PMC)][3])

### Dinamik aksiyon potansiyeli clamp’in gerçek rolü

Dinamik clamp:

* çeşitli biyofiziksel değişikliklerin **net nöronal sonucunu** bütünleştirir,
* R1882Q’nun ateşleme frekansını artırdığını gösterir,
* değişikliğin yönünü **gain-of-function** olarak netleştirir.

Fakat güncel VCEP’de dinamik clamp, tek başına kalibre edilmiş ayrı bir PS3_Strong eşiği olarak tanımlanmamıştır. Tam güç PS3’ün en temiz dayanağı, yukarıdaki nicel voltage-clamp sonuçlarıdır. Dinamik clamp ise mekanizma yönünü ve biyolojik anlamı güçlendirir. ([PubMed][4])

---

## 3. PM1 gerekçesi düzeltilmeli

Şu gerekçe teknik olarak yeterli değildir:

> “Bu kodon tekrarlayan varyant konumudur, dolayısıyla PM1.”

**Tekrarlayan olgularda görülme PS4 alanına girer.** PM1 ise varyantın önceden tanımlanmış, patojenik varyantlardan zengin ve benign varyantlardan görece arınmış bir bölgede bulunmasına dayanır.

SCN2A VCEP v2.0 için PM1 yalnızca varyant, ekli güncel **Pathogenic Enriched Region/PM1 tablosunda** belirtilen aminoasit aralığına giriyorsa Moderate düzeyde uygulanabilir. Dolayısıyla p.Arg1882’nin güncel PM1 tablosunda bulunduğu doğrulanmalı; yalnızca “recurrent codon” ifadesiyle PM1 verilmemelidir. ([Cspec][2])

Daha doğru yazım:

> **p.Arg1882, SCN2A VCEP tarafından tanımlanan patojenik varyantlardan zengin bölge içinde yer alıyorsa PM1_Moderate uygulanır. Aynı varyantın bağımsız hastalarda tekrarlanması ise ayrıca PS4 kapsamında değerlendirilir.**

---

## 4. PM2 `+1`

Güncel SCN2A VCEP’de PM2 Supporting düzeyindedir. Varyant:

* gnomAD gibi uygun popülasyon veri tabanlarında en fazla bir allelde görülüyorsa,
* en az 10.000 allel güvenilir biçimde değerlendirilmişse,

`PM2_Supporting = +1` uygulanabilir. Dolayısıyla popülasyon yokluğu ve pozisyonun yeterli kapsamı doğrulanmışsa bu bölüm uygundur. ([Cspec][2])

---

# Senaryonun mevcut dört kriterle doğru puanı

PM1’in güncel tabloda doğrulandığını kabul edersek:

[
PS2_M=+2
]

[
PM2_P=+1
]

[
PM1_M=+2
]

[
PS3_S=+4
]

[
\boxed{\text{Toplam}=9}
]

Nokta sisteminde:

* `6–9` → olası patojenik
* `≥10` → patojenik

olduğundan bu dört kriter, tek de novo olgu üzerinden **olası patojenik** sınıfa ulaşır; patojenik sınıfa ulaşmaz. ([PubMed Central (PMC)][5])

---

## Patojenik sınıfa nasıl ulaşır?

`p.Arg1882Gln` zaten tek bir olguya dayanan bir varyant değildir. Berecki ve arkadaşları **yedi R1882Q bireyi** tanımlamış ve varyantı gün 1 başlangıçlı fokal nöbetlerle ilişkili tekrarlayan SCN2A varyantlarından biri olarak göstermiştir. ([PubMed][4])

Bağımsız ve yeterli fenotip bilgisi bulunan ek olgular, de novo kanıtında kullanılmayan probandlardan seçilerek PS4 altında değerlendirilebilir:

* Bir ek uygun bağımsız olgu → `PS4_Supporting = +1`
* İki–üç uygun bağımsız olgu → `PS4_Moderate = +2`
* Dört veya daha fazla uygun bağımsız olgu → `PS4_Strong = +4`

Böylece, örneğin yalnızca bir ek bağımsız olgu kullanılırsa:

[
9+1=10
]

ve patojenik sınıfa ulaşılır. Aynı probandı hem PS2 hem PS4 için iki kez kullanmamak gerekir; VCEP kürasyonlarında PS4 için “additional case” yaklaşımı uygulanmaktadır. ([Cspec][2])

Alternatif olarak ikinci bağımsız, ebeveynliği doğrulanmış de novo olgu bulunursa toplam de novo puanı 2’ye çıkar ve PS2_Strong olur:

[
PS2_S(+4)+PM2_P(+1)+PM1_M(+2)+PS3_S(+4)=11
]

Bu durumda senin verdiğin `+11 → patojenik` hesabı doğru olur; fakat **tek trioyla değil, en az iki bağımsız doğrulanmış de novo olguyla**.

---

## Tedavi ve PS3 cümlesindeki düzeltme

Şu ifade:

> “PS3 burada fonksiyon bozulduğu için değil, yönü gösterdiği için bu kadar değerlidir.”

ACMG açısından doğru kurulmamış.

**PS3’ün gücü**, valide ve nicel fonksiyonel deneylerin hastalık mekanizmasıyla uyumlu anormal kanal işlevini göstermesinden gelir. GoF yönünün belirlenmesi ise PS3 puanından ayrı olarak:

* fenotip korelasyonu,
* mekanizma sınıflandırması,
* hassas tedavi seçimi

bakımından ek klinik değer taşır.

Erken başlangıçlı SCN2A GoF tablolarında sodyum kanal blokerlerinden yarar görülebilir; ancak bu mutlak değildir. Berecki kohortunda R1882Q hastalarında yarar ağırlıklı olmakla birlikte phenytoin yanıtı evrensel değildi. Daha geniş sodyum kanalopati verileri de erken başlangıçlı GoF varyantlarla sodyum kanal blokeri yanıtı arasında genel bir ilişkiyi destekler. ([PubMed][6])

## Düzeltilmiş örnek

> **Örnek 1 — Yenidoğanda dirençli nöbet; `SCN2A p.Arg1882Gln`**
>
> Doğumun ilk gününde fokal nöbetlerle başvuran bebekte trio WES ile heterozigot `SCN2A NM_001040142.2:c.5645G>A, p.Arg1882Gln` varyantı saptanmıştır. Biyolojik anne ve babalık doğrulanmış tek bir olguda de novo oluşum `PS2_Moderate (+2)` sağlar. Varyantın uygun popülasyon veri tabanlarında bulunmaması `PM2_Supporting (+1)` olarak değerlendirilir. p.Arg1882 güncel SCN2A VCEP PM1 tablosunda tanımlanmış patojenik varyantlardan zengin bölge içinde yer alıyorsa `PM1_Moderate (+2)` uygulanabilir.
>
> Patch-clamp çalışmalarında mutant kanalın persistan akımı WT’nin yaklaşık %247’sine çıkmış, aktivasyon voltajında yaklaşık 6,0 mV ve inaktivasyon voltajında yaklaşık 4,4 mV kayma gösterilmiştir. Bu değerlerin her biri SCN2A VCEP’nin Strong fonksiyonel eşiklerini karşılar; bu nedenle `PS3_Strong (+4)` uygulanır. Dinamik aksiyon potansiyeli clamp çalışması, bu biyofiziksel değişikliklerin net sonucunun artmış nöronal ateşleme olduğunu ve varyantın gain-of-function yönünde davrandığını gösterir.
>
> Bu dört kriterin toplamı `+9` olup olası patojenik sınıfa karşılık gelir. Varyantın bağımsız hastalarda tekrarlanması PS4 kapsamında eklendiğinde veya ikinci doğrulanmış de novo olguyla PS2 Strong düzeye yükseldiğinde toplam ≥10 olur ve patojenik sınıfa ulaşılır. GoF yönünün gösterilmesi yalnızca varyant sınıflandırmasını desteklemez; erken başlangıçlı SCN2A epilepsisinde sodyum kanal blokerlerinin seçimini de yönlendirebilir. Tedavi yanıtı bireysel olduğundan fonksiyon yönü tek başına ilaç garantisi değildir.

**Net sonuç:** `PS3_Strong (+4)` bu varyant için savunulabilir. Hatalı olan PS3 değil, **tek bir trio olgusuna PS2_Strong (+4) verilmesi** ve PM1’in yalnızca “tekrarlayan kodon” gerekçesiyle uygulanmasıdır.

[1]: https://erepo.clinicalgenome.org/cspec/ui/svi/doc/643243138?version=1.0.0 "Criteria Specification Registry"
[2]: https://cspec.genome.network/cspec/ui/svi/doc/GN068 "Criteria Specification Registry"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6795554/?utm_source=chatgpt.com "Resurgent and Gating Pore Currents Induced by De Novo SCN2A Epilepsy Mutations - PMC"
[4]: https://pubmed.ncbi.nlm.nih.gov/29844171/ "Dynamic action potential clamp predicts functional separation in mild familial and severe de novo forms of SCN2A epilepsy - PubMed"
[5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8011844/?utm_source=chatgpt.com "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines - PMC"
[6]: https://pubmed.ncbi.nlm.nih.gov/32090326/?utm_source=chatgpt.com "Biological concepts in human sodium channel epilepsies and ..."


<br>

### B27 · Bölüm 17 — Klinik Senaryolarla Sentez: Hastadan Mekanizmaya

**Yer:** `Bölüm_17_Klinik_Senaryolarla_Sentez.md` · 2.2 "Negatif" ne demektir? Altı kör nokta · satır 75

> Şüpheli genetik hastalığı olan çocuklarda tanısal getiriyi karşılaştıran, 37 çalışma ve 20.068 çocuğu kapsayan bir sistematik derleme ve meta-analiz, ***tüm genom dizilemenin tanısal getirisini 0,41, tüm ekzom dizilemeninkini 0,36 ve kromozomal mikroarray'inkini 0,10*** olarak bildirmiştir. Aynı analizde, kohort içi karşılaştırma yapan çalışmalarda **trio** analizinin tek bireye göre tanı olasılığını anlamlı biçimde artırdığı gösterilmiştir (olasılık oranı 2,04). Yazarlar, şüpheli genetik hastalığı olan çocuklarda WGS/WES'in **birinci basamak genomik test** olarak düşünülmesi gerektiği sonucuna varmışlardır (Clark ve ark., 2018).

**Sorulan:** Bu meta-analiz sayıları Türkiye pratiğine beklenti olarak aktarılabilir mi? Daha güncel getiri verisi kullanılmalı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Clark ve ark. 2018’deki `%41 WGS`, `%36 WES`, `%10 CMA` değerleri Türkiye’de beklenen tanısal getiri olarak doğrudan kullanılamaz.** Bunlar ilgili meta-analizin tarihsel havuz tahminleridir; evrensel test performansı değildir. Kitapta Clark çalışması korunabilir, ancak güncel beklenti için 2025 meta-analizi ve doğrudan karşılaştırmalı yeni çalışmalar kullanılmalıdır. ([PubMed Central (PMC)][1])

## Neden Türkiye’ye doğrudan aktarılamaz?

Tanısal getiri, cihazın sabit bir özelliği değildir:

[
\text{Tanısal getiri}
=====================

f(\text{kohort seçimi, fenotip, önceki testler, aile yapısı, analiz kapsamı, yorumlama})
]

Özellikle şu değişkenler sonucu ciddi biçimde değiştirir:

* Ağır multisistemik veya sendromik hastaların seçilmesi
* İzole otizm, epilepsi, kısa boy veya nöromüsküler fenotip gibi endikasyon farklılıkları
* İlk basamak ile önceki testleri negatif “zor olgu” kohortu arasındaki fark
* Trio, duo veya singleton analiz
* CNV, mtDNA, mozaiklik, repeat ve splice analizinin teste dâhil edilmesi
* Derin fenotipleme ve yeniden fenotipleme kalitesi
* Yalnız P/LP varyantların mı, yoksa fenotiple uyumlu VUS’ların da mı “tanı” sayıldığı
* Yeniden analiz sıklığı

Bu nedenle farklı yayınlardaki yüzdeler ancak **aynı tanı tanımı ve benzer kohortlar** kullanılmışsa karşılaştırılabilir.

## Güncel meta-analiz ne gösteriyor?

Pandey ve arkadaşlarının 2025 meta-analizi, 2011–2023 arasında yayımlanmış **108 çalışma ve 24.631 pediatrik probandı** kapsadı. Aynı kohort içinde karşılaştırma yapan çalışmalarda genom çapında dizilemenin—GS veya ES—birleşik tanısal getirisi `%34,2`, genom çapında olmayan testlerin getirisi `%18,1` bulundu. ([digitalcommons.library.tmc.edu][2])

GS ile ES’yi doğrudan karşılaştıran yalnız üç çalışma temel alındığında:

[
GS = 30{,}6%
]

[
ES = 23{,}2%
]

bulundu. Ancak güven aralıkları genişti, heterojenlik yüksekti ve tanı olasılığı farkı istatistiksel anlamlı değildi: `OR 1,7; %95 GA 0,94–2,92; p=0,13`. Dolayısıyla bu sonuç “GS her klinik durumda ES’den yaklaşık %7,4 daha fazla tanı koyar” şeklinde yorumlanamaz. ([ScienceDirect][3])

Bunu destekleyen 2026 tarihli randomize uygulama çalışmasında 1.048 trio ES veya GS koluna dağıtıldı; tanısal getiriler sırasıyla `%33,8` ve `%33,6` bulundu. Bu sonuç, iyi tasarlanmış ES ile kısa-okuma GS’nin rutin kodlayan varyantların ağırlıkta olduğu kohortlarda benzer ilk raporlama getirisine ulaşabileceğini gösterir. GS’nin avantajı daha çok tek testle CNV/SV, intronik ve bazı diğer varyant sınıflarını kapsama, veri yeniden analiz edilebilirliği ve tanısal iş akışını birleştirme alanındadır. ([PubMed][4])

## Trio için `OR 2,04` güncel beklenti olarak kullanılmalı mı?

**Hayır; evrensel bir çarpan gibi kullanılmamalıdır.**

Clark çalışmasındaki `OR 2,04`, dahil edilen eski kohortların birleşik sonucudur. Bu:

> “Singleton getiri %30 ise trio getiri yaklaşık %60 olur.”

anlamına gelmez.

2025’te yapılan doğrudan GS karşılaştırmasında uzman değerlendirmesinden sonra P/LP tanısal getiri singleton GS’de `%39,1`, trio GS’de `%40,0` bulundu. Trio; özellikle de novo varyantların gösterilmesi, faz tayini, resesif adayların filtrelenmesi ve aday varyant sayısının azaltılmasında yararlıydı, fakat mutlak tanı artışı yalnız `%0,9` idi. Deneyimi daha az ekiplerin prospektif analizinde ise trio yaklaşımının faydası daha belirgindi. ([Springer Nature Link][5])

Bu nedenle trio avantajını şöyle anlatmak daha doğrudur:

> **Trio analiz, tanısal getiriyi her kohortta iki katına çıkarmaz; ancak de novo ve bileşik heterozigot varyantların yorumunu hızlandırır, faz bilgisini sağlar, VUS yükünü azaltır ve ek segregasyon testlerine duyulan ihtiyacı düşürür.**

Türkiye’de yüksek akrabalık bulunan seçilmiş otozomal resesif kohortlarda çok sayıda tanı homozigot varyantlarla konulabilir; bu nedenle trio–singleton farkı, de novo ağırlıklı dışlanmış nörogelişimsel kohortlardan farklı olabilir.

## Türkiye verileri ne gösteriyor?

Türkiye’den 190 akraba evliliği bulunan ve yoğun biçimde seçilmiş nörogenetik aileyi içeren trio-WES çalışmasında bilinen hastalık genleriyle tanısal getiri `%72` idi; yeni aday genler de eklendiğinde `%86` olarak bildirildi. Bu olağanüstü yüksek oran; akrabalık, ağır nörogenetik fenotip, derin fenotipleme, aile temelli analiz ve araştırma kapsamında yeni gen adaylarının “çözülmüş” gruba eklenmesiyle ilişkilidir. Türkiye’deki genel pediatrik genetik polikliniği için beklenen WES getirisi olarak kullanılamaz. ([PubMed Central (PMC)][6])

Türkiye’de 172 çocuğu içeren 2024 tarihli klinik WGS kohortunda toplam “çözülmüş” oran `%61` olarak bildirildi. Fakat yalnız **robust genetic diagnosis** oranı `%34,8` idi; `%61’e` ulaşılması için klinik olarak ilişkili kabul edilen VUS’ların “likely genetic diagnosis” olarak eklenmesi gerekti. Dolayısıyla bu `%61`, yalnız P/LP varyantlardan oluşan klasik meta-analiz tanısal getirisiyle doğrudan karşılaştırılamaz. Kohortun yaklaşık `%29’u` ayrıca uluslararası hastalardan oluşuyordu ve özel bir referans merkezinde seçilmişti. ([Frontiers][7])

Bu iki Türkiye çalışması önemli bir noktayı gösterir: **Türkiye’de tanısal getiri tek bir ulusal yüzdeyle tanımlanamaz.** Akrabalık ve otozomal resesif hastalık yükü bazı seçilmiş kohortlarda getiriyi artırabilir; buna karşılık çok sayıda homozigot aday varyant yorumlamayı zorlaştırabilir. Ayrıca yerel popülasyonun referans veri tabanlarında yetersiz temsili, benign Türkiye’ye özgü varyantların VUS olarak raporlanmasına yol açabilir.

## Türkiye için hangi beklenti kullanılmalı?

Geniş ve heterojen bir pediatrik CA/DD/ID veya olası Mendelci hastalık kohortunda, **P/LP temelli rutin klinik ES/GS için yaklaşık `%30–40` başlangıç beklentisi** savunulabilir. Bu, güncel uluslararası meta-analiz ve doğrudan karşılaştırmalı çalışmaların ortak aralığıdır; Türkiye’ye özgü doğrulanmış ulusal oran değildir. Seçilmiş ağır, multisistemik, ailevi veya akraba evliliği bulunan kohortlarda oran belirgin biçimde daha yüksek olabilir. Bu bir hizmet planlama tahminidir; her merkez kendi sonuçlarını fenotip, aile yapısı, test türü ve tanı tanımına göre denetlemelidir. ([epistemonikos.org][8])

ES/GS’nin konjenital anomaliler, gelişimsel gecikme veya entelektüel yetersizlikte erken kullanılması yönündeki ana sonuç güncelliğini korur. ACMG, bu hasta grubunda ES veya GS’nin birinci ya da ikinci basamak test olarak değerlendirilmesini güçlü biçimde önermektedir. Ancak bu öneri, her hastada mutlaka GS seçilmesi veya CMA’nın bütünüyle kaldırılması anlamına gelmez; test seçimi beklenen varyant sınıfına ve laboratuvarın valide analiz kapsamına dayanmalıdır. ([PubMed][9])

## Metnin güncellenmiş biçimi

> Şüpheli nadir genetik hastalığı bulunan çocuklarda genom çapında dizileme, geleneksel veya hedefli testlerden daha yüksek tanısal getiri sağlar. Clark ve arkadaşlarının 2018 meta-analizinde WGS, WES ve CMA için sırasıyla `%41`, `%36` ve `%10` havuzlanmış tanısal getiri bildirilmiştir; ancak bu değerler tarihsel ve heterojen kohortlardan elde edilmiş olup güncel klinik pratiğe sabit oranlar olarak aktarılmamalıdır.
>
> Pandey ve arkadaşlarının 2025 meta-analizi, 108 çalışma ve 24.631 pediatrik proband içinde genom çapında dizilemenin tanısal getirisini karşılaştırmalı kohortlarda `%34,2` olarak bulmuştur. GS ile ES’nin doğrudan karşılaştırıldığı sınırlı sayıdaki çalışmada oranlar sırasıyla `%30,6` ve `%23,2` olsa da fark istatistiksel olarak kesin değildi. Daha sonraki randomize bir trio çalışmasında ES ve GS benzer tanısal getiri göstermiştir. Bu nedenle ES veya GS’den beklenen getiri teknoloji adından çok hasta seçimi, fenotipleme, aile temelli analiz, varyant kapsamı ve yorumlama kalitesine bağlıdır.
>
> Trio analiz özellikle de novo varyantların gösterilmesi, faz tayini ve aday varyantların filtrelenmesi açısından değerlidir; ancak Clark çalışmasındaki `OR 2,04` her kohorta uygulanabilecek sabit bir tanı artışı değildir. Türkiye’de akrabalık oranı ve otozomal resesif hastalık yükü seçilmiş kohortlarda tanısal getiriyi artırabilir, fakat yayımlanmış yüksek oranlar genel pediatrik genetik pratiğini temsil etmez. Türkiye’de geniş bir klinik kohort için başlangıç beklentisi olarak yaklaşık `%30–40` kullanılabilir; merkezler kendi tanısal getirilerini endikasyon, aile yapısı ve yalnız P/LP varyantları içeren standart bir tanı tanımıyla ayrıca hesaplamalıdır.

**Sonuç:** Clark 2018’i tarihsel dönüm noktası olarak tutun. Güncel ana sayı kaynağı olarak **Pandey 2025’i**, GS–ES farkının kesin olmadığını göstermek için de **2026 randomize çalışmasını** ekleyin. Türkiye için `%41/%36/%10` şeklinde sabit beklenti vermeyin.

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6037748/?utm_source=chatgpt.com "Meta-analysis of the diagnostic and clinical utility of genome ..."
[2]: https://digitalcommons.library.tmc.edu/cgi/viewcontent.cgi?article=1081&context=med_ethics&utm_source=chatgpt.com "A Meta-Analysis of Diagnostic Yield and Clinical Utility of ..."
[3]: https://www.sciencedirect.com/science/article/abs/pii/S1769721221001130?utm_source=chatgpt.com "Utility of clinical exome sequencing in the evaluation of ..."
[4]: https://pubmed.ncbi.nlm.nih.gov/41084864/?utm_source=chatgpt.com "Comparing the performance of exome and genome ..."
[5]: https://link.springer.com/article/10.1186/s13073-025-01516-7 "Evaluating genome sequencing strategies: trio, singleton, and standard testing in rare disease diagnosis | Genome Medicine | Springer Nature Link"
[6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9128813/ "High diagnostic rate of trio exome sequencing in consanguineous families with neurogenetic diseases - PMC"
[7]: https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2024.1347474/full "Frontiers | Impact of deep phenotyping: high diagnostic yield in a diverse pediatric population of 172 patients through clinical whole-genome sequencing at a single center"
[8]: https://www.epistemonikos.org/es/documents/0ec52103f97770fb59cee3cfec49acc865b1a52f?utm_source=chatgpt.com "A meta-analysis of diagnostic yield and clinical utility of genome ..."
[9]: https://pubmed.ncbi.nlm.nih.gov/34211152/?utm_source=chatgpt.com "Exome and genome sequencing for pediatric patients with ..."


<br>

---

## C. Kaynaksız mekanizma ve ders bilgisi (T4-a)

*Programatik denetimin kapatamadığı asıl kategori: kaynaksız, kulağa doğru gelen, "yerleşik ders bilgisi" sayılıp geçilen cümleler.*

### C1 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.E — Varyantın kökeni ve kalıtım kalıpları · satır 95

> Germline varyantların ailedeki dağılımı, klasik kalıtım kalıplarını oluşturur (Şekil 1.3). **Otozomal dominant** kalıtımda tek bir patojen allel hastalık için yeterlidir; soyağacında her kuşakta etkilenen bireyler görülür, geçiş dikeydir ve cinsiyetler eşit etkilenir — NF1, Marfan ve akondroplazi tipik örneklerdir. **Otozomal resesif** kalıtımda hastalık için iki patojen allel gerekir; bu nedenle sağlıklı taşıyıcı iki ebeveynden etkilenen bir çocuk doğabilir, desen daha yataydır ve ***akraba evliliği riski belirgin biçimde artırır*** (kistik fibroz, PKU, SMA). **X'e bağlı resesif** kalıtımda hemizigot oldukları için çoğunlukla erkekler etkilenir, kadınlar genellikle taşıyıcıdır ve karakteristik biçimde erkekten erkeğe geçiş görülmez (DMD, hemofili A). **X'e bağlı dominant** kalıtımda heterozigot kadınlar da etkilenir; bazı genlerde varyant erkekte erken letal olduğundan ailede tekrarlayan erkek kayıpları/düşükler bir ipucu olabilir. Son olarak **mitokondriyal (maternal)** kalıtımda varyant yalnızca anneden tüm çocuklara geçer, babadan hiçbirine geçmez; heteroplazmi nedeniyle ifade oldukça değişkendir (Bölüm 11).

**Sorulan:** Kalıtım kalıplarının özet tanımları doğru ve eksiksiz mi? Akraba evliliği ifadesi Türkiye bağlamında genişletilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

Metin **temel Mendelci kalıtım kalıplarını doğru yönde anlatıyor**, ancak mevcut hâliyle tam değil ve bazı cümleler fazla deterministik. Özellikle “her kuşakta görülür”, “cinsiyetler eşit etkilenir”, “kadınlar taşıyıcıdır” ve “anneden tüm çocuklara geçer” ifadeleri düzeltilmeli.

“Dikey” ve “yatay” görünüm tanımlayıcı ipuçlarıdır; kalıtım biçiminin zorunlu özellikleri değildir.

## Gerekli düzeltmeler

### Otozomal dominant

> “Tek bir patojen allel hastalık için yeterlidir.”

Genel olarak doğru, fakat daha teknik ifade:

> **Heterozigot patojenik varyant hastalık fenotipi oluşturmak için yeterli olabilir.**

“Her kuşakta etkilenmiş birey görülür” zorunlu değildir. Şunlar dikey paterni bozabilir:

* de novo varyant,
* eksik penetrans,
* geç başlangıç,
* hafif fenotipin gözden kaçması,
* parental somatik/gonadal mozaiklik,
* küçük aile yapısı.

NF1’in yaklaşık yarısı de novo oluşur; buna rağmen NF1 otozomal dominanttır. Ayrıca “cinsiyetler eşit etkilenir” yerine **“varyantın kadın ve erkek çocuklara aktarılma olasılığı eşittir”** denmelidir. Penetrans veya klinik şiddet cinsiyete bağlı farklılaşabilir. Heterozigot etkilenmiş bir ebeveyn için her gebelikte aktarım olasılığı genellikle %50’dir. ([NCBI][1])

### Otozomal resesif

> “Hastalık için iki patojen allel gerekir.”

Bunu şöyle kesinleştirin:

> **Aynı hastalık geninde, genellikle trans yerleşimli iki patojenik veya olası patojenik varyant gerekir.**

İki taşıyıcı ebeveyn için her gebelikte:

[
25% \text{ etkilenmiş},\qquad
50% \text{ taşıyıcı},\qquad
25% \text{ iki aile varyantını da taşımayan}
]

olasılığı vardır.

Akrabalık, akrabaların ortak bir atadan gelen aynı nadir resesif aleli taşıma olasılığını artırır. Ancak:

* bütün otozomal resesif hastalıklar akrabalıkla ilişkili değildir;
* akrabalık otozomal dominant, X’e bağlı veya mtDNA hastalıklarının temel riskini aynı biçimde artırmaz;
* yüksek taşıyıcılık oranı veya akrabalık durumunda resesif hastalık soyağacında **psödo-dominant**, yani ardışık kuşaklarda görülüyor gibi davranabilir.

### X’e bağlı resesif

Ana çerçeve doğru:

* erkekler hemizigot oldukları için daha sık etkilenir;
* erkekten erkeğe geçiş olmaz;
* etkilenmiş erkek X kromozomunu bütün kızlarına, hiçbir oğluna aktarmaz.

Fakat:

> “Kadınlar genellikle taşıyıcıdır.”

ifadesi eksik kalır. Heterozigot kadınlar skewed X-inaktivasyonu, Turner sendromu, X-kromozomu yapısal değişikliği veya diğer mekanizmalar nedeniyle semptomatik olabilir. Bu nedenle **“heterozigot kadınlar asemptomatik olabileceği gibi değişen derecelerde etkilenebilir”** denmelidir. ([NCBI][2])

### X’e bağlı dominant

Heterozigot etkilenmiş bir kadın, varyantı her kız veya erkek çocuğuna %50 olasılıkla aktarır. Etkilenmiş bir erkek:

* bütün kızlarına aktarır,
* hiçbir oğluna aktarmaz.

Erkek letalitesi bütün X’e bağlı dominant hastalıkların özelliği değildir. `IKBKG` ilişkili incontinentia pigmenti gibi belirli hastalıklarda görülür; mozaiklik, 47,XXY veya hipomorfik varyantlar erkek yaşamını mümkün kılabilir. Tekrarlayan erkek fetal kayıpları bu nedenle **bazı** X’e bağlı dominant bozukluklarda ipucudur. ([NCBI][3])

### Mitokondriyal kalıtım

Burada “mitokondriyal hastalık” yerine **“mtDNA ilişkili hastalık”** denmelidir. Çünkü mitokondriyal hastalıkların büyük bölümü nükleer genlerden kaynaklanabilir ve otozomal dominant, otozomal resesif veya X’e bağlı kalıtılabilir. ([NCBI][4])

Ayrıca:

> “Varyant anneden tüm çocuklara geçer.”

yerine:

> **mtDNA patojenik varyantı taşıyan annenin bütün çocukları varyantı alma açısından risk altındadır; heteroplazmik varyantlarda aktarılan mutant yük ve klinik sonuç çocuklar arasında belirgin biçimde değişebilir. Etkilenmiş erkeklerin çocukları klinik danışmanlıkta risk altında kabul edilmez.**

denmelidir. Tek büyük mtDNA delesyonlarının çoğu de novo olduğundan her mtDNA hastalığı ailede maternal desen oluşturmaz. ([NCBI][4])

## Özet eksiksiz mi?

Hayır. “Başlıca klasik kalıtım kalıpları” başlığı altında yeterli olabilir; fakat bütün kalıtım biçimlerini kapsamaz. En azından sonraki bölümde şunlar bulunmalıdır:

* Y’ye bağlı kalıtım,
* pseudootozomal kalıtım,
* de novo ve gonadal mozaiklik,
* genomik imprinting ve ebeveyn-kökeni etkisi,
* uniparental dizomi,
* tekrar genişlemesi ve anticipasyon,
* digenik/oligogenik modeller,
* somatik mozaiklik.

Bunlar eklenmeyecekse başlık **“Başlıca Mendelci ve mtDNA kalıtım kalıpları”** olmalıdır.

## Türkiye bağlamında akrabalık ifadesi genişletilmeli mi?

**Evet.** Yalnızca “akraba evliliği riski artırır” demek yetersizdir. Türkiye pratiğinde şu noktalar önemlidir:

* akrabalığın derecesi,
* pedigride birden fazla akrabalık halkası,
* aynı köy, aşiret veya kapalı topluluk içindeki endogami,
* kurucu varyantlar,
* ailede benzer çocuk kayıpları veya açıklanamayan hastalıklar,
* ROH/otozigotluk yükü,
* aynı çocukta birden fazla resesif hastalığın bulunabilmesi.

TÜİK’in 2025 verilerine göre yeni resmî evliliklerin %3,0’ı akraba evliliği olarak kaydedilmiştir; oran belirgin bölgesel farklılık gösterir. Bu değer yalnız ilgili yıldaki yeni evlilikleri ifade eder ve klinik popülasyondaki akrabalık yükünü doğrudan göstermez. ([Veri Portalı][5])

İlk kuzen çiftlerinde genel toplumdaki yaklaşık %2–3’lük majör konjenital/genetik sorun riskinin yaklaşık %4–6’ya çıktığı şeklinde bir danışmanlık çerçevesi kullanılabilir. Ancak ailede belirli bir otozomal resesif hastalık ve her iki eşte aynı varyant gösterilmişse ampirik %4–6 değil, **hastalığa özgü her gebelikte %25 risk** verilmelidir. ([The British Society for Genetic Medicine][6])

## Düzeltilmiş metin

> Germline varyantların kuşaklar arasındaki aktarımı başlıca Mendelci ve mtDNA kalıtım kalıplarını oluşturur; ancak penetrans, değişken ekspresivite, de novo varyantlar ve mozaiklik nedeniyle gerçek soyağaçları klasik şemalardan sapabilir. Otozomal dominant kalıtımda heterozigot patojenik varyant hastalık için yeterli olabilir ve etkilenmiş heterozigot bireyin her çocuğu varyantı %50 olasılıkla alır. Kadın ve erkek çocuklar için aktarım olasılığı eşittir; ancak penetrans ve şiddet farklı olabilir. Dikey geçiş sık görülse de de novo varyantlar, eksik penetrans veya parental mozaiklik nedeniyle aile öyküsü negatif olabilir. NF1, Marfan sendromu ve akondroplazi tipik örneklerdir.
>
> Otozomal resesif kalıtımda aynı gende, genellikle trans yerleşimli iki patojenik varyant gerekir. İki taşıyıcı ebeveynin her gebeliğinde etkilenmiş çocuk riski %25’tir. Akrabalık, ortak atadan gelen aynı nadir resesif alelin her iki eşte bulunma olasılığını artırır; ancak risk akrabalığın derecesine, aile öyküsüne, endogamiye ve kurucu varyantlara bağlıdır. Türkiye’de değerlendirme yalnız “akrabalık var/yok” biçiminde yapılmamalı; akrabalık halkaları ve aile kökeni üç kuşaklı pedigride ayrıntılı gösterilmelidir.
>
> X’e bağlı resesif kalıtımda erkekler hemizigot oldukları için daha sık ve çoğu kez daha ağır etkilenir; erkekten erkeğe geçiş olmaz. Heterozigot kadınlar asemptomatik olabileceği gibi X-inaktivasyonuna ve diğer genetik etkenlere bağlı olarak semptomatik de olabilir. DMD ve hemofili A tipik örneklerdir. X’e bağlı dominant kalıtımda heterozigot kadınlar da etkilenir; etkilenmiş erkek varyantı bütün kızlarına, hiçbir oğluna aktarır. Bazı X’e bağlı dominant hastalıklarda hemizigot erkek letalitesi nedeniyle tekrarlayan erkek fetal kayıpları görülebilir.
>
> mtDNA ilişkili maternal kalıtımda varyant kadınlar üzerinden aktarılır. Varyantı taşıyan annenin bütün çocukları kalıtım açısından risk altındadır; etkilenmiş erkeklerin çocuklarına aktarım beklenmez. Heteroplazmi, mitokondriyal darboğaz, doku dağılımı ve eşik etkisi nedeniyle kardeşler arasında mutant yük ve klinik şiddet belirgin biçimde farklı olabilir. Nükleer genlere bağlı mitokondriyal hastalıklar ise otozomal dominant, otozomal resesif veya X’e bağlı kalıtılabilir.

Bu sürüm, giriş düzeyi için yeterince kısa kalırken klinik genetik açısından yanıltıcı mutlaklıkları kaldırır.

[1]: https://www.ncbi.nlm.nih.gov/books/NBK1109/ "Neurofibromatosis 1 - GeneReviews® - NCBI Bookshelf"
[2]: https://www.ncbi.nlm.nih.gov/books/NBK115561/ "INHERITANCE PATTERNS - Understanding Genetics - NCBI Bookshelf"
[3]: https://www.ncbi.nlm.nih.gov/books/NBK1472/ "Incontinentia Pigmenti - GeneReviews® - NCBI Bookshelf"
[4]: https://www.ncbi.nlm.nih.gov/books/NBK1224/ "Primary Mitochondrial Disorders Overview - GeneReviews® - NCBI Bookshelf"
[5]: https://veriportali.tuik.gov.tr/tr/press/58137?utm_source=chatgpt.com "İstatistiklerle Aile - 2025 - Veri Portalı"
[6]: https://bsgm.org.uk/media/12702/british-society-for-genetic-medicine-parliamentary-briefing-on-cousin-marriages-final.pdf?utm_source=chatgpt.com "british-society-for-genetic-medicine-parliamentary-briefing- ..."


<br>

### C2 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.C — Varyasyon, allel ve varyant tipleri · satır 69

> İki insan genomu birbirinden milyonlarca pozisyonda farklıdır; ama bu farkların ezici çoğunluğu zararsızdır. Klinik genetiğin asıl zorluğu da buradadır: devasa bir nötr varyasyon arka planı içinden, hastalığa gerçekten neden olan varyantı ayıklamak. Bu nedenle modern dilde, herhangi bir referans-dışı değişikliğe nötr bir terim olan **varyant** denir; eskiden yaygın olan "mutasyon" sözcüğü artık daha çok yerleşik adlandırmalarda kullanılır, "polimorfizm" ise popülasyonda yaygın (genellikle %1'den sık) ve çoğunlukla zararsız varyantları anlatır. Patojen olup olmama, varyantın bir başka ekseni olarak ayrıca değerlendirilir; bir varyantın yaygın olması onu otomatik olarak benign yapmaz, ama nadir bir hastalık için güçlü bir benign ipucudur. Burada önemli bir uyarı vardır: ***referans dizi her zaman "sağlıklı" anlamına gelmez; referansta da patojen aleller bulunabilir***.

**Sorulan:** Bu uyarı doğru mu? Örnek verilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Evet, uyarı doğrudur ve mutlaka korunmalıdır.** Hatta daha açık yazılmalıdır:

> **Referans alel; normal, sağlıklı, ancestral, en sık veya benign alel anlamına gelmez. Yalnızca kullanılan referans dizide o pozisyonda bulunan aleldir.**

İnsan referans genomu, klinik olarak doğrulanmış “sağlıklı bir insanın genomu” değildir. GRCh38, birden fazla donörden gelen dizilerin birleştirildiği haploid bir mozaiktir; dizinin yaklaşık %70’i tek bir klon kütüphanesinden, büyük bölümü ise sınırlı sayıdaki donörden gelir. Ayrıca referans her lokusta popülasyondaki majör aleli temsil etmez. ([NCBI][1])

## Örnek verilmeli mi?

**Evet. Tek bir somut örnek kavramı çok iyi sabitler. En uygun örnek Factor V Leiden’dır.**

### Factor V Leiden: referans alelin genom sürümüne bağlı olması

`F5` genindeki Factor V Leiden varyantı:

[
\texttt{F5 c.1601G>A, p.Arg534Gln}
]

geleneksel adlandırmayla `p.Arg506Gln`, `rs6025`, tromboz riskini artıran işlev kazanımlı bir aleldir.

Bu hastalıkla ilişkili alel **GRCh37/hg19’da referans dizinin parçasıydı**. Bu nedenle onu homozigot taşıyan bir kişide standart “referanstan fark” temelli varyant çağırma işlemi aleli gözden kaçırabilirdi. GRCh38’de ilgili pozisyon düzeltilmiş ve yaygın, hastalıkla ilişkili olmayan alel referans yapılmıştır. ([PubMed Central (PMC)][2])

Bu örnek üç şeyi aynı anda gösterir:

* Referans alel “normal alel” değildir.
* `REF` ve `ALT` biyolojik özellik değil, kullanılan genom yapısına bağlı teknik etiketlerdir.
* Aynı alel bir genom sürümünde referans, başka bir sürümde alternatif olabilir.

Ancak Factor V Leiden’i kitapta **yüksek penetranslı klasik Mendelci patojenik varyant** gibi değil, **hastalıkla ilişkili ve tromboz riskini artıran alel** olarak tanımlamak daha doğru olur.

## Cümlenin teknik olarak daha güvenli biçimi

Mevcut ifade:

> “Referansta da patojen aleller bulunabilir.”

Yön olarak doğru, fakat biraz kaba. Daha doğru sürüm:

> **Referans dizi klinik bir “sağlıklı genom” değildir. Referans alel yalnızca kullanılan genom yapısında o pozisyonda bulunan baz veya dizidir; majör, ancestral, benign ya da işlevsel alel olmak zorunda değildir. Özellikle eski referans yapılarında hastalıkla ilişkili veya risk artırıcı aleller referans olarak bulunabilmiştir. Örneğin Factor V Leiden aleli GRCh37’de referans dizinin parçasıyken GRCh38’de yaygın non-risk alel referans hâline getirilmiştir.**

Bu sürüm, nadir ve yüksek penetranslı “patojenik” aleller ile daha yaygın risk alellerini birbirine karıştırmaz.

## Paragraftaki iki ek düzeltme

### “Polimorfizm çoğunlukla zararsızdır”

Genel popülasyon düzeyinde yön olarak doğru olsa da **polimorfizmin tanımına benignlik eklenmemelidir**. Polimorfizm klasik olarak frekans terimidir:

[
\mathrm{MAF}\geq1%
]

Daha doğru ifade:

> **Polimorfizm, klasik olarak popülasyonda en az %1 sıklığa ulaşan alelik çeşitliliği anlatır; klinik etkisi hakkında tek başına hüküm vermez.**

### “Yaygınlık nadir hastalık için güçlü benign ipucudur”

Bu da koşullu doğrudur. Alel frekansı:

* hastalığın prevalansı,
* penetransı,
* kalıtım biçimi,
* genetik heterojenitesi,
* kurucu aleller

ile karşılaştırılmalıdır.

Örneğin otozomal resesif bir hastalık aleli heterozigot taşıyıcılarda görece sık olabilir. Düşük penetranslı bir risk aleli de yaygın olabilir. Bu nedenle:

> **Varyantın hastalık modeliyle bağdaşmayacak kadar yüksek frekansta olması güçlü benign kanıttır.**

ifadesi daha doğrudur.

## Düzeltilmiş paragraf

> **İki insan genomu milyonlarca pozisyonda farklıdır; bu farklılıkların büyük çoğunluğu klinik hastalık oluşturmaz. Klinik genetiğin asıl güçlüğü, geniş nötr varyasyon arka planı içinden fenotipe gerçekten katkıda bulunan varyantları ayıklamaktır. Bu nedenle modern terminolojide, belirli bir referans diziye göre farklılık gösteren değişiklikler için nötr “varyant” terimi kullanılır. “Mutasyon” daha çok değişimin oluşma sürecini, yerleşik hastalık adlarını veya bazı deneysel ve onkolojik bağlamları anlatır. “Polimorfizm” ise klasik olarak popülasyonda en az %1 sıklığa ulaşan alelik çeşitliliği ifade eder; benignlik sınıfı değildir.**
>
> **Patojenite, popülasyon sıklığından ayrı bir eksende değerlendirilir. Bir varyantın yaygın olması onu otomatik olarak benign yapmaz; ancak frekansı ilgili nadir hastalığın prevalansı, penetransı ve kalıtım modeliyle bağdaşmıyorsa güçlü benign kanıt oluşturur. Tersine, bir varyantın çok nadir veya popülasyon veri tabanlarında bulunmaması da tek başına patojeniteyi göstermez.**
>
> **Referans dizi de “sağlıklı genom” olarak yorumlanmamalıdır. Referans alel yalnızca kullanılan genom yapısında o pozisyonda bulunan aleldir; majör, ancestral veya benign olmak zorunda değildir. Örneğin tromboz riskini artıran Factor V Leiden aleli GRCh37’de referans dizinin parçasıyken GRCh38’de yaygın non-risk alel referans hâline getirilmiştir.**

**Sonuç:** Uyarı doğru ve öğretim açısından gereklidir. Factor V Leiden örneği eklenmeli; fakat örneğin **GRCh37’ye özgü tarihsel bir referans sorunu** olduğu ve GRCh38’de düzeltildiği açıkça belirtilmelidir.

[1]: https://www.ncbi.nlm.nih.gov/grc/help/faq/ "Frequently Asked Questions - Genome Reference Consortium"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5769444/ "Challenges imposed by minor reference alleles on the identification and reporting of clinical variants from exome data - PMC"


<br>

### C3 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.H — Popülasyon ölçeği ve constraint: bir gen "hata kaldırıyor" mu? · satır 123

> Bu metriklerin neden klinik olarak önemli olduğu, bir LoF varyantıyla karşılaştığımız anda netleşir. Diyelim ki bir hastada bir geni erken sonlandıran bir varyant bulduk. Bu varyantın patojen olup olmadığına karar vermeden önce sorulması gereken ilk soru şudur: *"Bu gen, işlev kaybına duyarlı bir gen mi?"* Eğer gen yüksek pLI / düşük LOEUF ile kısıtlıysa, bu, LoF'un o gen için gerçekten bir hastalık mekanizması olduğuna dair güçlü bir destektir ve birazdan göreceğimiz PVS1 kriterinin uygulanabilirliğini artırır. Tersine, gen LoF'a son derece toleranssa, aynı varyant çok daha şüpheyle karşılanmalıdır. Ancak burada sık yapılan bir hataya düşmemek gerekir: bu metrikler **gen düzeyinde** önceliklendirme araçlarıdır, tek bir varyantın patojenitesini tek başlarına kanıtlamazlar; üstelik ***resesif hastalık yapan LoF genleri (hastalık için iki kopyanın da kaybı gerektiğinden) popülasyonda "tolerant" görünebilir*** — bu onları önemsiz yapmaz, yalnızca metriğin dominant doz hastalıkları için daha bilgilendirici olduğunu gösterir.

**Sorulan:** Constraint metriklerinin sınırları doğru anlatılmış mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

Metnin ana öğretisi doğru; ancak şu cümle **fazla güçlü ve teknik olarak hatalıdır**:

> “Yüksek pLI / düşük LOEUF, LoF’un o gen için hastalık mekanizması olduğuna dair güçlü bir destektir ve PVS1’in uygulanabilirliğini artırır.”

Constraint metrikleri, **belirli bir gen–hastalık ilişkisi için LoF mekanizmasını kanıtlamaz** ve PVS1’i doğrudan aktive etmez. Gösterdikleri şey daha sınırlıdır:

> Genel popülasyonda o genin, özellikle **heterozigot tahmini LoF varyantlarından beklenenden daha azını tolere ettiği**.

Bu, haploinsufficiency için biyolojik uyumluluk sağlar ve varyant/gen önceliklendirmesinde değerlidir. Ancak PVS1 için önce ilgili **gen–hastalık çiftinde LoF’un yerleşik hastalık mekanizması** olduğu bağımsız klinik ve deneysel verilerle gösterilmiş olmalıdır. ClinGen PVS1 rehberi bunu açık bir ön koşul olarak koyar. ([ClinGen][1])

## Düzeltilmesi gereken noktalar

### 1. Constraint, LoF hastalık mekanizmasıyla aynı şey değildir

Düşük LOEUF şu olasılıklarla uyumlu olabilir:

* heterozigot LoF’un ağır gelişimsel hastalık oluşturması,
* embriyonik veya erken yaşam letalitesi,
* hücresel yaşamsallığın bozulması,
* üreme başarısının azalması,
* henüz hastalık ilişkisi kurulmamış güçlü negatif seçilim.

Dolayısıyla:

[
\text{düşük LOEUF}
\not\Rightarrow
\text{kanıtlanmış haploinsufficiency hastalığı}
]

ve:

[
\text{düşük LOEUF}
\not\Rightarrow
\text{otomatik PVS1}
]

Doğru sıra şöyledir:

1. Gen–hastalık ilişkisi geçerli mi?
2. O hastalık için LoF mekanizması yerleşik mi?
3. Varyant gerçekten işlevsel null etki oluşturuyor mu?
4. Hangi PVS1 gücü uygulanabilir?
5. Constraint verisi bu değerlendirmeyle uyumlu mu?

Constraint dördüncü veya beşinci basamakta **bağlamsal destek** sağlar; ilk üç sorunun yerine geçmez.

### 2. “Gen LoF’a toleranslıysa varyant şüphelidir” dikkatli yazılmalı

Yüksek LOEUF iki farklı durumu bir araya getirir:

* gerçekten heterozigot LoF’a toleranslı genler,
* gen kısa olduğu veya yeterince az LoF varyantı beklendiği için constraint ölçümü istatistiksel olarak zayıf genler.

LOEUF’nin üst güven sınırını kullanması nedeniyle düşük değer oldukça bilgilendiricidir; buna karşılık yüksek değer her zaman gerçek toleransı kanıtlamaz. Karczewski ve arkadaşları yüksek LOEUF grubunun, hem kısıtsız hem de ölçüm gücü yetersiz genleri içerdiğini belirtmiştir. ([Nature][2])

Bu nedenle:

> “Yüksek LOEUF, PVS1’i dışlar.”

yanlıştır.

Daha doğru ifade:

> **Yüksek LOEUF veya düşük pLI, heterozigot LoF’a karşı güçlü popülasyonel seçilim kanıtı bulunmadığını gösterir; ancak LoF mekanizmasını tek başına reddetmez.**

### 3. Resesif genler konusundaki açıklama doğru

Bu bölümünüz yerindedir. pLI ve LOEUF esas olarak **heterozigot pLoF varyantlarına karşı seçilimi** yakalar. Otozomal resesif hastalıklarda heterozigot taşıyıcılar genellikle sağlıklı olduğundan, bu genler güçlü şekilde kısıtlı görünmeyebilir. gnomAD analizinde bilinen haploinsufficient genler düşük LOEUF bölgesinde zenginleşirken, otozomal resesif hastalık genleri dağılımın daha orta bölümlerinde yer almıştır. ([Nature][2])

Fakat “resesif genler tolerant görünür” yerine şu ifade daha doğrudur:

> **Resesif hastalık genleri heterozigot LoF’a toleranslı görünebilir; bu metrikler bialelik inaktivasyona karşı seçilimi yeterince ölçmez.**

Gerçek homozigot LoF toleransı için:

* homozigot pLoF bireyler,
* otozigot kohortlar,
* gen knockout verileri,
* bialelik hastalık olguları

ayrıca değerlendirilmelidir.

### 4. Erken stop varyantı otomatik LoF değildir

Metin, “geni erken sonlandıran varyant” ile “gerçek LoF” arasındaki farkı açıkça koymalıdır. Bir nonsense veya frameshift varyant:

* son ekzonda bulunabilir ve NMD’den kaçabilir,
* doğal olarak düşük kullanılan bir transkripti etkileyebilir,
* hastalıkla ilgisiz alternatif ekzon içinde olabilir,
* fonksiyonel olarak önemsiz C-terminal bölgeyi kaybettirebilir,
* alternatif başlangıç kodonuyla kurtarılabilir,
* in-frame ekzon atlamasına yol açabilir,
* LOFTEE tarafından düşük güvenli pLoF olarak işaretlenebilir.

Transkript ekspresyonunun dikkate alınması, gnomAD’deki yanlış pLoF anotasyonlarının anlamlı bir kısmını filtreleyebilir. Bu nedenle constraint metriği doğru olsa bile varyantın ilgili transkriptte gerçekten null etkili olduğu ayrıca gösterilmelidir. ([PubMed Central (PMC)][3])

### 5. pLI yerine LOEUF öncelikli olmalı

pLI, ExAC döneminde geliştirilen ve genleri kategorik sınıflara ayırmaya çalışan bir metriktir; esas olarak `pLI >0,9` biçiminde dikotomik kullanılmıştır. LOEUF ise observed/expected oranının belirsizliğini içeren sürekli bir ölçüdür ve güncel gnomAD yaklaşımında tercih edilmektedir. ([Nature][2])

2026 itibarıyla gnomAD v4.1.1:

* LOEUF kullanımını önermekte,
* güçlü pLoF constraint için **LOEUF <0,45** eşiğini önermektedir,
* bunun v2.1.1’deki eski `<0,35` eşiğinin doğrudan sayısal devamı olmadığını belirtmektedir.

Sürüm değiştikçe dağılım ve eşikler değiştiğinden, raporda gnomAD sürümü yazılmalıdır. ([gnomad.broadinstitute.org][4])

### 6. Teknik ve biyolojik sınırlar eklenmeli

Constraint değerlendirilirken ayrıca şunlar kontrol edilmelidir:

* **Gen ve transkript uzunluğu:** Kısa genlerde beklenen pLoF sayısı azdır.
* **Transkript seçimi:** Gen düzeyinde değer, hastalıkla ilişkili izoformu maskeleyebilir.
* **Dokuya özgü ekspresyon:** Kullanılmayan ekzonlardaki pLoF’lar yanıltabilir.
* **Kapsama ve mappability:** gnomAD v4.1.1 düşük kapsama ve düşük haritalanabilirlik için uyarı bayrakları yayımlamaktadır. ([gnomad.broadinstitute.org][4])
* **Geç başlangıçlı hastalıklar:** Üreme çağından sonra ortaya çıkan fenotipler negatif seçilim tarafından daha zayıf yakalanabilir.
* **Eksik penetrans:** Heterozigot pLoF taşıyıcıları veri tabanında bulunabilir.
* **Popülasyon temsili:** Orta Doğu ve bazı diğer popülasyonların eksik temsili, Türkiye verileri açısından özellikle önemlidir. ([Nature][2])
* **Mekanizma farklılığı:** Bir genin hastalığı missense GOF veya DN ile oluşuyorsa pLoF constraint, incelenen varyant için doğru mekanizmayı göstermeyebilir.

## Metnin düzeltilmiş biçimi

> **Bu metriklerin klinik önemi, tahmini bir işlev kaybı varyantıyla karşılaşıldığında ortaya çıkar. Örneğin bir hastada nonsense, frameshift veya zorunlu splice bölgesini etkileyen bir varyant saptandığında yalnız varyantın kesici görünmesi yeterli değildir. Önce ilgili gen–hastalık ilişkisinde LoF’un yerleşik hastalık mekanizması olup olmadığı, ardından varyantın klinik olarak anlamlı transkriptte gerçekten null etki oluşturup oluşturmadığı değerlendirilmelidir.**
>
> **pLI ve özellikle LOEUF, genel popülasyonda bir genin heterozigot tahmini LoF varyantlarından ne ölçüde arındığını gösteren gen düzeyinde constraint metrikleridir. Düşük LOEUF, genin heterozigot inaktivasyona karşı negatif seçilim altında olduğunu gösterir ve haploinsufficiency hipotezini biyolojik olarak destekleyebilir. Ancak bu veri, belirli bir hastalık için LoF mekanizmasını kanıtlamaz, bağımsız bir ACMG kriteri değildir ve PVS1’in uygulanmasının yerine geçmez. PVS1 yalnızca ilgili gen–hastalık çifti için LoF mekanizması yerleşikse ve varyantın gerçek null etkisi uygun karar ağacıyla gösterilebiliyorsa uygulanmalıdır.**
>
> **Tersine, yüksek LOEUF bir genin mutlaka LoF’a biyolojik olarak toleranslı olduğunu göstermez. Kısa genlerde veya beklenen pLoF sayısının düşük olduğu transkriptlerde ölçüm gücü yetersiz olabilir. Ayrıca otozomal resesif hastalık genleri, heterozigot taşıyıcılar seçilim altında olmadığı için popülasyonda görece toleranslı görünebilir; geç başlangıçlı, eksik penetranslı veya dokuya özgü hastalıklar da güçlü constraint oluşturmayabilir. Bu nedenle constraint metrikleri varyant sınıflandırma kanıtı olarak değil, gen ve mekanizma önceliklendirmesinde kullanılan bağlamsal veriler olarak değerlendirilmelidir.**

**Net sonuç:** Sınırlar genel olarak doğru anlatılmış; fakat “yüksek constraint, LoF hastalık mekanizmasına güçlü kanıttır ve PVS1’i artırır” cümlesi düzeltilmelidir. Constraint, **haploinsufficiency ile uyumluluk sinyalidir; mekanizma veya patojenite kanıtı değildir.**

[1]: https://clinicalgenome.org/docs/recommendations-for-interpreting-the-loss-of-function-pvs1-acmg-amp-variant-criterion/ "Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion - ClinGen | Clinical Genome Resource"
[2]: https://www.nature.com/articles/s41586-020-2308-7 "The mutational constraint spectrum quantified from variation in 141,456 humans | Nature"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7334198/?utm_source=chatgpt.com "Transcript expression-aware annotation improves rare variant ..."
[4]: https://gnomad.broadinstitute.org/news/2026-03-gnomad-v4-1-1/ "gnomAD v4.1.1 | gnomAD browser"


<br>

### C4 · Bölüm 2 — Loss-of-Function (İşlev Kaybı) Mekanizmaları

**Yer:** `Bölüm_02_Loss_of_Function.md` · 1. Kavramsal tanım · satır 30

> | Kavram | Tanım | Klinik anlamı |
> |--------|-------|---------------|
> | **Loss-of-function (LoF)** | Gen ürününün işlevinin kısmen/tamamen kaybı | Mekanizmanın yönü "azalma"dır; doz/eşik mantığı geçerli |
> | **Null allel (amorf)** | Hiç işlevsel ürün üretmeyen allel | En şiddetli LoF ucu (tam fonksiyon kaybı) |
> | **Hipomorfik allel** | ***Azalmış ama sıfır olmayan işlev*** | Rezidüel fonksiyon fenotipi hafifletir |
> | **Rezidüel fonksiyon** | Varyant sonrası kalan işlev miktarı | Genotip–fenotip korelasyonunun motoru |
> | **Nonsense-mediated decay (NMD)** | PTC taşıyan mRNA'yı yıkan gözetim mekanizması | "Transkript yok" → gerçek null; kaçarsa → truncated protein |
> | **NMD escape** | PTC'nin NMD'den kurtulması (genelde son ekzon) | Truncated protein üretilir → DN/GoF riski (Bölüm 5) |
> | **Truncated protein** | Erken sonlanmış kısa protein | İşlevsiz, yarı-işlevsel veya toksik olabilir |
> | **Haploinsufficiency** | Tek işlevsel allelin (%50 doz) yetersizliği | Heterozigot LoF → dominant hastalık (Bölüm 3) |
> | **Resesif LoF** | Hastalık için iki allelin de kaybı gerekir | Heterozigot taşıyıcı sağlıklı |
> | **Compound heterozigot** | Aynı gende iki farklı patojen allel (trans) | Resesif hastalıkların büyük kısmı; faz şart |
> | **LoF intoleransı** | Genin LoF'a popülasyon düzeyinde dayanıksızlığı | "Bu gende LoF beklenen mekanizma mı?" |

**Sorulan:** Kavram tablosundaki tanımlar (null/amorf, hipomorfik, LoF) doğru ve Türkçe karşılıkları uygun mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

Tablonun genel çerçevesi doğru; fakat **null alel, NMD, haploinsufficiency ve LoF intoleransı satırları mevcut biçimleriyle yanıltıcıdır.**

En önemli düzeltme:

> **Null alel, “hiç ürün üretmeyen alel” değil, işlevsel katkısı sıfır olan aleldir.**

Null alel hiç RNA/protein üretmeyebilir; ancak normal miktarda transkript veya protein üretip tamamen işlevsiz de olabilir. Muller’in klasik sınıflamasında **amorfik alel**, tam işlev kaybı gösteren aleldir; hipomorfik alel ise kısmi işlev kaybıdır. Bunlar sekans tipinden çok **fonksiyonel sonuç sınıflarıdır**. 

Türkçe kullanımda:

* **Null alel**: klinik insan genetiğinde en açık ve yerleşik kullanım.
* **Amorfik alel**: tarihsel Muller terminolojisi için uygun.
* **Amorf alel**: anlaşılır; fakat sıfat biçimi olarak “amorfik alel” daha doğal.
* **Hipomorfik alel**: doğru ve yerleşik.
* **Bileşik heterozigot**: “compound heterozigot” yerine tercih edilmeli.
* **Alel**: metin boyunca bu yazım kullanılmalı; “allel” ile karıştırılmamalı.

## Temel üç kavram

### Loss-of-function

Mevcut tanım yön olarak doğru:

> Gen ürününün işlevinin kısmen veya tamamen azalması.

Ancak LoF iki farklı düzeyde kullanılabilir:

1. **Varyant etkisi:** Varyant, ürün miktarını veya aktivitesini azaltır.
2. **Hastalık mekanizması:** Azalmış gen işlevi hastalığa neden olur.

Bunlar aynı şey değildir. Bir varyant laboratuvar deneyinde işlevi azaltabilir; fakat ilgili gen–hastalık ilişkisi için LoF yerleşik hastalık mekanizması olmayabilir. Ayrıca nonsense veya frameshift gibi “kesici” görünen bir varyant NMD’den kaçıp dominant-negatif ya da başka bir anormal ürün etkisi de oluşturabilir. Güncel hastalık-mekanizması terminolojisi bu nedenle “azalmış ürün düzeyi”, “değişmiş ürün dizisi” ve aşağı akım fonksiyonel mekanizmayı birbirinden ayırmayı önerir. ([PubMed Central (PMC)][1])

### Null/amorfik alel

Önerilen tanım:

> **İlgili biyolojik bağlamda ölçülebilir işlevsel katkısı bulunmayan alel.**

“Hiç ürün üretmez” yalnızca null alellerin bir alt grubudur:

* RNA-null: anlamlı transkript oluşmaz.
* Protein-null: protein oluşmaz.
* Fonksiyonel null: protein oluşur fakat aktivitesi sıfırdır.
* Genetik null/amorf: fonksiyonel olarak tam işlev kaybı davranışı gösterir.

Dolayısıyla “hiç işlevsel ürün üretmeyen” ifadesi kullanılabilir; ancak **“hiç ürün üretmeyen”** denmemelidir.

Ayrıca:

> “En şiddetli LoF ucu”

yerine:

> **“Moleküler işlev kaybı spektrumunun tam kayıp ucu”**

denmelidir. Null alel, LoF açısından en uç noktadır; fakat **klinik olarak mutlaka en ağır fenotipi oluşturmaz**. Dominant-negatif veya toksik GoF varyantları null alelden daha ağır olabilir.

### Hipomorfik alel

Mevcut tanım doğrudur:

> **Azalmış fakat sıfır olmayan işlev gösteren alel.**

Ancak azalma farklı şekillerde oluşabilir:

* Daha az RNA veya protein üretimi
* Normal miktarda fakat düşük aktiviteli protein
* Düşük stabilite
* Kısmi hücresel lokalizasyon kusuru
* Proteinin yalnız bazı işlevlerinin kaybı

Dolayısıyla hipomorfi yalnızca “az miktarda protein” anlamına gelmez. Fonksiyonel etkinin WT’den düşük, null alelden yüksek olması gerekir. ([ScienceDirect][2])

## Düzeltilmiş tablo

| Kavram                                   | Düzeltilmiş tanım                                                                                                                    | Klinik anlamı                                                                                                                                 |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Loss-of-function — LoF**               | Gen ürününün miktarını veya biyolojik aktivitesini kısmen ya da tamamen azaltan fonksiyonel sonuç                                    | Mekanizmanın yönü azalmadır; klinik sonuç allelik gereksinime, doz duyarlılığına ve kalan işleve bağlıdır                                     |
| **Null (amorfik) alel**                  | İlgili biyolojik bağlamda işlevsel katkısı sıfır olan alel; RNA/protein hiç oluşmayabilir veya oluşan ürün tamamen işlevsiz olabilir | Tam moleküler işlev kaybıdır; fakat mutlaka en ağır klinik fenotip anlamına gelmez                                                            |
| **Hipomorfik alel**                      | WT’ye göre azalmış, fakat sıfır olmayan işlev gösteren alel                                                                          | Rezidüel işlev sıklıkla daha hafif, geç başlangıçlı veya inkomplet fenotiple ilişkilidir                                                      |
| **Rezidüel işlev**                       | Mutant alelin veya genotipin belirli biyolojik bağlamda koruduğu fonksiyon düzeyi                                                    | Genotip–fenotip korelasyonunun önemli belirleyicilerindendir; dokuya, izoforma ve kullanılan fonksiyonel teste bağlı olabilir                 |
| **Nonsense-mediated mRNA decay — NMD**   | Belirli koşulları karşılayan prematür terminasyon kodonu içeren transkriptlerin düzeyini azaltan RNA gözetim mekanizması             | Mutant transkript ve kesilmiş protein miktarını azaltabilir; “transkript tamamen yoktur” sonucu otomatik çıkarılamaz                          |
| **NMD’den kaçış — NMD escape**           | PTC içeren transkriptin NMD tarafından yeterince yıkılmaması ve translasyona devam edebilmesi                                        | Kesilmiş protein oluşmasına izin verir; sonuç null, hipomorfik, dominant-negatif, GoF veya neomorfik olabilir                                 |
| **Kesilmiş protein — truncated protein** | Normal C-terminal dizisinin bir bölümünü kaybetmiş, erken sonlanmış protein                                                          | İşlevsiz, kısmen işlevli, kararsız, dominant-negatif veya toksik olabilir                                                                     |
| **Haploinsufficiency**                   | Tek işlevsel alelin ürettiği gen ürününün normal fenotipi sürdürmeye yetmemesi                                                       | İlgili gen–hastalık çiftinde heterozigot LoF dominant hastalık oluşturabilir; gerçek doz zorunlu olarak tam %50 değildir                      |
| **Resesif LoF mekanizması**              | Hastalığın ortaya çıkması için iki alelin birleşik işlevinin hastalık eşiğinin altına düşmesinin gerekmesi                           | İki alelin de tam null olması şart değildir; null/null, null/hipomorf veya hipomorf/hipomorf genotipler hastalık oluşturabilir                |
| **Bileşik heterozigot**                  | Aynı gende iki farklı varyantın karşı homologlarda, yani trans konumda bulunması                                                     | Bir genotip tanımıdır; varyantların patojenik olduğunu kendiliğinden göstermez. Resesif tanı için her iki varyant ayrıca değerlendirilmelidir |
| **LoF intoleransı / pLoF constraint**    | Referans popülasyonda bir genin beklenene göre heterozigot tahmini LoF varyantlarından arınmış olması                                | Heterozigot LoF’a karşı negatif seçilimi bağlamlandırır; LoF’un ilgili hastalık için yerleşik mekanizma olduğunu tek başına kanıtlamaz        |

## NMD satırı mutlaka değiştirilmeli

Şu ifade doğru değildir:

> “Transkript yok → gerçek null.”

NMD çoğunlukla mutant transkript düzeyini **azaltır**; her hücrede ve dokuda tamamen ortadan kaldırmak zorunda değildir. NMD etkinliği dokuya, hücresel duruma, transkript mimarisine ve PTC konumuna göre değişebilir. Ayrıca klasik EJC modelinde PTC’nin son ekzon–ekzon birleşiminin yaklaşık 50–55 nükleotid upstream’inde olması önemlidir; fakat bu kuralın istisnaları vardır. ([PubMed Central (PMC)][3])

Daha doğru klinik anlam:

> **NMD’ye uğrayan transkript, mutant protein üretimini genellikle belirgin ölçüde azaltır ve null/LoF mekanizmasını destekleyebilir; ancak gerçek null sonucu deneysel veya güçlü mekanistik kanıt olmadan kesinleştirilmemelidir.**

ClinGen PVS1 yaklaşımı da nonsense veya frameshift görünümünün tek başına yeterli olmadığını; ilgili transkript, NMD beklentisi, ekzonun biyolojik önemi ve hastalık mekanizmasının ayrıca değerlendirilmesi gerektiğini belirtir. ([PubMed Central (PMC)][4])

## LoF intoleransı satırı da yeniden yazılmalı

Şu klinik karşılık fazla güçlü:

> “Bu gende LoF beklenen mekanizma mı?”

LOEUF/pLI gibi constraint ölçütleri bu soruyu doğrudan yanıtlamaz. Doğru soru:

> **“Bu gen, genel popülasyonda heterozigot tahmini LoF varyantlarına karşı negatif seçilim gösteriyor mu?”**

Düşük LOEUF, haploinsufficiency ile uyumludur; fakat:

* gen–hastalık ilişkisini,
* belirli hastalıkta LoF mekanizmasını,
* incelenen varyantın gerçek null olduğunu,
* PVS1 uygulanabilirliğini

tek başına kanıtlamaz.

## Son öneri

Tablonun ilk üç satırını şu kısa biçimde kullanın:

| Kavram                     | Tanım                                                                                               | Klinik anlamı                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Loss-of-function — LoF** | Gen ürününün miktarının veya işlevinin kısmen ya da tamamen azalması                                | Azalmış işlevin klinik sonucu, hastalığın allelik gereksinimine ve rezidüel aktiviteye bağlıdır |
| **Null (amorfik) alel**    | İşlevsel katkısı sıfır olan alel; ürün hiç oluşmayabilir veya oluşan ürün tamamen işlevsiz olabilir | Tam moleküler işlev kaybıdır; klinik olarak mutlaka en ağır varyant sınıfı değildir             |
| **Hipomorfik alel**        | WT’ye göre azalmış, fakat sıfır olmayan işlev gösteren alel                                         | Rezidüel işlev çoğu zaman fenotipin şiddetini, başlangıç yaşını ve penetransını değiştirir      |

Bu sürüm hem Muller terminolojisine hem de güncel klinik insan genetiği kullanımına uygundur.

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11039201/?utm_source=chatgpt.com "Toward robust clinical genome interpretation: Developing a consistent terminology to characterize Mendelian disease-gene relationships—allelic requirement, inheritance modes, and disease mechanisms - PMC"
[2]: https://www.sciencedirect.com/science/article/pii/S0039625723001571?utm_source=chatgpt.com "Hypomorphic variants in inherited retinal and ocular diseases: A review of the literature with clinical cases - ScienceDirect"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8773229/ "Nonsense-Mediated mRNA Decay, a Finely Regulated Mechanism - PMC"
[4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6185798/?utm_source=chatgpt.com "Recommendations for interpreting the loss of function PVS1 ..."


<br>

### C5 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · 2.2. Doza duyarlılık hangi gen sınıflarında, neden kümelenir? · satır 72

> **Stokiyometrik kompleks üyeleri.** Bazı proteinler hücrede tek başına değil, sabit oranlarda bir araya gelen çok-alt-birimli komplekslerde iş görür (ribozom, spliceozom, kohesin, bazı yapısal kompleksler). Bir alt birimin dozu yarıya inerse, kompleksin **doğru stokiyometride** montajı bozulur; eksik veya dengesiz alt birimler hem işlevsiz kompleks hem de serbest, yanlış katlanmış kalıntılar yaratabilir. **Gen dengesi hipotezi** (gene ***balance hypothesis***), kompleks üyelerinin neden doza duyarlı genler arasında zenginleştiğini açıklar: dengesizlik etkilerinin, makromoleküler komplekslerin, etkileşim ağının ve sinyal yolaklarının üyeleri arasındaki **stokiyometrik farklardan** kaynaklandığı öne sürülür (Birchler ve Veitia, 2012).

**Sorulan:** "Dengeli ifade hipotezi" bu adla anılıyor mu ve burada doğru kullanılmış mı? (Kitapta kaynaksız.)

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**“Dengeli ifade hipotezi” yerleşik ve doğru karşılık değildir.** Kullanılması gereken ad:

> **Gen dengesi hipotezi** (*gene balance hypothesis*)
> veya daha açıklayıcı biçimde
> **Gen dozaj dengesi hipotezi** (*gene dosage balance hypothesis*)

Veitia’nın erken çalışmalarında **gene dosage balance hypothesis**, Birchler ve Veitia’nın 2012 sentezinde ise **gene balance hypothesis** adı kullanılır. Hipotez yalnızca genlerin “dengeli ifade edilmesini” değil, etkileşen ürünlerin **göreli dozlarının ve stokiyometrisinin korunmasını** anlatır. “Dengeli ifade” ifadesi konuyu mRNA ekspresyon düzeyine indirgediği için yanıltıcıdır. ([PubMed Central (PMC)][1])

## Paragraf doğru mu?

**Ana mekanizma doğru; fakat mevcut anlatım fazla deterministik.**

Şu cümle:

> “Bir alt birimin dozu yarıya inerse, kompleksin doğru stokiyometride montajı bozulur.”

şöyle yazılmalıdır:

> **Bir alt birimin dozunun azalması, alt birim kompleks oluşumunu sınırlıyorsa tam monte edilmiş kompleks sayısını azaltabilir ve diğer alt birimlerle stokiyometrik dengesizlik oluşturabilir.**

Çünkü bir kompleks üyesinin dozunun yarıya inmesi her zaman:

* kompleks montajının tamamen bozulacağı,
* serbest proteinlerin yanlış katlanacağı,
* klinik haploinsufficiency oluşacağı

anlamına gelmez.

Sonuç; hangi alt birimin sınırlayıcı olduğuna, kompleksin montaj sırasına, paraloglarla telafiye, transkripsiyonel düzenlemeye ve protein kalite kontrolüne bağlıdır. Hipotez, dozdaki değişimin özellikle kompleksler, etkileşim ağları ve sinyal yolaklarındaki **göreli oranları** bozarak fenotip oluşturabileceğini öne sürer. ([PNAS][2])

## “Serbest, yanlış katlanmış kalıntılar” ifadesi

Bu bölüm de kesinleştirilmemelidir:

> “Eksik veya dengesiz alt birimler serbest, yanlış katlanmış kalıntılar yaratır.”

Doğrusu:

> **Komplekse katılamayan eş alt birimler ‘orphan subunit’ olarak kalabilir; bunlar çoğunlukla hücresel kalite kontrol yolaklarıyla yıkılır, fakat bazı bağlamlarda birikme, agregasyon veya proteotoksik stres oluşturabilir.**

Kompleks üyelerinin orantısız üretimi her zaman yanlış katlanma yaratmaz. Hücreler fazla veya eşleşmemiş alt birimleri seçici olarak yıkarak stokiyometriyi önemli ölçüde tamponlayabilir. Oligosakkariltransferaz kompleksinde yapılan deneyler, eşleşmemiş alt birimlerin hızlandırılmış degradasyonunun stokiyometrik dengesizliği düzeltebildiğini göstermiştir. ([PubMed Central (PMC)][3])

Ayrıca alt birimlerden biri azaldığında ortaya çıkan “serbest” ürün çoğunlukla azalan proteinin kendisi değil, **birleşecek partner bulamayan diğer kompleks üyeleridir**.

## Hipotezin klinik kullanım sınırı

Hipotez şu gözlemi açıklamak için uygundur:

> Çok alt birimli komplekslerin, düzenleyici ağların ve sinyal yolaklarının bazı üyeleri neden kopya sayısı değişimlerine karşı duyarlıdır?

Ancak şu çıkarım yapılamaz:

[
\text{Kompleks üyesi}
\Rightarrow
\text{haploinsufficient gen}
]

Her kompleks üyesi doz duyarlı değildir. Bazı alt birimler:

* fazla miktarda üretilir,
* sınırlayıcı değildir,
* paraloglarla telafi edilir,
* protein düzeyinde doz kompansasyonuna uğrar,
* yalnız belirli doku veya gelişim dönemlerinde sınırlayıcı hâle gelir.

Bu nedenle hipotez **gen düzeyinde biyolojik açıklama ve önceliklendirme sağlar**; tek başına bir gen–hastalık mekanizmasını veya varyant patojenitesini kanıtlamaz.

## Önerilen düzeltilmiş metin

> **Stokiyometrik kompleks üyeleri.** Bazı proteinler tek başına değil, belirli oranlarda bir araya gelen çok alt birimli komplekslerin parçası olarak işlev görür; ribozom, spliceozom ve kohesin bunun örnekleridir. Bir alt birimin dozunun azalması, o alt birim kompleks montajında sınırlayıcıysa tam oluşmuş kompleks sayısını düşürebilir ve diğer üyelerle stokiyometrik dengesizlik oluşturabilir. Komplekse katılamayan eş alt birimler hücresel kalite kontrol yolaklarıyla yıkılabilir; bazı koşullarda ise birikerek agregasyon veya proteotoksik stres oluşturabilir. Bununla birlikte transkripsiyonel ve posttranslasyonel doz kompansasyonu bu etkileri kısmen tamponlayabilir.
>
> **Gen dengesi veya gen dozaj dengesi hipotezi** (*gene balance/gene dosage balance hypothesis*), kopya sayısındaki göreli değişikliklerin makromoleküler kompleksler, protein etkileşim ağları ve sinyal yolakları içindeki stokiyometrik ilişkileri bozarak fenotip oluşturabileceğini öne sürer. Bu model, kompleks ve düzenleyici ağ üyelerinin doz duyarlı genler arasında neden zenginleşebildiğini açıklar; ancak her kompleks üyesinin haploinsufficient olduğunu veya belirli bir LoF varyantının patojenik olduğunu tek başına göstermez.

Kaynak olarak şu iki çalışma eklenmelidir:

* **Veitia RA.** *Gene Dosage Balance in Cellular Pathways: Implications for Dominance and Gene Duplicability.* Genetics. 2004;168:569–574. DOI: `10.1534/genetics.104.029785`. ([OUP Academic][4])
* **Birchler JA, Veitia RA.** *Gene Balance Hypothesis: Connecting Issues of Dosage Sensitivity Across Biological Disciplines.* PNAS. 2012;109:14746–14753. DOI: `10.1073/pnas.1207726109`. ([PNAS][2])

**Net düzeltme:** “Dengeli ifade hipotezi”ni çıkarın. Kitapta ilk kullanımda **“gen dozaj dengesi hipotezi (*gene balance hypothesis*)”**, sonraki kullanımlarda **“gen dengesi hipotezi”** yazın.

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1448121/?utm_source=chatgpt.com "Gene Dosage Balance in Cellular Pathways: Implications for Dominance and Gene Duplicability - PMC"
[2]: https://www.pnas.org/doi/10.1073/pnas.1207726109?utm_source=chatgpt.com "Gene balance hypothesis: Connecting issues of dosage ..."
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4501358/?utm_source=chatgpt.com "Protein degradation corrects for imbalanced subunit stoichiometry in OST complex assembly - PMC"
[4]: https://academic.oup.com/genetics/article/168/1/569/6059564?ijkey=7fff0a633462d2127f343efe0e093911116c4ccf&keytype2=tf_ipsecsha&utm_source=chatgpt.com "Gene Dosage Balance in Cellular Pathways | Genetics | Oxford Academic"


<br>

### C6 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · Öğrenme hedefleri · satır 15

> Bu bölümü tamamlayan okuyucu:
> 1. Haploinsufficiency'yi doz–yanıt eğrisi ve **klinik eşik** kavramıyla tanımlayabilir ve neden dominant kalıtıma yol açtığını açıklayabilir.
> 2. Hangi gen sınıflarının (transkripsiyon faktörleri, kromatin düzenleyiciler, yapısal/stokiyometrik kompleks üyeleri, ***morfojen***ler) ve **neden** doza duyarlı olduğunu gerekçelendirebilir.
> 3. Farklı varyant tiplerinin (nonsense/frameshift, kanonik splice, destabilize missense, tek-ekzon ve **tam gen delesyonu/CNV**) aynı "%50 doz" son yoluna nasıl yakınsadığını gösterebilir.
> 4. Haploinsufficiency'nin neden sıklıkla **değişken penetrans ve ekspresivite** gösterdiğini (eşiğe yakınlık, modifiye ediciler, stokastik gürültü) açıklayabilir.
> 5. Bir genin doz duyarlılığını öngören popülasyon metriklerini (pLI, LOEUF, pHaplo, HI-indeksi) doğru yorumlayabilir ve sınırlarını bilir.
> 6. Tanıda neden **dizileme + doz analizinin (MLPA/array/WGS-CNV) birlikte** gerektiğini ve yalnız dizilemenin neyi kaçırdığını açıklayabilir.
> 7. PVS1'i haploinsufficiency mekanizmalı genlerde doğru uygular; ClinGen/ACMG **CNV dozaj puanlama** çerçevesini (Riggs ve ark., 2020) tanır.
> 8. Triplosensitivity (kopya artışına duyarlılık) kavramını haploinsufficiency'nin ayna görüntüsü olarak ayırt edebilir.

**Sorulan:** Morfojen gradyanı ve eşik-bağımlı hücre kaderi anlatımı doğru mu? (Kitapta kaynaksız, "yerleşik ders bilgisi" olarak etiketli.)

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Morfojen gradyanı ve eşik-bağımlı hücre kaderi anlatımı biyolojik olarak doğrudur; ancak “morfojenler doza duyarlıdır” şeklinde genellenmemelidir.** Ayrıca hücre kaderi, çoğu sistemde yalnızca anlık morfojen konsantrasyonuna göre belirlenen sabit bir eşik modeli değildir.

En doğru çerçeve:

> **Bazı gelişimsel morfojenler ve bunların sinyal yolakları, sinyal düzeyindeki nicel değişikliklerin hücre kaderi sınırlarını değiştirebilmesi nedeniyle doz duyarlıdır. Hücreler çoğu zaman morfojenin yalnız konsantrasyonunu değil, sinyalin süresini, zaman-integralini ve gen düzenleyici ağın durumunu birlikte yorumlar.**

## Klasik model neden doğru?

Yerel bir kaynaktan salgılanan morfojen dokuda uzamsal bir aktivite gradyanı oluşturur. Farklı konumlardaki hücreler farklı sinyal düzeylerine maruz kalır; belirli yanıt eşikleri aşıldığında farklı hedef gen programları ve hücre kaderleri ortaya çıkabilir.

Örneğin ventral nöral tüpte SHH sinyali, birbirinden ayrılmış progenitör alanların oluşmasını sağlar. Ancak Balaskas ve arkadaşlarının deneyleri, bu alanların yalnızca “yüksek–orta–düşük SHH konsantrasyonu” ile açıklanmadığını; SHH sinyalinin düzeyi ve süresinin, `PAX6–OLIG2–NKX2.2` gibi karşılıklı baskılayıcı transkripsiyon faktörü ağları tarafından birlikte yorumlandığını göstermiştir. ([PubMed][1])

BMP için de konsantrasyon eşiği modeli doğrudan deneysel destek bulur. Zebrafish gastrulasında farklı pSMAD5 düzeylerinin farklı hedef gen kümelerini aktive ettiği ve dorsoventral alanları oluşturduğu gösterilmiştir. ([PLOS][2])

Dolayısıyla şu temel anlatım doğrudur:

[
\text{uzamsal sinyal gradyanı}
\rightarrow
\text{farklı hücresel yanıt düzeyleri}
\rightarrow
\text{farklı gen programları}
\rightarrow
\text{farklı hücre kaderleri}
]

## Fakat “sabit konsantrasyon eşikleri” yeterli değildir

Kitapta şu biçimde anlatılırsa fazla basitleştirilmiş olur:

> Hücre A, morfojen konsantrasyonu X’i aşarsa kader 1; aşmazsa kader 2 olur.

Daha güncel modelde hücrenin okuduğu girdi şunların bileşimidir:

[
\text{Hücre kaderi}
===================

f(
\text{sinyal şiddeti},
\text{sinyal süresi},
\text{zaman integrali},
\text{önceki hücresel durum},
\text{gen düzenleyici ağ}
)
]

İnsan pluripotent kök hücrelerinde BMP yanıtının bazı kader kararlarında anlık düzeyden çok sinyalin **zaman-integraliyle** ilişkili olduğu gösterilmiştir. Düşük düzeyde uzun süreli sinyal ile yüksek düzeyde kısa süreli sinyal benzer toplam yanıt oluşturabilir. ([Nature][3])

Benzer biçimde BMP4 ve Nodal çalışmalarında hücrelerin yalnız mutlak konsantrasyonu değil, konsantrasyonun zaman içindeki değişim hızını ve hücreler arası topluluk etkilerini de okuyabildiği gösterilmiştir. ([PubMed][4])

Bu nedenle **“eşik”**, sabit bir ekstrasellüler ligand konsantrasyonu olarak değil, hücrenin aşağı akım sinyal ve transkripsiyon ağında ulaştığı **etkin yanıt eşiği** olarak anlatılmalıdır.

## Haploinsufficiency ile bağlantısı

Morfojen üreten bir genin tek kopyasının kaybı teorik olarak:

[
\text{ligand üretimi}\downarrow
\rightarrow
\text{gradyan amplitüdü veya erişim mesafesi}\downarrow
\rightarrow
\text{eşiklerin aşıldığı alanların değişmesi}
\rightarrow
\text{hücre kaderi sınırlarının kayması}
]

sonucunu oluşturabilir.

Ancak şu varsayım doğru değildir:

[
\text{heterozigot LoF}
\Rightarrow
\text{morfojen düzeyi tam } %50
\Rightarrow
\text{gradyan da tam } %50
]

Gerçek sonuç ligand işlenmesi, salgılanması, ekstrasellüler taşınması, reseptör düzeyi, geri bildirim, doku büyümesi ve yolak içi kompansasyon tarafından değiştirilir. SHH yolak dinamiklerinde `PTCH1` ve `GLI` aracılı geri bildirimlerin sinyalin zamansal ve uzamsal profilini değiştirdiği deneysel olarak gösterilmiştir. ([Nature][5])

İnsanlarda heterozigot `SHH` varyantlarının holoprozensefaliye neden olması, gelişimsel sinyal miktarının klinik olarak doz duyarlı olabileceğini gösteren uygun bir örnektir. Ancak aynı ailede ağır malformasyondan klinik olarak fark edilmeyen taşıyıcılığa kadar geniş değişkenlik bulunması, fenotipin basit bir “%50 SHH” modeline indirgenemeyeceğini gösterir. ([PubMed][6])

## “Morfojenler doza duyarlı gen sınıfıdır” denmeli mi?

Bu biçimde **hayır**. Bütün morfojen genleri haploinsufficient değildir.

Şu ifade daha doğru:

> **Gelişimsel morfojenleri ve morfojen yolaklarının bazı bileşenlerini kodlayan genler, sinyal düzeyinin hücre kaderi eşiklerine yakın olduğu bağlamlarda doz duyarlılığı gösterebilir.**

Doz duyarlılığı şunlara bağlıdır:

* genin heterozigot kaybının ligand üretimini gerçekten sınırlayıp sınırlamadığı,
* yolakta geri bildirim ve kompansasyon bulunması,
* gelişim dönemindeki güvenlik payı,
* dokunun farklı sinyal düzeylerine duyarlılığı,
* ilgili gen–hastalık ilişkisinde LoF mekanizmasının gösterilmiş olması.

Bu nedenle morfojen olmak, tek başına:

[
\text{morfojen geni}
\Rightarrow
\text{haploinsufficient gen}
]

sonucunu vermez.

## Öğrenme hedefinin düzeltilmiş biçimi

Mevcut madde:

> Hangi gen sınıflarının — transkripsiyon faktörleri, kromatin düzenleyiciler, yapısal/stokiyometrik kompleks üyeleri, morfojenler — ve neden doza duyarlı olduğunu gerekçelendirebilir.

Şöyle değiştirilmesi daha doğru:

> **Transkripsiyon faktörleri, kromatin düzenleyicileri, stokiyometrik kompleks üyeleri ve bazı gelişimsel morfojen/yolak genlerinin hangi mekanizmalarla doz duyarlılığı gösterebildiğini açıklayabilir; bu sınıflara üyeliğin tek başına haploinsufficiency kanıtı olmadığını ayırt edebilir.**

Kitap içindeki mekanizma paragrafı için uygun metin:

> **Morfojen gradyanları ve hücre kaderi eşikleri.** Gelişim sırasında bazı salgılanan sinyaller dokuda uzamsal aktivite gradyanları oluşturur. Hücreler bulundukları konuma göre farklı sinyal düzeylerine maruz kalır ve belirli aşağı akım yanıt eşikleri aşıldığında farklı transkripsiyon programlarına ve hücre kaderlerine geçebilir. Bir morfojenin veya yolak bileşeninin dozunun azalması, gradyanın amplitüdünü, süresini veya erişim alanını değiştirerek hücre kaderi sınırlarını kaydırabilir. Ancak hücreler yalnızca anlık ligand konsantrasyonunu okumaz; sinyal süresi, zaman-integrali, geri bildirim devreleri ve hücresel yetkinlik de sonucu belirler. Bu nedenle morfojen yolakları doz duyarlılığı için biyolojik olarak elverişlidir, fakat her morfojen geni haploinsufficient değildir.

**“Yerleşik ders bilgisi” etiketi kullanılabilir; fakat paragraf kaynaksız bırakılmamalıdır.** En az Balaskas 2012 ve bir BMP eşik/dinamik çalışması kaynak gösterilmelidir.

[1]: https://pubmed.ncbi.nlm.nih.gov/22265416/?utm_source=chatgpt.com "Gene regulatory logic for reading the Sonic Hedgehog signaling gradient in the vertebrate neural tube - PubMed"
[2]: https://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.3001059&utm_source=chatgpt.com "The BMP signaling gradient is interpreted through concentration thresholds in dorsal–ventral axial patterning | PLOS Biology"
[3]: https://www.nature.com/articles/s41467-024-45719-9?utm_source=chatgpt.com "Time-integrated BMP signaling determines fate in a stem ..."
[4]: https://pubmed.ncbi.nlm.nih.gov/28760810/?utm_source=chatgpt.com "Morphogen and community effects determine cell fates in response to BMP4 signaling in human embryonic stem cells - PubMed"
[5]: https://www.nature.com/articles/ncomms7709?utm_source=chatgpt.com "Ptch1 and Gli regulate Shh signalling dynamics via ..."
[6]: https://pubmed.ncbi.nlm.nih.gov/8896572/?utm_source=chatgpt.com "Mutations in the human Sonic Hedgehog gene cause ..."


<br>

### C7 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · 4.4. Haploinsufficiency neden değişken penetrans ve ekspresivite gösterir? · satır 140

> Haploinsufficiency, Bölüm 1'de tanıtılan **eksik penetrans ve değişken ekspresivite** kavramlarının en sık zeminlerinden biridir, ve bunun nedeni yine eşik mantığında gizlidir. Doz tam eşiğin **kıyısına** düştüğünde, sistemin eşiğin altında mı üstünde mi kalacağını belirleyen küçük etkenler öne çıkar: aynı yolaktaki **modifiye edici** varyantlar, ikinci (sağlam) allelin ifade düzeyindeki bireysel farklar, çevresel etkenler ve gelişim sırasındaki **stokastik (rastlantısal) gen ifadesi gürültüsü**. Eşikten uzak (çok düşük doz) varyantlarda fenotip daha öngörülebilir ve ağırken, ***eşiğe yakın doz bırakanlarda penetrans eksik, ekspresivite değişken olur***. Bu, neden aynı ailede aynı HI varyantını taşıyan bireylerin farklı şiddette etkilenebildiğini açıklar (örn. Holt-Oram'da aile içi değişkenlik; Bruneau ve ark., 2001; [DOI](https://doi.org/10.1016/s0092-8674(01)00493-7)).

**Sorulan:** HI'da değişken penetransın eşik-yakınlığıyla açıklanması doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Eşik-yakınlığı modeli doğrudur ve haploinsufficiency’de eksik penetransı açıklamak için güçlü bir kavramsal çerçevedir. Ancak mevcut metin bunu evrensel ve kanıtlanmış tek mekanizma gibi sunuyor.** Ayrıca penetrans ile fenotip şiddeti kısmen birbirine karıştırılmış.

Daha doğru sonuç:

> Bir haploinsufficient genotipin oluşturduğu biyolojik çıktı, hastalık eşiğine yakın bir dağılım gösteriyorsa küçük genetik, çevresel veya stokastik değişiklikler bireyin ya da belirli bir klinik bulgunun eşiğin hangi tarafında kalacağını belirleyebilir.

Bu modelde önemli olan yalnızca ortalama protein miktarı değildir. Eşikle karşılaştırılması gereken değişken; ilgili doku ve gelişim dönemindeki protein aktivitesi, transkripsiyonel ağ çıktısı, sinyal düzeyi veya hücre kaderi gibi **fenotipe yakın işlevsel çıktı** olabilir. Modern eşik modellerinde penetrans, bu biyolojik çıktının olasılık dağılımının hastalık eşiğini aşan bölümüdür. ([PubMed Central (PMC)][1])

## Doğru anlatılan kısımlar

Aynı varyantı taşıyan kişiler arasındaki farkları şu etkenler oluşturabilir:

* ikinci, sağlam alelin cis-düzenleyici özellikleri ve alel-spesifik ekspresyonu;
* aynı yolaktaki genetik modifiye ediciler;
* epigenetik ve gelişimsel durum;
* çevresel etkiler;
* transkripsiyonel patlamalar, hücre sayısı ve hücre kaderi kararlarındaki stokastik değişkenlik;
* dokular arasındaki kompansasyon ve biyolojik tamponlama kapasitesi.

Genetik olarak aynı model organizmalarda ve kontrol edilen çevrelerde bile farklı penetrans görülmesi, stokastik süreçlerin eşik çevresinde fenotip oluşturabileceğini destekler. İnsanlarda ise genetik arka plan, çevre ve stokastisite çoğunlukla birlikte etkili olduğundan bunların bireysel katkısını ayırmak daha zordur. ([PubMed Central (PMC)][1])

## Düzeltilmesi gereken noktalar

### 1. Haploinsufficiency, eksik penetrans demek değildir

Bazı HI hastalıkları son derece yüksek penetranslıdır. Bir sistemde tek sağlam alelin sağladığı işlev, ilgili fenotip eşiğinin belirgin biçimde altında kalıyorsa hemen hemen bütün taşıyıcılarda bulgu ortaya çıkabilir.

Dolayısıyla:

[
\text{HI}\not\Rightarrow\text{eksik penetrans}
]

Daha doğru ilişki:

[
\text{HI}+\text{eşik çevresinde işlevsel çıktı}
\Rightarrow
\text{eksik penetransa yatkınlık}
]

“HI, eksik penetransın en sık zeminlerinden biridir” ifadesi nicel olarak kanıtlanması zor ve gereksiz ölçüde güçlüdür. Şöyle yazın:

> **Haploinsufficiency, eksik penetrans ve değişken ekspresivitenin açıklanmasında eşik modelinin özellikle yararlı olduğu hastalık mekanizmalarından biridir.**

### 2. “Doz tam eşiğin kıyısına düşer” fazla basit

Heterozigot null varyant protein miktarını her zaman tam `%50` yapmaz. Sağlam alel:

* yukarı regüle olabilir,
* bireyler arasında farklı miktarda eksprese edilebilir,
* dokuya göre farklı kompanse edilebilir,
* protein yarı ömrü ve ağ geri bildirimleriyle doğrusal olmayan sonuç oluşturabilir.

Ayrıca eşik, doğrudan gen ürününün miktarında değil, aşağı akım bir transkripsiyonel ağ veya hücresel süreçte bulunabilir. TBX5 modellerinde azaltılmış dozun, kardiyak gelişimle ilişkili gen düzenleyici ağları ve farklı kardiyomiyosit alt popülasyonlarını eşit olmayan biçimde etkilediği gösterilmiştir. ([PubMed Central (PMC)][2])

### 3. “Eşikten uzak varyantlar daha ağırdır” zorunlu değil

Fenotip eşiğinden belirgin biçimde hastalık tarafında kalmak genellikle **yüksek penetransı** öngörür. Ancak otomatik olarak daha ağır fenotip anlamına gelmez.

[
\text{eşikten uzaklık}
\rightarrow
\text{penetransın artması}
]

ilişkisi makuldür; fakat:

[
\text{eşikten uzaklık}
\rightarrow
\text{klinik şiddetin doğrusal artışı}
]

genel bir kural değildir.

Şiddet:

* başka bir biyolojik çıktıya,
* ek doku eşiklerine,
* gelişimsel zamanlamaya,
* organ rezervine,
* varyantın pleiotropik etkilerine

bağlı olabilir. Bir sendromdaki her klinik bulgunun kendi eşiği bulunabilir; bu nedenle aynı birey bir bulgu için eşiği aşarken başka bir bulgu için aşmayabilir. Bu yaklaşım, sendrom düzeyindeki değişken ekspresiviteyi klinik özelliklere özgü eksik penetransların birleşimi olarak ele alır. ([PubMed Central (PMC)][1])

## Holt–Oram örneği uygun mu?

**Uygundur; fakat Bruneau 2001 tek başına ileri sürdüğünüz zinciri kanıtlamaz.**

Bruneau ve arkadaşlarının `Tbx5` heterozigot fare modeli, TBX5 haploinsufficiency’nin kalp ve ön ekstremite anomalilerine yol açtığını ve doz duyarlılığının Holt–Oram patogenezindeki yerini gösterdi. Makalenin DOI’si:

`10.1016/S0092-8674(01)00493-7` ([ScienceDirect][3])

Ancak aile içi değişkenliği “eşik yakınlığı” ile daha doğrudan desteklemek için ek çalışmalar gerekir:

* Bir `Tbx5` allelik serisinde, küçük doz değişiklikleriyle kardiyak morfogenez ve gen ekspresyonu arasında duyarlı bir doz–fenotip ilişkisi gösterildi. ([ScienceDirect][4])
* İnsan Holt–Oram kohortunda fenotip şiddetinin yalnız TBX5 varyantının konumu veya genotipiyle güvenilir biçimde öngörülemediği bulundu. ([ScienceDirect][5])
* `KLF13` dozunun azaltılması, `Tbx5` heterozigot farelerde septal defekt penetransını artırdı; bu, yolak içi modifiye edicinin penetransı değiştirebildiğine dair doğrudan deneysel kanıttır. ([OUP Academic][6])

Dolayısıyla Holt–Oram için en doğru ifade:

> **TBX5 haploinsufficiency doz duyarlı bir gelişimsel ağ oluşturur; aile içi değişken ekspresivite, yalnız TBX5 varyant tipinden değil, genetik modifiye ediciler, ağ tamponlama kapasitesi ve muhtemelen gelişimsel stokastisiteden etkilenir.**

## Düzeltilmiş paragraf

> **Haploinsufficiency, eksik penetrans ve değişken ekspresivitenin açıklanmasında eşik modelinin özellikle yararlı olduğu hastalık mekanizmalarından biridir. Tek sağlam alelin oluşturduğu biyolojik çıktı hastalık eşiğine yakınsa, küçük değişiklikler fenotipin ortaya çıkıp çıkmamasını veya hangi klinik bulguların gelişeceğini belirleyebilir. Bu değişiklikler sağlam alelin ekspresyon düzeyinden, aynı yolaktaki genetik modifiye edicilerden, çevresel etkilerden, hücresel kompansasyondan ve gelişim sırasında ortaya çıkan stokastik moleküler dalgalanmalardan kaynaklanabilir.**
>
> **Buradaki “doz”, yalnızca toplam RNA veya protein miktarı değildir; ilgili doku ve gelişim döneminde fenotipe neden olan transkripsiyonel, sinyal veya hücresel ağ çıktısıdır. Bu çıktının dağılımı eşikle örtüşüyorsa bazı taşıyıcılar eşiği aşarken bazıları aşmayabilir; bu durum eksik penetransa yol açar. Etkilenen kişilerde farklı dokuların veya klinik özelliklerin farklı eşiklere sahip olması ise değişken ekspresivite oluşturabilir. Genotipin biyolojik çıktısı hastalık eşiğinin belirgin biçimde ötesindeyse penetrans genellikle yükselir; ancak bu durum klinik şiddetin zorunlu olarak doğrusal biçimde artacağı anlamına gelmez.**
>
> **Holt–Oram sendromu bu modele uygun bir örnektir. `TBX5` haploinsufficiency doz duyarlı kardiyak ve ekstremite gelişim ağlarını bozar; ancak aynı ailedeki fenotip şiddeti yalnızca TBX5 genotipiyle açıklanamaz. Deneysel modeller, TBX5 dozundaki küçük değişikliklerin gelişimsel çıktıyı değiştirebildiğini ve `KLF13` gibi yolak içi modifiye edicilerin kardiyak defekt penetransını artırabildiğini göstermiştir.**

**Net sonuç:** Eşik-yakınlığı açıklaması doğru ve kitapta tutulmalı. Ancak “HI sıklıkla değişkendir”, “düşük doz mutlaka daha ağırdır” ve “Bruneau 2001 bu mekanizmayı doğrudan kanıtlamıştır” biçimindeki mutlak çıkarımlar kaldırılmalıdır.

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10909503/ "How do stochastic processes and genetic threshold effects explain incomplete penetrance and inform causal disease mechanisms? - PMC"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7878434/?utm_source=chatgpt.com "Modeling human TBX5 haploinsufficiency predicts regulatory ..."
[3]: https://www.sciencedirect.com/science/article/pii/S0092867401004937?utm_source=chatgpt.com "A Murine Model of Holt-Oram Syndrome Defines Roles of the T-Box Transcription Factor Tbx5 in Cardiogenesis and Disease - ScienceDirect"
[4]: https://www.sciencedirect.com/science/article/pii/S0012160606008116?utm_source=chatgpt.com "Tbx5-dependent rheostatic control of cardiac gene ..."
[5]: https://www.sciencedirect.com/science/article/pii/S0002929707638968?utm_source=chatgpt.com "Expressivity of Holt-Oram Syndrome Is Not Predicted by TBX5 Genotype - ScienceDirect"
[6]: https://academic.oup.com/hmg/article/26/5/942/2970366 "oup.silverchair-cdn.com"


<br>

### C8 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 2.1. Zehirli alt birim: varyant ürün sağlamı nasıl "zehirler"? · satır 61

> **🔬 Deep-dive — DN'in iki ön koşulu ve neden bazı genlerde olur, bazılarında olmaz?** ***Bir varyantın DN etki yapabilmesi için iki şart gerekir***. **Birincisi, varyant ürün üretilmeli ve stabil kalmalıdır.** Erken stop kodonu yapan, NMD ile yıkılan ya da proteini tümüyle yok eden varyantlar DN yapamaz — ortada zehirleyecek bir ürün kalmaz; bunlar saf LoF/haploinsufficiency yapar. Bu yüzden DN varyantlar tipik olarak **missense veya in-frame** (küçük in-frame delesyon/insersiyon) değişikliklerdir: ürün yapılır, komplekse girebilecek kadar "normal" görünür, ama işlevi bozuktur. **İkincisi, ürün sağlam ürünle fiziksel olarak etkileşmelidir** — yani protein multimerik olmalı veya bir kompleksin/ağın parçası olmalıdır. Tek başına (monomer olarak) çalışan ve başka kopyalarla etkileşmeyen bir enzimde DN beklenmez; orada bir bozuk kopya yalnız kendi payını kaybettirir (haploinsufficiency). Gerasimavicius, Livesey ve Marsh (2022), patojenik missense varyantların yapısal etkilerini mekanizmaya göre çözümlediklerinde tam bu beklentiyi doğrulamıştır: DN varyantlar **protein–protein arayüzlerinde belirgin biçimde zenginleşir** ve LoF varyantlardan farklı olarak protein kararlılığını çok daha az bozarlar — yani "katlanmayı yıkıp ürünü yok eden" değil, "ürünü ayakta tutup etkileşimi/işlevi sabote eden" değişikliklerdir (Gerasimavicius ve ark., 2022, *Nat Commun*; [DOI](https://doi.org/10.1038/s41467-022-31686-6)).

**Sorulan:** İki ön koşul doğru ve yeterli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → Düzeltilmiş metin
Deep-dive — Dominant-negatif etkinin gereklilikleri ve neden bazı genlerde görülüp bazılarında görülmediği
Protein aracılı dominant-negatif bir etkinin oluşması için mutant alelin ilgili hücre ve gelişim döneminde anlamlı miktarda bir ürün oluşturması gerekir. Ürün hiç oluşmuyorsa veya mutant transkript ve protein etkin biçimde ortadan kaldırılıyorsa, sağlam alelin ürününü bozacak bir molekül kalmaz ve varyant genellikle basit LoF/haploinsufficiency yönünde davranır. Bununla birlikte nonsense, frameshift veya splice varyantları NMD’den kaçabilir ya da stabil kesilmiş protein oluşturabilir; bu nedenle varyant tipi tek başına DN mekanizmasını dışlamaz. DN varyantların missense ve in-frame değişikliklerde zenginleşmesinin nedeni, bu varyantların ürünün oluşmasını ve bazı moleküler etkileşimlerini koruma olasılığının daha yüksek olmasıdır.
İkinci gereklilik, mutant ürünün WT alelin sağladığı işlevi trans olarak aktif biçimde azaltmasıdır. En klasik mekanizma, mutant ve WT alt birimlerin karma multimer oluşturarak kompleksin zehirlenmesidir. Ancak doğrudan WT–mutant bağlanması zorunlu değildir. Mutant ürün sınırlı bir kompleks ortağını, kofaktörü veya substratı sekestre edebilir; aynı DNA/RNA hedefi, reseptör veya adaptör için rekabet edebilir; kompleks montajını, taşınmayı ya da WT proteinin kararlılığını bozabilir. Bu nedenle dominant-negatif etki multimerik proteinlerde özellikle sık görülse de yalnızca multimerlerle sınırlı değildir.
Mutant ürünün stabil ve etkileşim yeteneğine sahip olması da tek başına yeterli değildir. Karma kompleksin veya ortak yolak çıktısının basit bir alel kaybında beklenenden daha fazla azalması gerekir. Dominant-negatif mekanizma deneysel olarak, WT ve mutantın birlikte bulunduğu koşulun yalnızca %50 WT içeren haploinsufficiency kontrolünden daha düşük işlev göstermesiyle ortaya konmalıdır.
Gerasimavicius, Livesey ve Marsh, DN ile ilişkili patojenik missense varyantların protein–protein arayüzlerinde zenginleştiğini ve LoF varyantlara göre protein monomerini ortalama olarak daha az destabilize ettiğini göstermiştir. Bu bulgu, DN varyantların çoğunlukla ürünü tamamen yok etmek yerine etkileşim kapasitesini koruyarak kompleks veya ağ işlevini bozduğu modelini destekler. Ancak arayüz yerleşimi ve yapısal kararlılık tek başına dominant-negatif mekanizmayı kanıtlamaz.
Net sonuç: Birinci koşul doğru yönde fakat NMD açısından fazla mutlak; ikinci koşul ise “WT ile fiziksel etkileşim” yerine “WT yolak çıktısına aktif trans-interferans” olarak genişletilmelidir. Bu iki özellik gerekli biyolojik zemini sağlar, fakat DN mekanizmasını kanıtlamak için yeterli değildir.

<br>

### C9 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 8. Sık yapılan hatalar · satır 209

> **🟦 Klinikte dikkat kutusu**
> - ***Dominant, ağır, missense-ağırlıklı ve multimerik/kompleks bir protein → dominant-negatifi erken düşün***.
> - Aile içinde aynı varyantın çok değişken ağırlıkta seyrettiği DN tablolarında, modifiye edici etkiler ve doku-spesifik kompleks oranları rol oynayabilir (penetrans/ekspresivite, Bölüm 1).
> - Genetik danışmada DN hastalıklar genellikle **dominant** kalıtım riski (%50 aktarım) taşır; ancak de novo DN varyantlar da sıktır (özellikle ağır/letal formlarda).

**Sorulan:** Bu klinik pusula güvenilir mi, yoksa fazla kestirme mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

Bu kutu **mekanizma hipotezi kurmak için yararlı**, fakat mevcut hâliyle fazla kestirme. Özellikle ilk ve üçüncü cümle düzeltilmeli.

### 1. “Dominant + ağır + missense-ağırlıklı + multimerik → DN” güvenilir mi?

Bu kombinasyon **DN olasılığını artırır**, ancak DN’ye özgü değildir. Aynı desen özellikle **GOF/neomorfik** varyantlarda da görülür. Şiddet de ayırt edici değildir; ağır, erken başlangıçlı dominant hastalıklar HI, GOF veya DN mekanizmasıyla oluşabilir.

DN lehine daha özgül ipuçları şunlardır:

* Protein homomerik veya zorunlu oligomerik kompleks oluşturur.
* Patojenik missense/in-frame varyantlar oligomerizasyon ya da partner bağlanma arayüzlerinde kümelenir.
* Mutant protein tamamen destabilize olmaz; ürün oluşur ve etkileşime katılabilir.
* Null/delesyon varyantları daha hafif veya farklı bir fenotip oluştururken belirli missense varyantlar daha ağırdır.
* Varyantlar gen boyunca dağılmak yerine belirli domain veya üç boyutlu arayüzlerde toplanır.
* WT ve mutantın birlikte ifade edildiği deneyde işlev, yalnızca %50 WT içeren HI kontrolünden daha fazla azalır.

DN missense varyantların protein–protein arayüzlerinde zenginleşmesi ve HI ile ilişkili missense varyantlara göre proteinin monomerik yapısını ortalama olarak daha az destabilize etmesi bu yaklaşımı destekler. Bununla birlikte aynı çalışma, bu özelliklerin varyant düzeyinde DN mekanizmasını tek başına kanıtlamadığını da gösterir. ([Nature][1])

“Kompleks üyesi” ifadesi tek başına zayıftır. Birçok kompleks alt birimi DN değil, **haploinsufficiency** yoluyla hastalık yapar. Ayrıca bazı homomerler kotranslasyonel ve alel-spesifik biçimde monte olur; bu durum WT ve mutant alt birimlerin karışmasını azaltarak DN etkisini tamponlayabilir. Dolayısıyla multimerik yapı gerekli olasılığı yükseltir, fakat yeterli değildir. ([PubMed Central (PMC)][2])

### 2. Aile içi değişkenlik DN lehine midir?

Değişken penetrans ve ekspresivite DN hastalıklarda görülebilir; fakat **DN’ye özgü bir işaret değildir**. Aynı durum HI ve GOF hastalıklarında da yaygındır.

“Doku-spesifik kompleks oranları” ifadesi anlaşılır, ancak daha doğru değişkenler şunlardır:

* mutant:WT transkript veya protein oranı,
* partner alt birimlerin miktarı,
* izoform kullanımı,
* kompleksin montaj yolu,
* mutant ürünün stabilitesi ve lokalizasyonu,
* genetik modifiye ediciler,
* somatik veya parental mozaiklik.

Bu biyolojik değişkenler DN etkinin gücünü değiştirebilir; fakat aile içi değişkenlik gözleminden tek başına DN sonucu çıkarılamaz. Alel-spesifik kompleks montajının bazı DN etkileri tamponlayabilmesi, kompleks mimarisinin basit stokiyometrik hesaplardan daha karmaşık olduğunu gösterir. ([PubMed][3])

### 3. Genetik danışmanlık cümlesi

“DN hastalıklar genellikle dominant kalıtılır” esas olarak doğrudur; çünkü DN, mutant ürünün WT işlevini heterozigot durumda bozmasıdır. Ancak risk iki ayrı düzeyde anlatılmalıdır:

* **Varyant aktarım riski:** Konstitüsyonel heterozigot etkilenmiş bireyin her gebelikte varyantı aktarma olasılığı genellikle `%50`dir.
* **Hastalık geliştirme riski:** `%50 × penetrans` şeklinde düşünülmelidir; cinsiyet, yaş, mozaiklik ve diğer değiştiriciler sonucu etkileyebilir.

De novo saptanan bir varyantta iki farklı danışmanlık sorusu vardır:

1. **Probandın kardeşleri:** Rekürrens çoğunlukla düşüktür, fakat parental gonadal/gonosomal mozaiklik nedeniyle sıfır değildir. DDD kohortunda klinik olarak sağlıklı ebeveynlerde patojenik parental mozaiklik gösterilmiş ve bunun kardeş rekürrens riskini belirgin artırabileceği ortaya konmuştur. ([Nature][4])
2. **Probandın gelecekteki çocukları:** Varyant konstitüsyonel germline ise aktarım olasılığı `%50`dir; varyantın probandda postzigotik mozaik olması hâlinde gonadal tutulum bilinmediğinden risk bireyselleştirilmelidir.

> “De novo DN varyantlar özellikle ağır/letal formlarda sıktır”

ifadesi DN’ye özgü bir kural gibi yazılmamalıdır. De novo varyantların ağır, erken başlangıçlı ve üreme başarısını azaltan **dominant hastalıklarda genel olarak** zenginleşmesi beklenir; bu durum HI ve GOF hastalıkları için de geçerlidir. Büyük pediatrik genomik kohortlarda tanısal de novo varyantların ağır gelişimsel hastalıklarda belirgin ağırlık taşıdığı gösterilmiştir. ([New England Journal of Medicine][5])

## Düzeltilmiş klinik kutu

> **Klinikte dikkat**
>
> **Dominant kalıtım gösteren, missense veya in-frame varyantlarla ilişkili ve homomerik/oligomerik ya da sınırlı ortak partnerlerle çalışan bir proteinde dominant-negatif mekanizmayı erken düşünün; ancak GOF/neomorfik mekanizmayı da aynı anda değerlendirin.** Özellikle patojenik varyantların oligomerizasyon veya partner bağlanma arayüzlerinde kümelenmesi, mutant ürünün stabil kalması ve null varyantlardan farklı bir fenotip oluşturması DN olasılığını artırır. Bu özelliklerin hiçbiri tek başına mekanizmayı kanıtlamaz.
>
> Aile içi değişken penetrans ve ekspresivite; mutant:WT ürün oranı, izoform ve partner ekspresyonu, kompleks montajı, genetik modifiye ediciler ve mozaiklikten etkilenebilir. Ancak değişkenlik DN’ye özgü değildir ve mekanizma çıkarımı için tek başına kullanılmamalıdır.
>
> Konstitüsyonel heterozigot DN varyantlar çoğunlukla otozomal dominant aktarım gösterir; etkilenmiş bireyin varyantı her gebelikte aktarma olasılığı genellikle `%50`dir, fakat fenotip riski penetransa bağlıdır. Görünürde de novo olgularda kardeş rekürrens riski düşük olmakla birlikte parental gonadal/gonosomal mozaiklik nedeniyle sıfır değildir. Probandın gelecekteki çocukları açısından, konstitüsyonel varyant için aktarım olasılığı yine `%50`dir.

**Net sonuç:** Bunu “klinik pusula” olarak kullanabilirsiniz; ancak **tanısal kestirme** olarak kullanamazsınız. En önemli düzeltme, ilk satıra **GOF ayırıcı tanısını** eklemek ve “multimerik protein” gözleminden doğrudan DN sonucuna geçmemektir.

[1]: https://www.nature.com/articles/s41467-022-31686-6 "Loss-of-function, gain-of-function and dominant-negative mutations have profoundly different effects on protein structure | Nature Communications"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10413657/?utm_source=chatgpt.com "Buffering of genetic dominance by allele-specific protein complex assembly - PMC"
[3]: https://pubmed.ncbi.nlm.nih.gov/37256959/?utm_source=chatgpt.com "Buffering of genetic dominance by allele-specific protein complex assembly - PubMed"
[4]: https://www.nature.com/articles/s41467-019-11059-2 "Clinically-relevant postzygotic mosaicism in parents and children with developmental disorders in trio exome sequencing data | Nature Communications"
[5]: https://www.nejm.org/doi/full/10.1056/NEJMoa2209046?utm_source=chatgpt.com "Genomic Diagnosis of Rare Pediatric Disease in the United ..."


<br>

### C10 · Bölüm 6 — Neomorfik ve Antimorfik Alleller

**Yer:** `Bölüm_06_Neomorfik_Antimorfik.md` · 7.3. Toksik kazanım ve bir uyarı · satır 180

> Neomorfik spektrumun bir ucu **toksik kazanımdır**: ürünün zararlı bir fiziksel özellik kazanması. Bunun en bilinen biçimleri, repeat expansion hastalıklarında (poliglutamin → Huntington vb.) mutant proteinlerin yanlış katlanıp **agregat** oluşturmasıdır; bu mekanizma kendi bölümünde (Bölüm 9) ayrıntılı işlenecektir. Burada yalnızca kavramsal yerini işaretliyoruz: ***toksik kazanım da neomorfik gibi "varyant ürünün zararlı varlığından" doğar, dolayısıyla dominanttır*** ve basit LoF değildir. ⚠️ Belirli bir genin neomorfik/toksik mekanizma yaptığı iddiası, her zaman güncel ve gen-spesifik (tercihen VCEP/ClinGen) kaynakla doğrulanmalıdır; bazı genlerde mekanizma varyanta veya bağlama göre değişir.

**Sorulan:** Toksik kazanımın neomorfikle bu şekilde yan yana konması kavramsal olarak doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Kısmen doğru. Toksik işlev kazanımı ile neomorfik etki önemli ölçüde örtüşür; ancak bunlar eş anlamlı değildir ve “aynı spektrumun iki ucu” şeklinde doğrusal bir ilişki kurmak doğru olmaz.**

En doğru kavramsal ayrım şudur:

* **Neomorfik etki**, mutant ürünün WT üründe bulunmayan niteliksel olarak yeni bir işlev, etkileşim, lokalizasyon veya ifade paterni kazanmasını tanımlar.
* **Toksik işlev kazanımı**, mutant ürünün varlığının hücreye zarar verdiğini tanımlar.

Dolayısıyla neomorfi, **işlevde neyin değiştiğini**; toksik kazanım ise **bu değişikliğin patolojik sonucunu** tarif eder.

## Kavramların ilişkisi

| Mekanizma            | Esas değişiklik                                                    | Toksik olabilir mi?                    |
| -------------------- | ------------------------------------------------------------------ | -------------------------------------- |
| **Hipermorfik GoF**  | Normal işlevin miktarı/aktivitesi artar                            | Evet                                   |
| **Neomorfik GoF**    | Yeni işlev, etkileşim, lokalizasyon veya substrat özgüllüğü oluşur | Evet veya hayır                        |
| **Toksik GoF**       | Mutant ürünün kazanılmış/artmış özelliği hücreye zarar verir       | Tanım gereği evet                      |
| **Dominant-negatif** | Mutant ürün WT işlevine aktif olarak müdahale eder                 | Evet; fakat neomorfizmle aynı değildir |

Bu nedenle:

[
\text{Toksik GoF} \cap \text{Neomorfizm} \neq \varnothing
]

ancak:

[
\text{Toksik GoF} \neq \text{Neomorfizm}
]

Yeni bir agregasyon, anormal kendiliğinden birleşme, yeni bir protein partnerine bağlanma veya yeni hücresel kompartımana birikme özelliği kazanılmışsa toksik mekanizma **neomorfik GoF** olarak tanımlanabilir. Buna karşılık normal bir enzimatik ya da sinyal işlevinin aşırı aktivitesi toksik sonuç oluşturuyorsa bu daha çok **hipermorfik toksik GoF** olur. GenCC’nin 2025 taslak GoF çerçevesi de yeni işlev, yeni doku veya zamanda ekspresyon, yanlış lokalizasyon ve yeni hücresel bölgede birikme gibi farklı moleküler sonuçları GoF kapsamında ele alır. ([ClinGen][1])

## “Varyant ürünün zararlı varlığı” ifadesinin sınırı

Bu ifade sezgisel olarak yararlıdır; fakat toksik GoF’ye özgü değildir. Mutant ürünün zararlı biçimde mevcut olduğu mekanizmalar arasında şunlar bulunabilir:

* neomorfik toksisite,
* hipermorfik toksisite,
* dominant-negatif etki,
* toksik RNA kazanımı,
* RAN translasyonuyla oluşan toksik peptitler,
* anormal partner veya kofaktör sekestrasyonu.

Bu nedenle bölümde ana karşıtlığı şöyle kurmak daha doğru olur:

> **Basit LoF’da sorun işlevsel ürünün eksikliğidir; ürün-bağımlı toksik mekanizmalarda ise mutant ürünün oluşması ve zararlı moleküler özellik göstermesi patogenezin gerekli parçasıdır.**

Ancak “ürün varsa neomorfiktir” denemez. DN varyantta da mutant ürün gereklidir; fakat yeni bir bağımsız işlev kazanmak yerine WT işlevini engeller.

## PolyQ hastalıkları için anlatım düzeltilmeli

Huntington hastalığında genişlemiş polyQ dizisi, huntingtin proteininin konformasyonunu, kendiliğinden birleşmesini ve etkileşim ağını değiştirerek toksik bir işlev kazanımına yol açar. Bu mekanizma niteliksel olarak yeni fiziksel özellikler içerdiği için **neomorfik toksik GoF** olarak anlatılabilir.

Fakat:

> “Mutant protein yanlış katlanır, agregat oluşturur ve agregat hücreyi öldürür.”

şeklindeki düz zincir fazla basittir.

Expanded huntingtin;

* çözünür monomerik ve oligomerik türler,
* proteolitik fragmanlar,
* anormal protein etkileşimleri,
* proteostaz, transkripsiyon ve hücresel taşıma bozuklukları,
* farklı büyüklüklerde agregatlar ve inklüzyonlar

oluşturabilir. Büyük inklüzyonların her zaman doğrudan toksik olmadığı; bazı deneylerde yaygın çözünür mutant huntingtin düzeyini azaltarak hücre sağkalımıyla ilişkili olduğu gösterilmiştir. Bu nedenle “agregasyon eğilimi” mekanizmanın parçasıdır, fakat görünür agregatların tek toksik tür olduğu söylenmemelidir. ([PubMed][2])

Daha güvenli ifade:

> **Kodlanan CAG/polyQ genişlemelerinde mutant protein yeni konformasyonel ve etkileşimsel özellikler kazanır; çözünür oligomerler, anormal protein etkileşimleri ve agregasyon/proteostaz bozukluğu birlikte toksik GoF oluşturabilir.**

Ayrıca “repeat expansion hastalıkları” genellenmemelidir. Repeat genişlemeleri mekanizma bakımından heterojendir:

* **HTT ve bazı ataksiler:** toksik polyQ protein kazanımı
* **DM1:** genişlemiş CUG RNA aracılı toksik GoF ve RNA bağlayıcı proteinlerin sekestrasyonu
* **FMR1 tam mutasyonu:** metilasyon ve transkripsiyonel susturma yoluyla LoF
* Bazı hastalıklar: RNA toksisitesi, RAN translasyonu ve LoF’un birlikte katkısı

DM1’de genişlemiş CUG RNA’nın MBNL proteinlerini bağlayarak RNA işlenmesini bozması doğrudan gösterilmiş; FMR1 tam mutasyonunda ise tekrar bölgesinin demetilasyonu gen ekspresyonunu yeniden aktive ederek susturma/LoF modelini desteklemiştir. ([ScienceDirect][3])

## “Dolayısıyla dominanttır” çıkarımı yapılmamalı

Bu cümle mekanizma ile kalıtım biçimini birbirine bağlayarak fazla kesinleşiyor:

> “Mutant ürünün zararlı varlığından doğar, dolayısıyla dominanttır.”

Ürün-bağımlı toksik mekanizmalar **sıklıkla dominant fenotip oluşturur**, çünkü tek mutant alelin ürettiği ürün toksisite eşiğini aşabilir. Fakat dominans otomatik bir moleküler sonuç değildir. Şunlara bağlıdır:

* mutant ürün miktarı,
* toksisite eşiği,
* WT ve mutant alel oranı,
* doku ve cinsiyet bağlamı,
* hücresel temizleme kapasitesi,
* yaş ve gelişimsel zamanlama.

Bu nedenle:

> **“Toksik GoF genellikle dominant kalıtımla ilişkilidir”**

denebilir; fakat:

> **“Toksik GoF olduğu için dominanttır”**

denmemelidir.

## Kaynak uyarısı nasıl yazılmalı?

“Tercihen VCEP/ClinGen” doğru yönde, fakat VCEP tek başına yeterli bir kaynak hiyerarşisi değildir. Her gen için VCEP bulunmaz ve VCEP’nin ana görevi varyant sınıflandırmasıdır. Mekanizma için şu sıra kullanılmalıdır:

1. Güncel ClinGen GCEP veya GenCC mekanizma kürasyonu varsa kontrol edilmesi
2. Gen/hastalık için VCEP spesifikasyonu varsa kullanılması
3. Varyant-spesifik fonksiyonel çalışmaların incelenmesi
4. Null, knock-in ve WT–mutant karşılaştırmalı modellerin değerlendirilmesi

GenCC’nin GoF mekanizma çerçevesi Eylül 2025 itibarıyla hâlâ taslak durumdadır. ClinGen’in 2026 gene-validity yazım rehberi de yalnızca “GoF/LoF” etiketi vermek yerine, mümkün olduğunda protein birikmesi, yeni lokalizasyon veya hücre ölümüne yol açan işlevsel değişiklik gibi gerçek biyolojik disfonksiyonun doğrudan tarif edilmesini önerir. ([ClinGen][4])

## Düzeltilmiş metin

> **Neomorfik işlev kazanımının patolojik sonuçlarından biri toksik kazanımdır.** Mutant ürün, WT proteinde bulunmayan yeni bir konformasyon, kendiliğinden birleşme özelliği, etkileşim, lokalizasyon veya substrat özgüllüğü kazanır ve bu yeni özellik hücreye zarar verirse mekanizma neomorfik toksik GoF olarak tanımlanabilir. Bununla birlikte toksik GoF ile neomorfizm eş anlamlı değildir: normal işlevin aşırı artması da toksik olabilir; neomorfik bir işlev ise mutlaka toksik olmak zorunda değildir.
>
> Kodlanan CAG/polyglutamin genişlemeleri bu örtüşmenin bilinen örneklerindendir. Huntington hastalığında genişlemiş polyQ dizisi huntingtin proteininin konformasyonunu, protein etkileşimlerini ve kendiliğinden birleşme eğilimini değiştirir. Çözünür oligomerler, anormal etkileşimler ve proteostaz bozukluğu toksisiteye katkıda bulunabilir; büyük inklüzyonların kendisi her zaman başlıca toksik tür değildir. Ayrıca repeat genişlemeleri tek bir mekanizma oluşturmaz: bazıları toksik protein, bazıları toksik RNA, bazıları gen susturulmasıyla LoF, bazıları ise birleşik mekanizmalar üzerinden hastalık yapar.
>
> Ürün-bağımlı toksik mekanizmalar sıklıkla dominant kalıtımla ilişkilidir; ancak toksik özellik dominansı otomatik olarak belirlemez. Belirli bir gen–hastalık ilişkisinde neomorfik veya toksik GoF iddiası güncel hastalık-spesifik kürasyonlar ve varyant düzeyindeki fonksiyonel çalışmalarla doğrulanmalıdır.

**Net sonuç:** Toksik GoF’yi neomorfizmin zorunlu bir “ucu” olarak değil, **neomorfizmle kesişebilen ayrı bir mekanistik tanım** olarak yerleştirin.

[1]: https://clinicalgenome.org/docs/draft-gain-of-function-mechanism-of-pathogenicity-framework/ "DRAFT GOF framework position statement"
[2]: https://pubmed.ncbi.nlm.nih.gov/15483602/?utm_source=chatgpt.com "Inclusion body formation reduces levels of mutant ..."
[3]: https://www.sciencedirect.com/science/article/pii/S2211124725003535?utm_source=chatgpt.com "Article DM1 repeat-expanded RNAs confer RNA toxicity as ..."
[4]: https://clinicalgenome.org/working-groups/gencc-mechanism-curation/ "GenCC Mechanism Curation - ClinGen | Clinical Genome Resource"


<br>

### C11 · Bölüm 7 — Splicing (Kırpılma) Varyantları

**Yer:** `Bölüm_07_Splicing.md` · 3. Varyant tipleri · satır 71

> ***| Varyant tipi (yer) | Tipik splicing sonucu |*** Notlar / ilgili bölüm |
> |---|---|---|
> | **Kanonik ±1/±2 (GT…AG)** | Ekzon atlama veya intron tutulması | En öngörülebilir; PVS1 (splice) zemini (§6) |
> | **Splice bölgesi ±3…±6** | Değişken; zayıflamış tanıma | Öngörü + RNA kanıtı gerekir |
> | **Dallanma noktası / polipirimidin** | Ekzon atlama (çoğunlukla) | İntronik ama kritik |
> | **Ekzonik ESE/ESS (sessiz veya missense)** | Ekzon atlama (örn. SMN2 ekzon 7) | "Sessiz patojen"; missense'in ikinci yüzü |
> | **Derin intronik** | Sözde-ekzon eklenmesi / kriptik bölge | Standart panelde gözden kaçar; WGS + SpliceAI |
> | **Çerçeveye etki** | Out-of-frame → NMD/LoF · in-frame → DN/GoF olabilir | §2.1; Bölüm 2, 5, 6 |

**Sorulan:** Varyant tipi → tipik splicing sonucu tablosunun tüm satırları doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Tablonun temel yönü doğru, fakat hiçbir satır mevcut biçimiyle tam güvenli değil.** En ciddi sorunlar şunlar:

* Kanonik splice varyantları yalnız ekzon atlama veya intron tutulması yapmaz.
* “±3…±6 splice bölgesi” donor ve acceptor için simetrik bir tanım değildir.
* ESE ve ESS değişiklikleri aynı sonucu oluşturmaz.
* “Çerçeveye etki” bir varyant konumu değil, RNA sonucunun protein düzeyindeki devamıdır.
* Kanonik splice pozisyonu tek başına otomatik PVS1 anlamına gelmez.

ClinGen’in güncel varyant sınıflandırma sayfası, 2023 SVI Splicing Subgroup önerilerini hâlen temel splice-yorumlama rehberi olarak göstermektedir. ([ClinGen][1])

## Satırların tek tek denetimi

### 1. Kanonik ±1/±2

Mevcut satır:

> **Kanonik ±1/±2 (GT…AG)** → Ekzon atlama veya intron tutulması

**Eksik.**

Daha kesin terminoloji:

* Donor splice site: intronik `+1/+2`
* Acceptor splice site: intronik `−2/−1`

“±1/±2” pratik kısaltmadır; fakat donor ve acceptor yönlerini bulanıklaştırır. İnsan intronlarının çoğu GT–AG mimarisindedir, ancak nadir non-kanonik intronlar da vardır.

Kanonik splice bölgesinin bozulması şu sonuçlardan herhangi birini oluşturabilir:

* tam ekzon atlama,
* tam veya kısmi intron tutulması,
* intronik kriptik splice bölgesinin kullanılması,
* ekzon içindeki kriptik bölgenin kullanılması ve ekzonun bir kısmının kaybı,
* intronik dizinin bir kısmının ekzona eklenmesi,
* birden fazla anormal transkriptin birlikte oluşması.

Kanonik splice varyantları sık olarak ekzon atlamaya yol açsa da RNA sonucu varyant konumundan tek başına kesinleştirilemez. ([PubMed][2])

Ayrıca:

[
\text{kanonik splice varyantı}\not\Rightarrow\text{otomatik PVS1}
]

PVS1 için:

1. İlgili gen–hastalık ilişkisinde LoF yerleşik mekanizma olmalı.
2. Beklenen splice sonucunun NMD oluşturup oluşturmayacağı değerlendirilmelidir.
3. İn-frame ekzon kaybında kaybolan bölgenin işlevsel önemi incelenmelidir.
4. Hastalıkla ilişkili transkript ve alternatif izoformlar dikkate alınmalıdır.

Bazı gen-spesifik VCEP kuralları kanonik splice varyantlarında RNA analizi olmadan PVS1 kullanımına izin verir; ancak kriter gücü öngörülen transkript sonucuna göre değişir. ([erepo.clinicalgenome.org][3])

### 2. “Splice bölgesi ±3…±6”

Bu tanım **fazla kaba ve acceptor tarafı için hatalıdır.**

`+3…+6`, özellikle **5′ donor bölgesinin uzatılmış konsensüsü** için kullanılabilecek bir aralıktır. Acceptor tarafı ise aynı şekilde `−3…−6` ile sınırlandırılamaz. Acceptor tanınması şunları kapsar:

* `−3` pozisyonu,
* polipirimidin traktı,
* branchpoint,
* branchpoint ile acceptor arasındaki AG-exclusion zone,
* acceptor çevresindeki daha geniş intronik bağlam.

Yakın intronik donor varyantlarının mekanizması çoğunlukla splice-site zayıflaması iken, acceptor tarafındaki mekanizmalar daha heterojendir. Acceptor çevresinde yeni AG oluşturulması bile kriptik acceptor kullanımı, ekzon atlama veya intron tutulması oluşturabilir. ([PubMed][4])

> “Öngörü + RNA kanıtı gerekir”

ifadesi de mutlak yazılmamalıdır.

Daha doğrusu:

> **Kalibre edilmiş splice tahmin araçlarıyla değerlendirme gerekir; RNA kanıtı, özellikle non-kanonik varyantlarda sonucu ve anormal transkript oranını belirlemek için güçlü biçimde tercih edilir.**

RNA analizi her sınıflandırmada zorunlu değildir; gen-spesifik VCEP kuralları ve diğer kanıtlar yeterli olabilir. ClinGen, tahmin ve gözlenen RNA sonuçlarının ayrı kanıt kodları ve uygun güçlerle değerlendirilmesini önerir. ([PubMed][5])

### 3. Dallanma noktası / polipirimidin traktı

Mevcut sonuç:

> Ekzon atlama, çoğunlukla

**Yön olarak doğru ama fazla dar.**

Branchpoint veya polipirimidin traktı bozuklukları şunlara yol açabilir:

* ekzon atlama,
* tam veya kısmi intron tutulması,
* alternatif branchpoint kullanımı,
* kriptik acceptor aktivasyonu,
* birden fazla anormal izoform.

Deneysel branchpoint varyantlarında hem ekzon atlama hem intron tutulması gösterilmiştir. Branchpointler ayrıca tek ve sabit olmayabilir; aynı intron birden fazla alternatif branchpoint kullanabilir. Bu nedenle yalnız genomik konuma bakarak sonuç tahmini zordur. ([PubMed][6])

“İntronik ama kritik” notu doğrudur; ancak **kritikliği varyant bazında doğrulanmalıdır**.

### 4. Ekzonik ESE/ESS

Mevcut satır:

> ESE/ESS → Ekzon atlama

**Bu biçimde yanlış.**

ESE ve ESS zıt yönde çalışan düzenleyici elemanlardır:

* **ESE bozulması** → ekzon tanınması azalabilir → ekzon atlama artabilir.
* **Yeni ESS oluşması** → ekzon atlama artabilir.
* **ESS bozulması** → baskı kalkabilir → ekzon inklüzyonu artabilir.
* Ekzonik varyant yeni donor/acceptor oluşturursa ekzonun bir bölümünün çıkarılması veya intronik dizinin eklenmesi görülebilir.

Dolayısıyla satır yalnız “ekzon atlama” ile sınırlandırılmamalıdır. Ekzonik sinonim ve missense varyantların intron tutulması da oluşturabildiği gösterilmiştir. ([PubMed][7])

SMN2 örneği öğreticidir, ancak doğru anlatılmalıdır. SMN1–SMN2 arasındaki ekzon 7 `C>T` farkı translasyon açısından sinonimdir ve ekzon 7 inklüzyonunu azaltır. Mekanizma, ESE kaybı ve/veya ESS oluşumu modelleriyle açıklanmıştır. Fakat bu, standart anlamda “bir hastada saptanmış patojenik sinonim varyant” örneğinden çok, **paralog-spesifik alternatif splicing düzenlenmesi** örneğidir. ([PubMed Central (PMC)][8])

“Sessiz patojen” ifadesini kullanmayın. Doğru terim:

> **Splice-altering sinonim varyant**

### 5. Derin intronik varyant

Mevcut satır:

> Sözde-ekzon eklenmesi / kriptik bölge

**Ana sonuç doğru, fakat kapsam eksik.**

Derin intronik varyantların en klasik sonucu:

* kriptik donor veya acceptor aktivasyonu,
* pseudoekzon inklüzyonu

olmakla birlikte şunlar da oluşabilir:

* kısmi intron tutulması,
* tam intron tutulması,
* mevcut bir kriptik splice bölgesinin güçlenmesi,
* intronik enhancer/silencer bozulması,
* doğal ekzonların atlanması.

Derin intronik hastalık varyantlarında pseudoekzonizasyon en sık bildirilen mekanizmalardandır; ancak tek mekanizma değildir. ([PubMed][9])

> “WGS + SpliceAI”

aday bulmak için uygundur, fakat sonuç kanıtı değildir. Daha doğru not:

> **WES ve standart hedef paneller yakalama tasarımına bağlı olarak kaçırabilir. WGS ve splice-prediction araçları adayı belirleyebilir; patojenik RNA sonucunun tercihen ilgili dokuda RNA analiziyle doğrulanması gerekir.**

SpliceAI skoru tek başına hangi anormal transkriptin oluşacağını veya transkript oranını kesin olarak göstermez.

### 6. “Çerçeveye etki”

Bu satır aynı tabloda bulunmamalıdır. Çünkü:

> **Out-of-frame veya in-frame olmak varyantın yeri değil, oluşan RNA ürününün protein-kodlama sonucudur.**

Ayrı bir “anormal transkriptin sonucu” tablosuna taşınmalıdır.

Ayrıca mevcut formül fazla basit:

> Out-of-frame → NMD/LoF
> In-frame → DN/GoF olabilir

Daha doğru çerçeve:

| RNA sonucu                            | Olası moleküler sonuç                                                                    |
| ------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Out-of-frame**                      | PTC oluşabilir; NMD, NMD’den kaçan kesilmiş protein, hipomorfik etki veya nadiren DN/GoF |
| **In-frame ekzon/sekans kaybı**       | LoF, hipomorfik etki, DN, GoF veya klinik olarak önemsiz sonuç                           |
| **İn-frame intronik ekleme**          | Yeni aminoasitler, protein kararsızlığı, domain bozukluğu veya yeni işlev                |
| **Kısmi normal transkript korunması** | Etki anormal/normal transkript oranına bağlı; hipomorfik fenotip mümkün                  |

İn-frame sonuç otomatik olarak DN/GoF değildir. İşlevsel domainin kaybı veya protein kararsızlığı nedeniyle basit LoF da oluşturabilir.

---

## Düzeltilmiş tablo

| Varyant konumu/mekanizması                                                    | Olası splicing sonuçları                                                                                | Klinik yorum notu                                                                                                                  |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Kanonik donor `+1/+2`; acceptor `−2/−1`**                                   | Tam/kısmi ekzon atlama, intron tutulması, kriptik donor/acceptor kullanımı, kısmi intronik ekleme       | LoF mekanizması ve öngörülen transkript sonucu uygunsa PVS1 karar ağacı uygulanır; kanonik konum tek başına otomatik PVS1 değildir |
| **Uzatılmış donor bölgesi, özellikle `+3…+6`**                                | Doğal donorun zayıflaması; ekzon atlama, intron tutulması veya kriptik donor kullanımı                  | Kalibre edilmiş prediction gerekir; RNA analizi özellikle sınıflandırıcı olabilir                                                  |
| **Uzatılmış acceptor bölgesi: `−3`, polipirimidin traktı, AG-exclusion zone** | Ekzon atlama, intron tutulması, yeni/kriptik acceptor kullanımı                                         | Donor tarafıyla simetrik bir `−3…−6` modeli kullanılmamalıdır                                                                      |
| **Branchpoint**                                                               | Ekzon atlama, intron tutulması, alternatif branchpoint veya kriptik acceptor kullanımı                  | Birden fazla branchpoint bulunabilir; tahmin belirsizliği yüksektir                                                                |
| **Ekzonik ESE/ESS veya yeni splice-site oluşumu**                             | Ekzon inklüzyonunun azalması veya artması, tam/kısmi ekzon atlama, intron tutulması                     | Sinonim veya missense olabilir; protein etkisi ile splice etkisi ayrı değerlendirilmelidir                                         |
| **Derin intronik**                                                            | Pseudoekzon inklüzyonu, kriptik splice-site aktivasyonu, kısmi/tam intron tutulması, doğal ekzon atlama | WGS + prediction aday bulur; uygun RNA doğrulaması güçlü biçimde tercih edilir                                                     |
| **RNA ürününün çerçeve etkisi**                                               | Out-of-frame veya in-frame anormal transkript                                                           | Ayrı bir downstream-sonuç basamağıdır; NMD, domain kaybı, rezidüel transkript oranı ve NMD escape birlikte değerlendirilmelidir    |

## Sonuç

Tablo korunabilir; ancak:

1. `±1/±2` yerine donor ve acceptor yönlerini ayrı yazın.
2. `±3…±6` satırını donor ve acceptor olarak ayırın.
3. ESE ile ESS’yi aynı yönde göstermeyin.
4. Derin intronik sonucu pseudoekzonla sınırlamayın.
5. “Çerçeveye etki” satırını ayrı bir sonuç tablosuna taşıyın.
6. PVS1’i varyant konumuna değil, **gen–hastalık mekanizması ve beklenen RNA/protein sonucuna** bağlayın.

[1]: https://clinicalgenome.org/tools/clingen-variant-classification-guidance/?utm_source=chatgpt.com "ClinGen Variant Classification Guidance"
[2]: https://pubmed.ncbi.nlm.nih.gov/30904096/?utm_source=chatgpt.com "Understanding human DNA variants affecting pre-mRNA splicing in the NGS era - PubMed"
[3]: https://erepo.clinicalgenome.org/cspec/ui/svi/doc/1568416522?utm_source=chatgpt.com "BMPR2 - Criteria Specification Registry"
[4]: https://pubmed.ncbi.nlm.nih.gov/35847480/?utm_source=chatgpt.com "Prevalence, parameters, and pathogenic mechanisms for splice-altering acceptor variants that disrupt the AG exclusion zone - PubMed"
[5]: https://pubmed.ncbi.nlm.nih.gov/37352859/?utm_source=chatgpt.com "Recommendations from the ClinGen SVI Splicing Subgroup"
[6]: https://pubmed.ncbi.nlm.nih.gov/16835862/?utm_source=chatgpt.com "Phenotypic consequences of branch point substitutions - PubMed"
[7]: https://pubmed.ncbi.nlm.nih.gov/29680930/?utm_source=chatgpt.com "Splicing mutations in human genetic disorders: examples, detection, and confirmation - PubMed"
[8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1380224/?utm_source=chatgpt.com "Determinants of Exon 7 Splicing in the Spinal Muscular ... - PMC"
[9]: https://pubmed.ncbi.nlm.nih.gov/28497172/?utm_source=chatgpt.com "Deep intronic mutations and human disease - PubMed"


<br>

### C12 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 2.1 İmprint nasıl kurulur ve okunur? · satır 56

> ***Metilasyonun aleli her zaman doğrudan susturmadığını vurgulamak gerekir; kimi ICR'ler bir izolatör (insulator) üzerinden çalışır***. Bunun ders kitabı örneği, bu bölümün ilerleyen kısmında Beckwith-Wiedemann ve Silver-Russell sendromları bağlamında ayrıntılandıracağımız 11p15.5'teki *IGF2/H19* bölgesidir. Burada ICR1, metilsiz maternal alelde CTCF proteinini bağlayarak bir izolatör kurar; bu izolatör, ortak enhancer'ların *IGF2*'ye ulaşmasını engeller, dolayısıyla maternal alelde *H19* ifade edilir, *IGF2* susar. Paternal alelde ise ICR1 metilidir, CTCF bağlanamaz, izolatör kurulamaz ve enhancer'lar *IGF2*'yi çalıştırır. Böylece **aynı metilasyon işareti**, bağlamına göre bir geni açar (*IGF2*, paternal) başka birini kapatır (*H19*, paternal) — imprintin "tek şalter, çift sonuç" mantığı budur.

**Sorulan:** İzolatör mekanizması (H19/IGF2, CTCF) doğru anlatılmış mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Mekanizma ana hatlarıyla doğru anlatılmıştır.** Ancak iki nokta düzeltilmelidir:

1. **IC1 metilasyonu `IGF2`’yi doğrudan açmaz**; CTCF bağlanmasını ve izolatör işlevini ortadan kaldırarak enhancer–`IGF2` etkileşimine izin verir.
2. Paternal `H19` susturulması yalnızca “izolatörün kurulmaması” ile açıklanmaz; paternal kromozomda `H19` promotörü ve çevresindeki baskılayıcı epigenetik durum da önemlidir.

Bu nedenle “aynı metilasyon işareti bir geni açar, diğerini kapatır” öğretici bir özet olsa da **doğrudanlık izlenimi vermemelidir**.

---

## Adım adım doğruluk denetimi

### Maternal alel

Şu anlatım doğrudur:

> ICR1 metilsizdir → CTCF bağlanır → izolatör oluşur → enhancer’ların `IGF2` promotörlerine erişimi engellenir → `IGF2` baskılanır.

IC1, güncel klinik terminolojide **`H19/IGF2:IG-DMR`** olarak da adlandırılır. Maternal alelde metilsizdir ve CTCF yalnızca bu metilsiz alele bağlanarak downstream enhancer’ların `IGF2` promotörleriyle etkileşmesini sınırlar. `H19` maternal alelden ifade edilir. ([NCBI][1])

Ancak “CTCF fiziksel olarak enhancer’ın önüne duvar örer” anlatımı fazla mekanik olabilir. Güncel modelde CTCF:

* enhancer–promotör temaslarını sınırlar,
* alele özgü kromatin loop’ları oluşturur,
* cohesin ve diğer kromatin düzenleyicileriyle üç boyutlu genom mimarisini düzenler.

Dolayısıyla **izolatör**, basit bir doğrusal engelden çok alele özgü kromatin organizasyonudur. ([PubMed Central (PMC)][2])

### Paternal alel

Bu bölüm de temelde doğrudur:

> ICR1 metillidir → CTCF bağlanamaz → izolatör işlevi kaybolur → downstream enhancer’lar `IGF2` promotörleriyle etkileşebilir → paternal `IGF2` ifade edilir.

Paternal IC1 metilasyonu, CTCF bağlanmasını engeller ve enhancer’ların `IGF2` promotörlerine erişmesine izin verir. ([PubMed Central (PMC)][3])

Ancak şu bağlantı eksiktir:

> “İzolatör kurulamaz, dolayısıyla `H19` susar.”

`H19`’un susturulması yalnızca izolatör kaybının pasif sonucu değildir. Paternal alelde `H19` promotörü gelişim sırasında metilasyon ve baskılayıcı kromatin kazanır; bu nedenle enhancer’lar paternal `H19` promotörünü etkinleştirmez ve bunun yerine `IGF2` ile etkileşir. ([PubMed Central (PMC)][4])

---

## “Aynı metilasyon işareti bir geni açar, diğerini kapatır” doğru mu?

**Sonuç düzeyinde doğru, mekanizma düzeyinde sadeleştirilmiştir.**

Paternal IC1 metilasyon durumu:

* `IGF2` açısından **dolaylı olarak aktive edicidir**: CTCF izolatörünü kaldırır.
* `H19` açısından **susturucu epigenetik durumla ilişkilidir**: `H19` promotörü ve lokusu baskılanır.

Dolayısıyla şu ifade:

> “Metilasyon `IGF2`’yi açar.”

yerine:

> **“IC1 metilasyonu, CTCF-bağımlı izolasyonu kaldırarak `IGF2`’nin enhancer’lara erişmesine izin verir.”**

denmelidir.

Benzer şekilde:

> “Aynı metilasyon işareti `H19`’u kapatır.”

ifadesi de:

> **“Paternal IC1 metilasyon durumu, `H19` promotörünün metilasyonu ve baskılanmasıyla birlikte `H19` ekspresyonunu susturur.”**

şeklinde yazılmalıdır.

Burada “tek şalter, çift sonuç” benzetmesi kullanılabilir; ancak bunun **bir cis-düzenleyici merkez aracılığıyla iki genin karşılıklı ekspresyonunun koordine edilmesini** anlattığı belirtilmelidir.

---

## Hastalıklarla bağlantısı da modeli doğrular

Bu karşılıklı düzenleme, 11p15.5 imprinting bozukluklarının zıt büyüme fenotiplerini açıklar:

* **Maternal IC1 metilasyon kazanımı:** maternal alel paternalize olur; CTCF bağlanması kaybolur, `IGF2` ekspresyonu artar ve BWS yönünde aşırı büyüme ortaya çıkabilir.
* **Paternal IC1 metilasyon kaybı:** paternal alel maternalize olur; CTCF bağlanması kazanılır, paternal `IGF2` ekspresyonu azalır ve SRS yönünde büyüme kısıtlılığı ortaya çıkabilir. ([NCBI][1])

Bu örnek, metilasyonun her zaman “yakınındaki geni susturan basit bir kapatma etiketi” olmadığını çok iyi gösterir.

---

## Düzeltilmiş metin

> **Metilasyonun bir aleli her zaman doğrudan susturmadığını vurgulamak gerekir; bazı imprinting kontrol bölgeleri metilasyona duyarlı bir izolatör mekanizması üzerinden çalışır. Bunun klasik örneği, 11p15.5’teki `IGF2/H19` bölgesidir. Bu bölgedeki imprinting kontrol merkezi IC1 — güncel adlandırmayla `H19/IGF2:IG-DMR` — maternal alelde metilsizdir. Metilsiz IC1’e CTCF bağlanır ve alele özgü bir kromatin sınırı oluşturur. Bu düzenleme, `H19`’un downstream’inde bulunan enhancer’ların maternal `IGF2` promotörleriyle etkileşmesini engeller; böylece maternal alelde `IGF2` baskılanırken `H19` ifade edilir.**
>
> **Paternal alelde IC1 metillidir. Metilasyon CTCF bağlanmasını engellediği için izolatör işlevi kurulamaz ve enhancer’lar paternal `IGF2` promotörleriyle etkileşebilir. Aynı paternal epigenetik bağlamda `H19` promotörü de metillenerek susturulur. Bu nedenle IC1’in alele özgü metilasyon durumu iki genin karşılıklı ekspresyonunu koordine eder: paternal alelde `IGF2` açık, `H19` kapalı; maternal alelde ise `H19` açık, `IGF2` kapalıdır.**
>
> **Bu örnek, DNA metilasyonunun etkisinin genomik bağlama bağlı olduğunu gösterir. IC1 metilasyonu `IGF2`’yi doğrudan aktive etmez; CTCF-bağımlı izolasyonu kaldırarak enhancer erişimine izin verir. Dolayısıyla burada tek bir cis-düzenleyici şalter, iki gen üzerinde karşılıklı sonuç oluşturur.**

## Net düzeltme

“Tek şalter, çift sonuç” ifadesi korunabilir. Ancak:

> **“Aynı metilasyon işareti `IGF2`’yi açar ve `H19`’u kapatır”**

yerine:

> **“IC1’in paternal metilasyon durumu, CTCF-bağımlı izolasyonu kaldırarak `IGF2` ekspresyonuna izin verir ve `H19`’un susturulduğu epigenetik durumu destekler.”**

yazılması mekanistik olarak daha doğrudur.

[1]: https://www.ncbi.nlm.nih.gov/books/NBK1394/ "Beckwith-Wiedemann Syndrome - GeneReviews® - NCBI Bookshelf"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3471092/?utm_source=chatgpt.com "More than insulator: multiple roles of CTCF at the H19-Igf2 ..."
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10482337/?utm_source=chatgpt.com "Establishment of paternal methylation imprint at the H19/Igf2 ..."
[4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8330897/?utm_source=chatgpt.com "The number of the CTCF binding sites of the H19/IGF2:IG ..."


<br>

### C13 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 2.3 Uniparental dizomi nasıl oluşur? · satır 74

> **🔬 Deep-dive — İzodizomi neden iki ayrı yolla hastalık yapar?** ***UPD'nin iki ayrı patojenik yüzü vardır*** ve bunları karıştırmamak gerekir. **(1) İmprint dengesizliği:** UPD imprintli bir kromozomu tutuyorsa (15, 11, 7, 14, 6, 20…), her iki kopyanın tek ebeveynden gelmesi imprint dozunu bozar — bu yolla PWS, AS, SRS ve TNDM oluşur. Bu yol için izo/hetero ayrımı önemli değildir; önemli olan ebeveyn kökenidir. **(2) Resesif varyantın homozigotlaşması:** İzodizomi, tek bir homoloğun özdeş kopyası olduğu için, o homologdaki her varyant **homozigot** hâle gelir. Anne bir resesif hastalık için taşıyıcıysa (heterozigot) ve çocuk o kromozomun izodizomisini taşıyorsa, çocuk **baba hiç taşıyıcı olmadığı hâlde** resesif hastalığı homozigot olarak sergileyebilir. Bu, bir çocukta beklenmedik (ebeveyn taşıyıcılığıyla açıklanamayan) resesif bir hastalık görüldüğünde neden UPD'nin akla gelmesi gerektiğini açıklar. Heterodizomi ise iki farklı homolog içerdiği için bu maskeleme etkisini yaratmaz — ancak trizomi kurtarma sonrası mayotik rekombinasyon nedeniyle sıklıkla parçalı izodizomi segmentleri de barındırabilir.

**Sorulan:** İzodizominin iki mekanizması (imprint dengesizliği + resesif varyantın homozigotlaşması) doğru ayrılmış mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**İki temel patojenik mekanizma doğru ayrılmıştır.** Ancak başlık ve bazı mutlak ifadeler düzeltilmelidir:

> **İmprinting bozukluğu izodizomiye özgü değildir; hem izodizomi hem heterodizomi bunu yapabilir.**
> **Resesif alelin homozigotlaşması ise izodizomik bölgeye özgüdür.**

Bu nedenle başlık:

> **“UPD neden iki temel yolla hastalık yapar?”**

olmalıdır. “İzodizomi neden iki ayrı yolla…” başlığı, imprinting mekanizmasını yanlışlıkla izodizomiye özgüymüş gibi gösterebilir.

---

## 1. İmprint dengesizliği doğru anlatılmış mı?

Evet. Bir UPD, klinik olarak anlamlı bir imprinting bölgesini içeriyorsa iki kromozom kopyasının da aynı ebeveyn kökenine sahip olması, normalde bulunması gereken maternal–paternal epigenetik tamamlayıcılığı ortadan kaldırır. Bu mekanizma açısından belirleyici olan:

* UPD’nin maternal mi paternal mi olduğu,
* hangi kromozomal bölgeyi içerdiği,
* ilgili imprinting domaininin etkilenip etkilenmediği,
* varsa mozaiklik düzeyidir.

İki kopyanın birbirinin aynısı olması — izodizomi — ya da aynı ebeveynin iki farklı homologundan gelmesi — heterodizomi — imprinting sonucunu esas olarak değiştirmez; çünkü her iki durumda da ebeveyn kökeni aynıdır. ([Nature][1])

Ancak:

> “İzo/hetero ayrımı önemli değildir.”

yerine:

> **“İzo/hetero ayrımı imprinting fenotipinin oluşması açısından belirleyici değildir; ancak oluşum mekanizmasının, resesif varyant riskinin ve laboratuvar yönteminin yorumlanmasında önemlidir.”**

denmelidir.

### Örnekler yönleriyle verilmelidir

* **Maternal UPD15** → Prader–Willi sendromu
* **Paternal UPD15** → Angelman sendromu
* **Maternal UPD7** → Silver–Russell sendromu olgularının yaklaşık %7–10’u
* **Paternal UPD6** → 6q24 ilişkili geçici neonatal diabetes mellitus
* **Paternal UPD11p15**, çoğunlukla segmental ve mozaik → Beckwith–Wiedemann spektrumu
* **Maternal/paternal UPD14** → sırasıyla Temple/Kagami–Ogata sendromları

Dolayısıyla yalnız sendrom adlarını vermek yerine ebeveyn kökenini de yazmak öğretim açısından gereklidir. ([NCBI][2])

“İmprint dozunu bozar” ifadesi anlaşılır. Daha kesin ifade:

> **“Ebeveyn-kökenine özgü metilasyon ve gen ekspresyon dozunu bozar.”**

---

## 2. Resesif varyantın homozigotlaşması doğru mu?

**Evet, fakat “her varyant homozigot olur” ifadesinin kapsamı belirtilmelidir.**

Tam kromozom izodizomisinde, tek bir ebeveyn homologunun iki özdeş kopyası bulunduğundan o homologdaki aleller genomik olarak homozigot hâle gelir. Segmental veya karma UPD’de ise yalnızca **izodizomik segmentteki** aleller homozigotlaşır. Uzun homozigotluk bölgelerinin ekzom, genom veya SNP-array ile saptanabilmesi bu mekanizmaya dayanır. ([NCBI][3])

Şu cümle:

> “Anne taşıyıcıysa ve çocuk o kromozomun izodizomisini taşıyorsa çocuk hastalığı homozigot olarak gösterir.”

fazla deterministiktir. Anne heterozigotsa iki farklı homologu vardır; yalnızca **patojenik varyantı taşıyan homologun iki kopyası** çocuğa geçtiğinde varyant homozigotlaşır.

Doğru ifade:

> **Anne veya baba resesif bir hastalık aleli için heterozigotsa ve çocuk varyantı taşıyan ebeveyn homologunun izodizomisini edinirse, diğer ebeveyn varyantı taşımadığı hâlde çocuk patojenik varyant için homozigot olabilir.**

Bu mekanizma, akraba olmayan ailelerde ve yalnızca bir ebeveynin taşıyıcı olduğu durumlarda otozomal resesif hastalık oluşturabilir. ([PubMed Central (PMC)][4])

---

## 3. Heterodizomi cümlesi nasıl düzeltilmeli?

Mevcut ifade:

> “Heterodizomi ise iki farklı homolog içerdiği için bu maskeleme etkisini yaratmaz.”

Burada **“maskeleme” yanlış terimdir**. İzodizomi resesif varyantı maskelemez; tam tersine onu **ortaya çıkarır veya açığa çıkarır**:

> *unmasking of a recessive allele*

Daha doğru cümle:

> **Saf heterodizomi, aynı ebeveynin iki farklı homologunu içerdiği için tek bir homologdaki heterozigot varyantı homozigotlaştırmaz.**

Ancak “heterodizomi resesif hastalığa yol açamaz” şeklinde mutlaklaştırılmamalıdır:

1. Birçok UPD, rekombinasyon nedeniyle saf heterodizomi veya saf izodizomi değildir; aynı kromozom üzerinde heterodizomik ve izodizomik segmentler birlikte bulunabilir. Resesif varyant, izodizomik segment içindeyse homozigotlaşabilir. ([PubMed Central (PMC)][5])
2. Teorik olarak aynı ebeveynin iki homologunda aynı genin iki farklı patojenik varyantı varsa heterodizomi bu iki aleli birlikte aktararak bileşik heterozigotluk oluşturabilir. Bu olağan taşıyıcı senaryosu değildir, ancak “imkânsız” denmesini engelleyen biyolojik bir istisnadır.

“Trizomi kurtarma sonrası mayotik rekombinasyon nedeniyle parçalı izodizomi segmentleri” ifadesinin yönü doğrudur. Daha kesin anlatım:

> **Mayoz sırasında daha önce gerçekleşmiş crossing-over nedeniyle, trizomi kurtarma sonucu oluşan UPD kromozomu heterodizomik ve izodizomik segmentlerin karışımını içerebilir.**

---

## 4. Klinik çıkarım doğru mu?

Şu klinik çıkarım doğrudur:

> Bir çocukta homozigot otozomal resesif bir varyant saptanıyor, fakat yalnızca anne veya baba heterozigot taşıyıcı bulunuyorsa UPD düşünülmelidir.

Ancak UPD tek açıklama değildir. Ayırıcı değerlendirmede şunlar da bulunmalıdır:

* diğer aleli içeren ekzon veya gen delesyonu ve yalancı homozigotluk,
* alel dropout veya teknik genotipleme hatası,
* parental mozaiklik,
* çok nadiren ikinci alelde bağımsız de novo olay,
* örnek veya akrabalık uyuşmazlığı.

Bu durumda trio verisinde:

* allel dengesi ve okuma hizalamaları,
* CNV,
* homozigotluk/ROH paterni,
* kromozom boyunca Mendel uyumsuzlukları,
* ebeveyn kökeni

birlikte değerlendirilmelidir. ACMG, UPD analizinin kullanılan yöntemin izodizomi, heterodizomi, segmental UPD ve mozaikliği hangi ölçüde yakalayabildiği belirtilerek yapılmasını önerir. ([PubMed][6])

Önemli teknik sınır:

> **SNP-array ve tekil ES/GS uzun izodizomik bölgeleri gösterebilir; saf heterodizomi homozigotluk oluşturmadığından ebeveyn örnekleri veya ebeveyn-kökeni analizi olmadan kaçabilir.**

---

## “İki patojenik yüz” eksiksiz bir sınıflama mı?

Bunlar UPD’nin **iki klasik ve temel doğrudan hastalık mekanizmasıdır**:

1. Ebeveyn-kökenine bağlı imprinting bozukluğu
2. İzodizomik bölgede resesif varyantın homozigotlaşması

Ancak “yalnızca iki sonuç vardır” denmemelidir. UPD’ye yol açan kromozomal kurtarma olayı bazen:

* rezidüel trisomik hücre hattı,
* plasentaya sınırlı mozaiklik,
* yapısal kromozom anomalisi

ile birlikte bulunabilir ve fenotipe ayrıca katkı sağlayabilir. Bu nedenle “iki ayrı patojenik yüz” yerine **“iki temel doğrudan mekanizma”** daha güvenlidir. ([PubMed Central (PMC)][7])

## Düzeltilmiş metin

> **🔬 Deep-dive — UPD neden iki temel yolla hastalık yapar?**
> UPD’nin iki klasik doğrudan patojenik mekanizması vardır ve bunlar birbirinden ayrılmalıdır.
>
> **1. İmprinting dengesizliği:** UPD klinik olarak anlamlı bir imprinting domainini içeriyorsa, her iki kromozom kopyasının aynı ebeveyn kökenine sahip olması normal maternal–paternal epigenetik dengeyi bozar. Bu mekanizma açısından belirleyici olan UPD’nin maternal veya paternal kökeni ve etkilenen kromozomal bölgedir; UPD’nin izodizomik ya da heterodizomik olması imprinting fenotipinin ortaya çıkması açısından esas belirleyici değildir. Örneğin maternal UPD15 Prader–Willi, paternal UPD15 Angelman, maternal UPD7 Silver–Russell ve paternal UPD6 6q24 ilişkili geçici neonatal diabetes mellitus oluşturabilir.
>
> **2. Resesif varyantın homozigotlaşması:** İzodizomide tek bir ebeveyn homologunun iki özdeş kopyası bulunur. Bu nedenle tam kromozom izodizomisinde o homologdaki, segmental izodizomide ise yalnız ilgili segmentteki aleller homozigotlaşır. Ebeveyn resesif bir hastalık aleli için heterozigotsa ve çocuk varyantı taşıyan homologun iki kopyasını edinirse, diğer ebeveyn varyantı taşımadığı hâlde çocuk patojenik varyant için homozigot olabilir.
>
> **Saf heterodizomi**, aynı ebeveynin iki farklı homologunu içerdiğinden tek bir homologdaki heterozigot varyantı homozigotlaştırmaz. Bununla birlikte mayotik rekombinasyon nedeniyle birçok UPD kromozomu heterodizomik ve izodizomik segmentlerin karışımını içerir; resesif hastalık riski izodizomik segmentlerde devam eder.
>
> Bu nedenle bir çocukta homozigot resesif varyant saptandığı hâlde yalnızca bir ebeveyn taşıyıcıysa, UPD ayırıcı tanıda düşünülmeli; fakat diğer alelin delesyonu, teknik alel dropout ve diğer olası açıklamalar da dışlanmalıdır.

**Net sonuç:** Kavramsal ayrım doğrudur. En önemli düzeltmeler, başlığın **“UPD’nin iki mekanizması”** olarak değiştirilmesi, maternal taşıyıcı örneğinin koşullu yazılması ve heterodizomi için “maskeleme” yerine **“homozigotlaştırma/ortaya çıkarma etkisi”** terminolojisinin kullanılmasıdır.

[1]: https://www.nature.com/articles/s41436-020-0782-9?utm_source=chatgpt.com "Diagnostic testing for uniparental disomy"
[2]: https://www.ncbi.nlm.nih.gov/books/NBK1330/?utm_source=chatgpt.com "Prader-Willi Syndrome - GeneReviews® - NCBI Bookshelf - NIH"
[3]: https://www.ncbi.nlm.nih.gov/books/NBK535150/table/resources_Table1.T.genetic_disorders_cau/?utm_source=chatgpt.com "Table. [Genetic Disorders Caused by Imprinting...]. - NCBI - NIH"
[4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6785455/?utm_source=chatgpt.com "Uniparental isodisomy caused autosomal recessive diseases"
[5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8187148/?utm_source=chatgpt.com "Uniparental disomy in a population of 32067 clinical exome trios"
[6]: https://pubmed.ncbi.nlm.nih.gov/32296163/?utm_source=chatgpt.com "Diagnostic testing for uniparental disomy"
[7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8851757/?utm_source=chatgpt.com "Uniparental disomy is a chromosomic disorder in the first place"


<br>

### C14 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 2.3 Uniparental dizomi nasıl oluşur? · satır 68

> UPD'yi klinik olarak anlamak için oluşum mekanizmasını bilmek şarttır, çünkü ***mekanizma hem hangi lokusların homozigot olduğunu hem de tekrarlanma riskini belirler***. Şekil 10.2'te gösterilen üç ana yol vardır. En sık yol **trizomi kurtarma**dır: mayoz sırasında (özellikle mayoz I'de) ayrılamama sonucu dizomik bir gamet oluşur; bu gamet normal bir gametle döllenince trizomik bir zigot ortaya çıkar. Trizomiler çoğu kez yaşamla bağdaşmadığından, embriyo fazla kromozomu atarak "kurtulmaya" çalışır. Eğer atılan kromozom, tek kopyayı sağlayan ebeveynden geliyorsa, geriye kalan iki kopya aynı ebeveynden olur — **UPD** oluşur. Mayoz I hatası kaynaklı olduğunda bu UPD **heterodizomik** olur: aynı ebeveynin iki *farklı* homoloğunu içerir. Ancak bu kuralı mutlaklaştırmamak gerekir. Kromozom 7 üzerinde yapılan bir derleme, maternal UPD7 olgularında izodizomi (n = 11) ile tam/kısmi heterodizominin (n = 12) **hemen hemen eşit sayıda** bildirildiğini ve olguların yaklaşık **yarısının** post-zigotik mitotik segregasyon hatasından kaynaklandığını göstermiştir; yani UPD7'de trizomi kurtarma tek yol değildir (Mergenthaler ve ark., 2000). Pratik çıkarım: bir UPD'nin izo mu hetero mu olduğu, oluşum mekanizmasını *olasılıklı* olarak gösterir, kesin belirlemez.

**Sorulan:** UPD oluşum mekanizmalarının (trizomi kurtarma, monozomi kurtarma, gamet tamamlama) klinik sonuçlara bağlanması doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Temel mekanizmalar doğru; ancak metin oluşum paterni ile mekanizma arasında gereğinden fazla bire bir ilişki kuruyor.** Özellikle şu üç nokta düzeltilmeli:

1. **Mayoz I hatası → tam heterodizomi** kuralı mutlak değildir; mayotik rekombinasyon nedeniyle aynı kromozomda heterodizomik ve izodizomik segmentler birlikte bulunabilir.
2. “Üç ana yol” eksiktir; **postzigotik mitotik mekanizmalar** ayrı bir dördüncü kategori olarak verilmelidir.
3. Mergenthaler 2000’deki “UPD7 olgularının yaklaşık yarısı postzigotik” çıkarımı tarihsel olarak doğru aktarılmıştır; ancak çalışmanın mekanizma çıkarımı günümüzde fazla kesin kabul edilir.

## “Mekanizma klinik sonucu belirler” cümlesi

Şu ifade yön olarak doğru:

> Mekanizma hem hangi lokusların homozigot olduğunu hem de tekrarlanma riskini belirler.

Fakat **“belirler” yerine “önemli ölçüde etkiler ve mekanizma hakkında ipucu verir”** denmelidir.

Çünkü:

* İzodizomik segmentlerin dağılımı resesif varyantların homozigotlaşma riskini belirler.
* Maternal/paternal köken imprinting sonucunu belirler.
* Trizomi kurtarma, rezidüel trisomik mozaiklik veya plasentaya sınırlı mozaiklik ihtimalini gündeme getirir.
* Tekrarlama riski ise yalnız UPD paternine değil, **altta yatan nondisjunction olayına, parental kromozom yeniden düzenlenmesine, Robertsonian translokasyona, marker kromozoma ve mozaikliğe** bağlıdır.

ACMG de UPD veya homozigotluk paterninden belirli bir oluşum mekanizmasının kesin olarak çıkarılmasını sınırlayan faktörler bulunduğunu vurgular. ([gimjournal.org][1])

## Mekanizmaların doğru klinik bağlantısı

| Oluşum mekanizması                | Beklenen genomik patern                                                                                            | Klinik açıdan önemli sonuç                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| **Trizomi kurtarma**              | Mayoz I hatasında ağırlıklı heterodizomi; mayoz II hatasında ağırlıklı izodizomi; rekombinasyon varsa karma patern | İmprinting bozukluğu, izodizomik segmentlerde resesif varyant; rezidüel trisomik veya plasental mozaiklik ihtimali |
| **Monozomi kurtarma**             | Tek kalan kromozomun kopyalanmasıyla genellikle tam izodizomi                                                      | Kromozom boyunca homozigotlaşma ve resesif varyant açığa çıkması; imprintli kromozomsa ebeveyn-kökeni etkisi       |
| **Gamet komplementasyonu**        | Dizomik gamet + nullizomik gamet; patern disomik gametin mayotik kökenine bağlı                                    | İmprinting ve resesif hastalık riski UPD paternine bağlıdır; postzigotik “kurtarma” gerçekleşmez                   |
| **Postzigotik mitotik mekanizma** | Tam veya segmental izodizomi; sıklıkla mozaik patern                                                               | Dokuya özgü mozaiklik, segmental imprinting bozukluğu veya lokal resesif homozigotlaşma                            |

Trizomi kurtarma, özellikle tüm kromozomu içeren UPD’lerde en sık kabul edilen oluşum mekanizmasıdır; ancak monosomi kurtarma, gamet komplementasyonu ve postzigotik olaylar da iyi tanımlanmıştır. Büyük klinik trio analizleri, **tam izodizominin bile yalnızca tek bir mekanizmaya özgü olmadığını** göstermektedir. ([PubMed][2])

---

## 1. Trizomi kurtarma anlatımı

Şu bölüm doğrudur:

> Dizomik gamet normal gametle birleşir → trizomik zigot oluşur → fazla kromozom kaybedilir → diğer ebeveynden gelen tek kromozom kaybedilirse UPD kalır.

Ancak “embriyo kurtulmaya çalışır” teleolojik bir ifadedir. Daha bilimsel anlatım:

> **Erken mitozlardan birinde fazla kromozomun kaybı, bazı hücrelerde disomik kromozom sayısını yeniden oluşturabilir.**

Fazla kromozom rastgele kaybedilirse teorik olarak:

* aynı ebeveynden gelen kromozomlardan biri kaybedildiğinde biparental disomi,
* diğer ebeveynden gelen tek kromozom kaybedildiğinde UPD

oluşur. Trizomi kurtarma her zaman tam değildir; rezidüel anöploid hücre hattı veya confined placental mosaicism kalabilir. Bu durum özellikle prenatal yorum açısından klinik önem taşır. ([NCBI][3])

### “Özellikle mayoz I’de” çıkarılmalı

Nondisjunction hem mayoz I’de hem mayoz II’de olabilir ve dağılım kromozoma, ebeveyn kökenine ve yaşa göre değişir. Dolayısıyla genel UPD anlatımında:

> “özellikle mayoz I’de”

demek gereksiz bir genellemedir.

---

## 2. Mayoz I → heterodizomi kuralı

**Temel öğretim modeli olarak doğru, fakat tüm kromozom için kesin değildir.**

Rekombinasyon yok varsayılırsa:

* **Mayoz I nondisjunction:** aynı ebeveynin iki farklı homoloğu → heterodizomi
* **Mayoz II nondisjunction:** aynı homologun kardeş kromatitleri → izodizomi

Ancak crossing-over nedeniyle homologlar ve kardeş kromatitler tüm uzunlukları boyunca saf biçimde farklı veya özdeş değildir. Bu nedenle daha doğru kural:

* Mayoz I hatası genellikle **sentromer çevresinde heterodizomi** oluşturur.
* Mayoz II hatası genellikle **sentromer çevresinde izodizomi** oluşturur.
* Distal bölgelerde rekombinasyona bağlı karma izo/heterodizomi görülebilir.

Bu yüzden bir UPD’nin izo veya heterodizomik yapısı oluşum mekanizması hakkında **olasılıklı çıkarım** sağlar; tek başına kesin mekanizma kanıtı değildir. ([NCBI][4])

---

## 3. Monozomi kurtarma

Bu mekanizma kitapta açık biçimde eklenmelidir:

> Bir gamet ilgili kromozomu taşımıyorsa ve normal gametle birleştiğinde monozomik zigot oluşursa, tek kalan ebeveyn kromozomunun postzigotik olarak kopyalanması disomiyi yeniden oluşturabilir.

Sonuç tipik olarak:

[
\text{tek ebeveyn kromozomu}
\rightarrow
\text{kopyalanma}
\rightarrow
\text{tam izodizomi}
]

olur.

Klinik olarak bu mekanizma, bütün kromozom boyunca resesif varyantların homozigotlaşması açısından en belirgin paternlerden biridir. Bununla birlikte tam izodizomi görüldüğünde “kesin monosomi kurtarmadır” denemez; benzer patern postzigotik mitotik hata, bazı mayoz II/trizomi kurtarma olayları veya gamet komplementasyonuyla da oluşabilir. ([PubMed][5])

---

## 4. Gamet komplementasyonu

Terim Türkçede:

> **Gamet komplementasyonu**
> veya
> **gametlerin birbirini tamamlaması**

olarak verilebilir.

Bir ebeveynden ilgili kromozomu iki kopya taşıyan dizomik gamet, diğer ebeveynden kromozomu hiç taşımayan nullizomik gametle birleşir:

[
n+1+n-1=2n
]

Zigot kromozom sayısı bakımından disomiktir, ancak iki kopya da aynı ebeveyndendir. Burada zigot düzeyinde trizomi veya monozomi kurtarma aşaması yoktur.

Ortaya çıkan patern:

* dizomik gamet mayoz I hatasından geldiyse çoğunlukla heterodizomik/karma,
* mayoz II hatasından geldiyse çoğunlukla izodizomik/karma

olabilir.

Bu nedenle gamet komplementasyonu genomik paternden trizomi kurtarmadan her zaman kesin olarak ayırt edilemez. ([PubMed][5])

---

## 5. Postzigotik mitotik mekanizma eksik

Metnin kendisi UPD7’de postzigotik olaylardan söz ettiği hâlde bunları “üç ana yol” arasında saymıyor. Bu yapısal bir tutarsızlıktır.

Postzigotik mekanizmalar şunları içerebilir:

* mitotik nondisjunction ve ardından kromozom kopyalanması/kaybı,
* mitotik rekombinasyon,
* segmental copy-neutral loss of heterozygosity,
* anöploid hücre hattının kısmi kurtarılması.

Bunlar özellikle:

* **tam izodizomi,**
* **segmental izodizomi,**
* **mozaik UPD**

oluşturabilir. Klinik sonuç etkilenen dokuya ve izodizomik segmentin imprintli veya resesif hastalık lokusu içerip içermemesine bağlıdır. ([jmg.bmj.com][6])

---

## Mergenthaler 2000 örneği kullanılmalı mı?

Çalışmadaki sayılar doğru aktarılmıştır:

* izodizomi: `n=11`
* tam veya kısmi heterodizomi: `n=12`
* yazarların çıkarımı: yaklaşık yarısının postzigotik mitotik segregasyon hatasından kaynaklanmış olabileceği. ([PubMed][7])

Ancak çalışma şu varsayımı kullanmıştır:

> Tam izodizomi → postzigotik mitotik hata
> Heterodizomi → mayotik nondisjunction + trizomi kurtarma

Bugün bu eşleştirmenin özgül olmadığı bilinmektedir. Tam izodizomi:

* monosomi kurtarma,
* mayoz II kökenli trizomi kurtarma,
* gamet komplementasyonu,
* postzigotik mitotik hata

ile oluşabilir. Dolayısıyla 2000 tarihli “olguların yaklaşık yarısı postzigotik” sonucu **patern temelli tarihsel bir çıkarımdır; kesin biçimde kanıtlanmış vaka oranı gibi verilmemelidir.** ([PubMed Central (PMC)][8])

Daha güvenli kullanım:

> **Mergenthaler ve arkadaşlarının 2000 tarihli küçük literatür derlemesinde maternal UPD7 olgularında izodizomi ile tam/kısmi heterodizomi benzer sayılarda bildirilmiş ve yazarlar bu paterni postzigotik olayların önemli katkısı olarak yorumlamıştır. Bununla birlikte günümüzde izodizomi ve heterodizomi paternlerinin tek bir oluşum mekanizmasına özgü olmadığı bilinmektedir.**

---

## Tekrarlama riski bölümü nasıl kurulmalı?

Şu bağlantı doğrudan kurulmamalıdır:

> İzodizomi gördüm → oluşum mekanizmasını biliyorum → tekrarlama riskini biliyorum.

Daha doğru danışmanlık modeli:

1. UPD tam mı, segmental mi, mozaik mi?
2. Maternal mi paternal mi?
3. İzo/heterodizomik bölgelerin dağılımı nedir?
4. Parental karyotipte Robertsonian translokasyon veya başka yeniden düzenlenme var mı?
5. Prenatal veya plasental anöploidi kanıtı var mı?
6. UPD bir imprinting bozukluğuna mı, resesif hastalığa mı yol açtı?
7. Parental veya gonadal mozaiklik şüphesi var mı?

Sporadik nondisjunction ve kromozom kurtarma olaylarında tekrarlama riski çoğunlukla düşüktür; ancak parental yapısal kromozom anomalisi bulunduğunda risk farklı olabilir. Bu nedenle tekrarlama riski, yalnız UPD tipinden değil **altta yatan sitogenetik olaydan** türetilmelidir. ([gimjournal.org][1])

## Düzeltilmiş metin

> **UPD’nin oluşum mekanizmasını anlamak klinik yorum açısından önemlidir; çünkü mekanizma, izodizomik bölgelerin dağılımını, resesif varyantların homozigotlaşma olasılığını, eşlik eden anöploid mozaiklik riskini ve genetik danışmanlığı etkiler. Bununla birlikte izodizomi veya heterodizomi paterni mekanizmayı her zaman kesin olarak göstermez; mayotik rekombinasyon ve farklı kurtarma yolları benzer genomik paternler oluşturabilir.**
>
> **En sık mekanizmalardan biri trizomi kurtarmadır. Mayotik nondisjunction sonucu oluşan dizomik bir gamet normal gametle birleştiğinde trizomik zigot meydana gelir. Erken postzigotik bölünmeler sırasında fazla kromozomun kaybı disomik bir hücre hattı oluşturabilir. Kaybedilen kromozom, tek kopyayı sağlayan ebeveynden gelirse geriye kalan iki kromozom aynı ebeveyn kökenli olur ve UPD oluşur. Mayoz I hataları genellikle sentromer çevresinde heterodizomi, mayoz II hataları ise sentromer çevresinde izodizomi oluşturur; ancak crossing-over nedeniyle kromozomun distal bölgelerinde izodizomik ve heterodizomik segmentler birlikte bulunabilir.**
>
> **Monozomi kurtarmada tek kalan ebeveyn kromozomu kopyalanarak genellikle tam izodizomi meydana gelir. Gamet komplementasyonunda ise bir dizomik ve bir nullizomik gamet birleşerek kromozom sayısı normal, fakat iki kopyası da tek ebeveynden gelen bir zigot oluşturur. Ayrıca mitotik nondisjunction ve mitotik rekombinasyon gibi postzigotik olaylar tam, segmental veya mozaik izodizomiye yol açabilir. Bu nedenle UPD’nin izo/heterodizomi yapısı oluşum mekanizmasına dair değerli bir ipucudur, fakat kesin kanıt değildir.**

**Net sonuç:** Trizomi kurtarma, monozomi kurtarma ve gamet komplementasyonu doğru mekanizmalardır; fakat kitapta **postzigotik mitotik mekanizmalar dördüncü başlık olarak eklenmeli**, mayoz I–heterodizomi ilişkisi sentromer odaklı ve olasılıklı biçimde yazılmalı, Mergenthaler 2000 sonucu ise tarihsel ve sınırlı bir çıkarım olarak sunulmalıdır.

[1]: https://www.gimjournal.org/article/S1098-3600%2821%2901179-5/fulltext?utm_source=chatgpt.com "Diagnostic testing for uniparental disomy"
[2]: https://pubmed.ncbi.nlm.nih.gov/21651501/?utm_source=chatgpt.com "The consequences of uniparental disomy and copy number neutral loss-of-heterozygosity during human development and cancer - PubMed"
[3]: https://ncbi.nlm.nih.gov/books/NBK5191/box/further_illus-215/?report=objectonly&utm_source=chatgpt.com "[Box], Learn More (trisomy rescue) - GeneReviews® - NCBI Bookshelf"
[4]: https://ncbi.nlm.nih.gov/books/NBK535150/?utm_source=chatgpt.com "Resources for Genetics Professionals — Genetic Disorders Caused by Imprinting Errors and Uniparental Disomy Not Detectable by Sequence Analysis - GeneReviews® - NCBI Bookshelf"
[5]: https://pubmed.ncbi.nlm.nih.gov/8362910/?utm_source=chatgpt.com "Uniparental disomy revisited: the first twelve years - PubMed"
[6]: https://jmg.bmj.com/content/38/8/497.short?utm_source=chatgpt.com "Complex and segmental uniparental disomy (UPD)"
[7]: https://pubmed.ncbi.nlm.nih.gov/10818216/ "Formation of uniparental disomy 7 delineated from new cases and a UPD7 case after trisomy 7 rescue. Presentation of own results and review of the literature - PubMed"
[8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8187148/?utm_source=chatgpt.com "Uniparental disomy in a population of 32,067 clinical exome trios - PMC"


<br>

### C15 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 1. Kavramsal tanım · satır 40

> Son olarak iki özel kavram, tabloyu tamamlar. **Letal-mozaik hipotezi**, bazı varyantların konstitüsyonel hâlde embriyoyu öldürdüğünü, ancak mozaik hâlde — sağlam hücrelerle karışık olarak — yaşayabildiğini öne sürer (Happle, 1987); ***bu hipotez, bir grup sendromun neden istisnasız sporadik olduğunu açıklar***. **Revertant mozaiklik** ise ters yöndeki olaydır: konstitüsyonel olarak hastalıklı bir bireyde, bazı hücrelerde ikinci bir olay varyantı düzelterek sağlıklı hücre klonları oluşturur.

**Sorulan:** Happle'ın letal-mozaik hipotezi bugün hâlâ geçerli mi? "Daima sporadik" ifadesi tutuyor mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Happle’ın letal-mozaik hipotezi bugün de geçerlidir; hatta bazı hastalıklarda moleküler olarak doğrulanmış bir biyolojik modeldir.** Ancak:

> **“Bu sendromlar istisnasız sporadiktir” ifadesi fazla mutlak ve genetik danışmanlık açısından sakıncalıdır.**

Güncel terminolojide bu gruplar için **zorunlu mozaik hastalıklar** veya **obligat mozaiklik** (*obligate mosaic disorders/mosaicism*) ifadeleri de kullanılır:

> Belirli bir patojenik varyant konstitüsyonel olarak bulunduğunda embriyonik yaşamla bağdaşmazken, yalnızca hücrelerin bir bölümünde bulunduğunda canlı doğum ve hastalık fenotipi mümkün olur.

Happle’ın 2025 tarihli güncel sınıflamasında “letal varyantların mozaik hâlde yaşaması” hâlâ ayrı bir mozaiklik kategorisi olarak korunmakta ve modelin McCune–Albright, Proteus, Schimmelpenning ve ensefalokraniyokütanöz lipomatozis dâhil yaklaşık 15 fenotipte moleküler bulgularla desteklendiği belirtilmektedir. ([freidok.uni-freiburg.de][1])

---

## Hipotezin doğru olan özü

Metindeki şu temel fikir doğrudur:

[
\text{konstitüsyonel ağır varyant}
\rightarrow
\text{embriyonik letalite}
]

[
\text{aynı varyantın postzigotik mozaiği}
\rightarrow
\text{yaşamla bağdaşan segmental hastalık}
]

Mozaiklik yaşamı şu nedenlerle mümkün kılabilir:

* mutant hücre yükünün sınırlı kalması,
* yaşamsal organların tamamen etkilenmemesi,
* WT hücrelerin doku işlevini kısmen koruması,
* mutant ve WT hücreler arasındaki hücresel rekabet,
* varyantın yalnız belirli hücre soylarında bulunması.

Bununla birlikte Happle’ın özgün modelindeki:

> “Mutant hücreler yalnızca normal hücrelerin yakınında yaşayabilir.”

ifadesi bütün hastalıklar için literal bir zorunluluk olarak kullanılmamalıdır. Günümüzde esas kavram, **WT hücrelerin varlığının organizma veya doku düzeyinde varyant yükünü tolere edilebilir hâle getirmesidir**; doğrudan komşu hücresel kurtarma her bozuklukta gösterilmiş değildir.

---

## En önemli sınır: Letalite gen düzeyinde değil, çoğunlukla varyant düzeyindedir

Şu çıkarım yapılmamalıdır:

[
\text{Gen X mozaik hastalık yapıyor}
\Rightarrow
\text{Gen X’in bütün konstitüsyonel varyantları letaldir}
]

Doğru yaklaşım:

> **Belirli bir varyantın, belirli aktivasyon düzeyinin veya belirli allelik sınıfın konstitüsyonel hâli letal olabilir.**

Aynı gende:

* daha zayıf hipomorfik veya hipermorfik varyantlar,
* farklı domainleri etkileyen varyantlar,
* farklı düzeyde yolak aktivasyonu oluşturan alleller

konstitüsyonel olarak yaşamla bağdaşabilir ve farklı bir fenotip oluşturabilir.

`PIK3CA` bunun iyi bir örneğidir. PIK3CA-ilişkili aşırı büyüme spektrumu çoğunlukla postzigotik mozaik varyantlardan oluşur; ancak nadir konstitüsyonel/de novo germline `PIK3CA` varyantları ve nadiren dominant aile öyküsüyle uyumlu olgular da bildirilmiştir. Bu nedenle “PIK3CA aktivasyonu konstitüsyonel olarak daima letaldir” denemez. ([NCBI][2])

---

## “Daima sporadik” neden düzeltilmeli?

### Hastalıkların çoğu gerçekten simplex görünür

Gerçek bir obligat mozaik bozuklukta varyant probandın embriyonik gelişimi sırasında postzigotik olarak oluştuğu için:

* ebeveynler genellikle etkilenmemiştir,
* ailede tek olgu vardır,
* kardeş rekürrens riski genellikle genel popülasyon düzeyindedir.

Örneğin moleküler olarak doğrulanmış Proteus sendromunda bugüne kadar doğrulanmış vertikal aktarım veya kardeş rekürrensi bildirilmemiştir. ([NCBI][3])

Ancak bundan:

> “Hiçbir zaman tekrarlamaz veya aktarılamaz.”

sonucu çıkarılamaz.

### Üç nedenle mutlaklık uygun değildir

**1. Tanımlanan sendrom gerçekten obligat mozaik olmayabilir.**
Bazı genlerin hem kalıtsal konstitüsyonel fenotipleri hem de segmental mozaik fenotipleri vardır. Bunlar Happle’ın gerçek letal-mozaik kategorisiyle karıştırılmamalıdır.

**2. Allelik heterojenlik vardır.**
Aynı genin güçlü aktive edici alleli yalnız mozaik hâlde yaşarken, daha zayıf bir alleli konstitüsyonel olarak yaşayabilir.

**3. Gonadal tutulum teorik olarak aktarım riski yaratabilir.**
Etkilenmiş mozaik bireyin germ hücreleri de varyantı taşıyorsa aktarım olasılığı sıfır değildir. Aktarılan varyant yavruda konstitüsyonel hâle gelirse:

* embriyonik kayıp,
* mozaik hastalıktan daha ağır veya farklı bir fenotip,
* bazı allellerde yaşamla bağdaşan konstitüsyonel hastalık

ortaya çıkabilir.

Genel mozaiklik rehberleri postzigotik de novo mozaik bozuklukların çoğunlukla simplex olduğunu belirtir; ancak mozaik bir bireyin germ hattı etkilenmişse aktarım riskinin teorik olarak `%50’den düşük` fakat sıfır olmayan bir değer olabileceğini vurgular. ([NCBI][4])

Bu yüzden klinik yazımda:

> **“İstisnasız sporadik”**

yerine:

> **“Genellikle de novo postzigotik oluşur ve ailede simplex olgu şeklinde görülür; doğrulanmış vertikal aktarım birçok klasik obligat mozaik hastalıkta bildirilmemiştir.”**

denmelidir.

---

## “Sporadik” ile “kalıtsal değil” aynı şey değildir

Bu ayrım önemlidir:

* **Sporadik/simplex:** Ailede yalnız bir etkilenmiş birey bulunması.
* **De novo:** Varyantın o bireyde yeni oluşması.
* **Postzigotik:** Varyantın döllenmeden sonra oluşması.
* **Kalıtsal olmama:** Varyantın bir ebeveynden aktarılmamış olması.
* **Aktarılamaz olma:** Probandın varyantı kendi çocuğuna geçiremeyeceği iddiası.

Bir mozaik hastalık aynı anda sporadik, de novo ve postzigotik olabilir; fakat probandın gonadları etkilenmişse teorik olarak aktarılamaz olduğu söylenemez.

---

## Revertant mozaiklik cümlesi de hafifçe düzeltilmeli

Mevcut ifade:

> “İkinci bir olay varyantı düzelterek sağlıklı hücre klonları oluşturur.”

Yön olarak doğru, fakat “varyantı düzeltmek” yalnız gerçek geri mutasyonu düşündürür. Revertant mozaiklik şu mekanizmalarla oluşabilir:

* gerçek geri mutasyon,
* ikinci bölge baskılayıcı varyantı,
* okuma çerçevesini geri kazandıran ikinci indel,
* mitotik rekombinasyon veya gen dönüşümü,
* patojenik alelin kaybı,
* alternatif splicing’i düzelten ikinci olay.

Bu nedenle klon her zaman tam olarak WT genotipine dönmez; **işlevsel olarak kurtarılmış** olabilir. ([New England Journal of Medicine][5])

---

## Düzeltilmiş metin

> **Son olarak iki özel kavram mozaiklik tablosunu tamamlar. Letal varyantların mozaik hâlde yaşayabilmesi hipotezi — günümüzde obligat mozaiklik olarak da adlandırılır — belirli patojenik varyantların konstitüsyonel hâlde embriyonik yaşamla bağdaşmadığını, ancak postzigotik olarak yalnızca hücrelerin bir bölümünde bulunduklarında yaşamla bağdaşan bir fenotip oluşturabildiğini ifade eder. Happle tarafından 1980’lerde önerilen bu model, McCune–Albright ve Proteus sendromu dâhil çeşitli bozukluklarda moleküler olarak desteklenmiştir.**
>
> **Bu hastalıklar çoğunlukla de novo postzigotik varyantlardan kaynaklanır ve ailede simplex olgu olarak görülür. Ancak “istisnasız sporadik” ifadesi kullanılmamalıdır. Letalite çoğu zaman genin tamamına değil belirli varyanta ve yolak aktivasyon düzeyine özgüdür; aynı gendeki daha hafif alleller konstitüsyonel olarak yaşayabilir. Ayrıca mozaik bireyin germ hattı etkilenmişse teorik aktarım riski sıfır değildir; aktarılan konstitüsyonel varyant embriyonik kayba, daha ağır bir fenotipe veya allelin etkisine bağlı farklı bir hastalığa yol açabilir.**
>
> **Revertant mozaiklik ise başlangıçta hastalık oluşturan genotipe sahip bir bireyde, bazı somatik hücrelerin ikinci bir genetik olayla işlevsel olarak düzelmesi ve seçici avantaj kazanarak sağlıklı ya da daha az etkilenmiş hücre klonları oluşturmasıdır. Bu kurtarma gerçek geri mutasyonla oluşabileceği gibi ikinci bölge varyantı, mitotik rekombinasyon, gen dönüşümü veya okuma çerçevesinin yeniden kurulması gibi mekanizmalarla da gerçekleşebilir.**

**Net sonuç:** Happle modeli güncelliğini koruyor; fakat **“bir grup sendromun neden genellikle de novo, postzigotik ve simplex olduğunu açıklar”** denmeli. **“İstisnasız/daima sporadik”** ifadesi çıkarılmalıdır.

[1]: https://freidok.uni-freiburg.de/files/270036/snP8kUTfVKtm1REx/JEADV%2BClinical%2BPractice%2B-%2B2025%2B-%2BHapple%2B-%2BCategories%2Bof%2BCutaneous%2BMosaicism.pdf "Categories of Cutaneous Mosaicism"
[2]: https://www.ncbi.nlm.nih.gov/books/NBK153722/ "PIK3CA-Related Overgrowth Spectrum - GeneReviews® - NCBI Bookshelf"
[3]: https://www.ncbi.nlm.nih.gov/books/NBK99495/ "Proteus Syndrome - GeneReviews® - NCBI Bookshelf"
[4]: https://www.ncbi.nlm.nih.gov/books/NBK585455/ "Resources for Genetics Professionals — Mosaicism - GeneReviews® - NCBI Bookshelf"
[5]: https://www.nejm.org/doi/full/10.1056/NEJMc0809896?utm_source=chatgpt.com "Revertant Mosaicism — Patchwork in the Skin | New England Journal of Medicine"


<br>

### C16 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 2.2 Hangi bölme tutuldu? Tekrarlanma riskinin tek belirleyicisi · satır 72

> Klinik genetikte mozaikliğin en önemli sonucu, tekrarlanma riskini yeniden tanımlamasıdır. Burada birbirine sürekli karıştırılan iki ayrı soru vardır ve bunları ayırmak zorunludur: *"Hastanın fenotipini ne açıklıyor?"* sorusunun cevabı **somatik bölmededir**; ***"Kardeşinde tekrar eder mi?" sorusunun cevabı ise germ hücresi bölmesindedir***. Şekil 12.2, bu iki bölmenin dört olası kombinasyonundan klinikte anlamlı olan üçünü karşılaştırır.

**Sorulan:** İki sorunun bu şekilde ayrılması danışma pratiğinde doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**İki soruyu ayırmak danışmanlık pratiğinde çok doğru ve öğreticidir.** Ancak mevcut ifade, öznenin kim olduğunu belirtmediği için yanlış anlaşılabilir:

* **Probandın fenotipi**, varyantın hastalıkla ilişkili somatik dokulardaki dağılımına bağlıdır.
* **Kardeş tekrarlanma riski**, probandın değil, **anne veya babanın germ hattında** varyant bulunup bulunmadığına bağlıdır.
* **Probandın kendi çocuklarına aktarım riski** ise probandın germ hattının etkilenip etkilenmediğine bağlıdır.

Dolayısıyla “somatik bölme fenotipi, germ hücresi bölmesi kardeş riskini belirler” ilkesi ancak **değerlendirilen bireyin ebeveyn olduğu açıkça belirtilirse** tam doğrudur.

## Temel ayrım

| Değerlendirilen durum            | Yanıtlanan soru                 | Belirleyici biyolojik değişken                       |
| -------------------------------- | ------------------------------- | ---------------------------------------------------- |
| **Probandın somatik mozaiği**    | Hastanın fenotipini açıklar mı? | İlgili doku ve hücre soylarındaki mutant hücre oranı |
| **Ebeveynin germ hattı mozaiği** | Kardeşte tekrar eder mi?        | Mutant varyantı taşıyan gametlerin oranı             |
| **Probandın germ hattı mozaiği** | Hastanın çocuklarına geçer mi?  | Probandın mutant gamet üretme olasılığı              |

Postzigotik varyant yalnız probandda oluşmuşsa, ebeveynlerin germ hattında bulunmaz ve kardeş tekrarlanma riskini artırması beklenmez. Buna karşılık klinik olarak sağlıklı ve kan testi negatif bir ebeveynde **germ hattına sınırlı mozaiklik** bulunabilir ve bu durum kardeş tekrarlanmasına yol açabilir. Erken embriyonik bir olay hem somatik hem germ hattı soylarına dağılırsa ebeveynde **gonosomal veya karışık mozaiklik** gelişir; ebeveyn hafif etkilenmiş olabilir ve aktarım riski yükselir. ([NCBI][1])

## Üç klinik mozaiklik kombinasyonu

Şekilde karşılaştırılan üç kombinasyon muhtemelen şunlardır:

### 1. Yalnız somatik mozaiklik

Varyant somatik hücrelerde bulunur, germ hattına katılmaz.

* Bireyde fenotip oluşturabilir.
* **Gerçekten somatik dokularla sınırlıysa** çocuklarına aktarılmaz.
* Ebeveyn söz konusuysa, kardeş tekrarlanma riskini artırmaz.

Ancak kan, tükürük veya deri örneğinde saptanmaması gonadların etkilenmediğini kanıtlamaz.

### 2. Germ hattına sınırlı mozaiklik

Varyant germ hücrelerinin bir bölümünde bulunur; rutin somatik örneklerde bulunmayabilir.

* Ebeveyn tamamen sağlıklı olabilir.
* Kan testi negatif olabilir.
* Birden fazla etkilenmiş çocuk doğabilir.
* Risk, mutant gametlerin oranına bağlıdır ve standart bir yüzdeyle kesin olarak verilemez.

Bu, “fenotip yok ama tekrarlanma riski var” durumunun temel açıklamasıdır.

### 3. Somatik ve germ hattı mozaiği — gonosomal mozaiklik

Varyant erken postzigotik dönemde oluşmuş ve hem somatik hem germ hattı soylarına dağılmıştır.

* Ebeveynde hafif, segmental veya atipik fenotip bulunabilir.
* Varyant düşük VAF ile kan veya başka dokularda saptanabilir.
* Kardeş tekrarlanma riski artar.
* Somatik VAF ile germ hücresindeki oran arasında ilişki olabilir; fakat bunlar eşit kabul edilemez.

Erken embriyonik varyantlar soma ve germ hattını birlikte etkileyebilirken, germ hattı ayrıştıktan sonra oluşan varyantlar yalnız gonadlarla sınırlı kalabilir. Bu gelişimsel zamanlama, hem klinik bulguları hem aktarım riskini belirleyen temel faktörlerden biridir. ([Nature][2])

## “Bölmeler” tamamen bağımsız değildir

“Somatik bölme” ve “germ hücresi bölmesi” öğretim açısından yararlı kavramlardır; ancak anatomik olarak birbirinden mühürlenmiş iki bağımsız kutu gibi sunulmamalıdır.

Erken postzigotik bir varyant:

[
\text{ortak embriyonik öncül hücre}
\rightarrow
\begin{cases}
\text{somatik soylar}\
\text{germ hattı}
\end{cases}
]

şeklinde her iki bölmeye de dağılabilir. Bu nedenle:

* somatik dokudaki düşük VAF, germ hattı tutulumuna ipucu verebilir;
* fakat germ hattındaki mutant hücre oranını kesin olarak göstermez;
* kan negatifliği, germ hattı mozaiğini dışlamaz;
* kan VAF’si doğrudan tekrarlanma riski olarak kullanılamaz.

Çoklu dokularda derin dizileme, varyantın gelişimsel zamanlaması hakkında daha iyi fikir verebilir. Paternal kaynaklı olaylarda sperm analizi mutant gamet oranını doğrudan ölçmeye yaklaşırken, maternal germ hattının doğrudan örneklenmesi genellikle mümkün değildir. ([Nature][2])

## Tekrarlanma riski ikili değildir

Şu model fazla basittir:

[
\text{germ hattında var} \Rightarrow \text{yüksek risk}
]

[
\text{germ hattında yok} \Rightarrow \text{sıfır risk}
]

Gerçekte risk sürekli bir değişkendir ve şunlara bağlıdır:

* varyantın anne veya baba kökenli olması,
* olayın gelişimsel zamanlaması,
* germ hücrelerinin ne kadarının mutant klondan geldiği,
* parental somatik mozaikliğin düzeyi ve doku dağılımı,
* önceki etkilenmiş gebeliklerin sayısı,
* varyantın spermde doğrudan gösterilip gösterilemediği.

Görünürde de novo varyantlar için geleneksel olarak verilen genel `%1–2` riski her aile için uygun değildir. Çoklu doku, haplotipleme ve gerektiğinde sperm analizi kullanılan kişiselleştirilmiş değerlendirmelerde bazı ailelerin riski `%0,1’in altına` indirilebilirken, parental karışık mozaiklik saptanan ailelerde belirgin şekilde daha yüksek riskler hesaplanmıştır. ([Nature][2])

## Düzeltilmiş metin

> **Klinik genetikte mozaikliğin en önemli sonuçlarından biri, fenotip ve tekrarlanma riskinin farklı hücresel dağılımlar tarafından belirlenmesidir. Bu nedenle birbirine karıştırılmaması gereken üç ayrı soru vardır. “Probandın fenotipini ne açıklıyor?” sorusu, varyantın hastalıkla ilişkili somatik dokulardaki dağılımı ve mutant hücre yüküyle ilgilidir. “Kardeşinde tekrar eder mi?” sorusu, anne veya babanın germ hattında varyant taşıyan hücrelerin bulunup bulunmadığıyla ilgilidir. “Proband kendi çocuğuna aktarabilir mi?” sorusu ise probandın germ hattının etkilenip etkilenmediğine bağlıdır.**
>
> **Somatik ve germ hattı soyları tamamen bağımsız bölmeler değildir. Erken postzigotik bir olay her iki hücre soyuna dağılarak gonosomal mozaiklik oluşturabilir; daha geç bir olay yalnız somatik dokularla veya yalnız germ hattıyla sınırlı kalabilir. Bu nedenle somatik dokuda ölçülen VAF, germ hattı tutulumuna ipucu verebilir fakat aktarım riskini doğrudan ölçmez; kan testinin negatif olması da germ hattına sınırlı mozaikliği dışlamaz.**

**Net sonuç:** Kavramsal ayrım güçlüdür ve kitapta tutulmalıdır. Ancak “kardeş riski germ hücresi bölmesindedir” cümlesi **“anne veya babanın germ hattındadır”** şeklinde yazılmalı; ayrıca probandın germ hattının kardeş riskini değil, **kendi çocuklarına aktarım riskini** belirlediği açıkça ayrılmalıdır.

[1]: https://www.ncbi.nlm.nih.gov/books/NBK585455/ "Resources for Genetics Professionals — Mosaicism - GeneReviews® - NCBI Bookshelf"
[2]: https://www.nature.com/articles/s41467-023-36606-w "Personalized recurrence risk assessment following the birth of a child with a pathogenic de novo mutation | Nature Communications"


<br>

### C17 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 1. Kavramsal tanım · satır 40

> Son olarak iki özel kavram, tabloyu tamamlar. **Letal-mozaik hipotezi**, bazı varyantların konstitüsyonel hâlde embriyoyu öldürdüğünü, ancak mozaik hâlde — sağlam hücrelerle karışık olarak — yaşayabildiğini öne sürer (Happle, 1987); bu hipotez, bir grup sendromun neden istisnasız sporadik olduğunu açıklar. ***Revertant mozaiklik ise ters yöndeki olaydır***: konstitüsyonel olarak hastalıklı bir bireyde, bazı hücrelerde ikinci bir olay varyantı düzelterek sağlıklı hücre klonları oluşturur.

**Sorulan:** Revertant mozaiklik anlatımı doğru mu? Bu konu bir textbook'ta bu ağırlıkta yer almalı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Revertant mozaiklik anlatımının özü doğrudur; ancak “letal-mozaik hipotezinin tersidir” ve “varyant düzelerek sağlıklı hücre oluşur” ifadeleri fazla basitleştirilmiştir.**

Daha doğru tanım:

> **Revertant mozaiklik, konstitüsyonel patojenik varyant taşıyan bir bireyde, postzigotik bir genetik olayın bazı hücrelerde patojenik etkinin tamamen veya kısmen ortadan kalkmasını sağlaması ve genetik ya da işlevsel olarak kurtarılmış bir hücre hattı oluşturmasıdır.**

GeneReviews bunu, germline patojenik varyant taşıyan hücrelerle, bu varyantın spontan somatik düzeltilmesiyle oluşan hücrelerin aynı bireyde birlikte bulunması olarak tanımlar. ([NCBI][1])

## “Ters yöndeki olaydır” doğru mu?

**Öğretici bir karşılaştırma olarak kullanılabilir; mekanistik olarak tam karşıtı değildir.**

* **Letal varyantın mozaik hâlde yaşaması:** Başlangıçtaki zigot genellikle WT’dir; postzigotik patojenik olay mutant hücre klonu oluşturur.
* **Revertant mozaiklik:** Başlangıçtaki zigot patojenik genotipi taşır; sonraki bir somatik olay bazı hücrelerde hastalık etkisini kurtarır.

Şematik olarak yönler karşıttır:

[
WT\ hücre \rightarrow mutant\ hücre\ klonu
]

ve

[
mutant\ hücre \rightarrow kurtarılmış\ hücre\ klonu
]

Ancak letal-mozaik hipotezi, mutant hücrelerin yalnız mozaik dağılımda yaşamla bağdaşmasını açıklayan özel bir modeldir. Revertant mozaiklik ise çok farklı, çoğunlukla konstitüsyonel hastalıklarda görülebilen somatik genetik kurtarma olayıdır. Bu nedenle **“ters yöndeki olay” yerine “karşıt yönde bir mozaikleşme örneği”** daha güvenlidir.

## “İkinci olay varyantı düzeltir” fazla dar

Düzeltme her zaman ilk varyantın gerçek anlamda eski hâline dönmesi değildir. Başlıca mekanizmalar şunlardır:

| Mekanizma                                    | Sonuç                                                        |
| -------------------------------------------- | ------------------------------------------------------------ |
| **Gerçek geri mutasyon**                     | Patojenik baz yeniden WT baza döner                          |
| **İkinci bölge baskılayıcı varyantı**        | İlk varyant korunur, fakat ikinci değişiklik işlevi kurtarır |
| **Çerçeve düzeltici ikinci indel**           | İlk frameshift’in ardından okuma çerçevesi yeniden kurulur   |
| **Mitotik gen dönüşümü**                     | Patojenik bölge sağlam homologdaki diziyle değiştirilir      |
| **Mitotik rekombinasyon / copy-neutral LOH** | Sağlam aleli taşıyan hücre hattı homozigotlaşabilir          |
| **Splicing’i düzelten ikinci değişiklik**    | Normal veya kısmen işlevsel transkript yeniden oluşabilir    |

İnsan hastalığında moleküler olarak gösterilen ilk klasik örneklerden biri, `COL17A1` ilişkili junctional epidermolizis büllozada mitotik gen dönüşümüyle oluşan revertant mozaikliktir. ([ScienceDirect][2])

“Revertant mozaiklik” ile daha geniş **somatik genetik kurtarma** kavramı da ayrılabilir. Kurtarıcı olay aynı geni veya aleli düzeltiyorsa revertant mozaiklik terimi uygundur. Başka bir gendeki somatik değişiklik patojenik yolu telafi ediyorsa **somatik genetik kurtarma** daha kapsayıcı bir terimdir. Hematopoietik Mendel hastalıklarında bu geniş kurtarma mekanizmalarının fenotipi hafifletebildiği gösterilmiştir. ([Nature][3])

## “Sağlıklı hücre klonları” her zaman doğru değil

Daha doğru ifade:

> **Genetik veya işlevsel olarak kurtarılmış hücre klonları**

Çünkü kurtarma:

* tam veya kısmi olabilir,
* yalnız belirli bir hücre işlevini düzeltebilir,
* yalnız bir doku ya da hücre soyunda bulunabilir,
* bireyin bütün klinik bulgularını düzeltmeyebilir.

Ayrıca tek bir hücrede kurtarıcı olayın ortaya çıkması, otomatik olarak klinik olarak görünür bir klon oluşturmaz. Hücrenin:

* kök/progenitör hücre niteliğinde olması,
* çoğalabilmesi,
* çevresindeki mutant hücrelere göre seçici avantaj kazanması

gerekebilir. Bu nedenle revertant hücreler epidermiste normal görünümlü yamalar oluşturabilirken, hematopoietik hastalıklarda belirli kan hücresi soylarında genişleyebilir. Epidermolizis büllozada birden fazla bağımsız kurtarma olayının aynı bireyde farklı normal deri alanları oluşturabildiği gösterilmiştir. ([New England Journal of Medicine][4])

## Klinik önemi nedir?

Revertant mozaiklik nadir görülse de dört nedenle öğreticidir:

1. **Beklenenden hafif veya yamalı fenotipi açıklayabilir.**
2. **Dokuya bağlı test sonucunu etkileyebilir.** Kurtarılmış hücrelerin seçici olarak genişlediği bir dokudan yapılan analiz, konstitüsyonel genotipi eksik temsil edebilir.
3. **Somatik klonal seçilimin yalnızca kanserde olmadığını gösterir.**
4. **“Doğal gen tedavisi” modeli sunar.** Özellikle epidermolizis büllozada hastanın kendiliğinden düzelmiş hücrelerinin otolog tedavide kullanılması araştırılmıştır. ([PubMed Central (PMC)][5])

Bununla birlikte kurtarılmış bir hematopoietik klonun bulunması bütün hastalık risklerini ortadan kaldırmayabilir. Örneğin Fanconi anemisinde kan sayımları düzelebilse bile non-revertant hücrelerden kaynaklanan kemik iliği neoplazisi ve solid tümör riskleri devam edebilir. ([ASH Publications][6])

## Textbook’ta bu ağırlıkta yer almalı mı?

**Evet, mozaiklik bölümünde kısa bir özel kavram kutusu olarak yer almalı; fakat letal-mozaik hipoteziyle eşit ağırlıklı temel bir kategori gibi genişletilmemelidir.**

Uygun ağırlık:

* Bir tanım paragrafı
* Mekanizmaları gösteren kısa bir satır veya şema
* Bir deri örneği: epidermolizis bülloza
* Bir hematolojik örnek: Fanconi anemisi veya Wiskott–Aldrich sendromu
* Bir klinik sonuç: fenotipin hafiflemesi ve örnek seçimi

Genel klinik genetik kitabında yaklaşık **150–250 kelimelik bir deep-dive kutusu** yeterlidir. Ayrıntılı tedavi potansiyeli ve hastalık bazlı mekanizmalar genodermatozlar veya kemik iliği yetmezliği bölümlerine bırakılmalıdır.

## Önerilen metin

> **Son olarak iki özel kavram mozaiklik tablosunu tamamlar. Letal varyantların mozaik hâlde yaşaması modelinde, konstitüsyonel durumda yaşamla bağdaşmayan belirli bir varyant postzigotik olarak yalnızca hücrelerin bir bölümünde bulunduğunda canlı bir fenotip oluşturabilir.**
>
> **Revertant mozaiklik ise karşıt yönde gelişen bir somatik mozaikleşme örneğidir. Konstitüsyonel patojenik varyant taşıyan bir bireyde postzigotik bir genetik olay, bazı hücrelerde patojenik etkinin tamamen veya kısmen ortadan kalkmasını sağlar. Bu olay gerçek geri mutasyonla oluşabileceği gibi ikinci bölge baskılayıcı varyant, okuma çerçevesini düzelten ikinci bir indel, mitotik rekombinasyon veya gen dönüşümü yoluyla da gerçekleşebilir. Bu nedenle hücreler her zaman tam WT genotipine dönmez; genetik veya işlevsel olarak kurtarılmış olabilir.**
>
> **Kurtarılmış hücreler seçici çoğalma avantajı kazanırsa klinik olarak fark edilebilir klonlar oluşturabilir. Epidermolizis büllozada normal görünümlü deri yamaları, bazı kalıtsal hematolojik hastalıklarda ise düzelmiş kan hücresi klonları bunun örnekleridir. Revertant mozaiklik beklenenden hafif veya bölgesel fenotipi açıklayabilir, test edilecek dokunun seçimini etkileyebilir ve “doğal gen tedavisi” için biyolojik bir model oluşturur.**

**Net sonuç:** Kavram kitapta kalmalı; ancak “varyant düzelir ve sağlıklı hücre oluşur” yerine **“patojenik etki tam veya kısmen kurtarılır ve işlevsel olarak düzelmiş hücre klonu oluşabilir”** denmelidir.

[1]: https://www.ncbi.nlm.nih.gov/books/NBK5191/ "GeneReviews Glossary - GeneReviews® - NCBI Bookshelf"
[2]: https://www.sciencedirect.com/science/article/pii/S0092867400818942?utm_source=chatgpt.com "Revertant Mosaicism in Epidermolysis Bullosa Caused by ..."
[3]: https://www.nature.com/articles/s41576-019-0139-x?utm_source=chatgpt.com "Somatic genetic rescue in Mendelian haematopoietic diseases | Nature Reviews Genetics"
[4]: https://www.nejm.org/doi/full/10.1056/NEJMc0809896?utm_source=chatgpt.com "Revertant Mosaicism — Patchwork in the Skin"
[5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3073671/?utm_source=chatgpt.com "Revertant mosaicism in skin: natural gene therapy - PMC - NIH"
[6]: https://ashpublications.org/blood/article/127/24/2971/35440/How-I-treat-MDS-and-AML-in-Fanconi-anemia?utm_source=chatgpt.com "How I treat MDS and AML in Fanconi anemia | Blood | American Society of Hematology"


<br>

### C18 · Bölüm 13 — Kodlamayan (Noncoding) ve Regülatör Varyantlar

**Yer:** `Bölüm_13_Noncoding_Regulator_Varyantlar.md` ·  · satır 3

> **Bölümün çekirdek tezi:** Genomun protein kodlayan kısmı %2'den azdır; klinik genetiğin neredeyse tamamı ise on yıllardır bu %2'ye bakmıştır. Kodlamayan varyantlar, bu kör noktanın adıdır. Bu bölümün çekirdek iddiası şudur: **kodlamayan bir varyant, proteinin tek bir amino asidini bile değiştirmeden hastalık yapabilir — çünkü hedefi ürünün kendisi değil, ürünün ifade programıdır.** Bir promotör varyantı genin ne kadar üretileceğini, bir enhancer varyantı hangi dokuda üretileceğini, bir 5′UTR varyantı ne kadar verimli çevrileceğini, bir TAD sınırı varyantı ise hangi genin üretileceğini bozar. Buradan üç klinik sonuç doğar: (1) bu varyantları görmek için **ekzom yetmez, WGS gerekir**; (2) ***fenotip çoğu zaman şaşırtıcı biçimde dar ve tek organa sınırlıdır, çünkü etkilenen düzenleyici doku-özgüdür***; (3) yorumlamada **PVS1 uygulanamaz** ve kanıtın ağırlık merkezi hesaplamadan **fonksiyonel deneye** kayar. Bölüm 8'de yapısal varyant ölçeğinde gördüğümüz düzenleyici mimariyi (TAD, enhancer hijacking) bu bölüm **tek nükleotid** ölçeğine indirir.

**Sorulan:** Bu genelleme doğru mu? PVS1'in uygulanamaması ve ağırlığın fonksiyonel deneye kayması ifadesi de değerlendirilsin.

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Bölümün ana mesajı doğru; ancak üç klinik sonuç fazla mutlaklaştırılmıştır.**

Özellikle:

1. **“Ekzom yetmez, WGS gerekir”** → genom çapında kodlamayan varyant araştırması için yön olarak doğru, fakat WGS her durumda zorunlu veya tek başına yeterli değildir.
2. **“Fenotip çoğu zaman dar ve tek organa sınırlıdır”** → mümkün ve önemli bir patern, ancak genel kural değildir.
3. **“PVS1 uygulanamaz”** → promotör/enhancer/UTR/izolatör varyantları için genel olarak doğru; fakat tüm kodlamayan varyantlar için yanlıştır. Splice etkili intronik varyantlar önemli istisnadır.

Ayrıca metin **“kodlamayan varyant” ile “düzenleyici varyant” kavramlarını eş anlamlı kullanıyor**. Bunlar aynı değildir.

---

## 1. “Genomun protein kodlayan kısmı %2’den azdır”

Doğrudur. İnsan ekzomu genomun yaklaşık `%1,5`’ini oluşturur; ancak “ekzom” ile yalnız protein kodlayan CDS tam olarak aynı değildir, çünkü ekzonik UTR dizileri de ekzom içinde değerlendirilebilir. ([Genom Enstitüsü][1])

Şu cümle ise retorik olarak fazla güçlüdür:

> “Klinik genetiğin neredeyse tamamı on yıllardır bu %2’ye bakmıştır.”

Klinik genetik tarihsel olarak yalnız kodlayan SNV’lere bakmamıştır. Karyotip, FISH, kromozomal mikroarray, MLPA, tekrar genişlemesi, metilasyon, UPD, mtDNA ve yapısal varyant analizleri uzun süredir kodlamayan veya genler arası bölgeleri de incelemektedir.

Daha doğru ifade:

> **Klinik dizileme ve sekans varyantı yorumlama pratiği, tarihsel olarak protein kodlayan ekzonlar ve kanonik splice bölgeleri üzerinde orantısız biçimde yoğunlaşmıştır.**

Nitekim kodlamayan varyantlara yönelik güncel yorumlama önerileri de geleneksel analizlerin esas olarak kodlayan bölgeler ve kanonik splice pozisyonlarına odaklandığını belirtmektedir. ([Springer][2])

---

## 2. “Kodlamayan varyantın hedefi ürün değil, ifade programıdır”

**Düzenleyici varyantlar için güçlü bir öğretim cümlesidir; bütün kodlamayan varyantlar için doğru değildir.**

Kodlamayan bölgelerde bulunan varyantlar farklı mekanizmalarla hastalık yapabilir:

* promotör/enhancer/izolatör bozukluğu,
* pre-mRNA splicing bozukluğu,
* 5′ veya 3′ UTR üzerinden translasyon ve RNA kararlılığı değişikliği,
* miRNA veya uzun kodlamayan RNA işlevi,
* toksik RNA oluşturan tekrar genişlemesi,
* RAN translasyonu,
* kromatin ve imprinting bozukluğu.

Örneğin derin intronik bir varyant pseudoekzon oluşturursa aminoasit dizisini ve okuma çerçevesini doğrudan değiştirebilir. Bir 5′UTR varyantı yeni `uAUG/uORF` oluşturabilir veya alternatif translasyon başlangıcı üzerinden proteinin N-terminal dizisini değiştirebilir. Kodlamayan varyantların çoğu protein dizisini doğrudan değiştirmese de **“kodlamayan bölgede bulunmak, protein dizisini etkileyememek anlamına gelmez.”** ([Springer][2])

Bu nedenle ana tez şu biçimde daha doğru olur:

> **Bir düzenleyici varyant, protein kodlayan diziyi değiştirmeden hastalık yapabilir; çünkü bozulma proteinin dizisinde değil, ürünün ne zaman, nerede, ne miktarda ve hangi transkript biçiminde üretileceğindedir.**

---

## 3. Dört mekanistik örnek doğru mu?

### Promotör

> “Bir promotör varyantı genin ne kadar üretileceğini bozar.”

Doğru ama eksik. Promotör varyantı:

* toplam transkripsiyon miktarını,
* transkripsiyon başlangıç bölgesini,
* kullanılan transkripti veya izoformu,
* gelişimsel zamanlamayı,
* uyarana yanıtı

değiştirebilir. Promotör tanımı da dokuya ve gelişim dönemine bağlı olabilir. ([Springer][2])

### Enhancer

> “Bir enhancer varyantı hangi dokuda üretileceğini bozar.”

Doğru yönlü, fakat enhancer yalnız doku seçmez. Aynı zamanda:

* ekspresyon düzeyini,
* hücre tipini,
* gelişim dönemini,
* uyarana bağlı aktivasyonu,
* ekspresyon alanının sınırlarını

değiştirebilir.

Daha doğru ifade:

> **Enhancer varyantı genin hangi hücrede, hangi gelişim döneminde ve ne düzeyde ifade edileceğini bozabilir.**

### 5′UTR

> “Bir 5′UTR varyantı ne kadar verimli çevrileceğini bozar.”

Bu klasik sonuçtur; fakat tek sonuç değildir. Varyant:

* ribozom taramasını,
* RNA ikincil yapısını,
* `uAUG/uORF` kullanımını,
* başlangıç kodonu seçimini,
* mRNA stabilitesini,
* bazı durumlarda splicing’i

etkileyebilir. Bazı `uAUG` varyantları proteinin N-terminalini de değiştirebilir. ([Springer][2])

### TAD sınırı

> “Bir TAD sınırı varyantı hangi genin üretileceğini bozar.”

Fikir doğru, ifade fazla ikili. TAD sınırı bozukluğu:

* normal enhancer–promotör temasını azaltabilir,
* komşu düzenleyici alanlar arasında ektopik temas oluşturabilir,
* bir enhancer’ın yanlış geni aktive etmesine yol açabilir,
* ekspresyon miktarını veya uzamsal paternini değiştirebilir.

En iyi doğrulanmış Mendelci örneklerin önemli kısmı TAD sınırını bozan **delesyon, inversiyon ve duplikasyon gibi yapısal varyantlardır**. EPHA4 bölgesindeki yeniden düzenlenmelerin enhancer’ları yanlış genlerle temas ettirdiği doğrudan gösterilmiştir. ([PubMed Central (PMC)][3])

Tek CTCF motifi veya küçük bir sınır elemanı değişikliği de etkili olabilir; ancak her CTCF motif varyantı TAD çökmesine yol açmaz. Sınırlar birden fazla CTCF bölgesiyle desteklenebilir ve genomik bağlama göre tamponlanabilir. Bu nedenle “TAD sınırı SNV’si” iddiası güçlü fonksiyonel ve üç boyutlu genom kanıtı gerektirir. Tek bir CTCF motifinin silinmesinin gelişimsel gen ekspresyonunu bozabildiği deneysel olarak gösterilmiş olsa da bu durum bütün sınırlar için genellenemez. ([PubMed][4])

---

## 4. “Ekzom yetmez, WGS gerekir”

### Doğru tarafı

Genom çapında:

* derin intronik,
* distal enhancer,
* izolatör,
* intergenik,
* TAD sınırı

varyantlarını sistematik biçimde araştırmak için standart ekzom dizilemesi yetersizdir. WGS, bu bölgelerde varyant saptama imkânını belirgin biçimde genişletir. ([Springer][2])

### Fazla mutlak tarafı

WGS her durumda zorunlu değildir:

* Bilinen bir promotör veya enhancer hedefli Sanger/panel analiziyle incelenebilir.
* Bazı ekzom kitleri UTR ve ekzon çevresindeki intronik bölgeleri kısmen kapsayabilir.
* CNV ve yapısal bozukluk array, MLPA veya hedefli yöntemlerle saptanabilir.
* Splicing bozukluğu bazen RNA analiziyle ortaya çıkarılabilir.

Dahası:

[
\text{WGS ile varyantın görülmesi}
\neq
\text{varyantın yorumlanabilmesi}
]

Klinik WGS analizleri kodlamayan varyantları sıklıkla filtrelemekte veya VUS olarak bırakmaktadır; temel darboğaz artık yalnız saptama değil, **işlevsel bölgeyi ve doğru hedef geni tanımlama** sorunudur. ([Springer][2])

Daha uygun cümle:

> **Genom çapında kodlamayan varyant araştırmasında standart ekzom çoğunlukla yetersizdir; WGS veya hipoteze dayalı hedefli düzenleyici bölge analizi gerekir. WGS varyantı görünür kılar, fakat patojenitesini kendiliğinden açıklamaz.**

---

## 5. “Fenotip çoğu zaman dar ve tek organa sınırlıdır”

**Bu olası bir sonuçtur; genel bir beklenti olarak yazılmamalıdır.**

Dokuya özgü bir enhancer yalnız belirli bir gelişimsel alanda işlev görüyorsa, varyant:

* izole ekstremite anomalisi,
* yalnız retina hastalığı,
* özgül kraniofasiyal malformasyon,
* tek bir endokrin veya hematolojik fenotip

oluşturabilir. Bu, kodlayan null varyantın oluşturduğu multisistemik sendromdan daha dar bir fenotip yaratabilir.

Ancak:

* promotör ve UTR’ler birden fazla dokuda kullanılabilir,
* enhancer’lar pleiotropik olabilir,
* bir düzenleyici bölge birden fazla geni etkileyebilir,
* TAD sınırı bozukluğu geniş bir lokusu yeniden düzenleyebilir,
* gelişimsel bir enhancer bozukluğu birden fazla organı etkileyebilir.

Güncel noncoding yorumlama rehberi, düzenleyici etkilerin **yüksek derecede dokuya özgü olabileceğini** ve bazı orta etkili varyantların yalnız tek doku veya organda hastalık yapabileceğini belirtir; fakat bunu bütün düzenleyici varyantlar için genel kural olarak sunmaz. ([Springer][2])

Doğru ifade:

> **Doku veya gelişim dönemi özgül düzenleyici elemanların bozulması, kodlayan LoF varyantlarına göre daha dar ya da organ-sınırlı fenotip oluşturabilir; ancak bu, kodlamayan varyantların zorunlu bir özelliği değildir.**

---

## 6. PVS1 gerçekten uygulanamaz mı?

### Promotör, enhancer, UTR ve izolatör varyantlarında

**Genel olarak PVS1 uygulanmamalıdır.**

PVS1, klasik olarak:

* nonsense,
* frameshift,
* kanonik `±1/±2` splice,
* başlangıç kodonu,
* tek veya çoklu ekzon delesyonu

gibi öngörülen null varyantlar için tanımlanmıştır. Noncoding yorumlama önerileri, mevcut PVS1 rehberinin kapsamadığı promotör, enhancer, UTR ve diğer düzenleyici varyantlarda PVS1 kullanılmasını önermemektedir; çünkü bu varyantların tam null etki oluşturduğu yalnız genomik konumdan güvenilir biçimde çıkarılamaz. ([Springer][2])

Bir promotör varyantı laboratuvar deneyinde ekspresyonu `%80` azaltmış olsa bile:

> **“Ekspresyon azaldı, dolayısıyla PVS1”**

denmez.

Uygun biçimde doğrulanmış fonksiyonel sonuç genellikle **PS3**, diğer klinik ve genetik kanıtlarla birlikte değerlendirilir.

### Fakat tüm kodlamayan varyantlar için yasak değildir

Kanonik splice pozisyonları genomik olarak kodlamayan bölgelerdedir ve uygun LoF mekanizmasında PVS1 alabilir.

Daha da önemlisi, ClinGen SVI’nin 2023 splicing rehberi, nonkanonik intronik veya ekzonik splice varyantlarında RNA deneyinin LoF transkriptini göstermesi durumunda **`PVS1_Strength(RNA)`** kullanımını önermektedir. Bu uygulama, gen-spesifik PVS1 karar ağacına, oluşan transkriptin miktarına ve NMD/in-frame etkisine bağlıdır. ([Johns Hopkins University][5])

Dolayısıyla doğru kural:

> **Saf düzenleyici promotör/enhancer/UTR/izolatör varyantlarında PVS1 genellikle uygulanmaz. Ancak kodlamayan bölgede bulunan ve LoF splicing sonucu oluşturduğu uygun RNA kanıtıyla gösterilen varyantlarda PVS1(RNA) uygulanabilir.**

---

## 7. “Kanıtın ağırlık merkezi hesaplamadan fonksiyonel deneye kayar”

**Yön olarak doğrudur, fakat fonksiyonel deney tek hâkim kanıt değildir.**

Kodlamayan varyantlarda hesaplamalı tahminlerin özgüllüğü genellikle kodlayan varyantlara göre daha düşüktür. Standart missense patojenite araçları noncoding varyantlara uygulanamaz; düzenleyici bölge tanımı, hücre tipi, hedef gen ve etki yönü ayrıca belirlenmelidir. ([Springer][2])

Fonksiyonel kanıt bu nedenle merkezi hâle gelir:

* hasta RNA’sında ekspresyon veya splicing,
* alel-spesifik ekspresyon,
* ilgili hücrede CRISPR perturbasyonu,
* promotör/enhancer reporter deneyleri,
* protein veya translasyon ölçümü,
* gerektiğinde kromatin erişilebilirliği ve temas analizleri.

Ancak işlevsel deneyin klinik ağırlığı şu koşullara bağlıdır:

* doğru hücre ve doku modelinin kullanılması,
* ilgili gelişim döneminin temsil edilmesi,
* uygun WT ve benign kontroller,
* varyantın gerçek endojen kromatin bağlamında değerlendirilmesi,
* ölçülen etkinin bilinen hastalık mekanizmasıyla aynı yönde olması,
* deneyin gen–hastalık için klinik olarak anlamlı eşikleri ayırt edebilmesi.

Noncoding rehberi fonksiyonel kanıtın çok önemli olduğunu belirtir; ancak uygun olmayan doku veya yalnız tek olası mekanizmayı ölçen negatif deneyler için `BS3` kullanılmaması gerektiğini özellikle vurgular. Ayrıca kromatin temas verisi çoğu zaman varyantı doğrudan patojenik ilan etmekten çok, düzenleyici eleman–hedef gen bağlantısını tanımlamak için kullanılır. ([Springer][2])

Bu nedenle kanıt mimarisi şöyledir:

[
\text{bölgenin işlevsel geçerliliği}
+
\text{doğru hedef gen}
+
\text{varyantın fonksiyonel etkisi}
+
\text{etki yönünün hastalık mekanizmasıyla uyumu}
+
\text{segregasyon/de novo/allelik kanıt}
+
\text{fenotip uyumu}
]

Hesaplama ortadan kalkmaz; **aday seçme ve hipotez üretme rolüne çekilir**. Fonksiyonel deney de tek başına değil, bağımsız genetik ve klinik kanıtlarla birleştirilir.

---

## 8. “TAD mimarisini tek nükleotid ölçeğine indirir” doğru mu?

Kısmen.

Bu bölüm:

* TF bağlanma motifleri,
* CTCF motifleri,
* promotörler,
* enhancer çekirdekleri,
* UTR motifleri

üzerindeki SNV ve küçük indelleri ele alabilir.

Ancak **enhancer hijacking ve TAD yeniden kablolanmasının klasik klinik örnekleri çoğunlukla yapısal varyant ölçeğindedir**. Bu nedenle:

> “Bölüm 8’deki mimariyi tek nükleotid ölçeğine indirir.”

yerine:

> **“Bölüm 8’de yapısal varyant ölçeğinde ele alınan düzenleyici mimarinin, SNV ve küçük indel düzeyindeki bozulma biçimlerini inceler.”**

denmesi daha doğru olur.

---

## Düzeltilmiş metin

> **Bölümün çekirdek tezi:** İnsan genomunun protein kodlayan ekzonları genomun `%2`’sinden daha azını oluşturur; buna karşın klinik dizileme ve sekans varyantı yorumlama pratiği tarihsel olarak büyük ölçüde protein kodlayan ekzonlar ve kanonik splice bölgeleri üzerinde yoğunlaşmıştır. Kodlamayan bölgelerdeki varyantlar bu tanısal kör noktanın önemli bir bölümünü oluşturur.
>
> **Bir düzenleyici varyant, protein kodlayan diziyi değiştirmeden hastalık yapabilir; çünkü bozulma proteinin aminoasit dizisinde değil, gen ürününün ne zaman, nerede, ne miktarda ve hangi transkript biçiminde üretileceğindedir.** Promotör varyantları transkripsiyon miktarını veya başlangıç bölgesini; enhancer varyantları hücre tipi, doku, gelişim dönemi ve ekspresyon düzeyini; 5′UTR varyantları translasyon başlangıcını, uORF kullanımını ve RNA kararlılığını; izolatör ve TAD sınırı varyantları ise enhancer–promotör temaslarını ve hedef gen seçimini bozabilir. Bununla birlikte bütün kodlamayan varyantlar saf düzenleyici değildir: intronik splice varyantları, kodlamayan RNA varyantları ve tekrar genişlemeleri farklı mekanizmalarla hastalık yapabilir.
>
> Buradan üç klinik sonuç çıkar. **Birincisi**, genom çapında kodlamayan varyant araştırmasında standart ekzom çoğunlukla yetersizdir; WGS veya hipoteze dayalı hedefli düzenleyici bölge analizi gerekir. WGS varyantı görünür kılar, ancak işlevsel elemanı, hedef geni ve patojenik etkiyi kendiliğinden belirlemez. **İkincisi**, doku veya gelişim dönemi özgül düzenleyici elemanların bozulması, bazı hastalıklarda dar veya organ-sınırlı fenotip oluşturabilir; ancak bu bütün noncoding varyantlar için genel bir kural değildir. **Üçüncüsü**, promotör, enhancer, UTR ve izolatör varyantlarında PVS1 genellikle uygulanmaz. Yorumlama; düzenleyici eleman–hedef gen ilişkisinin doğrulanması, etki yönünün hastalık mekanizmasıyla uyumu, fonksiyonel deney, segregasyon, de novo durum ve fenotip özgüllüğünün birlikte değerlendirilmesine dayanır. Buna karşılık LoF splicing sonucu oluşturan intronik varyantlarda, uygun RNA kanıtı ve gen-spesifik karar ağacı varsa PVS1(RNA) kullanılabilir.
>
> Bölüm 8’de yapısal varyant ölçeğinde ele alınan enhancer yeniden yönlenmesi ve üç boyutlu genom mimarisinin bozulması, bu bölümde SNV ve küçük indel düzeyindeki düzenleyici değişikliklerle tamamlanacaktır.

**Net sonuç:** Ana tez korunmalı; fakat “kodlamayan” yerine yer yer **“düzenleyici”** denmeli, WGS ve organ özgüllüğü koşullu yazılmalı, PVS1 cümlesine ise **splice varyantı istisnası** mutlaka eklenmelidir.

[1]: https://www.genome.gov/genetics-glossary/Exome?utm_source=chatgpt.com "Exome"
[2]: https://link.springer.com/article/10.1186/s13073-022-01073-3 "Recommendations for clinical interpretation of variants found in non-coding regions of the genome | Genome Medicine | Springer Nature Link"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4791538/?utm_source=chatgpt.com "Disruptions of Topological Chromatin Domains Cause Pathogenic Rewiring of Gene-Enhancer Interactions - PMC"
[4]: https://pubmed.ncbi.nlm.nih.gov/40015278/?fc=None&ff=20250228094520&v=2.18.0.post9+e462414&utm_source=chatgpt.com "Deletion of a single CTCF motif at the boundary of a chromatin domain with three FGF genes disrupts gene expression and embryonic development - PubMed"
[5]: https://pure.johnshopkins.edu/en/publications/using-the-acmgamp-framework-to-capture-evidence-related-to-predic/?utm_source=chatgpt.com "Using the ACMG/AMP framework to capture evidence ..."


<br>

### C20 · Bölüm 14 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_14_Ayni_Gen_Farkli_Hastalik.md` · 2.3 Üçüncü eksen: varyant konumu — domain ve izoform · satır 92

> Aynı doku-seçicilik sorusu daha geniş bir çerçevede de sorulmuştur: laminler bütün hücrelerde ifade edilirken hastalıkların neden büyük ölçüde doku-seçici fenotiplerle ortaya çıktığı hâlâ tam açıklanmış değildir; hastalık yapan varyantların nükleer morfolojiyi bozduğu gösterilmiştir, ancak bu bozulmanın patolojiye nasıl dönüştüğü ancak anlaşılmaya başlanmıştır (Worman, 2012). ⚠️ Dolayısıyla ***domain–fenotip haritaları güçlü örüntüler sunar, ancak birebir öngörü aracı olarak kullanılmamalıdır***.

**Sorulan:** Domain–fenotip haritalarının sınırı doğru çizilmiş mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Sınırın ana fikri doğru çizilmiş:** domain–fenotip ilişkileri, **kohort düzeyinde olasılıksal zenginleşmeler** gösterebilir; ancak tek bir `LMNA` varyantından birebir klinik fenotip çıkarmaya uygun değildir.

Bununla birlikte paragrafta iki düzeltme gerekir:

1. “Laminler bütün hücrelerde ifade edilir” yerine **“A-tipi laminler çoğu farklılaşmış somatik hücrede geniş biçimde ifade edilir”** denmelidir.
2. Worman 2012’deki “patolojiye dönüşüm ancak anlaşılmaya başlanmıştır” ifadesi artık tarihsel kalmıştır. Mekanizma hâlâ tamamen çözülmemiştir; ancak 2026 itibarıyla yalnız nükleer morfoloji bozukluğundan ibaret olmayan çok sayıda patojenik yol tanımlanmıştır. ([PubMed][1])

## Domain–fenotip haritaları ne ölçüde doğrudur?

`LMNA` için bazı tekrarlanabilir örüntüler vardır:

* Santral **α-helikal rod domainindeki** varyantlar çizgili kas hastalıkları ve kardiyomiyopati fenotiplerinde daha sık görülür.
* C-terminal tail ve özellikle **Ig-like fold** çevresindeki varyantlar lipodistrofi ve bazı metabolik/progeroid fenotiplerde zenginleşir.
* `p.Arg482` çevresindeki varyantlar Dunnigan tipi ailesel parsiyel lipodistrofiyle güçlü biçimde ilişkilidir.
* Bazı varyant sınıfları, özellikle kardiyomiyopatide, klinik riskle ilişkilendirilebilir; örneğin truncating/non-missense varyantlar bazı çalışmalarda daha yüksek ventriküler aritmi riskiyle ilişkilendirilmiştir. ([PubMed Central (PMC)][2])

Ancak bunlar:

[
\text{domain}
\rightarrow
\text{tek ve zorunlu fenotip}
]

biçiminde kurallar değildir.

Daha doğru ilişki:

[
\text{domain veya varyant sınıfı}
\rightarrow
\text{belirli fenotiplerde istatistiksel zenginleşme}
]

şeklindedir.

Sistematik değerlendirmelerde aynı aminoasit değişikliğinin farklı bireylerde farklı organ sistemlerini etkileyebildiği, aynı aile içinde değişkenlik görülebildiği ve çoklu sistem tutulumlu overlap fenotiplerinin sık olduğu gösterilmiştir. Güncel GeneReviews da `LMNA` ilişkili dilate kardiyomiyopati için güvenilir, spesifik bir genotip–fenotip korelasyonunun kurulmadığını belirtmektedir. ([PubMed Central (PMC)][3])

Bu nedenle metindeki:

> “güçlü örüntüler sunar”

ifadesi biraz yumuşatılmalıdır:

> **“bazı belirgin ve tekrarlanabilir zenginleşme örüntüleri sunabilir.”**

“Güçlü” sözcüğü özellikle bütün domainlere genellenirse kanıt düzeyini aşabilir.

## Neden bireysel öngörü aracı değildir?

### 1. Aynı domain içindeki varyantların moleküler sonuçları farklıdır

Aynı protein bölgesindeki iki varyanttan biri:

* protein miktarını azaltabilir,
* filament montajını bozabilir,
* dominant-negatif etki yapabilir,
* belirli bir partner etkileşimini değiştirebilir,
* lamin A işlenmesini etkileyebilir,
* kromatin bağlanmasını bozabilir.

Dolayısıyla yalnız koordinat veya domain bilgisi, mekanizmayı belirlemez.

### 2. Aynı varyant farklı fenotipler oluşturabilir

Aynı `LMNA` varyantı:

* izole kardiyak hastalık,
* iskelet kası hastalığı,
* kardiyomüsküler overlap,
* metabolik veya daha geniş bir laminopati

şeklinde ortaya çıkabilir. Bu durum yaşa bağlı penetrans, genetik arka plan, alel ekspresyonu, dokuya özgü partnerler ve çevresel/mekanik yük gibi değişkenlerle ilişkilidir. ([PubMed Central (PMC)][2])

### 3. Fenotipler zaman içinde genişleyebilir

Başlangıçta izole kas veya kardiyak fenotip olarak görülen bireylerde daha sonra diğer sistem bulguları gelişebilir. Bu nedenle erken yaştaki “doku-seçici” görünüm, yaşam boyu kesin organ sınırlılığı anlamına gelmez. `LMNA` ilişkili hastalıklarda kardiyak, nöromüsküler ve metabolik özelliklerin aynı kişide örtüşebildiği güncel klinik kaynaklarda vurgulanmaktadır. ([Wiley Online Library][4])

### 4. Domain korelasyonu ile klinik prognoz korelasyonu aynı değildir

Bir domainin belirli hastalık kategorisinde zenginleşmesi ile tanı konmuş bir hastada varyant tipinin aritmi veya ilerleme riskine katkıda bulunması iki ayrı sorudur.

Örneğin truncating `LMNA` varyantlarının kardiyak risk modellerinde kullanılması:

> “Bu varyant kardiyomiyopati yapacaktır.”

demekten çok:

> “Zaten `LMNA` kardiyomiyopatisi olan bir bireyde risk tahminine katkıda bulunabilir.”

anlamına gelir. ([JAMA Network][5])

## Doku seçiciliği açıklaması güncel mi?

Worman’ın 2012’de ortaya koyduğu temel paradoks hâlâ geçerlidir:

> Geniş biçimde ifade edilen bir nükleer iskelet proteini nasıl olup da kas, yağ dokusu, periferik sinir veya belirli gelişimsel sistemlerde seçici hastalık oluşturur?

Ancak bugün açıklama yalnız “nükleer şekil bozukluğu” üzerinden kurulmaz. Başlıca ve birbiriyle örtüşen modeller şunlardır:

* **Mekanik kırılganlık:** Kalp ve iskelet kası gibi yüksek mekanik stres altındaki hücrelerde nükleus ve nükleoskeletonun hasara daha açık olması.
* **LINC kompleksi ve mekanotransdüksiyon bozukluğu:** Nükleus–sitoiskelet bağlantısının ve mekanik sinyal aktarımının bozulması.
* **Kromatin ve gen düzenlenmesi:** Lamina-associated domain organizasyonu, heterokromatin konumlanması ve dokuya özgü gen programlarının değişmesi.
* **Dokuya özgü protein etkileşimleri:** Laminlerin farklı hücrelerde farklı nükleer zarf ve düzenleyici proteinlerle çalışması.
* **DNA hasarı, redoks stresi ve hücresel senesens.**
* **MAPK, TGF-β, YAP/TAZ, mTOR ve diğer sinyal yolaklarında düzensizlik.**
* **Proteostaz, otofaji ve farklılaşma kusurları.** ([PubMed Central (PMC)][6])

Bu modeller birbirini dışlamaz. Aynı varyant farklı hücrelerde farklı mekanizmaların bileşimiyle fenotip oluşturabilir.

Ayrıca nükleer morfoloji bozukluğu:

* patogenez hakkında değerli bir hücresel gösterge olabilir,
* fakat tek başına hastalığın bütün mekanizmasını açıklamaz,
* klinik şiddetin veya hangi organın tutulacağının güvenilir bir ölçüsü değildir.

Bu nedenle Worman 2012 tarihsel olarak kullanılabilir; ancak güncel bir kaynakla tamamlanmalıdır.

## Önerilen düzeltilmiş metin

> **Aynı doku-seçicilik sorusu laminopatilerde daha geniş bir çerçevede ortaya çıkar. `LMNA` kaynaklı lamin A/C proteinleri çoğu farklılaşmış somatik hücrede geniş biçimde ifade edildiği hâlde, patojenik varyantlar çizgili kas, kalp, yağ dokusu, periferik sinir veya belirli gelişimsel sistemleri görece seçici biçimde etkileyebilir. Bu paradoks henüz bütünüyle çözülmemiştir. Hastalık varyantlarının nükleer morfolojiyi ve mekanik dayanıklılığı bozabildiği gösterilmiş olmakla birlikte güncel modeller; nükleus–sitoiskelet bağlantısı, mekanotransdüksiyon, kromatin organizasyonu, dokuya özgü gen ekspresyonu, protein etkileşimleri, DNA hasarı, proteostaz ve hücresel stres yolaklarını birlikte içermektedir.**
>
> **`LMNA` varyantlarının protein üzerindeki konumu bazı kohort düzeyinde genotip–fenotip zenginleşmeleri gösterir: rod domainindeki varyantlar çizgili kas ve kardiyak fenotiplerde, tail/Ig-like bölgelerdeki bazı varyantlar ise lipodistrofik ve metabolik fenotiplerde daha sık görülür. Ancak bu ilişkiler olasılıksaldır. Aynı domain, hatta aynı varyant farklı bireylerde farklı, örtüşen veya zaman içinde genişleyen fenotipler oluşturabilir. Bu nedenle domain–fenotip haritaları mekanizma kurma, fenotip genişletme ve izlem planlama açısından yararlıdır; tek başına bireysel fenotip veya prognoz öngörmek için kullanılmamalıdır.**

## Kaynak kullanımı

Worman 2012 metinde kalabilir:

* **Worman HJ.** *Nuclear lamins and laminopathies.* Journal of Pathology. 2012;226:316–325. DOI: `10.1002/path.2999`. ([Pathways Journal][7])

Ancak yanına daha güncel bir sentez eklenmelidir:

* **Worman HJ.** *Molecular Pathology of Laminopathies.* Annual Review of Pathology. 2022;17:159–180. DOI: `10.1146/annurev-pathol-042220-034240`. ([Annual Reviews][8])
* LMNA genotip–fenotip sınırlarını sistematik ele alan 2022 meta-özet de domain korelasyonlarının genel olarak sınırlı olduğunu destekler. ([PubMed][9])

**Net sonuç:** Son uyarı doğrudur. Ancak **“güçlü domain–fenotip haritaları”** yerine **“kohort düzeyinde tekrarlanabilir fakat örtüşen olasılıksal örüntüler”** denmesi daha isabetlidir. Worman 2012’nin “ancak anlaşılmaya başlanmıştır” ifadesi de güncellenerek **“önemli mekanizmalar tanımlanmış olmakla birlikte doku seçiciliği tam açıklanamamıştır”** biçimine çevrilmelidir.

[1]: https://pubmed.ncbi.nlm.nih.gov/21953297/?utm_source=chatgpt.com "Nuclear lamins and laminopathies - PubMed"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8059629/?utm_source=chatgpt.com "Genotype-phenotype analysis of LMNA-related diseases predicts phenotype-selective alterations in lamin phosphorylation - PMC"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9777268/?utm_source=chatgpt.com "Genotype-Phenotype Correlations in Human Diseases Caused by Mutations of LINC Complex-Associated Genes: A Systematic Review and Meta-Summary - PMC"
[4]: https://onlinelibrary.wiley.com/doi/full/10.1002%2Fcns3.20075?utm_source=chatgpt.com "LMNA‐related muscular dystrophy presenting as an ..."
[5]: https://jamanetwork.com/journals/jamacardiology/fullarticle/2835674?utm_source=chatgpt.com "Prognostic Implications of LMNA Cardiomyopathy Genetic ..."
[6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4522394/?utm_source=chatgpt.com "Nuclear membrane diversity: underlying tissue-specific pathologies in disease? - PMC"
[7]: https://pathsocjournals.onlinelibrary.wiley.com/doi/full/10.1002/path.2999?utm_source=chatgpt.com "Nuclear lamins and laminopathies - Worman - 2012 - The Journal of Pathology - Wiley Online Library"
[8]: https://www.annualreviews.org/content/journals/10.1146/annurev-pathol-042220-034240?utm_source=chatgpt.com "Molecular Pathology of Laminopathies | Annual Reviews"
[9]: https://pubmed.ncbi.nlm.nih.gov/36552829/?utm_source=chatgpt.com "Genotype-Phenotype Correlations in Human Diseases Caused by Mutations of LINC Complex-Associated Genes: A Systematic Review and Meta-Summary - PubMed"


<br>

### C21 · Bölüm 14 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_14_Ayni_Gen_Farkli_Hastalik.md` · 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu) · satır 418

> ### 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu)
> "Bu bölümdeki tüm kaynakların PMID/DOI bilgisini kontrol et. PMID veya DOI veremediğin kaynağı çıkar. Kaynağı olmayan iddiayı 'kaynak doğrulaması gerekli' olarak işaretle."
>
> **Bu bölüm için durum:** **22/22 kaynak PMID+DOI doğrulandı** (9'u bu oturumda PubMed MCP ile — Thaxton 2022, Strande 2017, Toydemir 2006, Eriksson 2003, Worman 2012, Bertrand 2011, Marini 2007, Kaler 2011, Mantovani 2018; 12'si Bölüm_00 kaynak kütüğünden yeniden kullanıldı). Bölüm, 27.07.2026 tarihli iddia-düzeyi doğrulama turundan geçmiştir; turda *SCN2A*/otizm atfı Sanders 2018'e taşınmış ve "altı eksen" çerçevesi 🏷️ etiketlenmiştir (bkz. `Dogrulama_Kutugu.md`).
>
> **İşaretlenen iddialar:** (1) ⚠️ Domain–fenotip haritaları güçlü örüntüler sunar ancak birebir öngörü aracı değildir; laminopatilerde nükleer morfoloji bozukluğunun patolojiye nasıl dönüştüğü henüz tam açıklanmamıştır (Worman, 2012). (2) *COL4A3*/*COL4A4* (ince bazal membran nefropatisi ↔ otozomal resesif Alport sendromu) ve *RYR1* (malign hipertermi/santral kor ↔ bialelik konjenital miyopati) örnekleri, kalıtım modu eksenini örneklemek üzere ***yerleşik ders bilgisi düzeyinde verilmiştir; bu bölümde ayrıca PubMed doğrulaması yapılmamıştır***. (3) *FGFR3* varyant–fenotip eşleşmeleri (p.Asn540Lys, p.Gly380Arg, p.Lys650Met, p.Lys650Glu, p.Arg248Cys) yerleşik klinik genetik bilgisidir; bu bölümde doğrudan kaynaklanan noktalar p.Arg621His (Toydemir, 2006) ve p.Gly380Arg'nin konstitütif aktivasyonudur (Webster ve Donoghue, 1996). (3) 🏷️ **"Allelik serinin altı ekseni" çerçevesi kitabın pedagojik sentezidir**; literatürde bu adla yerleşik bir sınıflandırma değildir — eksenlerin bileşenleri kaynaklı, gruplama editöryaldir (§2 girişindeki etikete bkz.).

**Sorulan:** COL4A3/COL4A4 ve RYR1 örneklerinin kaynaksız, ders bilgisi olarak verilmesi kabul edilebilir mi? İçerik doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**İki örneğin temel biyolojisi doğrudur; ancak bu biçimde kaynaksız ve “yerleşik ders bilgisi” etiketiyle bırakılması uygun değildir.** Çünkü bunlar basit Mendel kuralları değil, **gen-spesifik allelik durum–kalıtım–fenotip eşleştirmeleridir**. Üstelik her iki örnekte de sınırlar ve terminoloji zaman içinde değişmiştir.

Ayrıca:

> **“22/22 kaynağın PMID/DOI’si doğrulandı”**, yalnız mevcut kaynakların bibliyografik kimliğinin doğru olduğunu gösterir.
> **Bölümdeki bütün iddiaların kaynaklandığını göstermez.**

COL4A3/COL4A4 ve RYR1 iddiaları ayrıca doğrulanmadıysa, bölüm teknik olarak tam bir **iddia-düzeyi doğrulama turundan geçmiş** sayılmaz.

---

# 1. `COL4A3` / `COL4A4` örneği

Mevcut özet:

> İnce bazal membran nefropatisi ↔ otozomal resesif Alport sendromu

**Çekirdek fikir doğru, fakat terminolojik ve mekanistik olarak fazla ikili.**

## Doğru olan

* `COL4A3` veya `COL4A4` genindeki **heterozigot patojenik/olası patojenik varyantlar**, otozomal dominant COL4A3/COL4A4 ilişkili Alport spektrumuna yol açabilir.
* Klinik tablo sıklıkla persistan glomerüler hematüri ve ince glomerüler bazal membranla başlar; proteinüri, kronik böbrek hastalığı ve nadiren son dönem böbrek hastalığı gelişebilir.
* Aynı genlerden birinde **bialelik patojenik varyantlar**, otozomal resesif Alport sendromuna ve genel olarak daha ağır/erken başlangıçlı hastalığa neden olur. Güncel kaynaklar heterozigot bireylerin yalnızca “ARAS taşıyıcısı” olarak adlandırılmasını önermemektedir; çünkü bu bireyler de klinik bulgu geliştirebilir. ([Ulusal Biyoteknoloji Bilgi Merkezi][1])

## Düzeltilmesi gereken taraf

“İnce bazal membran nefropatisi” burada genetik olarak ayrı ve daima benign bir hastalık gibi gösterilmemelidir. Bu terim:

* histopatolojik bir bulguyu,
* klinik bir fenotipi,
* geçmişte “benign familyal hematüri” denilen grubu

anlatmak için kullanılmıştır. Güncel yaklaşım, heterozigot `COL4A3/COL4A4` hastalığını daha geniş bir **Alport spektrumu veya COL4A3/4 ilişkili glomerülopati** içinde ele almaktadır. 2024 ERKNet/ERA/ESPN rehberi de bu hastalık grubunun çoklu kalıtım biçimleri, değişken penetrans ve geniş fenotip spektrumu taşıdığını vurgular. ([PubMed][2])

Dolayısıyla şu eşleştirme:

[
\text{heterozigot}=\text{TBMN}
\quad\text{ve}\quad
\text{bialelik}=\text{ARAS}
]

öğretici olmakla birlikte mutlak değildir.

### Daha doğru ifade

> **`COL4A3`/`COL4A4`: Heterozigot patojenik varyantlar otozomal dominant Alport spektrumuna yol açabilir; fenotip çoğu zaman hematüri ve ince glomerüler bazal membranla sınırlı veya hafif başlar, ancak bazı bireylerde ilerleyici böbrek hastalığı gelişebilir. Aynı genlerden birindeki bialelik patojenik varyantlar ise otozomal resesif Alport sendromuna ve genellikle daha ağır fenotipe neden olur.**

### Eklenmesi uygun kaynak

**Torra R, et al.** *Diagnosis, management and treatment of the Alport syndrome—2024 guideline on behalf of ERKNet, ERA and ESPN.*
PMID: **39673454**
DOI: **10.1093/ndt/gfae265** ([PubMed][2])

Alternatif/ek kaynak:

**Savige J, et al.** *Guidelines for Genetic Testing and Management of Alport Syndrome.*
PMID: **34930753**
DOI: **10.2215/CJN.04230321** ([PubMed][3])

---

# 2. `RYR1` örneği

Mevcut özet:

> Malign hipertermi/santral kor ↔ bialelik konjenital miyopati

**Genel allelik seri fikri doğru; eşleştirme fazla temiz ve kısmen yanıltıcıdır.**

## Doğru olan

`RYR1` aynı gen içinde farklı kalıtım biçimleri ve mekanizmalar gösteren güçlü bir örnektir:

* Heterozigot, çoğunlukla işlev kazanımlı varyantlar → otozomal dominant malign hipertermi yatkınlığı
* Heterozigot dominant-negatif veya başka işlev bozucu varyantlar → dominant `RYR1` ilişkili miyopati, klasik olarak santral kor hastalığı
* Bialelik varyantlar, özellikle en az bir LoF veya ağır hipomorfik alel → otozomal resesif konjenital miyopati; multiminicore hastalığı, sentronükleer miyopati, konjenital fiber-type disproportion ve core miyopati gibi tablolar

2026 EMQN rehberi, `RYR1` varyantlarının malign hipertermi yatkınlığı, egzersiz ilişkili rabdomiyoliz ve hem dominant hem resesif konjenital miyopatilerle ilişkili olduğunu belirtmektedir. Genel mekanistik eğilim GoF–malign hipertermi, dominant-negatif–dominant miyopati ve LoF–resesif miyopati yönündedir. ([Nature][4])

## Fazla basitleştirilen taraf

### Santral kor yalnız dominant değildir

Santral kor hastalığı klasik olarak dominant `RYR1` varyantlarıyla ilişkilidir; ancak core patolojisi ve core miyopati spektrumu bialelik hastalıkta da görülebilir. Buna karşılık resesif `RYR1` hastalığı yalnızca tek bir histolojik alt tipe indirgenemez. ([Nature][4])

### Malign hipertermi ve miyopati tamamen ayrık değildir

Bazı `RYR1` varyantları:

* yalnız malign hipertermi yatkınlığı,
* yalnız dominant veya resesif miyopati,
* malign hipertermi yatkınlığı ile miyopatinin birlikte bulunduğu örtüşen fenotipler

oluşturabilir. 2026 EMQN rehberi belirli missense varyantların hem malign hipertermi hem dominant veya resesif core miyopatiyle ilişkili olabildiğini özellikle belirtmektedir. ([Nature][4])

Bu nedenle şu basit şema güvenli değildir:

[
\text{heterozigot RYR1}
=======================

\text{MH veya CCD}
]

[
\text{bialelik RYR1}
====================

\text{konjenital miyopati}
]

Zigozite tek başına fenotipi belirlemez; varyant mekanizması, protein bölgesi, ikinci alel ve klinik bağlam birlikte değerlendirilmelidir.

### Daha doğru ifade

> **`RYR1`: Heterozigot işlev kazanımlı varyantlar sıklıkla otozomal dominant malign hipertermi yatkınlığına; heterozigot dominant-negatif varyantlar dominant miyopatiye, özellikle santral kor hastalığına yol açabilir. Bialelik LoF veya hipomorfik varyantlar ise genellikle otozomal resesif konjenital miyopati spektrumu oluşturur. Bununla birlikte malign hipertermi ve miyopati fenotipleri örtüşebilir; santral kor veya diğer histopatolojik paternler tek bir kalıtım biçimine özgü değildir.**

### Eklenmesi uygun kaynak

**Robinson RL, et al.** *EMQN Best Practice Guidelines for Genetic Testing and Reporting in RYR1-related disorders.*
PMID: **42120542**
DOI: **10.1038/s41431-026-02121-x** ([PubMed][5])

Malign hipertermi varyant yorumlaması için ek VCEP kaynağı:

**Johnston JJ, et al.** *Variant curation expert panel recommendations for RYR1 pathogenicity classifications in malignant hyperthermia susceptibility.*
PMID: **33767344**
DOI: **10.1038/s41436-021-01125-w** ([PubMed][6])

---

## Kaynaklandırma kararı

Bu iki örnek için doğru editöryal politika:

| İddia türü                                                  |      Kaynaksız bırakılabilir mi? |
| ----------------------------------------------------------- | -------------------------------: |
| “Otozomal resesif hastalıkta genellikle iki alel etkilenir” | Ders kitabı düzeyinde bazen evet |
| “Aynı gen farklı zigozitelerde farklı hastalık yapabilir”   |    Genel cümle olarak bazen evet |
| `COL4A3/COL4A4` heterozigot–bialelik fenotip eşleşmesi      |                        **Hayır** |
| `RYR1` varyant mekanizması–kalıtım–fenotip eşleşmesi        |                        **Hayır** |
| Spesifik sendrom, histoloji veya terminoloji iddiası        |                        **Hayır** |

“Yerleşik ders bilgisi” etiketi kaynak zorunluluğunu kaldırmamalıdır. Özellikle kitabınızın kendi doğrulama komutu:

> “Kaynağı olmayan iddiayı kaynak doğrulaması gerekli olarak işaretle.”

dediği için, bu iki iddia ya kaynaklandırılmalı ya da doğrulanmamış olarak kalmalıdır. Kaynak eklenmeden **“27.07.2026 tarihli iddia-düzeyi doğrulama turundan geçmiştir”** denmesi metodolojik olarak tutarlı değildir.

## Doğrulama kütüğü için önerilen yeni kayıt

> **(2) `COL4A3/COL4A4` ve `RYR1` allelik seri örnekleri güncel gen-spesifik kaynaklarla doğrulandı.** Heterozigot `COL4A3/COL4A4` patojenik varyantları otozomal dominant Alport spektrumuna, bialelik varyantlar otozomal resesif Alport sendromuna yol açabilir; “ince bazal membran nefropatisi” ayrı ve zorunlu olarak benign bir kategori olarak kullanılmamıştır (Torra ve ark., 2024 rehberi; PMID 39673454; DOI 10.1093/ndt/gfae265). `RYR1` için heterozigot GoF–malign hipertermi, heterozigot DN–dominant miyopati ve bialelik LoF/hipomorfik–resesif miyopati eğilimleri korunmuş; ancak örtüşen fenotipler ve istisnalar belirtilmiştir (Robinson ve ark., 2026; PMID 42120542; DOI 10.1038/s41431-026-02121-x).

**Net sonuç:** Örnekler kalmalı, fakat ikisi de kaynaklandırılmalıdır. `COL4A3/COL4A4` örneğinde **TBMN terminolojisi yumuşatılmalı**; `RYR1` örneğinde ise **dominant MH/CCD ile bialelik miyopati arasında kesin bir sınır varmış gibi gösterilmemelidir.**

Ayrıca işaretlenen iddialar listesinde iki ayrı madde **“(3)”** olarak numaralandırılmış; “Allelik serinin altı ekseni” maddesi **(4)** yapılmalıdır.

[1]: https://www.ncbi.nlm.nih.gov/books/NBK1207/ "Alport Syndrome - GeneReviews® - NCBI Bookshelf"
[2]: https://pubmed.ncbi.nlm.nih.gov/39673454/ "Diagnosis, management and treatment of the Alport syndrome - 2024 guideline on behalf of ERKNet, ERA and ESPN - PubMed"
[3]: https://pubmed.ncbi.nlm.nih.gov/34930753/?utm_source=chatgpt.com "Guidelines for Genetic Testing and Management of Alport Syndrome - PubMed"
[4]: https://www.nature.com/articles/s41431-026-02121-x "EMQN Best Practice Guidelines for Genetic Testing and Reporting in RYR1-related disorders | European Journal of Human Genetics"
[5]: https://pubmed.ncbi.nlm.nih.gov/42120542/?utm_source=chatgpt.com "EMQN Best Practice Guidelines for Genetic Testing and Reporting in RYR1-related disorders - PubMed"
[6]: https://pubmed.ncbi.nlm.nih.gov/33767344/?utm_source=chatgpt.com "Variant curation expert panel recommendations for RYR1 pathogenicity classifications in malignant hyperthermia susceptibility - PubMed"


<br>

### C22 · Bölüm 14 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_14_Ayni_Gen_Farkli_Hastalik.md` · 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu) · satır 418

> ### 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu)
> "Bu bölümdeki tüm kaynakların PMID/DOI bilgisini kontrol et. PMID veya DOI veremediğin kaynağı çıkar. Kaynağı olmayan iddiayı 'kaynak doğrulaması gerekli' olarak işaretle."
>
> **Bu bölüm için durum:** **22/22 kaynak PMID+DOI doğrulandı** (9'u bu oturumda PubMed MCP ile — Thaxton 2022, Strande 2017, Toydemir 2006, Eriksson 2003, Worman 2012, Bertrand 2011, Marini 2007, Kaler 2011, Mantovani 2018; 12'si Bölüm_00 kaynak kütüğünden yeniden kullanıldı). Bölüm, 27.07.2026 tarihli iddia-düzeyi doğrulama turundan geçmiştir; turda *SCN2A*/otizm atfı Sanders 2018'e taşınmış ve "altı eksen" çerçevesi 🏷️ etiketlenmiştir (bkz. `Dogrulama_Kutugu.md`).
>
> **İşaretlenen iddialar:** (1) ⚠️ Domain–fenotip haritaları güçlü örüntüler sunar ancak birebir öngörü aracı değildir; laminopatilerde nükleer morfoloji bozukluğunun patolojiye nasıl dönüştüğü henüz tam açıklanmamıştır (Worman, 2012). (2) *COL4A3*/*COL4A4* (ince bazal membran nefropatisi ↔ otozomal resesif Alport sendromu) ve *RYR1* (malign hipertermi/santral kor ↔ bialelik konjenital miyopati) örnekleri, kalıtım modu eksenini örneklemek üzere **yerleşik ders bilgisi** düzeyinde verilmiştir; bu bölümde ayrıca PubMed doğrulaması yapılmamıştır. (3) *FGFR3* varyant–fenotip eşleşmeleri (p.Asn540Lys, p.Gly380Arg, p.Lys650Met, p.Lys650Glu, p.Arg248Cys) ***yerleşik klinik genetik bilgisidir***; bu bölümde doğrudan kaynaklanan noktalar p.Arg621His (Toydemir, 2006) ve p.Gly380Arg'nin konstitütif aktivasyonudur (Webster ve Donoghue, 1996). (3) 🏷️ **"Allelik serinin altı ekseni" çerçevesi kitabın pedagojik sentezidir**; literatürde bu adla yerleşik bir sınıflandırma değildir — eksenlerin bileşenleri kaynaklı, gruplama editöryaldir (§2 girişindeki etikete bkz.).

**Sorulan:** Listelenen FGFR3 varyant–fenotip eşleşmelerinin tamamı doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Evet, listelenen beş temel varyant–fenotip eşleşmesinin tamamı doğrudur.** Bunlar `FGFR3` allelik serisinin klasik örnekleridir:

| Varyant         | Temel fenotip eşleşmesi     | Değerlendirme |
| --------------- | --------------------------- | ------------- |
| **p.Asn540Lys** | Hipokondroplazi             | Doğru         |
| **p.Gly380Arg** | Akondroplazi                | Doğru         |
| **p.Lys650Met** | SADDAN                      | Doğru         |
| **p.Lys650Glu** | Tanatoforik displazi tip II | Doğru         |
| **p.Arg248Cys** | Tanatoforik displazi tip I  | Doğru         |

Ancak bunlar **“bu varyant yalnızca ve daima bu fenotipi oluşturur”** biçiminde kullanılmamalıdır. Özellikle akondroplazi–hipokondroplazi sınırında klinik örtüşme, `p.Lys650Met` için ise ağır FGFR3 kondrodisplazi spektrumu bulunabilir.

---

## 1. `p.Asn540Lys` → hipokondroplazi

Doğru ve en yerleşik eşleşmelerden biridir.

Güncel MANE transkriptiyle iki farklı nükleotid değişikliği aynı protein sonucunu oluşturabilir:

* `NM_000142.5:c.1620C>A`
* `NM_000142.5:c.1620C>G`

Her ikisi de:

[
p.Asn540Lys
]

sonucunu verir. Güncel GeneReviews, bu iki varyantı hipokondroplazide ilk hedeflenecek değişiklikler olarak belirtmekte ve birlikte moleküler olarak tanımlanmış olguların yaklaşık `%70–80`’ini açıklayabildiklerini bildirmektedir. Ayrıca `p.Asn540Lys` taşıyan hipokondroplazi olgularının ortalama olarak diğer bazı hipokondroplazi genotiplerinden daha belirgin fenotipe sahip olabileceği belirtilir. ([Ulusal Biyoteknoloji Bilgi Merkezi][1])

Temel kaynaklar:

* Bellus et al., 1995 — PMID **7670477**, DOI **10.1038/ng0795-357**
* Prinos et al., 1995 — PMID **8589686**, DOI **10.1093/hmg/4.11.2097** ([Nature][2])

**Kullanılacak karşılık:**

> `FGFR3 p.Asn540Lys` — klasik ve en sık hipokondroplazi varyantı.

---

## 2. `p.Gly380Arg` → akondroplazi

Doğrudur. Bu, akondroplazinin açık ara en sık nedenidir.

İki farklı nükleotid değişikliği aynı aminoasit değişimini oluşturur:

* `NM_000142.5:c.1138G>A`
* `NM_000142.5:c.1138G>C`

Her ikisi de:

[
p.Gly380Arg
]

sonucunu verir. Güncel ClinVar ve GeneReviews bu değişimi klasik akondroplazi varyantı olarak tanımlamaktadır. ([Ulusal Biyoteknoloji Bilgi Merkezi][3])

Temel kaynak:

* Shiang et al., 1994 — PMID **7913883**, DOI **10.1016/0092-8674(94)90302-6** ([Springer][4])

### Küçük sınır

`p.Gly380Arg` ile `p.Asn540Lys` arasında klinik olarak mutlak bir duvar yoktur. Hipokondroplazi ve hafif akondroplazi fenotipleri bazı hastalarda örtüşebilir; bu nedenle GeneReviews, hipokondroplazi şüphesi olan olgularda hem `p.Asn540Lys` hem de `p.Gly380Arg` oluşturan değişikliklerin değerlendirilmesini önerir. ([Ulusal Biyoteknoloji Bilgi Merkezi][1])

Dolayısıyla:

> `p.Gly380Arg` → **esas olarak akondroplazi**

denmelidir; “başka hiçbir fenotipte görülemez” denmemelidir.

---

## 3. `p.Lys650Met` → SADDAN

Doğrudur. Tam fenotip adı:

> **Severe achondroplasia with developmental delay and acanthosis nigricans — SADDAN**

Doğru HGVS:

[
\texttt{NM_000142.5:c.1949A>T, p.Lys650Met}
]

Tavormina ve arkadaşları bu varyantı ağır iskelet displazisi, nörogelişimsel bozukluk ve çocuklukta gelişen yaygın akantozis nigrikans ile ilişkili ayrı bir fenotip olarak tanımlamıştır. ([PubMed][5])

Temel kaynak:

* Tavormina et al., 1999 — PMID **10053006**, DOI **10.1086/302275**

### Önemli nüans

`p.Lys650Met` için yalnızca:

> “ağır akondroplazi”

yazmak eksik kalır. **SADDAN** adı kullanılmalıdır. Bununla birlikte nadir olgularda TD-benzeri radyolojik ve klinik özelliklerle örtüşen ağır bir FGFR3 kondrodisplazi fenotipi bildirilmiştir; dolayısıyla sınır tamamen keskin değildir. ([WashU Research Profiles][6])

---

## 4. `p.Lys650Glu` → tanatoforik displazi tip II

Doğrudur ve eşleşme oldukça güçlüdür.

Doğru HGVS:

[
\texttt{NM_000142.5:c.1948A>G, p.Lys650Glu}
]

Tavormina ve arkadaşlarının ilk serisinde bu varyant, incelenen TD tip II olgularının tamamında saptanmıştır. Güncel ClinVar da bu değişimi tanatoforik displazi tip II ile patojenik olarak ilişkilendirir. ([PubMed][7])

Temel kaynak:

* Tavormina et al., 1995 — PMID **7773297**, DOI **10.1038/ng0395-321**

### Nomenklatür açısından kritik ayrım

Birbirine komşu iki değişiklik karıştırılmamalıdır:

| Fenotip       | DNA değişikliği | Protein       |
| ------------- | --------------- | ------------- |
| **TD tip II** | `c.1948A>G`     | `p.Lys650Glu` |
| **SADDAN**    | `c.1949A>T`     | `p.Lys650Met` |

Bu ayrım kitapta açık yazılmalıdır. ([Ulusal Biyoteknoloji Bilgi Merkezi][8])

---

## 5. `p.Arg248Cys` → tanatoforik displazi tip I

Doğrudur.

Doğru HGVS:

[
\texttt{NM_000142.5:c.742C>T, p.Arg248Cys}
]

Bu varyant ekstrasellüler bölgede yeni bir sistein oluşturur ve tanatoforik displazi tip I’in en sık tekrarlayan varyantlarından biridir. İlk geniş çalışmada 39 TD tip I olgusunun 22’sinde saptanmıştır; güncel ClinVar kaydı da TD tip I için patojenik ve çelişkisizdir. ([Nature][9])

Temel kaynak:

* Tavormina et al., 1995 — PMID **7773297**, DOI **10.1038/ng0395-321**

Ancak:

> `p.Arg248Cys` = TD tip I’in tek nedeni

denmemelidir. `p.Ser249Cys`, `p.Tyr373Cys` ve başka ekstrasellüler sistein oluşturan varyantlar da TD tip I oluşturabilir.

---

## Mekanizma şiddeti açısından tablo

Bu varyantlar aynı gen içindeki **işlev kazanımı şiddet ve nitelik spektrumunu** göstermek için uygundur:

| Varyant       | Protein bölgesi                  | Klasik fenotip  |
| ------------- | -------------------------------- | --------------- |
| `p.Asn540Lys` | Proksimal tirozin kinaz bölgesi  | Hipokondroplazi |
| `p.Gly380Arg` | Transmembran domain              | Akondroplazi    |
| `p.Arg248Cys` | Ekstrasellüler Ig-benzeri domain | TD tip I        |
| `p.Lys650Met` | Kinaz aktivasyon halkası         | SADDAN          |
| `p.Lys650Glu` | Kinaz aktivasyon halkası         | TD tip II       |

Ancak bu sıralama basit bir:

[
\text{kinaz aktivitesi arttıkça fenotip doğrusal biçimde ağırlaşır}
]

modeline indirgenmemelidir. Reseptör işlenmesi, lokalizasyon, ligand bağımsız dimerizasyon, sinyalin süresi ve farklı aşağı akım yolakların aktivasyonu da fenotipi etkiler.

---

## `p.Gly380Arg` için “konstitütif aktivasyon” ifadesi

Webster ve Donoghue’nun 1996 çalışmasına dayanarak bu ifade **kabul edilebilir**. Çalışma `p.Gly380Arg` değişiminin liganddan bağımsız reseptör tirozin kinaz aktivitesini ve bazal fosforilasyonu artırdığını göstermiştir. Sonraki çalışmalar dimer kararlılığındaki artışın küçük fakat anlamlı olduğunu ve mekanizmanın yalnız “reseptör daima açık” şeklinde basit olmadığını göstermiştir. ([PubMed Central (PMC)][10])

Kitapta daha güvenli ifade:

> **`p.Gly380Arg`, liganddan bağımsız/bazal FGFR3 sinyalini artıran aktive edici bir varyanttır.**

“Tamamen ve sürekli aktif reseptör” ifadesinden daha doğrudur.

---

## Kaynaklandırma kararı

Bu beş eşleşme gerçekten yerleşik klinik genetik bilgisidir; fakat **spesifik varyant–fenotip iddiaları kaynaksız bırakılmamalıdır**. Bölümün kendi doğrulama ilkesiyle de uyumsuzdur.

Şu ifade:

> “22/22 kaynak doğrulandı ve bölüm iddia düzeyinde doğrulamadan geçti.”

ancak FGFR3 eşleşmeleri de kaynaklandırıldıktan sonra tam olarak savunulabilir.

### Doğrulama kütüğü için uygun yeni kayıt

> **FGFR3 allelik seri örnekleri varyant düzeyinde doğrulandı:** `p.Asn540Lys`—hipokondroplazi (Bellus ve ark., 1995; PMID 7670477; DOI 10.1038/ng0795-357), `p.Gly380Arg`—akondroplazi (Shiang ve ark., 1994; PMID 7913883; DOI 10.1016/0092-8674(94)90302-6), `p.Lys650Met`—SADDAN (Tavormina ve ark., 1999; PMID 10053006; DOI 10.1086/302275), `p.Lys650Glu`—tanatoforik displazi tip II ve `p.Arg248Cys`—tanatoforik displazi tip I (Tavormina ve ark., 1995; PMID 7773297; DOI 10.1038/ng0395-321). Eşleşmeler temel fenotipi gösterir; klinik örtüşme ve nadir istisnalar nedeniyle birebir deterministik kurallar olarak kullanılmamıştır.

**Net sonuç:** Beş eşleşme de doğru. Düzeltilmesi gereken şey içerik değil, **kaynaklandırma eksikliği ve eşleşmelerin mutlak bir varyant→tek fenotip haritası gibi sunulma riski**dir.

[1]: https://www.ncbi.nlm.nih.gov/books/NBK1477/pdf/Bookshelf_NBK1477.pdf "Hypochondroplasia"
[2]: https://www.nature.com/articles/ng0795-357?utm_source=chatgpt.com "A recurrent mutation in the tyrosine kinase domain of fibroblast growth factor receptor 3 causes hypochondroplasia | Nature Genetics"
[3]: https://www.ncbi.nlm.nih.gov/clinvar/variation/16327/ "VCV000016327.152 - ClinVar - NCBI"
[4]: https://link.springer.com/article/10.1186/s13023-024-03031-1 "Review of published 467 achondroplasia patients: clinical and mutational spectrum | Orphanet Journal of Rare Diseases | Springer Nature Link"
[5]: https://pubmed.ncbi.nlm.nih.gov/10053006/?utm_source=chatgpt.com "A novel skeletal dysplasia with developmental ... - PubMed"
[6]: https://profiles.wustl.edu/en/publications/fgfr3-related-condition-a-skeletal-dysplasia-with-similarities-to/?utm_source=chatgpt.com "FGFR3-related condition: a skeletal dysplasia with ..."
[7]: https://pubmed.ncbi.nlm.nih.gov/7773297/?utm_source=chatgpt.com "Thanatophoric dysplasia (types I and II) caused by ... - PubMed"
[8]: https://www.ncbi.nlm.nih.gov/clinvar/RCV000017728/?utm_source=chatgpt.com "NM_000142.5(FGFR3):c.1948A>G (p.Lys650Glu) AND Thanatophoric dysplasia, type 2 - ClinVar - NCBI"
[9]: https://www.nature.com/articles/ng0395-321?utm_source=chatgpt.com "Thanatophoric dysplasia (types I and II) caused by distinct mutations in fibroblast growth factor receptor 3 | Nature Genetics"
[10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC85119/?utm_source=chatgpt.com "The Transmembrane Mutation G380R in Fibroblast Growth ..."


<br>

### C23 · Bölüm 14 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_14_Ayni_Gen_Farkli_Hastalik.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 227

> **PM1 (mutasyonel hotspot / kritik domain).** ***Hotspot her zaman bir hastalığın hotspot'udur***. Domain-temelli kanıt, ancak hastanın fenotibi o domainle ilişkili hastalık varlığına uyuyorsa geçerlidir.

**Sorulan:** PM1'in bu şekilde koşullanması doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**İlk cümle doğru yönde; ikinci cümle PM1 ile fenotip kanıtını birbirine karıştırıyor.**

PM1 açısından daha doğru ilke şudur:

> **Hotspot veya kritik domain, aynı gen–hastalık–mekanizma bağlamı için tanımlanmış olmalıdır. Hastanın fenotip uyumu ise PM1’in değil, esas olarak PP4’ün ve genel olgu yorumunun konusudur.**

Dolayısıyla:

> “Domain-temelli kanıt ancak hastanın fenotipi o domainle ilişkili hastalığa uyuyorsa geçerlidir.”

ifadesi mevcut biçimiyle fazla katıdır.

---

## “Hotspot her zaman bir hastalığın hotspot’udur” doğru mu?

**PM1 bağlamında büyük ölçüde evet; genel biyoloji açısından hayır.**

“Hotspot” sözcüğü farklı şeyleri anlatabilir:

* yüksek mutasyon hızına sahip bir genomik bölge,
* somatik kanser varyantlarının kümelendiği bir bölge,
* belirli bir kalıtsal hastalıkta patojenik varyantların zenginleştiği bölge,
* belirli bir işlevsel mekanizmaya ait aminoasit kalıntıları.

PM1 için gereken, yalnızca “sık değişen bölge” değildir. Bölgenin:

* incelenen **gen–hastalık ilişkisi** için anlamlı olması,
* ilgili **varyant sınıfında** patojenik varyantlardan zenginleşmesi,
* benign varyasyon açısından görece fakir olması,
* tercihen bir VCEP veya güçlü hastalık-spesifik veriyle önceden tanımlanmış olması

gerekir. Orijinal ACMG/AMP tanımı PM1’i “benign varyasyon içermeyen mutasyonel hotspot veya kritik ve iyi tanımlanmış işlevsel domain” olarak tanımlar; ClinGen ise hotspot ve domainlerin **hastalık-spesifik** olarak değerlendirilmesini önerir. ([PubMed Central (PMC)][1])

Bu nedenle daha doğru cümle:

> **PM1’deki hotspot, incelenen hastalık ve patojenik mekanizma için tanımlanmış patojenik varyant zenginleşme bölgesidir; yalnız yüksek mutasyon oranı veya genel protein önemi PM1 için yeterli değildir.**

---

## Fenotip uyumu PM1’in ön koşulu mu?

**Doğrudan değil.**

PM1, varyantın protein üzerindeki konumuna ilişkin **varyant düzeyinde pozisyonel kanıttır**. Fenotip özgüllüğü ise ayrı bir kanıt kategorisidir:

* **PM1:** Varyant, ilgili hastalık için tanımlanmış hotspot/kritik bölgede mi?
* **PP4:** Hastanın fenotipi veya aile öyküsü, ilgili gen–hastalık ilişkisine özgül mü?

Bu iki kanıt birbirinden ayrılmalıdır.

### Örnek durumlar

| Durum                                                                                             | PM1                             | Fenotip yorumu                                         |
| ------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------ |
| Varyant, hastalık A için doğrulanmış hotspotta; hasta hastalık A ile uyumlu                       | Uygulanabilir                   | PP4 ayrıca değerlendirilebilir                         |
| Varyant, hastalık A hotspotunda; hasta hastalık B açısından değerlendiriliyor                     | Hastalık B’ye taşınamaz         | Yanlış gen–hastalık bağlamı                            |
| Varyant, hastalık A hotspotunda; hasta A’nın atipik/eksik fenotipine sahip                        | PM1 yine uygulanabilir olabilir | PP4 verilmeyebilir; olgu nedenselliği daha belirsizdir |
| Varyant genel bir protein domaininde, fakat hastalık-spesifik patojenik zenginleşme gösterilmemiş | Genellikle uygulanmaz           | Fenotip uyumu PM1 eksikliğini telafi etmez             |

Örneğin ClinGen RASopathy VCEP, PM1 bölgelerini RASopati genleri ve mekanizmaları için özel olarak tanımlamıştır. Bu bölgelerin başka bir allelik hastalıkta veya farklı mekanizmada otomatik kullanılması uygun değildir. ([PubMed Central (PMC)][2])

---

## Domain–fenotip ilişkisi ne zaman önem kazanır?

Aynı gen farklı:

* hastalıklar,
* kalıtım biçimleri,
* moleküler mekanizmalar,
* varyant kümeleri

oluşturuyorsa domain–fenotip ilişkisi kritik hâle gelir.

Örneğin bir genin:

* bir domainindeki varyantlar dominant GoF hastalığı,
* başka bölgesindeki varyantlar resesif LoF hastalığı

oluşturabilir. Bu durumda GoF hastalığı için tanımlanmış hotspotu, resesif LoF hastalığı sınıflandırmasına taşımak yanlış olur.

Ancak bu ilişki şöyle kurulmalıdır:

[
\text{domain/hotspot}
+
\text{aynı gen–hastalık–mekanizma}
\rightarrow
\text{PM1 uygulanabilirliği}
]

Şöyle değil:

[
\text{hastanın fenotipi domain fenotipine uyuyor}
\rightarrow
\text{PM1}
]

Fenotip uyumu bölgenin PM1 statüsünü oluşturmaz. PM1 bölgesi bağımsız kohort ve varyant verileriyle önceden tanımlanmalıdır.

---

## Kritik domain tek başına yeterli mi?

**Hayır.** Bir domainin UniProt veya InterPro’da adlandırılmış olması PM1 için yeterli değildir.

Şunlar aranmalıdır:

1. Domainin protein işlevi açısından kritik olduğuna ilişkin güçlü bilgi
2. İlgili hastalıkta patojenik missense/in-frame varyantların bu bölgede zenginleşmesi
3. Aynı bölgede benign varyasyonun azlığı
4. Hastalık mekanizmasıyla uyum
5. Varyantın beklenen moleküler etkisinin domain-temelli mekanizmayla uyumu

Örneğin ATM VCEP, benign ve patojenik varyantların birlikte bulunduğu bazı bölgelerde PM1 kullanılmamasını açıkça belirtir. Bu, “önemli domain” etiketinin tek başına yeterli olmadığını gösterir. ([ClinGen][3])

Bazı VCEP’ler PM1’i:

* Supporting,
* Moderate,
* bazı özel durumlarda daha yüksek güçte

kalibre eder. Bu nedenle varsayılan PM1_Moderate kullanımı yerine mevcut VCEP spesifikasyonu kontrol edilmelidir. Örneğin beyin malformasyonu VCEP’si bazı genler için PM1’i Supporting düzeyinde tanımlamıştır. ([ClinGen][4])

---

## Ek dikkat noktaları

### Somatik hotspot, germline PM1 değildir

Bir aminoasit kanserlerde sık değişiyor diye germline hastalık sınıflandırmasında otomatik PM1 uygulanamaz. Somatik verinin germline hastalık mekanizmasıyla ilişkisi ayrıca gösterilmelidir.

### Splice etkisi dışlanmalıdır

Missense görünümlü bir varyant hotspotta olsa bile asıl etkisi splicing ise:

* PM1’in protein düzeyindeki gerekçesi uygun olmayabilir,
* splice kanıt çerçevesi kullanılmalıdır.

Bazı VCEP spesifikasyonları PM1 kullanımında splice etkisinin ayrıca değerlendirilmesini açıkça ister. ([Evrensel Veri Deposytosu][5])

### Çifte kanıt sayımına dikkat edilmelidir

Hotspotun tanımı aynı patojenik varyantlara dayanıyorsa, aynı verinin:

* PM1,
* PM5,
* PS4,
* fonksiyonel domain gerekçesi

altında tekrar tekrar sayılması kanıtı şişirebilir. Bazı VCEP’ler bu nedenle PM1 ve PM5’in birlikte kullanımını sınırlar. ([Evrensel Veri Deposytosu][5])

---

## Önerilen düzeltilmiş metin

> **PM1 — mutasyonel hotspot veya kritik işlevsel bölge.** PM1’deki hotspot ya da domain, yalnızca gen veya protein düzeyinde değil, incelenen **gen–hastalık–mekanizma ve varyant sınıfı** bağlamında tanımlanmalıdır. Bir bölgenin genel olarak önemli bir protein domaini olması, yüksek mutasyon oranı göstermesi veya somatik kanser varyantları içermesi tek başına PM1 için yeterli değildir. İlgili bölgede patojenik varyantların zenginleştiği, benign varyasyonun ise sınırlı olduğu gösterilmeli; varsa ClinGen VCEP spesifikasyonu kullanılmalıdır.
>
> **Hastanın fenotip uyumu PM1’den ayrı değerlendirilir.** Fenotipin ilgili hastalığa özgül olması PP4’ü veya genel olgu–varyant nedenselliğini destekleyebilir; ancak PM1’in kendisi varyantın hastalık-spesifik hotspot veya kritik bölgedeki konumuna dayanır. Aynı gendeki farklı bir allelik hastalık veya mekanizma için tanımlanmış hotspot/domain, incelenen hastalığa otomatik olarak aktarılamaz.

## En kısa doğru formül

Mevcut ifade yerine:

> **Hotspot, PM1 açısından gen–hastalık–mekanizma spesifiktir. Domain-temelli PM1, bölgenin incelenen hastalık için patojenik varyantlardan zengin ve benign varyasyondan fakir olduğunun gösterilmesine dayanır. Hastanın fenotip uyumu ise PM1’den ayrı olarak PP4 ve genel nedensellik değerlendirmesinde ele alınır.**

**Net sonuç:** “Hotspot hastalık-spesifiktir” uyarısı korunmalı; fakat PM1’i doğrudan hastanın fenotipine koşullayan ikinci cümle değiştirilmelidir. Fenotip uyumu **PM1’i oluşturmaz**; doğru **gen–hastalık–mekanizma bağlamının seçilmesini** ve varyantın o hastadaki nedenselliğini etkiler.

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4544753/?utm_source=chatgpt.com "Standards and Guidelines for the Interpretation of Sequence ..."
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6119537/?utm_source=chatgpt.com "ClinGen's RASopathy Expert Panel Consensus Methods for ..."
[3]: https://www.clinicalgenome.org/site/assets/files/7451/clingen_hbop_acmg_specifications_atm_v1_1.pdf?utm_source=chatgpt.com "ACMG Classification Rules Specified for ATM"
[4]: https://www.clinicalgenome.org/docs/clingen-brain-malformations-expert-panel-specifications-to-the-acmg-amp-variant-interpretation-guidelines-version-1/?utm_source=chatgpt.com "Summary of ACMG-AMP Criteria for AKT3, MTOR, PIK3CA ..."
[5]: https://erepo.clinicalgenome.org/cspec/ui/svi/doc/643243119?utm_source=chatgpt.com "BRAF - Criteria Specification Registry"


<br>

### C24 · Bölüm 16 — Mekanizmadan Varyant Yorumuna: ACMG/ClinGen Sentezi

**Yer:** `Bölüm_16_Mekanizmadan_Varyant_Yorumuna.md` · 3. Varyant tipleri · satır 144

> | Varyant tipi | İlk bakılacak kriterler | Mekanizma kontrolü | Tipik tuzak |
> |---|---|---|---|
> | Nonsens / çerçeve kayması (NMD'ye giren) | PVS1 → PM2 → PP1/PS2 | LoF, bu hastalığın mekanizması mı? | Kapı kontrol edilmeden PVS1 uygulamak |
> | Son ekzon / NMD kaçışı | PVS1 (gücü düşürülmüş) | Kalan protein işlev görebilir mi? | Tam güçle uygulayıp sınıfı şişirmek |
> | Tam gen delesyonu | CNV puanlama çerçevesi | Doz duyarlılığı kanıtlanmış mı? | Dizi varyantı kriterlerini CNV'ye uygulamak |
> | Missense — hotspot/arayüzde | PM1 → PS3 → PM2 → PP3 | GoF/DN mi, LoF mi? | ***Mekanizma yönünü belirlemeden PS3 yorumlamak*** |
> | Missense — dağınık konumda | PM2 → PP3 (kalibre) → PS3 | Genin mekanizması ne? | Kalibre edilmemiş araç oylaması |
> | Kanonik splice (±1,2) | PVS1 (splice karar ağacı) → RNA kanıtı **PVS1_Strength** | Çerçeve korunuyor mu? | Otomatik tam güç varsaymak · RNA bulgusunu PS3 ile kodlamak |
> | Derin intronik / sessiz | PP3 (splice öngörüsü) → RNA kanıtı **PVS1_Strength**; etki yoksa **BP7** | Kriptik bölge aktive oluyor mu? | "Sessiz = zararsız" saymak · RNA bulgusunu PS3 ile kodlamak |
> | Kodlamayan / düzenleyici | PS3 → PM2; PVS1 ve PM1 genellikle yok | Element ve hedef gen tanımlı mı? | Kodlayan kriterleri olduğu gibi taşımak |
> | Tekrar genişlemesi | Ayrı çerçeve: alel boyu eşikleri | Tekrar tipi ve eşik biliniyor mu? | Dizileme temelli kriter uygulamaya çalışmak |
> | mtDNA varyantı | mtDNA'ya özgü spesifikasyon | Heteroplazmi düzeyi ve doku? | Nükleer kriterleri doğrudan kullanmak |
> | Düşük VAF (mozaik) | PS2/PM6 dikkatle; doku seçimi | Postzigotik mi? | Segregasyonu klasik biçimde yorumlamak |

**Sorulan:** Hızlı-referans tablosundaki "sık hata" sütununun tüm satırları doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Hayır. “Sık hata” sütununun yönü genel olarak doğru olsa da 11 satırın 5’i revizyon gerektiriyor.** En önemli sorunlar:

* Son ekzon varyantlarında PVS1’in otomatik olarak yalnız “düşürülmesi”
* Her RNA bulgusunun PS3 olarak kodlandığının düşünülmesi
* Tekrar genişlemelerinde “dizileme temelli kriter” ifadesi
* Düşük VAF’nin doğrudan PS2/PM6’ya bağlanması
* Negatif RNA sonucunun otomatik BP7/BS3 kabul edilmesi

ClinGen’in güncel toplu rehberi PVS1, splice kanıtı, PS2/PM6, PS3/BS3, PM2 ve PP3/BP4’ü birbirinden ayrı karar çerçeveleri olarak ele alır; dolayısıyla tablo bir “kriter uygulama algoritması” gibi değil, kontrol listesi gibi sunulmalıdır. ([ClinGen][1])

## Satır bazında denetim

| Varyant tipi                           | Hüküm                             | “Sık hata” için daha güvenli ifade                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nonsens / frameshift, NMD beklenen** | **Doğru**                         | **İlgili gen–hastalıkta LoF mekanizmasını, klinik olarak anlamlı transkripti, NMD beklentisini ve olası transkript kurtarmasını değerlendirmeden PVS1 uygulamak.** PVS1 yalnız varyant tipine bakılarak verilmez. ([ClinGen][2])                                                                                                                                                                                                                                                            |
| **Son ekzon / NMD kaçışı**             | **Revize edilmeli**               | **NMD kaçışını otomatik null saymak veya otomatik olarak “düşürülmüş PVS1” vermek.** Varyant bazen PVS1 alamaz; bazen kritik bir bölgeyi kaldırıyorsa belirli güçte PVS1 alabilir; bazen DN/GoF mekanizmasına yönelir.                                                                                                                                                                                                                                                                      |
| **Tam gen delesyonu**                  | **Doğru**                         | **CNV’yi yalnız SNV/indel kriterleriyle sınıflandırmak veya aynı doz kaybını hem CNV puanlamasında hem PVS1 ile iki kez saymak.** Konstitüsyonel tam gen delesyonlarında esas çerçeve ACMG/ClinGen CNV puanlaması ve doz duyarlılığı kürasyonudur. ([PubMed][3])                                                                                                                                                                                                                            |
| **Missense — hotspot/arayüz**          | **Doğru, fakat genişletilmeli**   | **Deneyin ölçtüğü yönün hastalık mekanizmasıyla uyumunu ve deneyin validasyonunu kontrol etmeden PS3 vermek.** Bir deney varyantın aktiviteyi azalttığını gösterse bile hastalık GoF ile oluşuyorsa bu sonuç PS3’ü desteklemeyebilir. ClinGen PS3 değerlendirmesinin ilk basamağını hastalık mekanizmasının tanımlanması olarak belirler. ([ClinGen][4])                                                                                                                                    |
| **Missense — dağınık konumda**         | **Doğru**                         | **Birden fazla kalibre edilmemiş aracın çoğunluk oyunu kullanmak veya her aracı bağımsız PP3 kanıtı gibi saymak.** Tercihen tek, bağımsız verilerle kalibre edilmiş aracın belirlenmiş eşikleri kullanılmalıdır. ([ClinGen][5])                                                                                                                                                                                                                                                             |
| **Kanonik splice**                     | **Kısmen doğru**                  | **Kanonik konumu otomatik PVS1_VeryStrong saymak; yalnız splicing sonucunu ölçen RNA bulgusunu PS3 olarak kodlamak.** ClinGen 2023 yaklaşımında doğrudan RNA-splicing sonucu, uygunsa `PVS1_Strength(RNA)` ile yakalanır. Ancak RNA’dan bağımsız protein, enzim veya hücresel işlev deneyleri yine PS3 oluşturabilir. ([ClinGen][6])                                                                                                                                                        |
| **Derin intronik / sinonim**           | **Kısmen doğru**                  | **“Sinonim = benign” demek; saf splice RNA sonucunu PS3 olarak kodlamak; uygun olmayan dokuda negatif RNA sonucunu otomatik BP7/BS3 kabul etmek.** Negatif deneyde ilgili transkriptin iki alelden de yeterli düzeyde ifade edildiği, kapsamın yeterli olduğu ve dokuya özgü splicing’in dışlanabildiği gösterilmelidir. ([ClinGen][6])                                                                                                                                                     |
| **Kodlamayan / düzenleyici**           | **Doğru, fakat genişletilmeli**   | **Kodlayan varyant kriterlerini değişiklik yapmadan taşımak veya düzenleyici eleman–hedef gen bağlantısı gösterilmeden herhangi bir reporter sonucunu PS3 saymak.** PVS1 çoğunlukla uygulanmaz; ancak PM1 tamamen yasak değildir. İyi tanımlanmış patojenik TF motifleri veya dar enhancer hotspotlarında `PM1_Supporting` kullanılabilir. ([Springer][7])                                                                                                                                  |
| **Tekrar genişlemesi**                 | **Revize edilmeli**               | **Kısa varyantlar için geliştirilmiş standart ACMG/AMP kanıt kodlarını doğrudan uygulamak; yalnız tekrar sayısını değerlendirip motif bütünlüğü, kesintiler, metilasyon, somatik instabilite ve hastalığa özgü eşikleri ihmal etmek.** “Dizileme temelli kriter” denmemeli; çünkü repeat genişlemeleri artık NGS ve uzun-okuma yöntemleriyle de saptanabilir. ACMG bu nedenle genişlemelerin NGS ile saptanmasına özel bir points-to-consider belgesi yayımlamıştır. ([ACMG][8])            |
| **mtDNA varyantı**                     | **Doğru**                         | **Nükleer varyant kriterlerini değişiklik yapmadan uygulamak; heteroplazmi, doku dağılımı, maternal segregasyon, haplogrup ve mtDNA’ya özgü popülasyon verilerini hesaba katmamak.** Kullanılan sistem tamamen başka bir sınıflandırma değil, ACMG/AMP’nin mtDNA’ya özgü modifiye edilmiş biçimidir. ([ClinGen][9])                                                                                                                                                                         |
| **Düşük VAF / mozaiklik**              | **Önemli ölçüde revize edilmeli** | **Düşük VAF’yi tek başına gerçek mozaiklik veya de novo kanıtı saymak; yalnız VAF nedeniyle PS2/PM6 uygulamak; kan VAF’sini mutant hücre oranı ya da aktarım riskiyle eşitlemek.** Önce teknik artefakt, indeks kontaminasyonu, mapping sorunu ve kopya sayısı bağlamı dışlanmalı; proband mozaiği ile parental mozaiğin danışmanlık sonuçları ayrılmalıdır. PS2/PM6 gücü de parental ilişkilerin doğrulanması, fenotip özgüllüğü ve bağımsız gözlem sayısına dayanır; düşük VAF’ye değil.  |

## Özellikle değiştirilmesi gereken beş satır

### 1. Son ekzon / NMD kaçışı

Mevcut tuzak:

> Tam güçle uygulayıp sınıfı şişirmek

yalnızca hatanın bir yarısını gösterir. Diğer yaygın hata da şudur:

> Son ekzon olduğu için otomatik olarak `PVS1_Moderate` veya `PVS1_Supporting` vermek.

NMD’den kaçan varyantın değerlendirmesi şu sorulara bağlıdır:

* Kesilen bölge işlevsel olarak kritik mi?
* Aynı C-terminal bölgede bilinen patojenik kesici varyantlar var mı?
* Oluşan protein stabil mi?
* Mekanizma basit LoF mu, DN/GoF mi?
* Klinik olarak anlamlı transkript mi etkileniyor?

Bu nedenle en iyi tuzak cümlesi:

> **NMD kaçışını otomatik null kabul etmek veya varyantın protein düzeyindeki sonucunu incelemeden standart bir “düşürülmüş PVS1” uygulamak.**

### 2. Kanonik splice ve derin intronik RNA bulguları

“RNA bulgusunu PS3 ile kodlamak” uyarısı **yalnız saf splicing sonucu için doğrudur**. ClinGen Splicing Subgroup:

* tahmin edilen splice etkisini PP3/BP4,
* gözlenen LoF RNA sonucunu `PVS1_Strength(RNA)`,
* splice etkisi bulunmamasını uygun koşullarda BP7

ile yakalamayı önerir. PS3/BS3 ise RNA-splicing sonucu dışında kalan, iyi valide edilmiş protein veya hücresel işlev deneyleri için kullanılabilir. ([ClinGen][6])

Bu nedenle iki satırda da:

> **“Saf RNA-splicing sonucunu PS3 ile kodlamak”**

yazılmalıdır.

### 3. Negatif RNA sonucu

Tablodaki:

> “Etki yoksa BP7”

ifadesi tek başına risklidir. Şunlar doğrulanmadan BP7/BS3 verilmemelidir:

* genin incelenen dokuda ifade edilmesi,
* iki alelin de ölçülebilir olması,
* yeterli okuma derinliği,
* hastalıkla ilgili izoformun yakalanması,
* NMD baskılama gerekip gerekmediği,
* dokuya özgü splice etkisi olasılığı.

Negatif kan RNA’sı, örneğin yalnız kas veya retina izoformunu etkileyen bir varyantı dışlamayabilir. Noncoding rehberi de negatif fonksiyonel deneyin, olası mekanizmaların yalnız birini test ediyorsa benign kanıt olarak kullanılmamasını önerir. ([Springer][7])

### 4. Tekrar genişlemesi

Buradaki sorun “dizileme” sözcüğüdür. Hata:

> Dizilemeyle analiz etmek

değil,

> **SNV/küçük indel için tasarlanmış ACMG/AMP kriterlerini tekrar aleline mekanik olarak uygulamak**

olmalıdır.

Repeat genişlemelerinde yorum:

* normal/intermediate/premutasyon/full mutation sınırları,
* penetrans aralıkları,
* tekrar motifinin yapısı ve kesintileri,
* metilasyon,
* somatik ve germline instabilite,
* ebeveyn kökeni

gibi hastalığa özgü parametrelere dayanır.

### 5. Düşük VAF

Bu satırın ilk bakılacak kriterler bölümündeki:

> `PS2/PM6 dikkatle`

ifadesi de yanıltıcıdır. **Düşük VAF’nin ilk sorusu PS2/PM6 değil, varyantın gerçekliği ve dokusal dağılımıdır.**

Doğru sıra:

1. Analitik doğrulama
2. Kopya sayısı ve mapping bağlamı
3. İkinci doku incelemesi
4. Proband mı, ebeveyn mi mozaik?
5. Postzigotik zamanlama ve fenotip uyumu
6. De novo kriteri gerçekten karşılanıyorsa PS2/PM6 değerlendirmesi

## Tablonun diğer sütunlarındaki dört ek sorun

### PM2 varsayılan olarak Moderate yazılmış

Tablodaki `PM2` ifadeleri genel kullanımda:

> **`PM2_Supporting`**

olarak düzeltilmelidir. ClinGen, nadirliğin tek başına Moderate kanıt gücünü karşılamadığını belirterek PM2’yi Supporting düzeyine indirmiştir; gen/hastalık VCEP spesifikasyonu varsa o önceliklidir. 

### Oklar sabit bir algoritma izlenimi veriyor

> `PVS1 → PM2 → PP1/PS2`

gibi oklar, kriterlerin sırayla ve otomatik uygulanacağı izlenimini yaratır. ACMG kriterleri “varyant tipine göre reçete” değildir. Daha güvenli başlık:

> **Öncelikle değerlendirilecek kanıt alanları**

ve ayraç olarak ok yerine virgül kullanılmalıdır.

### Kodlamayan varyantlarda PM1 “genellikle yok” fazla geniş

PVS1 için bu genelleme büyük ölçüde doğrudur. Ancak PM1, dar ve iyi tanımlanmış düzenleyici hotspotlarda `PM1_Supporting` olarak kullanılabilir. Bu nedenle:

> **“PVS1 genellikle uygulanmaz; PM1 yalnız iyi tanımlanmış hastalık-spesifik motif/hotspotlarda Supporting düzeyinde düşünülebilir.”**

yazılmalıdır. ([Springer][7])

### PS3 hiçbir varyant tipi için otomatik “ilk kriter” değildir

PS3’ün uygulanabilmesi için:

* hastalık mekanizması,
* deney sınıfının uygunluğu,
* spesifik deneyin validasyonu,
* kontrol varyantları,
* ölçülen etkinin varyant düzeyindeki sonucu

incelenmelidir. Dolayısıyla missense veya düzenleyici satırında `PS3`’ün öne yazılması, deney varsa bile otomatik uygulanacağı anlamına gelmemelidir. ([ClinGen][4])

## Önerilen genel sütun başlığı ve dipnot

Sütun başlığı:

> **En sık yanlış uygulama**

Tablonun altına şu dipnot eklenmeli:

> **Bu tablo bir ACMG/AMP uygulama algoritması değildir. Kanıt kodları varyant tipine göre otomatik verilmez; her kriter gen–hastalık ilişkisi, kalıtım biçimi, hastalık mekanizması, ilgili transkript, assay validasyonu ve varsa güncel VCEP spesifikasyonu bağlamında uygulanır. PM2 genel olarak Supporting düzeyinde kullanılmalıdır. RNA-splicing deneyleri, yalnız splice sonucunu ölçüyorsa PS3/BS3 yerine ClinGen Splicing Subgroup çerçevesiyle değerlendirilir.**

**Net sonuç:** Sütun korunabilir; ancak son ekzon, iki splice satırı, tekrar genişlemesi ve düşük VAF satırları değiştirilmelidir. Ayrıca tablonun tamamında **PM2_Supporting**, PS3 validasyonu ve okların algoritmik görünümü düzeltilmelidir.

[1]: https://clinicalgenome.org/tools/clingen-variant-classification-guidance/ "ClinGen Variant Classification Guidance - ClinGen | Clinical Genome Resource"
[2]: https://clinicalgenome.org/docs/recommendations-for-interpreting-the-loss-of-function-pvs1-acmg-amp-variant-criterion/ "Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion - ClinGen | Clinical Genome Resource"
[3]: https://pubmed.ncbi.nlm.nih.gov/31690835/?utm_source=chatgpt.com "Technical standards for the interpretation and reporting of ..."
[4]: https://clinicalgenome.org/docs/recommendations-for-application-of-the-functional-evidence-ps3-bs3-criterion-using-the-acmg-amp-sequence-variant-interpretation/ "Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework - ClinGen | Clinical Genome Resource"
[5]: https://clinicalgenome.org/docs/calibration-of-computational-tools-for-missense-variant-pathogenicity-classification-and-clingen-recommendations-for-pp3-bp4-cri/ "Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria - ClinGen | Clinical Genome Resource"
[6]: https://clinicalgenome.org/docs/application-of-the-acmg-amp-framework-to-capture-evidence-relevant-to-predicted-and-observed-impact-on-splicing-recommendations/?utm_source=chatgpt.com "Recommendations from the ClinGen SVI Splicing Subgroup"
[7]: https://link.springer.com/article/10.1186/s13073-022-01073-3 "Recommendations for clinical interpretation of variants found in non-coding regions of the genome | Genome Medicine | Springer Nature Link"
[8]: https://www.acmg.net/ACMG/Medical-Genetics-Practice-Resources/Medical-Genetics-Practice-Resources.aspx?utm_source=chatgpt.com "Medical Genetics Practice Resources"
[9]: https://clinicalgenome.org/docs/specifications-of-the-acmg-amp-standards-and-guidelines-for-mitochondrial-dna-variant-interpretation/?utm_source=chatgpt.com "Specifications of the ACMG/AMP Standards and ..."


<br>

---

## D. Kitabın özgün pedagojik çerçeveleri (T5)

*Bunlar doğrulanamaz — yalnızca "iyi öğretiyor mu, yanıltıyor mu" diye değerlendirilebilir. Dördü de kitapta 🏷️ ile "yerleşik sınıflama değildir" diye etiketli.*

### D1 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 2. Mekanizmaları bir arada düşünmek: zincirin halkaları · satır 158

> **🔬 Deep-dive — Rezerv ve eşik kavramı.** Bu kitap boyunca tekrar tekrar karşımıza çıkacak birleştirici bir fikir vardır: hücre, bir genin işlevinin bir kısmını kaybetse bile çoğu zaman fenotip ortaya çıkmaz; hastalık ancak belli bir **eşik** aşıldığında görülür. Eşiğin nerede olduğu; genin doz duyarlılığına, dokunun fonksiyonel rezervine, görevi paylaşan akraba genlerin (paralogların) varlığına ve modifiye edici faktörlere bağlıdır. Bu "rezerv ve eşik" mantığı yalnızca haploinsufficiency'de değil, mitokondriyal hastalıklarda heteroplazmi eşiğinde (Bölüm 11) ve hipomorfik allellerin rezidüel fonksiyonunda (Bölüm 2) da aynen geçerlidir. Mekanizmaları öğrenirken bu ortak iskeleti hatırlamak, her bölümü bağımsız bir ezber olmaktan çıkarır.
>
> 🏷️ *Bileşenlerin her biri (doz duyarlılığı, fonksiyonel rezerv, paralog yedeklemesi, heteroplazmi eşiği) kendi bölümünde kaynaklıdır; ***bunları tek bir "rezerv ve eşik" başlığı altında toplamak kitabın pedagojik sentezidir*** — literatürde bu adla yerleşik bir çerçeve değildir.*

**Sorulan:** Çerçeve pedagojik olarak sağlam mı? Etiket yeterince görünür mü? Kitapta kalsın mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Çerçeve pedagojik olarak sağlam ve kitapta kalmalı.** Farklı bölümlerde tekrar eden nicel mantığı tek bir zihinsel model altında topluyor:

[
\text{işlev kaybı}
\rightarrow
\text{tamponlama/rezerv}
\rightarrow
\text{kritik işlev düzeyinin aşılması}
\rightarrow
\text{fenotip}
]

Ancak mevcut metindeki **“aynı mantık aynen geçerlidir”** ifadesi fazla güçlüdür. Haploinsufficiency, hipomorfik alleller ve mtDNA heteroplazmisi ortak bir eşik mantığıyla ele alınabilir; fakat biyolojik olarak aynı mekanizmanın örnekleri değildir.

## Düzeltilmesi gereken dört nokta

### 1. “Hücre” ile sınırlandırılmamalı

Eşik farklı örgütlenme düzeylerinde bulunabilir:

* moleküler kompleks,
* hücresel yolak,
* hücre,
* doku,
* organ veya fizyolojik sistem.

Örneğin bir dokunun klinik rezervi, tek tek hücrelerin moleküler rezervinden farklı olabilir. Bu nedenle:

> “Hücre, bir genin işlevinin bir kısmını kaybetse bile…”

yerine:

> **“Bir hücre, doku veya fizyolojik sistem, gen işlevindeki kısmi azalmayı belirli bir düzeye kadar tamponlayabilir…”**

denmesi daha kapsayıcıdır.

### 2. Eşik keskin bir açma-kapama noktası olmayabilir

“Belli bir eşik aşıldığında hastalık başlar” öğretici olmakla birlikte, biyolojik yanıt çoğu zaman gerçek bir dik çizgiden çok:

* sigmoid geçiş,
* eşik çevresinde olasılıksal bölge,
* hücreler ve dokular arasında farklı eşikler,
* klinik bulguya özgü ayrı eşikler

şeklindedir.

Haploinsufficiency’de azaltılmış gen dozu, sistem çıktısını işlev için gerekli düzeyin altına indirebilir; ancak gen ekspresyonundaki dalgalanmalar ve kompansasyon mekanizmaları bu geçişi kişiden kişiye değiştirebilir. Deneysel çalışmalar, haploinsufficient fenotiplerin sağlam alelin ekspresyonunun artırılmasıyla kurtarılabildiğini ve gen dozunun biyolojik çıktı üzerinde doğrusal olmayan etkiler oluşturabildiğini göstermektedir. ([Science][1])

Bu nedenle “eşik” şu şekilde tanımlanmalı:

> **İlgili klinik özelliğin ortaya çıkma olasılığının belirgin biçimde arttığı kritik işlev aralığı.**

### 3. Paralog varlığı değil, gerçek işlevsel telafi önemlidir

Şu ifade:

> “Görevi paylaşan akraba genlerin, yani paralogların varlığı…”

tek başına yeterli değildir. Bir paralog:

* farklı dokuda ifade edilebilir,
* farklı gelişim döneminde çalışabilir,
* yalnız bazı işlevleri paylaşabilir,
* kayıp sonrasında yukarı regüle olmayabilir.

Deneysel çalışmalar bazı paralogların gen kaybını gerçekten tamponladığını, ancak bu telafinin tür, doku ve yolak bağlamına göre değiştiğini göstermektedir. Dolayısıyla paralogların yalnız bulunması değil, **ilgili bağlamda örtüşen işlev ve ekspresyon göstermesi** gerekir. ([Nature][2])

Daha doğru ifade:

> **“İlgili dokuda işlevsel olarak örtüşen paralogların veya alternatif yolakların sağladığı tamponlama…”**

### 4. Heteroplazmi eşiği aynı modelin birebir karşılığı değildir

Haploinsufficiency’de temel değişken çoğunlukla etkin gen ürünü veya aşağı akım ağ çıktısıdır. Hipomorfik allellerde belirleyici, kalan alelik/genotipik işlevdir. mtDNA hastalıklarında ise:

* mutant mtDNA oranı,
* WT mtDNA kopya sayısı,
* toplam mtDNA yoğunluğu,
* varyantın biyokimyasal etkisi,
* hücre ve doku tipi,
* enerji talebi

birlikte önem taşır.

Cybrid deneyleri, heteroplazmi ile hücresel disfonksiyon arasındaki ilişkinin doğrusal olmadığını ve mtDNA kopya yoğunluğunun gözlenen eşiği değiştirebildiğini göstermiştir. Eşik aynı varyant için bile dokuya göre farklı olabilir. ([PubMed Central (PMC)][3])

Bu nedenle:

> “Heteroplazmi eşiğinde de aynen geçerlidir.”

yerine:

> **“Heteroplazmi eşiğiyle aynı ortak nicel mantığı paylaşır: biyolojik sistem belirli bir bozulma yükünü tamponlar, ancak kritik işlev aralığı geçildiğinde fenotip ortaya çıkar.”**

denmelidir.

## “Rezerv” ile “tamponlama” ayrılmalı

Çerçevenin daha güçlü olması için üç kavram tanımlanmalı:

| Kavram             | Anlamı                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| **Rezidüel işlev** | Varyanttan sonra mutant alel veya genotip tarafından korunan işlev                                      |
| **Rezerv**         | Sistemin normal ihtiyacın üzerindeki kullanılabilir kapasitesi                                          |
| **Tamponlama**     | Gen dozundaki veya işlevdeki değişikliğe rağmen sistem çıktısını koruyan aktif ya da pasif mekanizmalar |
| **Eşik**           | İlgili işlevsel çıktının klinik bulgu bakımından kritik düzeyi                                          |

Böylece hipomorfik allelin kalan aktivitesiyle paralog telafisi aynı şeymiş gibi sunulmaz:

* hipomorfik allel → **rezidüel işlev sağlar**;
* paralog veya alternatif yolak → **tamponlama sağlar**;
* organ kapasitesi → **fonksiyonel rezerv sağlar**;
* bunların ortak sonucu → sistem çıktısının **eşiğin hangi tarafında kaldığını** etkiler.

## Etiket yeterince görünür mü?

**Mevcut etiket içerik olarak doğru, fakat yeterince görünür değil.** Açıklama kutunun sonunda olduğu için okuyucu önce “rezerv ve eşik” ifadesini literatürde yerleşik bir model adı olarak algılayabilir.

Etiket doğrudan başlığa taşınmalıdır:

> **🏷️ Pedagojik sentez — Tamponlama, rezerv ve eşik**

İlk cümlede de statüsü belirtilmelidir:

> **Bu kitapta “tamponlama, rezerv ve eşik” adıyla kullanacağımız bu çerçeve, literatürde tek bir ad altında tanımlanmış bağımsız bir model değildir.**

Sonundaki mevcut dipnot korunabilir; fakat asıl uyarı başlangıçta bulunmalıdır.

Ayrıca kitap boyunca bu çerçeveye referans verilecekse ilk kullanımda küçük bir sembol veya sabit kısa ad kullanılması uygun olur:

> **TRE çerçevesi** gibi yeni bir kısaltma üretmeyin.
> **“Kitabın rezerv–eşik sentezi”** gibi açık bir ifade kullanın.

Yeni bir kısaltma, editöryal sentezi yerleşik bilimsel sınıflandırma gibi gösterebilir.

## Önerilen son metin

> ### 🏷️ Pedagojik sentez — Tamponlama, rezerv ve eşik
>
> Bu kitapta **tamponlama, rezerv ve eşik** başlığı altında kullanacağımız çerçeve, literatürde bu adla yerleşmiş bağımsız bir hastalık modeli değil; farklı genetik mekanizmalardaki ortak nicel mantığı görünür kılan pedagojik bir sentezdir.
>
> Bir hücre, doku veya fizyolojik sistem, gen işlevindeki kısmi azalmayı belirli bir düzeye kadar tolere edebilir. Bunun nedeni mutant allelin koruduğu **rezidüel işlev**, sistemin normal gereksinimin üzerindeki **fonksiyonel rezervi** ve paraloglar, alternatif yolaklar, geri bildirim mekanizmaları veya genetik modifiye ediciler tarafından sağlanan **tamponlama** olabilir. Klinik bulgu, ilgili biyolojik çıktı kritik işlev aralığının altına düştüğünde ortaya çıkar.
>
> Bu eşik her zaman keskin ve sabit değildir. Varyanta, dokuya, gelişim dönemine ve klinik özelliğe göre değişebilir; eşik çevresindeki bireylerde küçük genetik, çevresel veya stokastik farklar penetrans ve ekspresiviteyi değiştirebilir.
>
> Ortak mantık, farklı bölümlerde farklı biyolojik biçimlerde karşımıza çıkar. Haploinsufficiency’de tek sağlam alelin sağladığı işlev yetersiz kalabilir; hipomorfik genotiplerde fenotipi kalan işlev miktarı belirleyebilir; heteroplazmik mtDNA hastalıklarında ise mutant yük, WT mtDNA kapasitesi ve dokuya özgü enerji gereksinimi birlikte biyokimyasal eşiğin aşılmasına yol açabilir. Bunlar aynı moleküler mekanizma değildir; fakat hepsi sistemin bir bozulma yükünü belirli bir noktaya kadar tamponlayabildiği ortak bir nicel yapıyla yorumlanabilir.
>
> 🏷️ *Bu başlık kitabın pedagojik sentezidir. Doz duyarlılığı, genetik tamponlama, fonksiyonel rezerv, hipomorfik rezidüel işlev ve heteroplazmi eşiği literatürde ayrı ayrı tanımlanmış kavramlardır; burada tek bir üst çerçeve altında birleştirilmiştir.*

## Son karar

**Kitapta kalsın.** Bölümler arası mekanistik bağlantı kurması açısından yüksek eğitim değeri taşıyor. Ancak:

* başlıkta pedagojik sentez olduğu gösterilmeli,
* “aynen geçerlidir” yerine **“ortak nicel mantığı paylaşır”** denmeli,
* “rezerv”, “tamponlama” ve “rezidüel işlev” ayrılmalı,
* eşik, mutlak bir açma-kapama noktası değil **özellik ve bağlam bağımlı kritik işlev aralığı** olarak tanımlanmalıdır.

[1]: https://www.science.org/doi/10.1126/science.aau0629?utm_source=chatgpt.com "CRISPR-mediated activation of a promoter or enhancer ..."
[2]: https://www.nature.com/articles/s41588-019-0389-8.pdf?utm_source=chatgpt.com "Evolution of buffering in a genetic circuit controlling plant ..."
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5705840/?utm_source=chatgpt.com "Mitochondrial DNA density homeostasis accounts for a ... - PMC"


<br>

### D2 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.I — Penetrans ve ekspresivite: en sık karıştırılan ikili · satır 137

> Penetransla ilgili kritik ve sıkça gözden kaçan bir nokta, onun sabit bir sayı olmadığıdır; çoğu zaman **yaşa bağlı bir eğridir** (Şekil 1.6). Geç başlangıçlı hastalıklarda — özellikle herediter kanser sendromlarında — genç bir taşıyıcı henüz tamamen sağlıklı olabilir, ancak riski yaşla birlikte artar. Penetrans ayrıca cinsiyete de bağlı olabilir. Bunun pratik karşılığı, presemptomatik taramanın ve genetik danışmanın temelini oluşturur: "bu yaşta sağlıklı olması" bir varyantı dışlamaz. Tüm bu olguların — eksik penetransın ve değişken ekspresivitenin — altında yatan moleküler nedenler arasında allel dozu, diferansiyel allelik ekspresyon, kopya sayısı varyasyonu, cis ya da trans konumdaki modifiye edici varyantlar, yaş, cinsiyet ve epigenetik/çevresel etkenler sayılır (Cooper ve ark., 2013). Aklımızda tutmamız gereken basit pusula şudur: **Penetrans** "var mı?" (Presence), **Ekspresivite** "ne kadar?" (Extent) sorusudur — ***🏷️ bu İngilizce baş harflere dayanan bellek desteği kitabın kendi anlatım aracıdır***, yerleşik bir terminoloji kuralı değildir.

**Sorulan:** İngilizce baş harfe dayanan bir bellek desteği Türkçe bir kitapta işe yarar mı? Türkçe bir alternatif önerir misiniz?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

İngilizce bellek desteği **işe yarayabilir**, ancak Türkçe bir ders kitabında ana anlatım aracı olmamalıdır. `Penetrance–Presence / Expressivity–Extent` eşleşmesi akılda kalıcıdır; fakat okuyucunun aynı anda İngilizce sözcükleri ve baş harf ilişkisini hatırlamasını gerektirir.

Daha önemli teknik sorun şudur:

> **Penetrans yalnız “var mı?” değil, belirli bir genotipi taşıyanlarda fenotipin ortaya çıkma olasılığı/oranıdır.**
> **Ekspresivite yalnız “ne kadar?” değil, ortaya çıkan fenotipin şiddeti, kapsamı ve biçimidir.**

Bu nedenle mevcut pusula kullanılabilir, fakat tek başına tanım olarak bırakılmamalıdır.

## En iyi Türkçe karşılık

Yapay bir baş harf ezberi üretmek yerine şu ikili daha açık ve kalıcıdır:

> **Penetrans: Fenotip ortaya çıkar mı?**
> **Ekspresivite: Ortaya çıkarsa nasıl ve ne ölçüde ortaya çıkar?**

Bu formül hem ayrımı korur hem de ekspresiviteyi yalnız şiddete indirgemez.

### Daha kısa kutu biçimi

> **Penetrans = ortaya çıkma olasılığı**
> **Ekspresivite = ortaya çıkışın biçimi ve derecesi**

Bu, Türkçe kitap için en güvenli kısa pusuladır.

## Eşik temasıyla uyumlu alternatif

Kitapta eşik kavramı sık kullanıldığı için şu anlatım da güçlüdür:

> **Penetrans: Fenotip eşiği aşılmış mı?**
> **Ekspresivite: Eşik aşıldıysa fenotip ne kadar geniş ve ağır?**

Ancak bu ifade bütün penetrans mekanizmalarının tek bir biyolojik eşikten kaynaklandığı izlenimini verebilir. Bu nedenle kavramsal açıklamada kullanılabilir, temel tanımın yerine geçirilmemelidir.

## Önerilen nihai metin

> Aklımızda tutulması gereken basit ayrım şudur: **penetrans**, belirli bir genotipi taşıyan bireylerde fenotipin ortaya çıkıp çıkmadığını ve hangi oranda ortaya çıktığını; **ekspresivite** ise fenotip ortaya çıktığında hangi özelliklerle ve ne şiddette görüldüğünü anlatır. Kısaca:
>
> **Penetrans = ortaya çıkma olasılığı**
> **Ekspresivite = ortaya çıkışın biçimi ve derecesi**
>
> İngilizce terimlerle çalışan okuyucular için ek bir bellek desteği olarak *penetrance–presence* ve *expressivity–extent* eşleşmesi kullanılabilir. Bu eşleşme kitabın pedagojik aracıdır; yerleşik bir terminoloji kuralı değildir.

## Son karar

İngilizce baş harf desteğini **ikincil parantez içi ipucu** olarak tutun. Ana bellek cümlesi Türkçe olmalı:

> **Penetrans: ortaya çıkar mı ve ne sıklıkta?
> Ekspresivite: ortaya çıkarsa nasıl ve ne şiddette?**


<br>

### D3 · Bölüm 14 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_14_Ayni_Gen_Farkli_Hastalik.md` · 2. Moleküler mekanizma: allelik seriyi doğuran altı eksen · satır 54

> 🏷️ **Bu altı eksenli çerçeve kitabın pedagojik sentezidir.** Eksenlerin her biri ayrı ayrı kaynaklıdır ve bu kitabın önceki bölümlerinde tek tek işlenmiştir (mekanizma yönü → Bölüm 2–6; rezidüel işlev → Bölüm 2; varyant konumu → Bölüm 2 ve 7; kalıtım modu → Bölüm 1 ve 3; zamanlama → Bölüm 1 ve 12; bağlam → Bölüm 15). Buna karşılık ***"allelik serinin altı ekseni" literatürde bu adla yerleşik bir sınıflandırma değildir***; eksen sayısı ve gruplama editöryaldir ve öğretme kolaylığı için seçilmiştir. Bir raporda veya yayında bu çerçeveye yerleşik bir taksonomiymiş gibi atıf yapılmamalıdır.

**Sorulan:** Altı eksen doğru seçilmiş mi? Eksik/fazla eksen var mı? Çerçeve kitapta kalsın mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Çerçeve kitapta kalmalı.** Altı başlık, allelik heterojenliği ezberden çıkarıp mekanistik olarak düşünmeyi sağlayan güçlü bir öğretim matrisi oluşturuyor.

Ancak mevcut altı eksen **tam olarak birbirinden bağımsız değil** ve bir kritik unsur yeterince görünür değil:

> **Allelik gereksinim ve genotip konfigürasyonu** — monoallelik/biallelik durum, zigozite, faz, cis–trans ilişkisi, ikinci alelin niteliği ve ebeveyn kökeni.

Bu unsur yalnız “kalıtım modu” başlığı altında bırakılmamalıdır. Güncel GenCC terminolojisi de **kalıtım biçimi, allelik gereksinim ve hastalık mekanizmasını ayrı kavramlar** olarak ele almaktadır. ([PubMed][1])

En iyi çözüm eksen sayısını artırmak değil, mevcut altı ekseni yeniden adlandırıp sınırlarını netleştirmektir.

---

## Mevcut eksenlerin denetimi

| Mevcut eksen       | Hüküm                                             | Önerilen ad                                     |
| ------------------ | ------------------------------------------------- | ----------------------------------------------- |
| **Mekanizma yönü** | Doğru ve temel                                    | **Moleküler mekanizma ve etki yönü**            |
| **Rezidüel işlev** | Fazla LoF-merkezli                                | **İşlevsel etkinin büyüklüğü ve ürünün kaderi** |
| **Varyant konumu** | Yararlı fakat yalnız koordinat gibi anlaşılabilir | **Moleküler ve topolojik konum**                |
| **Kalıtım modu**   | Tek başına yetersiz                               | **Allelik gereksinim ve genotip mimarisi**      |
| **Zamanlama**      | Doğru fakat iki farklı anlamı karıştırabilir      | **Spatiotemporal mimari**                       |
| **Bağlam**         | Gerekli fakat fazla geniş                         | **Değiştirici biyolojik bağlam**                |

---

# 1. Moleküler mekanizma ve etki yönü

Bu eksen doğru seçilmiştir:

* LoF
* hipermorfik GoF
* neomorfik GoF
* dominant-negatif
* toksik ürün etkisi
* değişmiş splicing, lokalizasyon veya düzenleyici işlev

Ancak yalnız “artış/azalış” yönü yeterli değildir. Aynı gen için farklı varyantlar niceliksel olarak aynı yönde görünürken niteliksel olarak farklı patoloji oluşturabilir. Güncel mekanizma terminolojisi çalışmalarının da vurguladığı gibi “LoF” ve “GoF” gibi genel etiketler, doku, zaman, ürün, hücresel yerleşim ve etkilenen işlev belirtilmeden mekanizmayı eksik bırakabilir. ([PubMed][2])

Bu eksenin sorusu:

> **Varyant normal biyolojik çıktıyı hangi mekanizmayla ve hangi yönde değiştiriyor?**

---

# 2. İşlevsel etkinin büyüklüğü ve ürünün kaderi

**“Rezidüel işlev” tek başına yeterli değildir.** Bu ifade null–hipomorf spektrumu için uygundur; ancak GoF, DN ve neomorfik allelleri kapsamaz.

Örneğin şu nicelikler birbirinden farklıdır:

* LoF varyantında kalan işlev,
* GoF varyantında aktivite artışının miktarı,
* DN varyantta WT işlevinin ne ölçüde baskılandığı,
* toksik varyantta anormal ürün yükü,
* splice varyantında normal transkriptin korunma oranı.

Bu nedenle eksenin adı:

> **İşlevsel etkinin büyüklüğü ve ürünün kaderi**

olmalıdır.

Alt başlıkları:

* mutant transkript oluşuyor mu?
* NMD var mı, kısmi mı?
* protein stabil mi?
* normal hücresel bölgeye ulaşıyor mu?
* normal aktivitenin ne kadarı korunuyor?
* anormal aktivite ne ölçüde artıyor?
* mutant:WT ürün oranı nedir?

Bu eksen, mekanizmanın **türünden** çok **şiddetini ve moleküler gerçekleşme düzeyini** açıklar.

---

# 3. Moleküler ve topolojik konum

“Varyant konumu” doğru bir eksendir; fakat yalnız lineer protein koordinatı olarak anlatılmamalıdır.

Konum şunları kapsamalıdır:

* hastalıkla ilişkili transkript ve izoform,
* ekzon veya alternatif ekzon,
* protein domaini,
* katalitik merkez,
* oligomerizasyon veya partner arayüzü,
* sinyal peptidi ve transmembran bölge,
* intrinsically disordered bölge,
* promotör, enhancer, UTR veya splice-regülatör eleman,
* üç boyutlu protein kümelenmesi,
* kromatin ve TAD bağlamı.

Ancak bu eksenin temel uyarısı korunmalıdır:

[
\text{konum}
\neq
\text{mekanizma}
]

Konum mekanizma hipotezini destekler; tek başına işlevsel sonucu veya fenotipi belirlemez.

---

# 4. Allelik gereksinim ve genotip mimarisi

Mevcut çerçevenin en önemli revizyonu burada yapılmalıdır.

**Kalıtım modu**, çoğu zaman ailede gözlenen aktarım paternidir. Buna karşılık fenotipin ortaya çıkması için gereken genotip yapısı ayrı bir sorudur:

* tek alel yeterli mi?
* iki alel mi gerekli?
* heterozigot ve bialelik durumlar farklı şiddetlerde mi?
* iki varyant trans mı?
* varyantlar cis konumunda mı?
* ikinci alel null mı, hipomorfik mi?
* homozigotluk mu, bileşik heterozigotluk mu?
* birden fazla gen mi gerekli?
* ebeveyn kökeni önemli mi?
* kopya sayısı veya tekrar büyüklüğü ne?

GenCC, **allelik gereksinim**, **kalıtım biçimi**, **varyant sonucu** ve **hastalık mekanizmasını** ayrı bilgi alanları olarak tanımlar; bu ayrım özellikle aynı genin monoallelik ve bialelik hastalık oluşturduğu allelik serilerde önemlidir. ([PubMed][1])

Bu eksene şu başlık uygundur:

> **Allelik gereksinim, zigozite, faz ve ebeveyn kökeni**

“Kalıtım modu” bunun klinik gözlenen sonucu olarak alt başlıkta tutulabilir:

> **Genotip mimarisi hangi kalıtım paternini oluşturuyor?**

---

# 5. Spatiotemporal mimari

“Zamanlama” doğru seçilmiştir; fakat en az üç ayrı anlamı bulunur:

### Varyantın oluşma zamanı

* germline,
* erken postzigotik,
* geç postzigotik,
* somatik,
* gonosomal.

### Genin işlev gördüğü gelişim dönemi

* embriyogenez,
* fetal dönem,
* postnatal gelişim,
* erişkin doku homeostazı.

### Fenotipin ortaya çıkma zamanı

* konjenital,
* çocukluk başlangıçlı,
* yaşa bağlı penetrans,
* progresif veya dejeneratif.

Bunlara **mekânsal dağılım** da eklenmelidir:

* hangi doku,
* hangi hücre soyu,
* hangi gelişimsel alan,
* mozaik klonun dağılımı.

Bu nedenle “zamanlama” yerine:

> **Spatiotemporal mimari**

daha kapsayıcıdır.

---

# 6. Değiştirici biyolojik bağlam

“Bağlam” mutlaka kalmalıdır; ancak sınırlandırılmadan bırakılırsa diğer bütün eksenleri içine alan bir artık kategoriye dönüşür.

Açık alt başlıkları olmalıdır:

* genetik modifiye ediciler,
* cis-düzenleyici arka plan,
* sağlam alelin ekspresyonu,
* paralog ve yolak tamponlaması,
* cinsiyet,
* yaş,
* çevresel maruziyet,
* metabolik veya mekanik stres,
* tedavi,
* epigenetik durum,
* stokastik hücresel değişkenlik.

Aynı varyantın işlevsel sonucunun hücre tipi, gelişim zamanı, protein ortağı, genetik arka plan veya çevresel koşula bağlı değişebilmesi, mekanizma tanımlarında açık bağlam belirteçlerine ihtiyaç olduğunu gösterir. ([PubMed][2])

---

## Eksik bir yedinci eksen gerekli mi?

**Hayır.** Aşağıdaki unsurlar revize edilmiş altı eksene yerleştirilirse yedinci eksen gerekmez:

| Olası eksik unsur                             | Yerleştirileceği eksen                      |
| --------------------------------------------- | ------------------------------------------- |
| Zigozite, faz, cis/trans                      | Allelik gereksinim ve genotip mimarisi      |
| Parent-of-origin ve imprinting                | Allelik gereksinim ve genotip mimarisi      |
| NMD, protein stabilitesi, mutant:WT oranı     | İşlevsel etkinin büyüklüğü ve ürünün kaderi |
| Doku ve izoform özgüllüğü                     | Spatiotemporal mimari                       |
| Genetik arka plan ve çevre                    | Değiştirici biyolojik bağlam                |
| Varyant sınıfı: SNV, CNV, repeat, düzenleyici | Mekanizma + moleküler konum                 |
| Penetrans ve ekspresivite                     | Altı eksenin birleşik fenotip çıktısı       |

---

## Fazla veya çıkarılması gereken eksen var mı?

**Tamamen çıkarılması gereken bir eksen yoktur.** Ancak üç çift arasında örtüşme riski vardır:

### Mekanizma yönü ↔ rezidüel işlev

* Mekanizma: **ne oluyor?**
* Etki büyüklüğü: **ne ölçüde oluyor?**

Bu ayrım açık yazılırsa ikisi ayrı kalabilir.

### Kalıtım modu ↔ bağlam

Kalıtım paternini penetrans, cinsiyet veya ebeveyn kökeni değiştirebilir. Bu nedenle kalıtım modu bir alel özelliği gibi değil, allelik gereksinimin aile düzeyindeki görünümü olarak tanımlanmalıdır.

### Zamanlama ↔ bağlam

* Zamanlama/spatiotemporal mimari: **olay nerede ve ne zaman gerçekleşiyor?**
* Bağlam: **aynı olayın etkisini başka hangi faktörler değiştiriyor?**

Bu sınır konursa tekrar azalır.

---

## Başlıkta önemli bir düzeltme

Çerçevenin üç ekseni doğrudan allelin özelliğidir:

* mekanizma,
* etki büyüklüğü,
* konum.

Diğer üçü ise genotip, organizma ve çevre düzeyindedir:

* allelik gereksinim,
* spatiotemporal dağılım,
* bağlam.

Bu nedenle:

> **“Allelik serinin altı ekseni”**

yerine:

> **“Allelik seriyi yorumlamanın altı ekseni”**

veya daha kapsayıcı biçimde:

> **“Allelik seriden fenotipe: altı eksenli yorumlama çerçevesi”**

daha doğrudur.

İkinci başlık, bunun allelleri sınıflandıran katı bir taksonomi değil, **genotip–fenotip ilişkisini analiz eden bir düşünme aracı** olduğunu daha iyi gösterir.

---

## Önerilen nihai altı eksen

> ### 🏷️ Pedagojik sentez — Allelik seriden fenotipe altı yorumlama ekseni
>
> 1. **Moleküler mekanizma ve etki yönü:** Normal biyolojik çıktı hangi mekanizmayla azalıyor, artıyor veya nitelik değiştiriyor?
> 2. **İşlevsel etkinin büyüklüğü ve ürünün kaderi:** Ne kadar normal işlev korunuyor; mutant RNA veya protein ne ölçüde oluşuyor ve hangi aktiviteyi gösteriyor?
> 3. **Moleküler ve topolojik konum:** Hangi transkript, domain, arayüz, düzenleyici eleman veya üç boyutlu yapı etkileniyor?
> 4. **Allelik gereksinim ve genotip mimarisi:** Kaç alel etkilenmeli; zigozite, faz, ikinci alelin niteliği ve ebeveyn kökeni nedir?
> 5. **Spatiotemporal mimari:** Varyant ne zaman oluştu; hangi doku, hücre soyu, izoform ve gelişim döneminde etkili?
> 6. **Değiştirici biyolojik bağlam:** Genetik arka plan, cinsiyet, yaş, çevre, epigenetik durum ve biyolojik tamponlama fenotipi nasıl değiştiriyor?
>
> Bu eksenlerin birleşik çıktısı kalıtım paterni, penetrans, ekspresivite, başlangıç yaşı ve klinik şiddettir.

## Etiket yeterince görünür mü?

Mevcut etiket **açık ve metodolojik olarak dürüsttür**. Şu iki unsur özellikle doğru:

* literatürde yerleşik bir sınıflandırma olmadığının belirtilmesi,
* rapor ve yayınlarda standart taksonomi gibi kullanılmaması uyarısı.

Bununla birlikte görünürlüğü artırmak için etiket yalnız paragraf içinde değil, başlıkta da bulunmalıdır:

> **🏷️ Pedagojik sentez — Allelik seriden fenotipe altı yorumlama ekseni**

Ayrıca son cümle şu şekilde keskinleştirilebilir:

> **Bu çerçeve klinik varyant sınıflandırma kriteri, gen–hastalık kürasyon standardı veya yerleşik moleküler mekanizma ontolojisi değildir; farklı kanıt alanlarını sistematik biçimde sorgulamak için kullanılan editöryal bir düşünme aracıdır.**

## Son karar

**Kitapta kesinlikle kalsın.** Ancak mevcut hâliyle değil:

* **rezidüel işlev** → işlevsel etkinin büyüklüğü ve ürünün kaderi,
* **kalıtım modu** → allelik gereksinim ve genotip mimarisi,
* **zamanlama** → spatiotemporal mimari,
* **varyant konumu** → moleküler ve topolojik konum

olarak revize edilmelidir.

En önemli kavramsal düzeltme de başlıktadır:

> **“Allelik serinin altı ekseni” değil, “allelik seriyi yorumlamanın altı ekseni.”**

[1]: https://pubmed.ncbi.nlm.nih.gov/37982373/?utm_source=chatgpt.com "Toward robust clinical genome interpretation - PubMed - NIH"
[2]: https://pubmed.ncbi.nlm.nih.gov/41330372/?utm_source=chatgpt.com "Interpreting the functional impact of genetic variants - PubMed"


<br>

### D4 · Bölüm 16 — Mekanizmadan Varyant Yorumuna: ACMG/ClinGen Sentezi

**Yer:** `Bölüm_16_Mekanizmadan_Varyant_Yorumuna.md` · 2.6 Bütün kitabı tek tabloda toplamak · satır 123

> Şekil 16.3, bu bölümün ağırlık merkezidir: ***kitabın on dört mekanizma bölümünün her birinin, sekiz kriter ailesiyle ilişkisini tek matriste özetler***.

**Sorulan:** Matris pedagojik olarak sağlam mı? Normatif tabloyla karıştırılma riski yeterince önlenmiş mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Matris fikri pedagojik olarak güçlüdür ve kitapta kalmalıdır.** On dört mekanizma bölümünü sekiz kanıt ailesiyle tek düzlemde buluşturmak, okuyucunun şu ayrımı görmesini sağlar:

[
\text{hastalık mekanizması}
\neq
\text{ACMG kriteri}
]

ancak

[
\text{hastalık mekanizması}
\rightarrow
\text{hangi kanıtların anlamlı olacağını belirleyen bağlam}
]

Fakat yalnızca verdiğiniz açıklama cümlesi, matrisin **normatif bir ACMG/ClinGen eşleştirme tablosu sanılmasını önlemek için yeterli değildir**. Hücreleri görmeden matrisin içerik doğruluğu değerlendirilemez; ancak başlık ve uyarı düzeyinde risk belirgindir.

## Temel karıştırılma riski

Şu ifade:

> “Her mekanizma bölümünün sekiz kriter ailesiyle ilişkisini özetler.”

okuyucuda şu yanlış modeli oluşturabilir:

> “Mekanizmayı belirledim → tabloda işaretli kriterleri uygularım.”

Oysa kriterlerin uygulanabilirliği ve kanıt gücü yalnız mekanizma başlığına bağlı değildir. Ayrıca:

* gen–hastalık ilişkisi,
* kalıtım ve allelik gereksinim,
* varyant sınıfı,
* ilgili transkript,
* ölçülen işlevsel sonuç,
* deneyin validasyonu,
* mevcut gen/hastalık-spesifik VCEP kuralları

değerlendirilmelidir. ClinGen de kriterleri ayrı rehberlerle ele almakta ve gene/hastalığa özgü VCEP spesifikasyonlarını sürümlendirilmiş Criteria Specification Registry içinde yayımlamaktadır. ([ClinGen][1])

Bu nedenle matris:

> **kriter uygulama tablosu**

değil,

> **kanıt alanlarını sorgulama haritası**

olarak sunulmalıdır.

## Başlık mutlaka normatif olmadığını göstermeli

Önerilen şekil başlığı:

> ### 🏷️ Pedagojik sentez — Mekanizma × kanıt ailesi ilişki matrisi
>
> **Normatif olmayan yönlendirme haritası**

“Ağırlık merkezi” ifadesi kullanılabilir; ancak “normatif olmayan” ibaresi yalnız dipnotta değil, **başlıkta veya şeklin hemen üstünde** görünmelidir.

## Şeklin içine konması gereken uyarı

Şeklin altına küçük bir dipnot koymak yeterli değildir. Matrisin üstünde veya lejantında şu kutu bulunmalıdır:

> **Bu matris ACMG/AMP/ClinGen kriterlerinin resmî eşleştirmesi, karar ağacı veya puanlama tablosu değildir. Hücreler yalnızca belirli hastalık mekanizmalarında hangi kanıt ailelerinin sıklıkla veya koşullu olarak sorgulanabileceğini gösterir. İşaretli bir hücre kriterin karşılandığı, boş bir hücre ise kriterin kesinlikle uygulanamayacağı anlamına gelmez. Kriterin uygulanması ve gücü gen–hastalık bağlamına, varyantın gerçek moleküler sonucuna ve varsa güncel VCEP spesifikasyonuna göre belirlenir.**

Bu uyarı üç temel yanlış anlamayı önler:

* **İşaret = kriter kazanıldı** değildir.
* **Boşluk = kriter yasak** değildir.
* **Aynı hücre = her gen için aynı güç** değildir.

## Hücrelerde onay işareti kullanılmamalı

`✓` işareti, kriterin karşılandığı izlenimini yaratır. Bunun yerine ilişki düzeyi gösterilmelidir:

| Sembol | Anlam                                                    |
| ------ | -------------------------------------------------------- |
| **●**  | Bu mekanizmada sıklıkla merkezi kanıt alanı              |
| **◐**  | Koşullu; varyant ve gen–hastalık bağlamına bağlı         |
| **△**  | Özel spesifikasyon veya ayrı yorumlama çerçevesi gerekir |
| **—**  | Genellikle birincil kanıt alanı değildir                 |

Lejantta açıkça:

> **Semboller kriter gücü veya ACMG puanı göstermez.**

yazılmalıdır.

Renk kullanılacaksa tek başına renk koduna güvenilmemeli; semboller korunmalıdır.

## “Sekiz kriter ailesi” de pedagojik sentez olarak etiketlenmeli

Sekiz aile, kitabın kendi gruplamasıysa bu durum açık olmalıdır. Örneğin:

> **Sekiz kanıt ailesi, ACMG/AMP kriter kodlarını öğretim amacıyla daha geniş kanıt alanları altında toplayan editöryal bir sınıflamadır; resmî ACMG/ClinGen taksonomisi değildir.**

Çünkü ClinGen’in resmî rehberleri `PVS1`, `PS2/PM6`, `PS3/BS3`, `PM2`, `PM3`, `PP1/BS4`, `PP4`, `PP3/BP4` ve splice kanıtı gibi kriterleri ayrı metodolojik sorunlar üzerinden ele alır. ([ClinGen][2])

Dolayısıyla hem:

* **on dört mekanizma bölümü**
* hem de **sekiz kriter ailesi**

editöryal gruplamalarsa, matrisin iki ekseni de bu şekilde tanımlanmalıdır.

## Özel çerçeveler matriste ayrılmalı

Bazı varyant grupları standart germline SNV/indel kriterlerinin basit uzantısı değildir:

* konstitüsyonel CNV,
* mtDNA varyantları,
* tekrar genişlemeleri,
* düzenleyici noncoding varyantlar,
* somatik/mozaik varyantlar.

Bunlar için hücreye standart bir ilişki sembolü koymak yerine:

> **△ Özel çerçeve**

işareti kullanılmalıdır. Aksi hâlde matris, bütün varyantların aynı sekiz aileyle aynı biçimde yorumlandığı izlenimini oluşturur.

## Şekle eşlik edecek örnek şart

Matrisin altında tek bir örnek okuma verilmesi normatif riski ciddi biçimde azaltır:

> **Örnek:** Haploinsufficiency mekanizmasında null etki, popülasyon sıklığı, de novo/segregasyon ve fenotip kanıtları sıklıkla sorgulanır. Ancak bu durum nonsense bir varyanta otomatik olarak PVS1, PM2 veya PS2 verileceği anlamına gelmez. Önce ilgili gen–hastalık ilişkisinde LoF mekanizması, transkript sonucu, popülasyon verisinin uygunluğu ve de novo kanıtının kalitesi ayrı ayrı doğrulanır.

Bu örnek, okuyucuya matrisin **nasıl okunacağını** gösterir.

## Önerilen ana cümle

Mevcut cümle yerine:

> **Şekil 16.3, bu bölümün sentez haritasıdır: kitabın on dört mekanizma bölümünde ele alınan biyolojik mekanizmaların, sekiz geniş kanıt ailesiyle hangi noktalarda ve hangi koşullarda kesişebildiğini tek matriste gösterir. Bu matris bir ACMG/AMP uygulama algoritması veya resmî ClinGen eşleştirmesi değil, yorumlama sırasında hangi kanıt alanlarının sorgulanabileceğini gösteren pedagojik bir yönlendirme aracıdır.**

## Son karar

**Matris kalsın; hatta bölümün ağırlık merkezi olmaya uygundur.** Ancak mevcut tanıtım cümlesi tek başına normatif tabloyla karışmayı yeterince önlemiyor. Şu dört unsur zorunlu olmalı:

1. Başlıkta **“pedagojik sentez” ve “normatif olmayan”** ibaresi
2. İşaretin kriter kazanımı olmadığını açıklayan görünür uyarı
3. Onay işaretleri yerine koşullu ilişki sembolleri
4. VCEP ve özel varyant çerçevelerinin önceliğini belirten dipnot

Matrisin hücre bazındaki bilimsel doğruluğunu değerlendirmek için Şekil 16.3’ün kendisinin görülmesi gerekir.

[1]: https://clinicalgenome.org/tools/clingen-variant-classification-guidance/?utm_source=chatgpt.com "ClinGen Variant Classification Guidance"
[2]: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/?utm_source=chatgpt.com "Sequence Variant Interpretation"


<br>

### D5 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · 4.5. Bir genin haploinsufficient olduğunu nasıl anlarız? Popülasyon metrikleri · satır 148

> ![Şekil 3.4 — ***Dozaj duyarlılığı spektrumu ve onu ölçen metrikler***](assets/sekil_13_dozaj_duyarlilik_spektrumu.svg)

**Sorulan:** Dozaj duyarlılığını bir spektrum olarak sunmak doğru mu? Metriklerin (pLI, LOEUF, pHaplo, pTriplo, HI-indeksi) tek eksene yerleştirilmesi yanıltıcı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → ## Hüküm

**Tek kopya kaybına duyarlılığı bir spektrum olarak göstermek pedagojik olarak doğrudur.** Ancak şeklin mevcut hâli iki nedenle yanıltıcıdır:

1. Genel **“dozaj duyarlılığı”** ile yalnızca **heterozigot kayba duyarlılık/haploinsufficiency** aynı şeymiş gibi gösteriliyor.
2. `pLI`, `LOEUF`, `pHaplo`, `pTriplo` ve HI-indeksi aynı biyolojik özelliği aynı yöntemle ölçen, birbirine çevrilebilir metriklermiş gibi tek eksene yerleştiriliyor.

En doğru sonuç:

> **Spektrum kalsın; fakat “tek kopya kaybına duyarlılık spektrumu” olarak adlandırılsın. Metrikler eksenin üzerine aynı ölçüm cetvelinin parçaları gibi değil, farklı kanıt katmanları olarak yerleştirilsin. `pTriplo` ise ayrı bir kopya artışı ekseninde gösterilsin.**

---

# 1. Dozaj duyarlılığı gerçekten bir spektrum mudur?

**Evet, heterozigot gen kaybına tolerans süreklilik gösterir.** Bazı genlerde tek kopya kaybı neredeyse tamamen tamponlanırken bazı genlerde küçük bir doz azalması bile klinik sonuç oluşturabilir. LOEUF’nin kategorik bir etiket yerine sürekli bir ölçü olarak kullanılması da bu biyolojik sürekliliği yansıtır. gnomAD özellikle LOEUF’nin sürekli yorumlanmasını önermektedir. ([gnomAD][1])

Ancak şeklin başlığındaki **“dozaj duyarlılığı”** daha geniş bir kavramdır. Bir gen:

* kayba duyarlı, artışa toleranslı;
* kayba toleranslı, artışa duyarlı;
* hem kayba hem artışa duyarlı;
* her ikisine de görece toleranslı

olabilir.

ClinGen de haploinsufficiency ve triplosensitivity’yi birbirinden bağımsız olarak kürate eder. Dolayısıyla genel dozaj duyarlılığı tek çizgiden çok, en az iki eksenli bir özelliktir. ([ClinGen][2])

Bu nedenle mevcut başlık:

> **Şekil 3.4 — Dozaj Duyarlılığı Spektrumu ve Onu Ölçen Metrikler**

yerine:

> **Şekil 3.4 — Tek Kopya Kaybına Duyarlılık Spektrumu ve İlişkili Gen Düzeyi Göstergeleri**

olmalıdır.

“Ölçen” yerine **“ilişkili göstergeler”** denmesi önemlidir; çünkü bazıları ölçüm, bazıları tahmin, bazıları ise klinik kürasyondur.

---

# 2. Sol uçtaki “tampona dayanıklı (resesif)” etiketi doğru değil

Şekildeki:

> **Tampona dayanıklı (resesif)**

eşleştirmesi kaldırılmalıdır.

Otozomal resesif hastalık geni olmak, genin genel olarak “tamponlu” veya önemsiz olduğu anlamına gelmez. Yalnızca heterozigot kaybın çoğu durumda klinik eşiğin üzerinde yeterli işlev bıraktığını gösterebilir. Bialelik kayıp yine ağır hastalık veya letalite oluşturabilir.

Ayrıca:

* bazı genler hem monoallelik hem bialelik hastalık yapabilir;
* bazı resesif genler popülasyon constraint ölçümlerinde kısıtlı görünebilir;
* bazı dominant hastalıklar HI değil DN veya GoF mekanizmasıyla oluşur.

Daha doğru sol uç etiketi:

> **Heterozigot tek-kopya kaybına görece toleranslı**

Sağ uç:

> **Heterozigot tek-kopya kaybına duyarlı / HI ile uyumlu**

olmalıdır.

Bu değişiklik, kalıtım biçimi ile popülasyonel pLoF constraint’i birbirine karıştırmayı önler.

---

# 3. Gen sınıflarını eksen üzerinde sabit yerlere koymak fazla deterministik

Şekildeki:

* “çoğu enzim — yüksek rezerv; %50 yeter”
* “reseptör/taşıyıcı — ara duyarlılık”
* “TF, kromatin, yapısal, gelişim genleri — doz duyarlı”

ifadeleri yalnızca **genel zenginleşme eğilimleri** olarak kabul edilebilir.

Özellikle:

### “Çoğu enzimde %50 yeter”

Fazla geniş bir genellemedir. Enzimlerin bir kısmında yüksek katalitik rezerv bulunabilir; fakat hız sınırlayıcı, stokiyometrik, metabolik eşik oluşturan veya gelişimsel kritik enzimler haploinsufficient olabilir.

### “Reseptör/taşıyıcı ara duyarlıdır”

Yerleşik bir orta kategori değildir. Reseptör ve taşıyıcılar:

* HI,
* GoF,
* DN,
* bialelik LoF

dâhil çok farklı mekanizmalarla hastalık yapabilir.

### “Yapısal genler HI ucundadır”

Özellikle risklidir. Kollajenler ve başka yapısal multimerik proteinlerde ağır dominant fenotip çoğu zaman haploinsufficiency’den değil, **dominant-negatif etkiden** kaynaklanır.

Bu gen sınıfları eksenin üzerinde sabit konumlar olarak değil, eksenin altında şu notla gösterilmelidir:

> **Bazı transkripsiyon faktörleri, kromatin düzenleyicileri ve gelişimsel düzenleyici genler HI genleri arasında zenginleşir; ancak gen sınıfı tek başına doz duyarlılığını veya hastalık mekanizmasını belirlemez.**

---

# 4. Metrikler aynı şeyi ölçmüyor

| Gösterge                | Gerçekte neyi gösterir?                                                                     |                                                  Yön | Tek eksene konabilir mi?                                      |
| ----------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------: | ------------------------------------------------------------- |
| **LOEUF**               | Popülasyonda beklenene göre yüksek güvenli pLoF varyantlarının azalmasını ve belirsizliğini |                   Düşük = daha güçlü pLoF constraint | Kayba duyarlılık ekseniyle ilişkili; ancak klinik HI değildir |
| **pLI**                 | Genin pLoF-intolerant model sınıfına ait olma olasılığını                                   |                       Yüksek = daha güçlü constraint | LOEUF ile aynı veri ailesi; daha kategorik ve eski            |
| **pHaplo**              | CNV hastalık yükü ve diğer özelliklerden türetilmiş tahmini delesyon/HI duyarlılığını       |                      Yüksek = daha yüksek tahmini HI | Kayba duyarlılık yönünde, ancak LOEUF’den farklı model        |
| **HI-indeksi**          | Gen özelliklerinden hesaplanan eski, model-temelli HI tahmini                               | DECIPHER yüzdeliğinde düşük = daha yüksek tahmini HI | Ayrı tahmin katmanı; yönü bile diğerlerinden ters             |
| **pTriplo**             | Kopya artışına/duplikasyona duyarlılık tahmini                                              |                              Yüksek = daha yüksek TS | **Aynı eksene konmamalı**                                     |
| **ClinGen HI/TS skoru** | Gen veya bölge için klinik ve deneysel kanıtın uzman kürasyonu                              |                       Yüksek skor = daha güçlü kanıt | Tahmin metriği değil; referans kanıt katmanı                  |

## LOEUF

LOEUF, klinik haploinsufficiency olasılığı değildir. Popülasyonda yüksek güvenli pLoF varyantlarının nötr beklentiye göre ne ölçüde azaldığını gösterir. Düşük değer güçlü negatif seçilimle uyumludur.

gnomAD v4.1.1:

* LOEUF’nin sürekli kullanılmasını önermektedir;
* zorunlu bir eşik gerekiyorsa `LOEUF <0,45` değerini güçlü pLoF constraint için önermektedir;
* düşük kapsama ve düşük haritalanabilirlik bölgelerinin ayrıca kontrol edilmesini istemektedir. ([gnomAD][1])

Şekilde:

> “DÜŞÜK → intoleran”

yerine:

> **“Düşük → popülasyonda daha güçlü heterozigot pLoF depletion/constraint”**

yazılmalıdır.

“İntoleran” tek başına klinik hastalık çağrışımı yapıyor.

## pLI

`pLI ≥0,9`, güçlü pLoF constraint ile uyumlu tarihsel bir eşiktir; fakat:

> `pLI ≥0,9 → güçlü HI ipucu`

ifadesi biraz fazla güçlüdür.

Daha doğru:

> **`pLI ≥0,9` → güçlü pLoF constraint sinyali; HI hipoteziyle uyumlu, fakat HI mekanizmasını kanıtlamaz.**

pLI, gerçek anlamda “bu genin HI olma olasılığı” değildir; belirli bir popülasyonel constraint modelindeki sınıf olasılığıdır. LOEUF, constraint spektrumunu sürekli ve daha ayrıntılı gösterdiği için güncel gnomAD kullanımında tercih edilmektedir. ([PubMed Central (PMC)][3])

## pHaplo

pHaplo, pLI/LOEUF gibi yalnız popülasyondaki SNV pLoF azalmasını saymaz. Collins ve arkadaşlarının geniş CNV veri setlerinden geliştirdiği, delesyon etkisini tahmin eden ensemble modelinin çıktısıdır. `pHaplo ≥0,86`, yüksek tahmini HI/deletion-sensitivity grubu için önerilen eşiktir; ancak bu, genin klinik olarak kanıtlanmış haploinsufficient olduğu anlamına gelmez. ([PubMed][4])

Şekilde:

> “≥0,86 → HI”

yerine:

> **“≥0,86 → yüksek tahmini delesyon duyarlılığı/HI olasılığı; klinik kürasyon yerine geçmez”**

yazılmalıdır.

## HI-indeksi

Huang HI-indeksi, ekspresyon, ağ özellikleri, evrimsel bilgiler ve bilinen HI genlerinden türetilmiş daha eski bir tahmin modelidir. DECIPHER’daki yüzdelik kullanımında **düşük yüzde daha güçlü HI tahminini** gösterir; dolayısıyla pLI/pHaplo ile aynı görsel yönde okunmaz. Ayrıca sonraki değerlendirmeler, bu tür modellerde iyi çalışılmış hastalık genlerinden kaynaklanan çalışma yanlılığı bulunabileceğini göstermiştir. ([PubMed][5])

Bu nedenle şekle eklenecekse:

> **HI-indeksi — tarihsel/model-temelli tahmin; düşük yüzdelik daha yüksek HI olasılığı**

olarak açıkça işaretlenmelidir.

## pTriplo

`pTriplo`, kayba değil **kopya artışına** duyarlılığı öngörür. Collins ve arkadaşları yüksek tahmini TS için `pTriplo ≥0,94` eşiğini kullanmıştır. Aynı çalışmada pHaplo ve pTriplo ayrı çıktılar olarak geliştirilmiştir. ([Cell][6])

Bu nedenle pTriplo:

* pLI,
* LOEUF,
* pHaplo,
* HI-indeksi

ile aynı kayıp duyarlılığı çizgisine yerleştirilmemelidir.

---

# 5. “Popülasyon metrikleri” başlığı da yanlış

Şekilde:

> **Bu yeri öngören popülasyon metrikleri**

deniyor.

Bu başlık yalnız pLI ve LOEUF için yaklaşık olarak uygundur.

* `pLI/LOEUF`: popülasyonel pLoF constraint
* `pHaplo/pTriplo`: cross-disorder CNV verisi ve model-temelli tahmin
* HI-indeksi: gen özelliklerine dayalı tahmin
* ClinGen HI/TS: uzman klinik kürasyonu

Daha doğru başlık:

> **Tek kopya kaybına duyarlılığı farklı açılardan değerlendiren gen düzeyi göstergeleri**

veya daha kısa:

> **Birbirini tamamlayan gen düzeyi kanıt katmanları**

olmalıdır.

---

# 6. Uyarı kutusundaki iki cümle değiştirilmeli

Mevcut:

> Yüksek pLI / düşük LOEUF / yüksek pHaplo → gen büyük olasılıkla HI.

Fazla güçlüdür. Yerine:

> **Yüksek pLI, düşük LOEUF ve yüksek pHaplo, heterozigot gen kaybına duyarlılık ve HI hipotezini destekleyen, kısmen örtüşen göstergelerdir; hiçbiri tek başına klinik olarak kanıtlanmış HI mekanizması anlamına gelmez.**

Mevcut:

> Resesif LoF genleri genelde tolerant görünür — metrik HI’yi dışlamaz.

Burada yanlış hedef belirtilmiş. Doğrusu:

> **Bialelik LoF ile hastalık yapan genler heterozigot pLoF constraint göstermeyebilir; düşük constraint, resesif hastalık mekanizmasını veya genin klinik önemini dışlamaz.**

Son cümle doğrudur ve korunmalıdır:

> **Metrik gen düzeyinde bağlamsal ipucudur; tek bir varyantın patojenitesini tek başına kanıtlamaz.**

---

# Önerilen yeni görsel mimari

## Üst bölüm: yalnız kayıp duyarlılığı spektrumu

[
\text{Heterozigot kayba görece toleranslı}
\longrightarrow
\text{Heterozigot kayba duyarlı / HI}
]

Altında sabit gen sınıfları yerine:

> **Gen sınıfları yalnız olasılıksal zenginleşme gösterir; tek tek genler klinik ve mekanistik kanıtla değerlendirilir.**

## Orta bölüm: dört ayrı kanıt katmanı

### 1. Popülasyonel pLoF constraint

* **LOEUF** — temel sürekli gösterge
* **pLI** — eski/kategorik tamamlayıcı gösterge

### 2. Model-temelli delesyon duyarlılığı

* **pHaplo**
* **HI-indeksi** — tarihsel

### 3. Klinik kürasyon

* **ClinGen HI skoru**
* Gen–hastalık geçerliliği ve bilinen LoF mekanizması

### 4. Ayrı artış ekseni

[
\text{Duplikasyona toleranslı}
\longrightarrow
\text{Triplosensitive}
]

* **pTriplo**
* **ClinGen TS skoru**

Bu tasarım okuyucuya hem sürekliliği hem de metriklerin farklı epistemik statülerini gösterir.

---

## Önerilen şekil başlığı ve açıklaması

> ### Şekil 3.4 — Tek kopya kaybına duyarlılık spektrumu ve onu değerlendiren farklı kanıt katmanları
>
> Genler heterozigot tek-kopya kaybına tolerans bakımından sürekli bir dağılım gösterir. Ancak popülasyonel pLoF constraint ölçümleri (`LOEUF`, `pLI`), model-temelli haploinsufficiency tahminleri (`pHaplo`, HI-indeksi) ve klinik dozaj kürasyonu aynı şeyi ölçmez ve doğrudan birbirine dönüştürülemez. Bu göstergeler gen düzeyinde HI hipotezini önceliklendirebilir; belirli bir gen–hastalık ilişkisinde LoF mekanizmasını veya tek bir varyantın patojenitesini kanıtlamaz. Kopya artışına duyarlılık ise ayrı bir eksendir ve `pTriplo`/ClinGen TS verileriyle değerlendirilir.

## Net sonuç

* **Spektrum fikri doğru ve kalsın.**
* Spektrumun adı **“heterozigot tek-kopya kaybına duyarlılık”** olmalı.
* **“Resesif”**, kayba toleranslı ucun eş anlamlısı olarak kullanılmamalı.
* Gen sınıfları sabit konumlara yerleştirilmemeli; yalnız zenginleşme eğilimi olarak gösterilmeli.
* pLI/LOEUF, pHaplo ve HI-indeksi aynı ölçüm ailesi değildir.
* **pTriplo kesinlikle ayrı bir kopya artışı eksenine taşınmalı.**
* En güçlü klinik referans katmanı olarak **ClinGen HI/TS kürasyonu** tahmin metriklerinden ayrı gösterilmelidir.

[1]: https://gnomad.broadinstitute.org/news/2026-03-gnomad-v4-1-1/ "gnomAD v4.1.1 | gnomAD browser"
[2]: https://clinicalgenome.org/curation-activities/dosage-sensitivity/ "Dosage Sensitivity - ClinGen | Clinical Genome Resource"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/6615471/?utm_source=chatgpt.com "Measuring intolerance to mutation in human genetics - PMC"
[4]: https://pubmed.ncbi.nlm.nih.gov/35917817/?utm_source=chatgpt.com "A cross-disorder dosage sensitivity map of the human genome"
[5]: https://pubmed.ncbi.nlm.nih.gov/20976243/?utm_source=chatgpt.com "Characterising and predicting haploinsufficiency in the human ..."
[6]: https://www.cell.com/cell/fulltext/S0092-8674%2822%2900788-7?utm_source=chatgpt.com "A cross-disorder dosage sensitivity map of the human ..."


<br>


---

## E. Terminoloji kararları

*Bu maddeler tek bir paragrafa değil, kitabın tamamına yayılmış tercihleri sorar; o yüzden paragraf verilmemiştir.*

| # | Karar | D/Y/A ve notunuz |
|---|---|---|
| E1 | "Haploinsufficiency" İngilizce bırakılıp yanına "yetersiz doz" konması — tamamen Türkçeleştirilmeli mi? | |
| E2 | "Loss-of-function / gain-of-function / dominant-negatif"in İngilizce korunması | |
| E3 | "Varyant" tercih edilip "mutasyon"un yerleşik adlandırmalara bırakılması | |
| E4 | ACMG kriter kodlarının (PVS1, PS3, PM2…) çevrilmeden bırakılması | |
| E5 | Terimlerin çekim ekleriyle kullanımı ("haploinsufficiency'de", "triplosensitivity'nin") | |
| E6 | Splicing terimleri: "kriptik splice bölgesi", "ekzon atlanması", "intron tutulumu" | |
| E7 | `kitap/21_Sozluk.md` sözlüğünde eksik veya yanlış giriş var mı? | |

---

## F. Kapsam ve yapı kararları

*"Yanlış" değil, "eksik/fazla" sorusu.*

| # | Soru | D/Y/A ve notunuz |
|---|---|---|
| F1 | 17 bölümlük mekanizma sıralaması (LoF → HI → GoF → DN → neomorfik → splicing → CNV → repeat → imprinting → mitokondriyal → mozaiklik → noncoding → digenik → allelik seri → ACMG → sentez) pedagojik olarak doğru sırada mı? | |
| F2 | Eksik bölüm var mı? (farmakogenetik · kanser predispozisyon genetiği · prenatal/preimplantasyon tanı · genetik danışma süreci · çok faktörlü kalıtım ve poligenik risk) | |
| F3 | Her bölümün aynı 10 standart başlıkla ilerlemesi tekdüzelik yaratıyor mu? | |
| F4 | Klinik örneklerin gen seçimi (PAX6, TBX5, NF1, FGFR3, PTPN11, SCN2A, COL1A1, IDH1, SMN2, PMP22, UBE3A, MT-TL1, AKT1, GNAQ…) pediatrik genetik pratiğini temsil ediyor mu? | |
| F5 | Türkiye pratiğine özgü bir bölüm/ek gerekli mi? (akraba evliliği sıklığı, ulaşılabilir test menüsü, SGK geri ödeme, ulusal veri tabanları) | |
| F6 | Hedef kitle üçlü: yandal asistanı + genel pediatrist + tıp öğrencisi. Derinlik üçü için de uygun mu, yoksa öğrenciye ayrı okuma rehberi mi gerekli? | |
| F7 | 64 SVG + 49 Mermaid görselin sayısı ve dağılımı yeterli mi; görsel eksikliği çeken konu var mı? | |

---

## G. Uzman kanaati

**G1 — Bu hâliyle hekimlere yönelik yayımlanabilir mi?**

>
>

**G2 — Yayım öncesi mutlaka düzeltilmesi gerekenler:**

>
>

**G3 — Kitabın en zayıf bölümü ve nedeni:**

>
>

**G4 — Kitabın en güçlü yanı:**

>
>

**G5 — Hedef kitleye uygunluk (yandal asistanı / genel pediatrist / tıp öğrencisi):**

>
>

---E - F VE G BÖLÜMLERİNİ TEK BİR MEİTNDE VERİYORUM:
Aşağıdaki değerlendirme, erişilebilir **27.07.2026 tarihli, 17 bölümlü HTML sürümü** ve konuşma boyunca incelenen bölüm pasajları üzerinden yapılmıştır. Bu sürüm kitabı dört okuyucu grubuna göre kurguluyor, her bölümde on standart başlık kullanıyor ve mekanizma → varyant → hücresel sonuç → fenotip → test → yorum zincirini ana omurga olarak tanımlıyor. 

**Gösterim:**
**D:** Doğru, korunabilir · **A:** Ana fikir doğru, revizyon gerekli · **Y:** Değiştirilmeli

# E. Terminoloji kararları

| #      | Karar                                                                    | D/Y/A ve not                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------ | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **E1** | “Haploinsufficiency” İngilizce bırakılıp yanına “yetersiz doz” konması   | **A** — Tamamen Türkçeleştirmeyin. İlk kullanımda **“haploinsufficiency — tek işlevsel kopyanın yetersizliği”** veya **“haploinsufficiency — yetersiz gen dozu”** yazın. “Yetersiz doz” tek başına belirsizdir; ilaç dozu çağrışımı yapar. Sonraki kullanımlarda `HI` kullanılabilir. “Haployetersizlik” gibi yeni bir terim üretmeyin.                                                                                                               |
| **E2** | LoF / GoF / dominant-negatif terimlerinin İngilizce korunması            | **A** — İngilizce kısaltmalar korunmalı, fakat ana metinde Türkçe anlam önce gelmelidir: **işlev kaybı (*loss-of-function*, LoF)**; **işlev kazanımı (*gain-of-function*, GoF)**; **dominant-negatif etki (DN)**. “Baskın-olumsuz” yalnız ilk tanımda açıklayıcı karşılık olabilir; ana terim yapılmamalıdır.                                                                                                                                         |
| **E3** | “Varyant” tercih edilip “mutasyon”un yerleşik adlandırmalara bırakılması | **D** — Doğru politika. HGVS de sekans değişiklikleri için nötr “variant” dilini kullanır; “mutation” ve “polymorphism” tarihsel ya da bağlama özgü terimler olarak kalabilir. ([varnomen.hgvs.org][1]) “Mutasyonel hotspot”, “de novo mutasyon oranı”, “somatik sürücü mutasyon” gibi yerleşik kullanımlar tamamen yasaklanmamalıdır.                                                                                                                |
| **E4** | ACMG kriter kodlarının çevrilmeden bırakılması                           | **D** — `PVS1`, `PS3`, `PM2`, `PP3`, `BS3` gibi kodlar aynen kalmalıdır. İlk geçtiği yerde Türkçe açıklaması verilebilir; kodun kendisi çevrilmemelidir. ClinGen rehberleri bu kodları sürümlendirilmiş teknik tanımlayıcılar olarak kullanır. ([ClinGen][2])                                                                                                                                                                                         |
| **E5** | Terimlere Türkçe çekim eki eklenmesi                                     | **A** — `haploinsufficiency'de`, `triplosensitivity'nin` gibi biçimler okunabilir ama kitap dili açısından iyi değildir. Tercih sırası: **“haploinsufficiency durumunda”**, **“triplosensitivity kavramının”**, **“splicing sırasında”**. Kısaltmalarda ek kullanılabilir: **HI’de, LoF’un, PVS1’in, ACMG/AMP’nin**. İngilizce ortak adlara art arda Türkçe ek yapıştırmaktan kaçının.                                                                |
| **E6** | “Kriptik splice bölgesi”, “ekzon atlanması”, “intron tutulumu”           | **A** — Son iki terim uygundur. **“Kriptik splice bölgesi”** de klinik kullanımda anlaşılırdır; ilk kullanımda **“kriptik splice bölgesi (*cryptic splice site*)”** biçiminde tanımlayın. Bölüm başlığında `Splicing` korunabilir; “kırpılma” öğrenciye açıklayıcı karşılık olarak verilmeli, ana teknik terimin yerine geçirilmemelidir. Donor/acceptor, splice bölgesi, branchpoint ve polipirimidin traktı terminolojisi tek biçime bağlanmalıdır. |
| **E7** | `kitap/21_Sozluk.md` içeriği                                             | **A*** — Bu dosya erişilebilir kitap çıktısında bulunmadığı için giriş düzeyinde doğrulanamadı. Mevcut HTML ayrıca bağımsız sözlük yerine terimleri ilk geçtiği yerde tanımladığını söylüyor.  Sözlük dosyası görülmeden “eksik veya yanlış yok” denemez.                                                                                                                                                                                             |

## E7 için zorunlu sözlük kontrol listesi

Sözlükte en az şu ayrımlar açık ve doğru bulunmalıdır:

* **Alel** yazımı bütün kitapta tekleştirilmeli. Mevcut metindeki `allel/allelik` biçimleri Türkçe yayın politikası açısından yeniden kararlaştırılmalı; benim önerim **alel, alelik, bialelik, monoalelik** biçimleridir.
* `LoF` ile `pLoF`; **null alel** ile “ürün hiç oluşmaması”; **NMD** ile “transkript tamamen yokluğu” eşitlenmemeli.
* `Haploinsufficiency`, `LoF intoleransı`, `pLI`, `LOEUF` ve ClinGen HI kürasyonu ayrı girişler olmalı.
* `GoF`, hipermorfik, neomorfik, toksik GoF ve dominant-negatif eş anlamlı gösterilmemeli.
* **Antimorfik**, dominant-negatifin tarihsel karşılığı olarak tanımlanmalı; ayrı modern mekanizma gibi sunulmamalı.
* Splicing girişleri varyantın **konumu**, gözlenen **RNA sonucu** ve protein sonucu olarak ayrılmalı.
* Penetrans, ekspresivite, allelik gereksinim, kalıtım biçimi, faz ve ebeveyn kökeni ayrı kavramlar olmalı.
* `VAF`, mutant hücre oranı, heteroplazmi ve mozaik hücre fraksiyonu eşitlenmemeli.
* `CNV`, dozaj duyarlılığı, haploinsufficiency ve triplosensitivity birbirine indirgenmemeli.

# F. Kapsam ve yapı kararları

| #      | Soru                                                | D/Y/A ve not                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------ | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **F1** | 17 bölümlük sıra pedagojik olarak doğru mu?         | **A** — Ana sıra güçlü: önce temel mekanizmalar, sonra özel genomik mimariler, sonunda ACMG ve klinik sentez. İki değişiklik öneriyorum: **Allelik Seriler, Digenik/Oligogenik bölümden önce gelmeli**; okuyucu önce tek gen içindeki çeşitliliği tamamlamalı, sonra çok lokuslu modellere geçmelidir. Ayrıca Bölüm 6’nın başlığındaki **“antimorfik” çıkarılmalı**; bu konu Bölüm 5’teki dominant-negatif mekanizmanın tarihsel adı olarak kalmalıdır. Mevcut kitap zaten antimorfik ile dominant-negatifi eş anlamlı kabul ediyor; ayrı bölüm başlığında yeniden kullanılması yapısal tekrar yaratıyor. |
| **F2** | Eksik bölüm var mı?                                 | **A** — Bir gerçek mekanizma boşluğu var: **germline kanser yatkınlığı ve somatik ikinci vuruş**. `RB1`, `TP53`, `DICER1`, `APC`, MMR, `TSC1/2`, `NF1` üzerinden two-hit, LOH, doku seçiciliği ve mozaiklik ayrı bölüm ya da kapsamlı bir ana bölüm olmalıdır. **Multifaktöriyel kalıtım/poligenik risk** en azından kısa bir sınır bölümü veya ek gerektirir. Farmakogenetik, prenatal/PGT ve danışma süreci ise mekanizma omurgasının dışında; ayrı kitap, ek veya çevrim içi modül olmalıdır. Aneuploidiler ve kromozom segregasyonu da Bölüm 8 içinde görünür bir ana alt başlık olmalıdır.                        |
| **F3** | Her bölümde aynı on başlık tekdüzelik yaratıyor mu? | **A** — Aynı omurga aramayı kolaylaştırır ve korunmalıdır; fakat katı kota hâline gelmiş. Mevcut önsöz on başlığın her bölümde zorunlu olduğunu belirtiyor.  **Altı sabit çekirdek** yeterlidir: tanım, mekanizma, varyantlar, fenotipe dönüşüm, test, yorumlama. Klinik örnek, sık hata ve algoritma bölümün niteliğine göre birleştirilebilmeli. Kaynaklar ve öz-denetim zorunlu kalmalı. Başlık doldurmak için tekrarlanan metin üretilmemeli.                                                                                                                                                                      |
| **F4** | Klinik örnekler pediatrik pratiği temsil ediyor mu? | **A** — Örnekler güçlü fakat **dominant nörogelişimsel, iskelet ve sinyal yolağı hastalıkları lehine eğilimli**. PAX6, TBX5, FGFR3, PTPN11, SCN2A, COL1A1, AKT1 ve GNAQ mekanizma öğretmek için çok iyi; ancak pediatrik pratiğin tamamını temsil etmiyor. En az birer belirgin örnek daha gerekir: **AR metabolik/enzim hastalığı**, **X’e bağlı hastalık**, **renal/işitme spektrumu**, **kanser predispozisyonu**, **anöploidi/kromozom hastalığı**. `PAH`, `DMD`, `CFTR`, `COL4A3/4/5`, `RB1/DICER1` ve 22q11.2 gibi örnekler dengeyi artırır.                                                                     |
| **F5** | Türkiye pratiğine özgü bölüm/ek gerekli mi?         | **D** — Evet, fakat **ana mekanizma bölümü değil, sürümlendirilmiş ek** olmalı. Sabit içerik: akrabalık derecesi, endogami, kurucu varyant, otozigotluk/ROH, resesif test stratejisi, örnek sevk mantığı. Değişken içerik: SGK geri ödeme, test menüsü, laboratuvar listesi, mevzuat ve ulusal veri kaynakları. Bunlar basılı metinde hızla eskir; çevrim içi ek olarak tarih ve sürüm numarasıyla güncellenmelidir.                                                                                                                                                                                                   |
| **F6** | Üç hedef kitle için derinlik uygun mu?              | **A** — Aynı metin üçüne eşit ölçüde uygun değil. Ayrıca erişilebilir önsöz üç değil **dört** grup sayıyor: tıp öğrencisi, pediatrist, genetik uzmanı/yandal asistanı ve genomik veri yorumlayanlar.  Birincil hedef açıkça **yandal asistanı ve klinik genomik çalışan hekim** olmalı. Genel pediatrist ve öğrenci ikincil hedef kitle olarak tanımlanmalı. Her bölümde **Temel**, **Klinik** ve **İleri düzey** okuma işaretleri kullanılmalı.                                                                                                                                                                       |
| **F7** | 64 SVG + 49 Mermaid yeterli mi?                     | **A** — Sayı bakımından yetersizlik yok; muhtemel sorun fazlalık, tekrar ve bakım yüküdür. Mevcut dışa aktarılan HTML kapakta **“64 şekil”** diyor; 64 SVG + 49 Mermaid bilgisiyle görsel envanteri arasında sayı uyumsuzluğu var. Önce tek bir görsel kütüğü oluşturulmalı.  Yeni görsel üretmeden önce her görsel için şu test yapılmalı: “Metinsiz hangi tek kavramı öğretiyor?” Aynı sonucu veren şema ve algoritmalardan biri çıkarılmalı.                                                                                                                                                                        |

## Önerilen bölüm sırası

1. Temel kavramlar
2. LoF
3. Haploinsufficiency ve doz azalması
4. GoF
5. Dominant-negatif
6. Neomorfik ve toksik ürün mekanizmaları
7. Splicing
8. CNV, SV, anöploidi ve konum etkileri
9. Repeat expansion
10. İmprinting ve UPD
11. Mitokondriyal genetik
12. Mozaiklik
13. **Kanser predispozisyonu ve ikinci vuruş**
14. Kodlamayan/düzenleyici varyantlar
15. Allelik seriler
16. Digenik/oligogenik ve modifiye ediciler
17. ACMG/ClinGen sentezi
18. Klinik senaryolar

Bölüm sayısının 17’de tutulması zorunluysa kanser predispozisyonu, mozaiklik bölümünün ikinci ana yarısı olarak değil, **Bölüm 14 alelik serilerle birleştirilerek** yer açılabilir; fakat bağımsız bölüm daha temizdir.

# G. Uzman kanaati

## G1 — Bu hâliyle hekimlere yönelik yayımlanabilir mi?

> **Mevcut hâliyle hayır; kapsamlı bir final bilimsel ve editöryal revizyondan sonra evet.**

Bu bir “başarısız taslak” değildir. Yayımlanabilir bir kitabın omurgası, kapsamı ve pedagojik kimliği oluşmuştur. Özellikle mekanizmadan test seçimine ve varyant yorumuna uzanan zincir, kitabı sıradan bir sendrom/gen kataloğundan ayırıyor. Kitabın kapanış bölümünün klinik pratiği ters yönde—hastadan mekanizmaya—kurması da doğru bir final mimarisidir. 

Fakat konuşma boyunca düzelttiğimiz PVS1, constraint, dominant-negatif, neomorfik/toksik GoF, splicing, UPD, mozaiklik ve noncoding genellemeleri, metinde **sistematik olarak mutlaklaştırma eğilimi** bulunduğunu gösteriyor. Bunlar lokal cümle hataları değil, tüm kitapta uygulanması gereken bir final-pass ihtiyacıdır.

## G2 — Yayım öncesi mutlaka düzeltilmesi gerekenler

### 1. Kaynak doğrulama politikası yeniden yazılmalı

Mevcut:

> “PMID veya DOI veremediğin kaynağı çıkar.”

kuralı bilimsel açıdan fazla katıdır ve bazı en yetkili kaynakları dışlar. HGVS nomenklatürü, ClinGen web spesifikasyonları, CSpec kayıtları, gnomAD sürüm notları ve resmî veri tabanı kürasyonlarının her zaman PMID/DOI’si olmayabilir. ClinGen’in güncel kriter rehberi çevrim içi ve sürümlendirilmiş bir kaynaktır. ([ClinGen][2])

Yeni politika:

* Hakemli makale: PMID, DOI
* Resmî kılavuz/kürasyon: kurum, belge sürümü, yayın/güncelleme tarihi, kalıcı bağlantı, erişim tarihi
* Veri tabanı: veri sürümü/release
* Kitabın pedagojik sentezi: açıkça etiket
* Kaynaksız spesifik iddia: işaretle veya çıkar

Ayrıca **bibliyografik doğruluk**, iddianın gerçekten kaynak tarafından desteklendiği anlamına gelmez. “22/22 DOI doğrulandı” ile “bölüm iddia düzeyinde doğrulandı” ayrı denetimlerdir.

### 2. Bütün kitap için mekanizma-dili denetimi yapılmalı

Özellikle şu otomatik eşitlemeler aranmalı:

* truncating = gerçek null
* düşük LOEUF = kanıtlanmış HI
* missense + multimer = DN
* toksik GoF = neomorfik
* son ekzon = düşürülmüş PVS1
* kanonik splice = PVS1_VeryStrong
* noncoding = PVS1 uygulanamaz
* digenik adaylar = digenik hastalık
* domen konumu = fenotip/prognoz

### 3. Terminoloji kılavuzu ve sözlük bitirilmeli

Tek bir dosyada şu kararlar sabitlenmeli:

* alel/allel
* bialelik/bi-allelic
* dominant-negatif yazımı
* LoF/GoF ilk kullanım şablonu
* splicing ve Türkçe karşılıkları
* İngilizce terimlere ek getirme politikası
* gen, transkript, protein ve HGVS biçimlendirmesi
* sendrom/hastalık/spektrum terminolojisi

### 4. Bölüm yapısı düzeltilmeli

* Bölüm 6’dan “antimorfik” çıkarılmalı.
* Allelik seriler, digenik/oligogenik bölümden önce gelmeli.
* Kanser predispozisyonu/ikinci vuruş mekanizması eklenmeli.
* Bölüm 8’de anöploidi ve kromozom segregasyonu görünür hâle getirilmeli.
* Bölüm 13 noncoding ile Bölüm 8’in TAD/enhancer-hijacking kapsam sınırı açıkça yazılmalı.

### 5. Görsel envanteri ve görsel bilimsel denetim tamamlanmalı

* Tekil ve değişmez şekil kimliği
* SVG/Mermaid sayılarının uzlaştırılması
* Her görselde kaynak veya “pedagojik sentez” etiketi
* Renk-körlüğü ve gri ton erişilebilirliği
* Minimum punto
* Metinle görsel arasında çelişki denetimi
* Algoritmik/normatif olmayan şemalarda görünür uyarı

### 6. Üç katmanlı okuma sistemi kurulmalı

* **Temel:** öğrenci
* **Klinik uygulama:** pediatrist
* **İleri düzey/yorumlama:** yandal asistanı ve laboratuvar

Şu anda deep-dive kutuları bunu kısmen yapıyor; fakat yalnız kutu türüyle değil, bölüm düzeyinde okuma yolu oluşturulmalıdır.

### 7. Dış uzman incelemesi yapılmalı

En az:

* klinik genetik uzmanı,
* moleküler tanı laboratuvarı uzmanı,
* sitogenetik/CNV uzmanı,
* Türkçe bilimsel editör

tarafından birbirinden bağımsız okuma gerekir. Yazarın ve yapay zekânın yaptığı iddia doğrulaması, bağımsız hakem okumasının yerine geçmez.

## G3 — Kitabın en zayıf bölümü ve nedeni

> **Bölüm 15 — Digenik, Oligogenik Kalıtım ve Modifiye Edici Lokuslar**

Konu gerekli; fakat kitabın epistemik olarak en kırılgan alanıdır. Mevcut çekirdek tez monogenik–kompleks kalıtımı tek bir süreklilik olarak sunuyor.  Bu, pedagojik olarak çekici olsa da şu kategorilerin sınırlarını kolayca bulanıklaştırabilir:

* gerçek zorunlu digenik kalıtım,
* ikinci lokus modifikasyonu,
* eksik penetrans,
* dual/blended diagnosis,
* poligenik arka plan,
* tesadüfi ikinci VUS.

Bu bölüm ancak **kanıt hiyerarşisi** üzerine kurulursa güvenli olur:

1. Her iki gen için bağımsız geçerli gen–hastalık ilişkisi
2. Monogenik açıklamanın yetersizliği
3. Beklenen çift genotipin popülasyon ve segregasyon desteği
4. Bağımsız ailelerde tekrar
5. WT / A / B / A+B karşılaştırmalı fonksiyonel model
6. Dual diagnosis ve modifier modelinin dışlanması

Bölümün zayıflığı yazı kalitesinden değil, alanın standardizasyonunun diğer mekanizmalara göre daha düşük olmasından kaynaklanıyor.

## G4 — Kitabın en güçlü yanı

> **Gen–varyant–mekanizma–fenotip–test–yorum zincirini kitabın bütün katmanlarında aynı düşünme modeli olarak kullanması.**

Önsözde açıkça tanımlanan:

> mekanizma → varyant tipi → hücresel sonuç → klinik fenotip → tanısal test → varyant yorumu

zinciri kitabın özgün değeridir. 

Bu yaklaşım:

* varyant tipini mekanizmadan bağımsız yorumlamayı engeller,
* negatif testin sınırlarını görünür kılar,
* allelik serileri ezber olmaktan çıkarır,
* test seçimi ile biyolojik hipotezi bağlar,
* ACMG kriterlerini mekanik kod toplamından kurtarır.

Şekillerin dekorasyon değil öğretim aracı olarak tanımlanması ve klinik final bölümünün ters yönde akıl yürütmesi de bu ana mimariyi güçlendiriyor.

## G5 — Hedef kitleye uygunluk

| Hedef kitle                                                   | Mevcut uygunluk          | Karar                                                                                                                                                                       |
| ------------------------------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Çocuk genetiği yandal asistanı / genomik yorumlayan hekim** | **Yüksek**               | Kitabın gerçek birincil hedef kitlesi bu grup olmalı. Mekanizma, test ve ACMG bağlantısının derinliği uygundur. Final bilimsel düzeltmeler zorunludur.                      |
| **Genel pediatrist**                                          | **Orta**                 | Klinik ipuçları, test seçimi ve senaryolar değerli; ancak protein yapısı, fonksiyonel deney ve kriter kalibrasyonu bölümleri fazla ayrıntılıdır. Klinik okuma yolu gerekir. |
| **Tıp öğrencisi**                                             | **Düşük–orta**           | Baştan sona zorunlu ders kitabı olarak fazla yoğun. Seçili çekirdek metin, temel şekiller, klinik kutular ve ayrı bir öğrenci okuma rehberiyle uygun hâle gelir.            |
| **Laboratuvar/genomik veri yorumlayanlar**                    | **Yüksek fakat ikincil** | Mevcut önsöz bu grubu ayrıca hedefliyor. Bu grup korunacaksa kitap tanıtımında üç değil dört hedef kitle açıkça yazılmalıdır.                                               |

## Genel yayın kararı

> **Major revision — yeniden değerlendirme sonrası yayımlanabilir.**

Kitabın kapsamını büyütmek artık öncelik değildir. Öncelik:

1. kavramsal sınırların kesinleştirilmesi,
2. terminoloji bütünlüğü,
3. iddia–kaynak eşleştirmesi,
4. görsel ve bölüm içi tekrarların azaltılması,
5. hedef kitle katmanlandırmasıdır.

Yeni konu ve görsel eklemeye başlamadan önce bu beş katman tamamlanmalıdır.

[1]: https://varnomen.hgvs.org/recommendations/?utm_source=chatgpt.com "Sequence Variant Nomenclature"
[2]: https://www.clinicalgenome.org/tools/clingen-variant-classification-guidance/?utm_source=chatgpt.com "ClinGen Variant Classification Guidance - ClinGen | Clinical Genome Resource"


## Formu dolduran

| | |
|---|---|
| Ad, unvan | |
| Uzmanlık alanı | |
| Değerlendirme tarihi | |

---

### Form döndükten sonra ne olacak?

- **Y** ve **A** işaretli maddeler `Dogrulama_Kutugu.md`'ye "uzman değerlendirmesi turu" olarak işlenir; düzeltmeler ilgili bölümlere uygulanır ve bir kural değişiyorsa **kitap genelinde** aranır (önceki turların en önemli dersi buydu).
- **D** işaretli maddeler için metin değişmez; kütüğe "uzman onaylı" kaydı düşülür.
- Düzeltmelerden sonra `python3 build_book.py` ile kitap yeniden derlenir.
- Bu, kitabın denetlenebilirlik iddiasının son halkasıdır. Savunulan şey hatasızlık değil, **her iddianın hangi otoriteye karşı nasıl denetlendiğinin kayıtlı olmasıdır.**
