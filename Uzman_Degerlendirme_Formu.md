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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A2 · Bölüm 8 — CNV ve Yapısal Varyantlar

**Yer:** `Bölüm_08_CNV_Yapisal_Varyantlar.md` · 5. Tanısal testlerle ilişkisi · satır 127

> CNV/SV'lerde test seçimi, varyantın **tipine ve boyutuna** göre değişir. Kopya-sayısı değişimleri için altın standart **kromozomal mikroarray (CMA)**'dır. Miller ve ark. (2010), 33 çalışmayı ve CMA ile test edilmiş **21.698 hastayı** kapsayan bir derlemeye dayanarak, gelişimsel gerilik/zihinsel yetersizlik, otizm spektrum bozukluğu veya çoklu konjenital anomalisi olan bireylerde CMA'nın tanısal getirisinin **%15–20** olduğunu, G-bantlı karyotipin getirisinin ise **yaklaşık %3** düzeyinde kaldığını göstermiştir. Bu %3'lük rakamın nasıl hesaplandığı önemlidir: **Down sendromu ve diğer klinik olarak tanınabilen kromozomal sendromlar dışlanarak** verilmiştir — yani karyotipin "zaten klinikle tanınan" olguları yakalaması bu karşılaştırmaya dâhil edilmemiştir. Aradaki farkın kaynağı, CMA'nın submikroskopik delesyon ve duplikasyonlara çok daha duyarlı olmasıdır. Bu nedenle CMA **birinci-basamak sitogenetik test** olarak önerilir; ***karyotip ise belirgin kromozomal sendrom düşünülen olgular, ailede dengeli yeniden düzenlenme öyküsü veya tekrarlayan düşük öyküsü için saklanır*** (Miller ve ark., 2010, *Am J Hum Genet*; [DOI](https://doi.org/10.1016/j.ajhg.2010.04.006)). Önemli sınır: CMA **gerçekten dengeli** yeniden düzenlenmeleri (translokasyon/inversiyon) ve **düşük düzey mozaikliği** göremez. Yine de bu sınırı orantılı görmek gerekir: aynı derleme, bu iki durumun bu hasta grubunda anormal fenotipin görece seyrek nedeni olduğunu (**<%1**) belirtir — yani CMA'yı birinci basamağa taşıyan gerekçeyi ortadan kaldırmaz, yalnızca negatif bir CMA'dan sonra klinik şüphe sürüyorsa ne aranacağını söyler.

**Sorulan:** Karyotipin hangi durumlar için saklanacağı listesi eksiksiz mi? Türkiye pratiğinde bu öneri uygulanabilir mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A4 · Bölüm 9 — Tekrar Dizisi Genişlemesi (Repeat Expansion)

**Yer:** `Bölüm_09_Repeat_Expansion.md` · 5. Tanısal testlerle ilişkisi · satır 142

> **🟦 Klinikte dikkat — WES negatifliği tekrar hastalığını ekarte etmez:** Ataksi, miyotoni, entelektüel yetersizlik veya nörodejenerasyon ile başvuran bir hastada WES negatif çıksa bile, klinik tablo tekrar genişlemesi hastalıklarıyla uyumluysa ***hedefli PCR veya long-read WGS yapılmalıdır***. Tekrar genişlemesi WES'in "kör noktasıdır."

**Sorulan:** Hedefli PCR mı, long-read WGS mi önce gelmeli? Listelenen klinik tablolar (ataksi, miyotoni, EY, nörodejenerasyon) yeterli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A5 · Bölüm 9 — Tekrar Dizisi Genişlemesi (Repeat Expansion)

**Yer:** `Bölüm_09_Repeat_Expansion.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 174

> **🟦 Klinikte dikkat — Presemptomatik test ve etik boyutlar:** Huntington gibi tam penetranslı, tedavisi olmayan hastalıklarda presemptomatik genetik testler özel etik değerlendirme gerektirir. Pek çok uluslararası kılavuz, HD için presemptomatik test öncesinde kapsamlı genetik danışmanlık seanslarını zorunlu kılmaktadır. ***Çocuklara rutin presemptomatik HD testi yapılması önerilmez***.

**Sorulan:** Bu normatif ifade, ulusal/uluslararası kılavuzlarla uyumlu mu? İstisnaları (semptomatik çocuk, juvenil HD şüphesi) belirtilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A6 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 5. Tanısal testlerle ilişkisi · satır 146

> **Bu mekanizmayı hangi test yakalar? (özet):** ***İlk basamak daima metilasyon-duyarlı bir testtir*** (PWS/AS ve BWS/SRS için MS-MLPA veya metilasyon-spesifik PCR); bu test delesyon, UPD ve ID'nin üçünü birden yakalar. Metilasyon anormalse alt-tip belirlenir: **kopya sayısı** (delesyon?) MS-MLPA/array ile, **UPD** SNP array veya mikrosatellit/trio analiziyle, **ID** ise ne delesyon ne UPD bulunduğunda dışlamayla konur. İmprintli gen tek gense ve metilasyon normalse, sıra **dizilemeye** (nokta varyantı) gelir.

**Sorulan:** "Daima" ifadesi doğru mu? Klinik tablo çok tipikse doğrudan alt-tip testine gidilebilir mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A8 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 158

> **🟦 Klinikte dikkat — ClinGen'in *gen düzeyi* dozaj skorları imprintli lokuslarda yanıltıcıdır.** Bölüm 8'de tanıtılan haploinsufficiency (HI) skorunu imprintli bir gende sorguladığınızda beklediğinizi bulamazsınız: ClinGen gen dozaj listesinde *SNRPN*, *NDN*, *H19* ve *IGF2*'nin HI skoru **0**'dır ("kanıt yok"). Bu, bu genlerin doza duyarlı olmadığı anlamına **gelmez**; anlamı, patojenitenin **gen düzeyinde tek kopya kaybıyla** değil, **bölge ve damgalama düzeyinde** — yani hangi ebeveyn kopyasının kaybedildiğiyle — tanımlanmasıdır. Aynı tuzağın CNV'lerdeki karşılığını Bölüm 3'te *PMP22* üzerinden görmüştük: gen kaydı ile bölge kaydı farklı şeyler söyler. İmprintli bir lokusta refleks, **gen skoruna değil bölge kaydına ve metilasyon paternine** bakmaktır.
>
> **🟦 Klinikte dikkat — De novo ≠ düşük risk (her zaman değil):** İmprinting defektlerinin çoğu sporadik (primer epimutasyon) olup düşük tekrarlanma riski taşır. Ancak ID'lerin bir alt-kümesi, ICR içindeki küçük bir **mikrodelesyondan** kaynaklanır; bu genetik lezyon ebeveynden aktarılabilir ve %50'ye varan tekrarlanma riski yaratır. Bu yüzden "imprinting defekti" tanısı, danışmadan önce mutlaka **ICR mikrodelesyonu açısından incelenmelidir** — ***"epigenetik = sporadik" varsayımı tehlikelidir***.

**Sorulan:** "Mutlaka incelenmelidir" ifadesi pratikte uygulanabilir mi (test erişimi)? Hangi lokuslarda öncelikli?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A9 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 156

> **🟦 Klinikte dikkat — ClinGen'in *gen düzeyi* dozaj skorları imprintli lokuslarda yanıltıcıdır.** Bölüm 8'de tanıtılan haploinsufficiency (HI) skorunu imprintli bir gende sorguladığınızda beklediğinizi bulamazsınız: ClinGen gen dozaj listesinde *SNRPN*, *NDN*, *H19* ve *IGF2*'nin HI skoru **0**'dır ("kanıt yok"). Bu, bu genlerin doza duyarlı olmadığı anlamına **gelmez**; anlamı, patojenitenin **gen düzeyinde tek kopya kaybıyla** değil, **bölge ve damgalama düzeyinde** — yani hangi ebeveyn kopyasının kaybedildiğiyle — tanımlanmasıdır. Aynı tuzağın CNV'lerdeki karşılığını Bölüm 3'te *PMP22* üzerinden görmüştük: gen kaydı ile bölge kaydı farklı şeyler söyler. ***İmprintli bir lokusta refleks, gen skoruna değil bölge kaydına ve metilasyon paternine bakmaktır***.
>
> **🟦 Klinikte dikkat — De novo ≠ düşük risk (her zaman değil):** İmprinting defektlerinin çoğu sporadik (primer epimutasyon) olup düşük tekrarlanma riski taşır. Ancak ID'lerin bir alt-kümesi, ICR içindeki küçük bir **mikrodelesyondan** kaynaklanır; bu genetik lezyon ebeveynden aktarılabilir ve %50'ye varan tekrarlanma riski yaratır. Bu yüzden "imprinting defekti" tanısı, danışmadan önce mutlaka **ICR mikrodelesyonu açısından incelenmelidir** — "epigenetik = sporadik" varsayımı tehlikelidir.

**Sorulan:** Bu refleks doğru formüle edilmiş mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A10 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 5. Tanısal testlerle ilişkisi · satır 181

> **Bu mekanizmayı hangi test yakalar? (özet):** mtDNA lezyonları için hedefli **mtDNA dizileme + delesyon/kopya sayısı analizi**, doğru dokuda (***çocukta kan sıklıkla yeterlidir; erişkinde ve şüphe sürüyorsa idrar epiteli veya kas***) yapılmalıdır. Nükleer nedenler için **WES/WGS** gerekir. Pratikte iki genom birlikte değerlendirilmelidir; giderek artan biçimde **WGS**, her ikisini tek testte kapsadığı için tercih edilmektedir.

**Sorulan:** Doku sıralaması ve yaş ayrımı doğru mu? Kas biyopsisinin yeri günümüzde nerede?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A13 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 7. Pediatrik genetikten klinik örnekler · satır 239

> **Pearson ve Kearns-Sayre sendromları — tek büyük delesyon.** Holt ve arkadaşlarının 1988'de mitokondriyal miyopatili hastaların kasında büyük mtDNA delesyonlarını göstermesi, mtDNA'nın insan hastalığındaki rolünü kanıtlayan ilk bulgulardandır (Holt ve ark., 1988). Pediatride bu delesyonlar iki uçta karşımıza çıkar: süt çocukluğunda **Pearson sendromu** (sideroblastik anemi, pansitopeni, ekzokrin pankreas yetmezliği) ve daha ileri yaşlarda **Kearns-Sayre sendromu** (20 yaş öncesi başlayan progresif eksternal oftalmoplejı, pigmenter retinopati ve kardiyak ileti bozukluğu). Aynı lezyon tipi, delesyonun doku dağılımına göre kemik iliği ağırlıklı veya kas/göz ağırlıklı bir tablo yapar; Pearson'dan sağ kalan çocuklar zamanla Kearns-Sayre fenotipine kayabilir. **Öğreti:** tek büyük delesyonlar genellikle sporadiktir; bu, kardeş tekrarlanma riskini maternal kalıtımlı nokta varyantlarından ayıran kritik bir bilgidir. Ayrıca KSS'de ***kardiyak ileti bozukluğu ani ölüm riski taşıdığı için düzenli EKG izlemi zorunludur***.

**Sorulan:** İzlem sıklığı belirtilmeli mi? Holter/pacemaker eşiği eklenmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A14 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 195

> Birincisi, **popülasyon frekansı kriterleri (BA1/BS1/PM2) yeniden kalibre edilmiştir.** mtDNA'da bir varyantın sık görülmesi, çoğu zaman patojenite yokluğunun değil, o varyantın bir **haplogrup belirteci** olmasının işaretidir. İnsan popülasyonları farklı mtDNA haplogruplarına ayrılır ve her haplogrup, tanımı gereği bir dizi homoplazmik varyantla karakterizedir. Bu nedenle frekans değerlendirmesi, MITOMAP ve HelixMTdb gibi mtDNA-özgü veri tabanları üzerinden ve haplogrup bağlamı gözetilerek yapılmalıdır; ***genel nükleer frekans eşikleri doğrudan aktarılamaz***.

**Sorulan:** Veri tabanı seçimi ve haplogrup uyarısı yeterli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A15 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 2.4 Letal-mozaik hipotezi: neden bu sendromlar hiç kalıtılmaz? · satır 108

> **Blaschko çizgileri**, bu mozaikliğin deri üzerindeki görünür haritasıdır. Bu çizgiler ne sinir dağılımını ne damar dağılımını ne de dermatomları izler; embriyogenez sırasında deri hücre soylarının **göç yollarını** yansıtırlar. Sırtta V, gövde yanlarında S, ekstremitelerde çizgisel bir örüntü oluştururlar. Klinik değeri doğrudandır: bir deri lezyonu bu çizgileri izliyorsa, altta neredeyse kesinlikle mozaik bir varyant vardır ve ***test için kan değil, lezyonlu deri istenmelidir***.

**Sorulan:** "Neredeyse kesinlikle mozaik varyant vardır" ifadesinin kesinlik derecesi uygun mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A16 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 2.1 Zamanlama dağılımı, dağılım her şeyi belirler · satır 68

> Bu üçlüden çıkan pratik kural, bölümün en çok kullanılacak cümlesidir: **varyant ne kadar erken oluşursa o kadar çok hücre soyuna dağılır ve germline'a ulaşma olasılığı o kadar artar.** Klinikte bu kural iki yönde birden çalışır. İleri yönde: erken bir mozaik varyant beklediğinizden daha yaygın tutulum yapar. Geri yönde — ve tanısal olarak daha yararlı biçimde: yaygın tutulumlu bir hastada varyantı kanda bulma şansınız yüksekken, ***tek bir deri lezyonuyla sınırlı bir tabloda kan kesinlikle yanlış dokudur***.

**Sorulan:** "Kesinlikle" sözcüğü burada gerekli mi, yoksa yumuşatılmalı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A18 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 214

> Dördüncüsü ve ters yöndeki tuzak, **klonal hematopoezdir.** Yaş ilerledikçe, kan kök hücrelerinde biriken somatik varyantlar taşıyan klonlar genişleyebilir. Erişkin bir bireyin kanında düşük VAF'lı bir somatik varyant saptanması, bu varyantın hastanın klinik tablosuyla ilgili olduğu anlamına gelmez; özellikle *DNMT3A*, *TET2*, *ASXL1* gibi genlerdeki düşük düzeyli bulgular yaşla ilişkili klonal hematopoezin işareti olabilir. Bu nedenle kanda saptanan düşük VAF'lı bir varyantın hastalıkla ilişkisi, klinik tabloyla ve mümkünse ***ikinci bir dokuyla doğrulanmadan kurulmamalıdır***.

**Sorulan:** Klonal hematopoez ayrımı için yaş eşiği/VAF eşiği verilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A19 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 3. Varyant tipleri · satır 131

> Tablonun okunma biçimi şudur. İlk iki satır standart dizi varyantlarıdır ve tek sorun **duyarlılıktır**. Üçüncü ve dördüncü satırlar kopya sayısı/kromozom düzeyindedir; burada VAF mantığı geçerli değildir ve mozaiklik oranı farklı biçimde (hücre sayımı, alel dengesi) hesaplanır — ayrıca ***klasik karyotipte mozaikliği dışlamak için yeterli sayıda hücre sayılmış olması gerekir***. Beşinci satır, Bölüm 10'daki uniparental dizomiyle doğrudan köprü kurar: mitotik rekombinasyonla oluşan segmental UPD tipik olarak mozaiktir ve Beckwith-Wiedemann sendromunun paternal UPD11 alt tipinde bu mozaiklik kuraldır. Son satır ise bir yorum tuzağıdır ve 6. başlıkta ayrıca ele alınacaktır.

**Sorulan:** Sayı verilmeli mi (ör. 30–50 metafaz, düşük mozaiklikte daha fazla)?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A20 · Bölüm 13 — Kodlamayan (Noncoding) ve Regülatör Varyantlar

**Yer:** `Bölüm_13_Noncoding_Regulator_Varyantlar.md` ·  · satır 3

> **Bölümün çekirdek tezi:** Genomun protein kodlayan kısmı %2'den azdır; klinik genetiğin neredeyse tamamı ise on yıllardır bu %2'ye bakmıştır. Kodlamayan varyantlar, bu kör noktanın adıdır. Bu bölümün çekirdek iddiası şudur: **kodlamayan bir varyant, proteinin tek bir amino asidini bile değiştirmeden hastalık yapabilir — çünkü hedefi ürünün kendisi değil, ürünün ifade programıdır.** Bir promotör varyantı genin ne kadar üretileceğini, bir enhancer varyantı hangi dokuda üretileceğini, bir 5′UTR varyantı ne kadar verimli çevrileceğini, bir TAD sınırı varyantı ise hangi genin üretileceğini bozar. Buradan üç klinik sonuç doğar: (1) ***bu varyantları görmek için ekzom yetmez, WGS gerekir***; (2) fenotip çoğu zaman şaşırtıcı biçimde **dar ve tek organa sınırlıdır**, çünkü etkilenen düzenleyici doku-özgüdür; (3) yorumlamada **PVS1 uygulanamaz** ve kanıtın ağırlık merkezi hesaplamadan **fonksiyonel deneye** kayar. Bölüm 8'de yapısal varyant ölçeğinde gördüğümüz düzenleyici mimariyi (TAD, enhancer hijacking) bu bölüm **tek nükleotid** ölçeğine indirir.

**Sorulan:** Üç klinik sonucun tamamı doğru mu? "Dar ve tek organa sınırlı fenotip" genellemesi tutar mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A21 · Bölüm 7 — Splicing (Kırpılma) Varyantları

**Yer:** `Bölüm_07_Splicing.md` · 5. Tanısal testlerle ilişkisi · satır 114

> Splice varyantlarında temel ayrım nettir: **DNA testleri varyantı bulur, ama splicing etkisini RNA gösterir.** Kanonik splice varyantları WES/WGS ile yakalanır; ancak **derin intronik** varyantlar yalnız WGS ile görülür (WES intronları kapsamaz). ***Etkinin kanıtı için ise RNA-seq veya hedefe yönelik cDNA/RT-PCR gerekir*** — bu, splice yorumunda RNA kanıtının (PVS1_Strength / BP7) neden bu kadar değerli olduğunu açıklar (§6).

**Sorulan:** Doğru doku şartı ve minigen assay'in yeri yeterince vurgulanmış mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A22 · Bölüm 15 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_15_Ayni_Gen_Farkli_Hastalik.md` · 5. Tanısal testlerle ilişkisi · satır 195

> ***Allelik serilerde test seçiminin belirleyicisi cihaz değil, hangi hastalığın arandığı varsayımıdır.*** Aynı gen için hedefli hotspot dizilemesi bir hastalıkta yeterliyken, başka bir hastalıkta gen tamamı + delesyon/duplikasyon analizi gerekir. Aşağıdaki tablo bu bakışla okunmalıdır.

**Sorulan:** Bu ilke pratikte uygulanabilir mi, yoksa gen tamamının bakılması artık varsayılan mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### A23 · Bölüm 17 — Klinik Senaryolarla Sentez: Hastadan Mekanizmaya

**Yer:** `Bölüm_17_Klinik_Senaryolarla_Sentez.md` · 7. Pediatrik genetikten klinik örnekler: sekiz senaryo · satır 251

> **Senaryo 7 — Sekiz yaşında çocuk, kas güçsüzlüğü ve yüksek kreatin kinaz; panel ve ekzom negatif.** Klinik olarak konjenital kas hastalığı düşünülüyor; geniş panel ve ekzom sonuçsuz. **Mekanizma hipotezi:** kodlayan bölge dışında kalan bir splicing kusuru (Bölüm 7, 13). **Test:** ***kas dokusundan RNA dizileme*** (± WGS). **Yorum:** genetik tanısı konmamış nadir kas hastalıkları kohortunda transkriptom dizileme, aday splice-bozucu varyantların doğrulanmasını ve hem ekzonik hem **derin intronik** bölgelerdeki splice-değiştirici varyantların saptanmasını sağlamış, genel tanı oranı **%35** olmuştur; ayrıca sık tekrarlayan bir de novo intronik varyantın, kollajen VI benzeri distrofi düşünülen ve önceki genetik analizleri negatif olan hastaların yaklaşık dörtte birini açıkladığı gösterilmiştir (Cummings ve ark., 2017). **Öğreti:** RNA analizi burada iki iş birden yapar — tanıyı koyar ve Bölüm 16'da gördüğümüz gibi öngörüyü ölçüme çevirerek PS3'ü açar.

**Sorulan:** Bu senaryoda kas biyopsisi önerisi Türkiye koşullarında gerçekçi mi? Fibroblast alternatif olabilir mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

---

## B. Sayısal eşikler, oranlar ve öğretici basitleştirmeler

*Okuyucunun ezberleyip alıntılayacağı sayılar. Bir kısmı kitapta zaten "temsilî" diye etiketli — etiketin yeterli olup olmadığı da sorudur.*

### B1 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.C — Varyasyon, allel ve varyant tipleri · satır 69

> İki insan genomu birbirinden milyonlarca pozisyonda farklıdır; ama bu farkların ezici çoğunluğu zararsızdır. Klinik genetiğin asıl zorluğu da buradadır: devasa bir nötr varyasyon arka planı içinden, hastalığa gerçekten neden olan varyantı ayıklamak. Bu nedenle modern dilde, herhangi bir referans-dışı değişikliğe nötr bir terim olan **varyant** denir; eskiden yaygın olan "mutasyon" sözcüğü artık daha çok yerleşik adlandırmalarda kullanılır, "polimorfizm" ise popülasyonda yaygın (***genellikle %1'den sık***) ve çoğunlukla zararsız varyantları anlatır. Patojen olup olmama, varyantın bir başka ekseni olarak ayrıca değerlendirilir; bir varyantın yaygın olması onu otomatik olarak benign yapmaz, ama nadir bir hastalık için güçlü bir benign ipucudur. Burada önemli bir uyarı vardır: **referans dizi her zaman "sağlıklı" anlamına gelmez**; referansta da patojen aleller bulunabilir.

**Sorulan:** %1 eşiği hâlâ öğretilmeli mi, yoksa terk edilmiş bir tanım olarak mı sunulmalı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B2 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.E — Varyantın kökeni ve kalıtım kalıpları · satır 93

> Bir varyantın nereden geldiği, hem rekürrens riski hem de yorum açısından belirleyicidir. **Germline** (eşey hücresi) varyantları gametlerde bulunur, döllenmeyle bireyin tüm hücrelerine geçer ve sonraki kuşaklara aktarılabilir. **Somatik** varyantlar ise döllenmeden sonra tek bir hücrede ortaya çıkar ve yalnızca o hücrenin soyunda bulunur; kanserlerin ve birçok mozaik tablonun temelinde bunlar yatar. Çocukta yeni beliren ve ebeveynlerin kanında saptanamayan varyantlara *de novo* denir; bunların tipik rekürrens riski düşüktür, ancak ebeveynin eşey hücrelerinde gizli bir mozaiklik (gonadal mozaiklik) bulunabileceği için ***risk asla tam olarak sıfır değildir*** (Bölüm 12). Aynı bireyde genetik olarak farklı hücre popülasyonlarının bir arada bulunmasına ise **mozaiklik** denir ve kendi başına bir bölümü hak edecek kadar önemlidir.

**Sorulan:** Gonadal mozaiklik nedeniyle verilen bu ifade doğru mu? Sayısal bir tekrarlanma riski (%1–2 gibi) verilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B3 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 🔎 Bölüm sonu kaynak doğrulama · satır 289

> ### 🔎 Bölüm sonu kaynak doğrulama
> 6/6 kaynak PMID + DOI ile doğrulandı. "Kaynak doğrulaması gerekli" olarak işaretlenmiş açık bir iddia yoktur. Sayısal örnekler (penetrans için 6/8 gibi) ***belirli bir çalışmadan değil, kavramı göstermek için temsilî olarak verilmiştir***. Bölüm, 27.07.2026 tarihli doğrulama turundan geçmiştir (bkz. `Dogrulama_Kutugu.md`).

**Sorulan:** Temsilî sayı kullanımı öğretici mi, yoksa gerçek bir gen üzerinden gerçek penetrans verisi mi kullanılmalı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B4 · Bölüm 2 — Loss-of-Function (İşlev Kaybı) Mekanizmaları

**Yer:** `Bölüm_02_Loss_of_Function.md` · 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu) · satır 314

> ### 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu)
> "Bu bölümdeki tüm kaynakların PMID/DOI bilgisini kontrol et. PMID veya DOI veremediğin kaynağı çıkar. Kaynağı olmayan iddiayı 'kaynak doğrulaması gerekli' olarak işaretle."
>
> **Bu bölüm için durum:** 9/9 kaynak PMID+DOI doğrulandı. NMD eşik kuralı (son ekzon-ekzon bağlantısı ~50 nt) ***öğretici basitleştirmedir; gen/transkripte göre istisnalar olabilir*** ve RNA ile doğrulama önerilir. Bölüm, 27.07.2026 tarihli iddia-düzeyi doğrulama turundan geçmiştir (bkz. `Dogrulama_Kutugu.md`).

**Sorulan:** 50 nt kuralının bu şekilde sunulması yeterli mi? İstisnalar (son ekzon, ilk 150 nt, uzun 3'UTR) örneklenmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B5 · Bölüm 2 — Loss-of-Function (İşlev Kaybı) Mekanizmaları

**Yer:** `Bölüm_02_Loss_of_Function.md` · 4.5. C-terminal truncation neden bazen hafif, bazen ağır? · satır 156

> "Son ekzon = her zaman hafif/benign" varsayımı ***bu nedenle yanlıştır*** (Şekil 2.1B).

**Sorulan:** Bu uyarı doğru mu? Son ekzon varyantlarının ne zaman ağır olduğu yeterince açıklanmış mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B6 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · 2.1. Neden "yarım" bazen yetmez? Doz, eşik ve doğrusal olmayan yanıt · satır 58

> Bu çerçeve, Bölüm 2'deki "doz duyarlı genler → dominant; rezervli genler → resesif" ayrımını niceliksel bir resme oturtur. Vurgulanması gereken nokta, eğrinin **şeklinin gene özgü** olmasıdır: aynı %50 fiziksel kayıp, eğrinin dikliğine ve eşiğin yerine göre felç edici veya tamamen önemsiz olabilir. Bu yüzden ***"varyant %50 kayıp yapıyor" bilgisi tek başına fenotip hakkında hiçbir şey söylemez***; o kayıp **hangi gende** oldu sorusu belirleyicidir.

**Sorulan:** Doz–yanıt eğrisi çerçevesi öğretici olarak doğru mu? Aşırı basitleştirme riski var mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B7 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · 2.1. Neden "yarım" bazen yetmez? Doz, eşik ve doğrusal olmayan yanıt · satır 54

> Sezgimiz genellikle doğrusaldır: "%50 protein → %50 işlev → hafif etki" diye düşünmeye eğilimliyiz. Biyoloji çoğu zaman bizi bu sezgiden kurtarır, çünkü gen dozu ile **fenotipik sonuç** arasındaki ilişki nadiren düz bir çizgidir. Birçok sistem, geniş bir doz aralığında neredeyse sabit (platolu) çalışır: enzimler genelde substrat doygunluğu ve metabolik yedekle çalıştığı için aktivite %50'ye inse bile akı (flux) büyük ölçüde korunur. Bunun kuramsal gerekçesi metabolik kontrol analizinde verilmiştir: bir yolağın akısı üzerindeki kontrol çok sayıda enzime dağılır, tek bir enzimin duyarlılık katsayısı küçüktür ve heterozigottaki %50'lik aktivite düşüşü çoğu zaman ölçülebilir bir akı değişikliği yaratmaz — ***resesifliğin yaygınlığı, seçilimle kazanılmış bir "güvenlik payı" değil, enzim ağının kinetik yapısının doğrudan sonucudur*** (Kacser & Burns, 1981, *Genetics*; [DOI](https://doi.org/10.1093/genetics/97.3-4.639)). Bu tür genlerde doz–yanıt eğrisi erken yükselip platoya oturur; **klinik eşik %50 dozun altında** kalır ve tek allel kaybı sessizdir (Şekil 3.1'daki yeşil eğri). Buna karşılık bazı genlerde sistemin işleyişi tam da o ürünün konsantrasyonuna **keskin biçimde bağlıdır**; eğri neredeyse doğrusaldır veya eşiğe yakın diktir, ve %50 doz eğriyi **eşik bandının altına** sokar (kırmızı eğri). İşte haploinsufficiency, bir genin klinik eşiğinin %50 dozun **üstünde** kaldığı bu ikinci senaryodur.

**Sorulan:** Kacser & Burns (1981) çerçevesinin bu kadar kesin sunulması doğru mu? Bu tez literatürde tartışmalı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B8 · Bölüm 4 — Gain-of-Function (İşlev Kazanımı)

**Yer:** `Bölüm_04_Gain_of_Function.md` · 3. Varyant tipleri · satır 90

> Aşağıdaki tablo, GoF'a yol açabilen varyant tiplerini ve her birinin ürüne "fazla/yanlış aktiviteyi nasıl kazandırdığını" özetler. Dikkat edilecek nokta, bu listenin Bölüm 2–3'teki LoF/HI tablolarının neredeyse **tersi** olmasıdır: orada baskın aktör nonsense/frameshift/delesyon iken, burada baskın aktör **missense** ve nadir **in-frame** değişiklikler ile **duplikasyonlardır**; ***nonsense/frameshift ise GoF için tipik olarak beklenmez*** (çünkü onlar ürünü yok eder, GoF için aktif ürün gerekir).

**Sorulan:** Bu genelleme doğru mu? İstisnalar (ör. son ekzon kesilmesiyle otoinhibisyon kaybı) belirtilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B9 · Bölüm 4 — Gain-of-Function (İşlev Kazanımı)

**Yer:** `Bölüm_04_Gain_of_Function.md` · 4.3. GoF fenotipleri neden sıklıkla doğuştan ve "fazlalık" temalıdır? · satır 132

> GoF mekanizmalı genlerin büyük kısmı büyüme/sinyal yolaklarında (RTK'lar, RAS-MAPK, iyon kanalları) görev aldığından, fenotipler sıklıkla **aşırı sinyalin** sonuçlarını yansıtır: aşırı veya düzensiz büyüme, kanser yatkınlığı (kontrolsüz proliferasyon), aşırı nöronal uyarılabilirlik (epilepsi), veya gelişim programının erken/yanlış tetiklenmesiyle yapısal anomaliler. RAS-MAPK yolağının GoF'la sürekli uyarıldığı "RASopati"ler (Noonan ve ilişkili sendromlar) bu temanın iyi bir örneğidir: yüz dismorfisi, kalp defektleri, büyüme sorunları ve değişen kanser riski bir arada görülür. Önemli bir nüans: GoF'un FGFR3 örneğinde olduğu gibi aşırı sinyal bir "dur" sinyalini abartıyorsa fenotip *büyüme baskılanması* (cücelik) yönünde de olabilir — yani "fazla sinyal" her zaman "fazla büyüme" demek değildir; ***hangi yolakta fazlalık olduğu belirleyicidir***.

**Sorulan:** FGFR3 üzerinden kurulan bu ders doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B10 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 2.2. Multimer matematiği: DN neden haploinsufficiency'den ağırdır? · satır 69

> Bu hesabı mekanizmalar arasında karşılaştırınca DN'in ağırlığı somutlaşır. **Haploinsufficiency'de** (null allel) varyant ürün hiç üretilmez; ortada zehirleyecek bir şey yoktur, sağlam allelin ürünü korunur ve işlev yaklaşık **%50** kalır. **DN dimerde** (n=2) tümü-sağlam kompleks oranı (½)² = **¼ (~%25)**; geri kalan ¾ kompleks en az bir varyant alt birim içerdiği için zehirlenir. ***DN trimerde (n=3, örneğin kollajen) oran (½)³ = ⅛ (~%12)***; **DN tetramerde** (n=4, örneğin p53) (½)⁴ = **1/16 (~%6)**. Yani aynı "tek varyant allel" durumu, protein ne kadar çok alt birimliyse o kadar az sağlam kompleks bırakır. Buradaki ders nettir: DN, haploinsufficiency'nin "yarı doz" tablosunu çok aşan, çoğu kez **ağır** bir fenotipe yol açar — çünkü bozuk ürün yalnız eksiltmez, kalanı da harcar.

**Sorulan:** Bu multimer matematiği "rastgele birleşme + ½ varyant alt birim" varsayımıyla temsilî veriliyor. Öğretici mi, yanıltıcı mı? Kollajen için gerçek oran farklı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B11 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 4. Klinik fenotipe dönüşüm · satır 104

> **Soru 2 — DN neden çoğu kez daha ağır seyreder?** §2.2'deki multimer matematiği nedeniyle. Haploinsufficiency işlevi ~%50'ye indirirken, ***DN onu kompleks büyüklüğüne göre %25'e, %12'ye veya daha aşağıya çeker***. Bunun en çarpıcı klinik kanıtı, **aynı gende** null ve DN varyantların ürettiği şiddet farkıdır (OI'da tip I vs tip II–IV). Bu nedenle, bir genin hastalık spektrumunda hem çok hafif (null) hem çok ağır (missense) uçların bulunması, klinisyene mekanizma hakkında doğrudan bilgi verir.

**Sorulan:** "DN her zaman HI'dan ağırdır" genellemesi doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B12 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 2.2. Multimer matematiği: DN neden haploinsufficiency'den ağırdır? · satır 71

> **🔬 Deep-dive — Kollajenin "¾ bozuk" kuralı ve neden delesyon daha hafif?** Tip I kollajenin klasik örneği bu matematiği klinikte gösterir. Kollajen molekülü bir üçlü sarmaldır; her sarmalın düzgün örülmesi için üç zincirin de kusursuz olması ve ***özellikle sarmal boyunca her üçüncü konumdaki glisinlerin korunması gerekir*** (glisin, sarmalın iç eksenine sığabilen tek küçük amino asittir). *COL1A1* veya *COL1A2*'de bir glisini başka bir amino asitle değiştiren missense varyant, bozuk ama yine de sarmala katılmaya çalışan bir zincir üretir; bu zincir sarmalın katlanmasını yavaşlatır, aşırı modifikasyona ve yıkıma yol açar ve içine girdiği molekülü bozar — klasik bir "protein suicide" / zehirli alt birim örneği. Sonuçta sentezlenen kollajen moleküllerinin yaklaşık **¾'ü en az bir bozuk zincir** içerdiği için anormaldir. Buna karşılık, *COL1A1*'in bir kopyasını tümüyle susturan **null allel**, hiç bozuk zincir üretmez: hücre yalnızca **daha az ama normal** kollajen yapar (haploinsufficiency). İşte bu yüzden null allel **hafif osteogenesis imperfecta tip I** yaparken, glisin substitüsyonları **ağır (tip II–IV)** OI yapar (Forlino &amp; Marini, 2000, *Mol Genet Metab*; [DOI](https://doi.org/10.1006/mgme.2000.3039)). Aynı gen, iki farklı mekanizma, zıt ağırlık — ve bu, mekanizma çıkarımının en güçlü doğal deneyidir.

**Sorulan:** Kollajen glisin kuralının bu biçimde anlatımı doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B13 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 168

> **🟦 Klinikte dikkat — "Kısaltıcı varyant her zaman en kötü" değildir:** ***Sezgi, protein üretimini erken durduran (nonsense/frameshift) varyantların missense'ten daha ağır olacağını söyler***. DN genlerde bu **tersine dönebilir**: kısaltıcı/null varyant ürünü yok ettiği için *zehirleyemez* ve daha hafif (haploinsufficiency) tablo yapabilirken, ürünü ayakta tutan **missense** varyant kompleksi zehirleyip **daha ağır** hastalık yapabilir. Bu yüzden DN gende varyant tipinden şiddete doğrudan atlamayın; mekanizmayı sorun.

**Sorulan:** OI üzerinden kurulan bu ters-sezgi dersi doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B14 · Bölüm 6 — Neomorfik ve Antimorfik Alleller

**Yer:** `Bölüm_06_Neomorfik_Antimorfik.md` · 2.2. Neden tekrarlayan hotspot missense? · satır 63

> Neomorfik (ve çoğu antimorfik) varyantın çarpıcı bir ortak özelliği vardır: gen boyunca rastgele dağılmazlar, **belirli kodonlarda tekrar tekrar** ortaya çıkarlar. Bunun nedeni doğrudan mekanizmadan gelir. Yeni bir aktivite kazanmak, işlev kaybetmekten çok daha "zor"dur: bir proteini bozmanın binlerce yolu vardır (herhangi bir kritik kalıntıyı bozan herhangi bir LoF varyant işe yarar), ama ona **belirli yeni bir iş** kazandıracak değişiklik genellikle **çok özel, sayılı** kalıntılarda olur. Bu yüzden neomorfik varyantlar **hotspot** desenler çizer: ***IDH1'de neredeyse daima Arg132, IDH2'de Arg172/Arg140; histon H3'te Lys27***. Bu desen hem mekanizmanın bir sonucudur hem de varyant yorumunda güçlü bir araçtır (PM1 kriteri; §6). Gerasimavicius ve ark.'nın (2022) gösterdiği gibi, LoF dışı (DN/GoF/neomorf) varyantlar üç boyutlu uzayda kümelenme eğilimindedir ve standart tahmin araçları onları sıklıkla kaçırır — bu da hotspot bilgisinin önemini artırır (Gerasimavicius ve ark., 2022, *Nat Commun*; [DOI](https://doi.org/10.1038/s41467-022-31686-6)).

**Sorulan:** Hotspot listesi doğru ve güncel mi? H3K27M için gen adı (H3-3A/H3C2) belirtilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B15 · Bölüm 9 — Tekrar Dizisi Genişlemesi (Repeat Expansion)

**Yer:** `Bölüm_09_Repeat_Expansion.md` · 🔎 Bölüm sonu kaynak doğrulama komutu · satır 303

> **Bu bölüm için durum:** 10/10 kaynak PMID + DOI doğrulandı. İşaretlenen spekülatif iddia: DPR toksisitesinin hastalıktaki rölatif ağırlığı "aktif araştırma alanı" olarak etiketlendi. Tüm tekrar eşiği sayısal değerleri literatür konsensusu kaynaklı olup ***"temsilî" olarak verilmiştir; klinik kullanımda güncel gen-spesifik lab kılavuzları tercih edilmelidir***. Bölüm, 27.07.2026 tarihli iddia-düzeyi doğrulama turundan geçmiştir; turda *HTT* eşik aralıkları ve FMRP işlevi ders kitabı çapraz kontrolüyle (Thompson & Thompson 2023) yeniden çapalanmış, iki Mermaid algoritmasındaki satır sonları proje standardına (`<br/>`) çevrilmiş ve metindeki Kiril harf bulaşması giderilmiştir (bkz. `Dogrulama_Kutugu.md`).

**Sorulan:** Eşikleri temsilî bırakıp kılavuza yönlendirmek doğru bir tercih mi, yoksa net bir tablo mu verilmeli?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B16 · Bölüm 9 — Tekrar Dizisi Genişlemesi (Repeat Expansion)

**Yer:** `Bölüm_09_Repeat_Expansion.md` · Miyotonik Distrofi — Konjenital form: yenidoğan tuzağı · satır 190

> Konjenital DM1 (CDM1), neredeyse her zaman etkilenmiş anneden çok büyük CTG tekrar sayısı (***genellikle >1000***) miras alan yenidoğanlarda görülür. Ciddi hipotoni ("floppy infant"), solunum yetmezliği ve beslenme güçlükleriyle yoğun bakım başvurusuna yol açar. Annede bilinen DM1 yoksa (çünkü anne hafif etkilenmiş ve farkında olmayabilir), yenidoğanda açıklanamayan hipotoni varlığında anne değerlendirmesi ve DM1 PCR testi hayat kurtarabilir. CDM1, annenin miyotonisine bakılarak anlaşılabilecek bir durumdur (De Serres-Bérard ve ark., 2021; Chau ve Kalsotra, 2015).

**Sorulan:** CDM1 için verilen "neredeyse her zaman anneden" ve ">1000 CTG" ifadeleri doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B17 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 2.4 Çift genom: mitokondriyal fenotip ≠ mitokondriyal kalıtım · satır 95

> Bunun klinik sonucu belirleyicidir. ***Kompleks II tümüyle nükleer kodludur; dolayısıyla izole Kompleks II eksikliği hiçbir zaman maternal kalıtılmaz***. Kompleks I'in 45 civarındaki alt biriminin yalnızca 7'si mtDNA kaynaklıdır; geri kalanındaki bir varyant otozomal resesif bir hastalık üretir. Aynı klinik tablo — örneğin Leigh sendromu — hem *MT-ATP6*'daki bir mtDNA varyantından hem de *SURF1* gibi bir nükleer genden kaynaklanabilir; ilkinde risk maternaldir ve tüm çocuklara geçer, ikincisinde her gebelikte %25'tir. **Fenotip aynıdır, mekanizmanın son yolu aynıdır, ama kalıtım ve dolayısıyla aileye verilecek risk tümüyle farklıdır.**

**Sorulan:** Kompleks II ve Kompleks I alt birim sayıları (45 alt birimin 7'si mtDNA) doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B19 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 2.2 Poliplazmiden eşiğe: dozun sürekli hâle gelmesi · satır 73

> Eşiğin sayısal değeri varyant tipine ve dokuya göre değişir; nokta varyantları için tipik olarak yüksek oranlar (temsilî olarak %60–90 aralığı), tek büyük delesyonlar için ise daha düşük oranlar bildirilmiştir (Gorman ve ark., 2016). Ancak klinisyen için ezberlenmesi gereken sayı değil, **ilkedir**: eşik, dokunun oksidatif enerji talebiyle ters orantılıdır. Sürekli ve yüksek ATP tüketen dokular — merkezî sinir sistemi, kalp kası, iskelet kası, retina ve optik sinir, böbrek tübülü, iç kulak — düşük eşiklidir ve erken etkilenir. Fibroblast gibi düşük talepli dokular yüksek mutant yüklerini bile tolere edebilir. Mitokondriyal hastalıkların neden ***neredeyse her zaman çok sistemli ama nörolojik ve kardiyak ağırlıklı*** seyrettiğinin cevabı budur.

**Sorulan:** Bu genelleme doğru mu? İzole organ tutulumlu tablolar (LHON, izole miyopati) bu ifadeyi zayıflatıyor mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B20 · Bölüm 11 — Mitokondriyal Genetik: Heteroplazmi, Eşik ve Çift Genom

**Yer:** `Bölüm_11_Mitokondriyal_Genetik.md` · 2.3 Yüzde neden sabit değil: darboğaz ve mitotik segregasyon · satır 87

> **🔬 Deep-dive — mtDNA neden babadan geçmez, ve "hiç" mi geçmez?** Paternal mtDNA'nın elenmesi tek bir mekanizmaya değil, üst üste binen birkaç güvenceye dayanır. Birincisi basit bir **seyreltme** sorunudur: olgun bir oosit yüz binler mertebesinde mtDNA taşırken, sperm yalnızca birkaç yüz mitokondri getirir; oran baştan binde birler düzeyindedir. İkincisi **etkin yıkımdır**: döllenmeden sonra sperm kaynaklı mitokondriler işaretlenerek otofajik yolaklarla ortadan kaldırılır. Bu iki katmanın birlikte çalışması, insan pedigrilerinde ***maternal kalıtımın neden istisnasız görünen bir kural gibi davrandığını açıklar***. Literatürde çok az sayıda **paternal mtDNA geçişi** bildirimi bulunmakla birlikte, bunlar son derece nadirdir, bir kısmı tartışmalıdır ve klinik danışmanlık pratiğini değiştirmez. ⚠️ Bu istisnaların sıklığı ve mekanizması hâlâ tartışmalıdır; genetik danışmada maternal kalıtım kuralı esas alınmalı, paternal geçiş rutin bir olasılık olarak sunulmamalıdır.

**Sorulan:** Paternal mtDNA geçişi bildirimleri karşısında bu ifade nasıl konumlandırılmalı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B21 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 2.3 VAF: mozaikliğin sayısı ve tuzakları · satır 94

> **🔬 Deep-dive — VAF ne zaman hücre oranının yarısı DEĞİLDİR?** Dört durumda bu dönüşüm bozulur ve her biri klinikte karşımıza çıkar. **(1) Kopya sayısı değişimleri:** Mozaik bir delesyonda varyant "alel" kaybolmuş durumdadır; VAF yerine kopya sayısı oranı (veya alel dengesi) değerlendirilir ve yarıya bölme mantığı geçerli değildir. **(2) X kromozomu ve hemizigotluk:** Erkekte X'teki bir varyant hemizigottur; taşıyan hücrede tek alel vardır ve o alel varyanttır, dolayısıyla VAF doğrudan hücre oranına eşittir — yarıya bölmek yanlış olur. **(3) Homozigot veya bileşik heterozigot bağlam:** İkinci vuruşun eklendiği hücrelerde alel dengesi değişir. **(4) Örnek saflığı:** Bir doku örneği asla tek tip hücreden oluşmaz; lezyonlu deriden alınan bir biyopside lezyon hücreleri örneğin yalnızca %30'unu oluşturuyorsa, ***ölçülen VAF gerçek klonal yükü olduğundan çok daha düşük gösterir***. Bu son madde, cerrahi örneklerde patologla birlikte "lezyon-zengin" bölge seçmenin neden tanısal başarıyı artırdığını açıklar.

**Sorulan:** Örnek saflığı anlatımı doğru mu? Düzeltme yapılabileceği (lezyon oranına bölme) belirtilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B22 · Bölüm 14 — Digenik, Oligogenik Kalıtım ve Modifiye Edici Lokuslar

**Yer:** `Bölüm_14_Digenik_Oligogenik_Modifier.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 229

> **🟦 Klinikte dikkat — "İki gende varyant bulduk" bir gözlemdir, sonuç değildir:** Her sağlıklı bireyin genomunda çok sayıda nadir varyant bulunur; herhangi iki aday gende birer nadir varyantın rastlantısal olarak bir arada bulunması kaçınılmazdır. Digenik iddiayı kurmak için en az şu üçü gerekir: ***(1) iki ürün arasında gösterilebilir biyolojik bağ*** (aynı kompleks/yolak; protein–protein etkileşimi), **(2)** ailede **birlikte ayrışma** — yalnız çift-taşıyıcılar hasta, **(3)** **bağımsız ailelerde tekrarlanma**. Bunlara fonksiyonel birlikte-etki gösterimi eklenirse iddia güçlenir. Schäffer'in derlemesi, yayımlanmış insan digenik kalıtım örneklerinde en çok işe yarayan iki bilgi kaynağının **aday gen bilgisi** ve **protein–protein etkileşim bilgisi** olduğunu; buna karşılık pozisyonel bağlantı analizinin bu alanda büyük ölçüde başarısız kaldığını göstermiştir (Schäffer, 2013).

**Sorulan:** Üç koşul yeterli mi? Fonksiyonel model (hücre/hayvan) dördüncü koşul olarak eklenmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B23 · Bölüm 14 — Digenik, Oligogenik Kalıtım ve Modifiye Edici Lokuslar

**Yer:** `Bölüm_14_Digenik_Oligogenik_Modifier.md` · 2.2 Trialelik kalıtım: kalıtım modelinin kendisi sorgulanınca · satır 73

> Bu bulgunun kavramsal ağırlığı, tek bir hastalığın ötesindedir. Burada sorgulanan şey bir genin patojenitesi değil, **kalıtım modelinin kendisidir**: aynı lokusta iki patojen alel taşıyan bir bireyin sağlıklı kalabilmesi, "resesif" etiketinin her zaman yeterli olmadığını gösterir. ⚠️ Trialelik kalıtımın BBS'deki kapsamı ve genelleştirilebilirliği literatürde tartışılmıştır; ***bu modelin her ailede geçerli olduğu varsayılmamalı***, ancak kalıtım modelinin sorgulanabilir olduğu ilkesi korunmalıdır.

**Sorulan:** Trialelik kalıtım uyarısı yeterince güçlü mü? Model bugün büyük ölçüde terk edildi mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B24 · Bölüm 16 — Mekanizmadan Varyant Yorumuna: ACMG/ClinGen Sentezi

**Yer:** `Bölüm_16_Mekanizmadan_Varyant_Yorumuna.md` · 1. Kavramsal tanım · satır 45

> **İkincisi, tek bir kriter nadiren yeter.** En güçlü kriter olan PVS1 bile tek başına patojenik sınıfa ulaştırmaz; ***yanına en az bir destekleyici kanıt gerekir***. Bu, çerçevenin muhafazakârlığının kasıtlı bir özelliğidir.

**Sorulan:** Bu ifade nokta puanlama sisteminde doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B25 · Bölüm 16 — Mekanizmadan Varyant Yorumuna: ACMG/ClinGen Sentezi

**Yer:** `Bölüm_16_Mekanizmadan_Varyant_Yorumuna.md` · 2.1 Popülasyon kanıtı: "nadir" hastalığa göre tanımlanır · satır 77

> **🟦 Klinikte dikkat — Bir varyantın "gnomAD'de yok" olması ne kadar kanıttır?** Yokluk, PM2'yi (***orta güçte değil, günümüzde çoğu uzman grubunda destekleyici güce indirilmiş biçimde***) destekler; ama tek başına patojenite kanıtı değildir. Her insan genomunda çok sayıda nadir, işlevsel olarak zararsız varyant vardır. Gen düzeyinde kısıt ölçütleri bu kanıtı bağlamlandırır — **pLI** ExAC veri kümesiyle tanımlanmış (Lek ve ark., 2016), **LOEUF** ise gnomAD ile getirilmiştir (Karczewski ve ark., 2020): kısıtlı bir gende nadir bir kesici varyant anlamlıyken, kısıtsız bir gende aynı bulgu çok daha zayıftır.

**Sorulan:** PM2'nin destekleyiciye indirilmesi genel geçer mi, yoksa VCEP'e göre değişiyor mu diye sunulmalı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B26 · Bölüm 16 — Mekanizmadan Varyant Yorumuna: ACMG/ClinGen Sentezi

**Yer:** `Bölüm_16_Mekanizmadan_Varyant_Yorumuna.md` · 7. Pediatrik genetikten klinik örnekler (çözümlü) · satır 267

> **Örnek 1 — Yenidoğanda dirençli nöbet; *SCN2A* p.Arg1882Gln (de novo).** Doğumun ilk gününde fokal nöbetlerle başvuran bebekte trio WES ile de novo bir missense varyant saptanır. Kanıt zinciri şöyle kurulur: ebeveynlik doğrulanmış de novo (PS2, +4); popülasyonda yok (PM2, +1); bu kodon *SCN2A*'nın bilinen tekrarlayan varyant konumlarındandır (PM1, +2); elektrofizyolojik çalışmalar bu varyantın **işlev kazanımı** yönünde olduğunu ve dinamik aksiyon potansiyeli çalışmasında ateşlemede dramatik artış öngördüğünü göstermiştir (PS3, +4) (Berecki ve ark., 2018). ***Toplam +11 → patojenik***. **Öğreti:** mekanizma yönü burada yalnız sınıfı değil tedaviyi de belirler; erken başlangıçlı, işlev kazanımı yönündeki sodyum kanalı tablolarında sodyum kanal blokerleri yararlı olabilirken, işlev kaybı tablolarında aynı yaklaşım uygun değildir (Brunklaus ve ark., 2020). Ayrıca dikkat: PS3 burada "fonksiyon bozulmuş" dediği için değil, **yönü gösterdiği** için bu kadar değerlidir.

**Sorulan:** Bu çözümlü örneğin puanlaması doğru mu? PS3'ün tam güçte (+4) kullanılması bu veriyle savunulabilir mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### B27 · Bölüm 17 — Klinik Senaryolarla Sentez: Hastadan Mekanizmaya

**Yer:** `Bölüm_17_Klinik_Senaryolarla_Sentez.md` · 2.2 "Negatif" ne demektir? Altı kör nokta · satır 75

> Şüpheli genetik hastalığı olan çocuklarda tanısal getiriyi karşılaştıran, 37 çalışma ve 20.068 çocuğu kapsayan bir sistematik derleme ve meta-analiz, ***tüm genom dizilemenin tanısal getirisini 0,41, tüm ekzom dizilemeninkini 0,36 ve kromozomal mikroarray'inkini 0,10*** olarak bildirmiştir. Aynı analizde, kohort içi karşılaştırma yapan çalışmalarda **trio** analizinin tek bireye göre tanı olasılığını anlamlı biçimde artırdığı gösterilmiştir (olasılık oranı 2,04). Yazarlar, şüpheli genetik hastalığı olan çocuklarda WGS/WES'in **birinci basamak genomik test** olarak düşünülmesi gerektiği sonucuna varmışlardır (Clark ve ark., 2018).

**Sorulan:** Bu meta-analiz sayıları Türkiye pratiğine beklenti olarak aktarılabilir mi? Daha güncel getiri verisi kullanılmalı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

---

## C. Kaynaksız mekanizma ve ders bilgisi (T4-a)

*Programatik denetimin kapatamadığı asıl kategori: kaynaksız, kulağa doğru gelen, "yerleşik ders bilgisi" sayılıp geçilen cümleler.*

### C1 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.E — Varyantın kökeni ve kalıtım kalıpları · satır 95

> Germline varyantların ailedeki dağılımı, klasik kalıtım kalıplarını oluşturur (Şekil 1.3). **Otozomal dominant** kalıtımda tek bir patojen allel hastalık için yeterlidir; soyağacında her kuşakta etkilenen bireyler görülür, geçiş dikeydir ve cinsiyetler eşit etkilenir — NF1, Marfan ve akondroplazi tipik örneklerdir. **Otozomal resesif** kalıtımda hastalık için iki patojen allel gerekir; bu nedenle sağlıklı taşıyıcı iki ebeveynden etkilenen bir çocuk doğabilir, desen daha yataydır ve ***akraba evliliği riski belirgin biçimde artırır*** (kistik fibroz, PKU, SMA). **X'e bağlı resesif** kalıtımda hemizigot oldukları için çoğunlukla erkekler etkilenir, kadınlar genellikle taşıyıcıdır ve karakteristik biçimde erkekten erkeğe geçiş görülmez (DMD, hemofili A). **X'e bağlı dominant** kalıtımda heterozigot kadınlar da etkilenir; bazı genlerde varyant erkekte erken letal olduğundan ailede tekrarlayan erkek kayıpları/düşükler bir ipucu olabilir. Son olarak **mitokondriyal (maternal)** kalıtımda varyant yalnızca anneden tüm çocuklara geçer, babadan hiçbirine geçmez; heteroplazmi nedeniyle ifade oldukça değişkendir (Bölüm 11).

**Sorulan:** Kalıtım kalıplarının özet tanımları doğru ve eksiksiz mi? Akraba evliliği ifadesi Türkiye bağlamında genişletilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C2 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.C — Varyasyon, allel ve varyant tipleri · satır 69

> İki insan genomu birbirinden milyonlarca pozisyonda farklıdır; ama bu farkların ezici çoğunluğu zararsızdır. Klinik genetiğin asıl zorluğu da buradadır: devasa bir nötr varyasyon arka planı içinden, hastalığa gerçekten neden olan varyantı ayıklamak. Bu nedenle modern dilde, herhangi bir referans-dışı değişikliğe nötr bir terim olan **varyant** denir; eskiden yaygın olan "mutasyon" sözcüğü artık daha çok yerleşik adlandırmalarda kullanılır, "polimorfizm" ise popülasyonda yaygın (genellikle %1'den sık) ve çoğunlukla zararsız varyantları anlatır. Patojen olup olmama, varyantın bir başka ekseni olarak ayrıca değerlendirilir; bir varyantın yaygın olması onu otomatik olarak benign yapmaz, ama nadir bir hastalık için güçlü bir benign ipucudur. Burada önemli bir uyarı vardır: ***referans dizi her zaman "sağlıklı" anlamına gelmez; referansta da patojen aleller bulunabilir***.

**Sorulan:** Bu uyarı doğru mu? Örnek verilmeli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C3 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.H — Popülasyon ölçeği ve constraint: bir gen "hata kaldırıyor" mu? · satır 123

> Bu metriklerin neden klinik olarak önemli olduğu, bir LoF varyantıyla karşılaştığımız anda netleşir. Diyelim ki bir hastada bir geni erken sonlandıran bir varyant bulduk. Bu varyantın patojen olup olmadığına karar vermeden önce sorulması gereken ilk soru şudur: *"Bu gen, işlev kaybına duyarlı bir gen mi?"* Eğer gen yüksek pLI / düşük LOEUF ile kısıtlıysa, bu, LoF'un o gen için gerçekten bir hastalık mekanizması olduğuna dair güçlü bir destektir ve birazdan göreceğimiz PVS1 kriterinin uygulanabilirliğini artırır. Tersine, gen LoF'a son derece toleranssa, aynı varyant çok daha şüpheyle karşılanmalıdır. Ancak burada sık yapılan bir hataya düşmemek gerekir: bu metrikler **gen düzeyinde** önceliklendirme araçlarıdır, tek bir varyantın patojenitesini tek başlarına kanıtlamazlar; üstelik ***resesif hastalık yapan LoF genleri (hastalık için iki kopyanın da kaybı gerektiğinden) popülasyonda "tolerant" görünebilir*** — bu onları önemsiz yapmaz, yalnızca metriğin dominant doz hastalıkları için daha bilgilendirici olduğunu gösterir.

**Sorulan:** Constraint metriklerinin sınırları doğru anlatılmış mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C5 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · 2.2. Doza duyarlılık hangi gen sınıflarında, neden kümelenir? · satır 72

> **Stokiyometrik kompleks üyeleri.** Bazı proteinler hücrede tek başına değil, sabit oranlarda bir araya gelen çok-alt-birimli komplekslerde iş görür (ribozom, spliceozom, kohesin, bazı yapısal kompleksler). Bir alt birimin dozu yarıya inerse, kompleksin **doğru stokiyometride** montajı bozulur; eksik veya dengesiz alt birimler hem işlevsiz kompleks hem de serbest, yanlış katlanmış kalıntılar yaratabilir. **Gen dengesi hipotezi** (gene ***balance hypothesis***), kompleks üyelerinin neden doza duyarlı genler arasında zenginleştiğini açıklar: dengesizlik etkilerinin, makromoleküler komplekslerin, etkileşim ağının ve sinyal yolaklarının üyeleri arasındaki **stokiyometrik farklardan** kaynaklandığı öne sürülür (Birchler ve Veitia, 2012).

**Sorulan:** "Dengeli ifade hipotezi" bu adla anılıyor mu ve burada doğru kullanılmış mı? (Kitapta kaynaksız.)

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C7 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · 4.4. Haploinsufficiency neden değişken penetrans ve ekspresivite gösterir? · satır 140

> Haploinsufficiency, Bölüm 1'de tanıtılan **eksik penetrans ve değişken ekspresivite** kavramlarının en sık zeminlerinden biridir, ve bunun nedeni yine eşik mantığında gizlidir. Doz tam eşiğin **kıyısına** düştüğünde, sistemin eşiğin altında mı üstünde mi kalacağını belirleyen küçük etkenler öne çıkar: aynı yolaktaki **modifiye edici** varyantlar, ikinci (sağlam) allelin ifade düzeyindeki bireysel farklar, çevresel etkenler ve gelişim sırasındaki **stokastik (rastlantısal) gen ifadesi gürültüsü**. Eşikten uzak (çok düşük doz) varyantlarda fenotip daha öngörülebilir ve ağırken, ***eşiğe yakın doz bırakanlarda penetrans eksik, ekspresivite değişken olur***. Bu, neden aynı ailede aynı HI varyantını taşıyan bireylerin farklı şiddette etkilenebildiğini açıklar (örn. Holt-Oram'da aile içi değişkenlik; Bruneau ve ark., 2001; [DOI](https://doi.org/10.1016/s0092-8674(01)00493-7)).

**Sorulan:** HI'da değişken penetransın eşik-yakınlığıyla açıklanması doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C8 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 2.1. Zehirli alt birim: varyant ürün sağlamı nasıl "zehirler"? · satır 61

> **🔬 Deep-dive — DN'in iki ön koşulu ve neden bazı genlerde olur, bazılarında olmaz?** ***Bir varyantın DN etki yapabilmesi için iki şart gerekir***. **Birincisi, varyant ürün üretilmeli ve stabil kalmalıdır.** Erken stop kodonu yapan, NMD ile yıkılan ya da proteini tümüyle yok eden varyantlar DN yapamaz — ortada zehirleyecek bir ürün kalmaz; bunlar saf LoF/haploinsufficiency yapar. Bu yüzden DN varyantlar tipik olarak **missense veya in-frame** (küçük in-frame delesyon/insersiyon) değişikliklerdir: ürün yapılır, komplekse girebilecek kadar "normal" görünür, ama işlevi bozuktur. **İkincisi, ürün sağlam ürünle fiziksel olarak etkileşmelidir** — yani protein multimerik olmalı veya bir kompleksin/ağın parçası olmalıdır. Tek başına (monomer olarak) çalışan ve başka kopyalarla etkileşmeyen bir enzimde DN beklenmez; orada bir bozuk kopya yalnız kendi payını kaybettirir (haploinsufficiency). Gerasimavicius, Livesey ve Marsh (2022), patojenik missense varyantların yapısal etkilerini mekanizmaya göre çözümlediklerinde tam bu beklentiyi doğrulamıştır: DN varyantlar **protein–protein arayüzlerinde belirgin biçimde zenginleşir** ve LoF varyantlardan farklı olarak protein kararlılığını çok daha az bozarlar — yani "katlanmayı yıkıp ürünü yok eden" değil, "ürünü ayakta tutup etkileşimi/işlevi sabote eden" değişikliklerdir (Gerasimavicius ve ark., 2022, *Nat Commun*; [DOI](https://doi.org/10.1038/s41467-022-31686-6)).

**Sorulan:** İki ön koşul doğru ve yeterli mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C9 · Bölüm 5 — Dominant-Negatif (Baskın-Olumsuz Etki)

**Yer:** `Bölüm_05_Dominant_Negatif.md` · 8. Sık yapılan hatalar · satır 209

> **🟦 Klinikte dikkat kutusu**
> - ***Dominant, ağır, missense-ağırlıklı ve multimerik/kompleks bir protein → dominant-negatifi erken düşün***.
> - Aile içinde aynı varyantın çok değişken ağırlıkta seyrettiği DN tablolarında, modifiye edici etkiler ve doku-spesifik kompleks oranları rol oynayabilir (penetrans/ekspresivite, Bölüm 1).
> - Genetik danışmada DN hastalıklar genellikle **dominant** kalıtım riski (%50 aktarım) taşır; ancak de novo DN varyantlar da sıktır (özellikle ağır/letal formlarda).

**Sorulan:** Bu klinik pusula güvenilir mi, yoksa fazla kestirme mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C10 · Bölüm 6 — Neomorfik ve Antimorfik Alleller

**Yer:** `Bölüm_06_Neomorfik_Antimorfik.md` · 7.3. Toksik kazanım ve bir uyarı · satır 180

> Neomorfik spektrumun bir ucu **toksik kazanımdır**: ürünün zararlı bir fiziksel özellik kazanması. Bunun en bilinen biçimleri, repeat expansion hastalıklarında (poliglutamin → Huntington vb.) mutant proteinlerin yanlış katlanıp **agregat** oluşturmasıdır; bu mekanizma kendi bölümünde (Bölüm 9) ayrıntılı işlenecektir. Burada yalnızca kavramsal yerini işaretliyoruz: ***toksik kazanım da neomorfik gibi "varyant ürünün zararlı varlığından" doğar, dolayısıyla dominanttır*** ve basit LoF değildir. ⚠️ Belirli bir genin neomorfik/toksik mekanizma yaptığı iddiası, her zaman güncel ve gen-spesifik (tercihen VCEP/ClinGen) kaynakla doğrulanmalıdır; bazı genlerde mekanizma varyanta veya bağlama göre değişir.

**Sorulan:** Toksik kazanımın neomorfikle bu şekilde yan yana konması kavramsal olarak doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C12 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 2.1 İmprint nasıl kurulur ve okunur? · satır 56

> ***Metilasyonun aleli her zaman doğrudan susturmadığını vurgulamak gerekir; kimi ICR'ler bir izolatör (insulator) üzerinden çalışır***. Bunun ders kitabı örneği, bu bölümün ilerleyen kısmında Beckwith-Wiedemann ve Silver-Russell sendromları bağlamında ayrıntılandıracağımız 11p15.5'teki *IGF2/H19* bölgesidir. Burada ICR1, metilsiz maternal alelde CTCF proteinini bağlayarak bir izolatör kurar; bu izolatör, ortak enhancer'ların *IGF2*'ye ulaşmasını engeller, dolayısıyla maternal alelde *H19* ifade edilir, *IGF2* susar. Paternal alelde ise ICR1 metilidir, CTCF bağlanamaz, izolatör kurulamaz ve enhancer'lar *IGF2*'yi çalıştırır. Böylece **aynı metilasyon işareti**, bağlamına göre bir geni açar (*IGF2*, paternal) başka birini kapatır (*H19*, paternal) — imprintin "tek şalter, çift sonuç" mantığı budur.

**Sorulan:** İzolatör mekanizması (H19/IGF2, CTCF) doğru anlatılmış mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C13 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 2.3 Uniparental dizomi nasıl oluşur? · satır 74

> **🔬 Deep-dive — İzodizomi neden iki ayrı yolla hastalık yapar?** ***UPD'nin iki ayrı patojenik yüzü vardır*** ve bunları karıştırmamak gerekir. **(1) İmprint dengesizliği:** UPD imprintli bir kromozomu tutuyorsa (15, 11, 7, 14, 6, 20…), her iki kopyanın tek ebeveynden gelmesi imprint dozunu bozar — bu yolla PWS, AS, SRS ve TNDM oluşur. Bu yol için izo/hetero ayrımı önemli değildir; önemli olan ebeveyn kökenidir. **(2) Resesif varyantın homozigotlaşması:** İzodizomi, tek bir homoloğun özdeş kopyası olduğu için, o homologdaki her varyant **homozigot** hâle gelir. Anne bir resesif hastalık için taşıyıcıysa (heterozigot) ve çocuk o kromozomun izodizomisini taşıyorsa, çocuk **baba hiç taşıyıcı olmadığı hâlde** resesif hastalığı homozigot olarak sergileyebilir. Bu, bir çocukta beklenmedik (ebeveyn taşıyıcılığıyla açıklanamayan) resesif bir hastalık görüldüğünde neden UPD'nin akla gelmesi gerektiğini açıklar. Heterodizomi ise iki farklı homolog içerdiği için bu maskeleme etkisini yaratmaz — ancak trizomi kurtarma sonrası mayotik rekombinasyon nedeniyle sıklıkla parçalı izodizomi segmentleri de barındırabilir.

**Sorulan:** İzodizominin iki mekanizması (imprint dengesizliği + resesif varyantın homozigotlaşması) doğru ayrılmış mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C14 · Bölüm 10 — İmprinting, Uniparental Dizomi ve Epigenetik Mekanizmalar

**Yer:** `Bölüm_10_Imprinting_UPD_Epigenetik.md` · 2.3 Uniparental dizomi nasıl oluşur? · satır 68

> UPD'yi klinik olarak anlamak için oluşum mekanizmasını bilmek şarttır, çünkü ***mekanizma hem hangi lokusların homozigot olduğunu hem de tekrarlanma riskini belirler***. Şekil 10.2'te gösterilen üç ana yol vardır. En sık yol **trizomi kurtarma**dır: mayoz sırasında (özellikle mayoz I'de) ayrılamama sonucu dizomik bir gamet oluşur; bu gamet normal bir gametle döllenince trizomik bir zigot ortaya çıkar. Trizomiler çoğu kez yaşamla bağdaşmadığından, embriyo fazla kromozomu atarak "kurtulmaya" çalışır. Eğer atılan kromozom, tek kopyayı sağlayan ebeveynden geliyorsa, geriye kalan iki kopya aynı ebeveynden olur — **UPD** oluşur. Mayoz I hatası kaynaklı olduğunda bu UPD **heterodizomik** olur: aynı ebeveynin iki *farklı* homoloğunu içerir. Ancak bu kuralı mutlaklaştırmamak gerekir. Kromozom 7 üzerinde yapılan bir derleme, maternal UPD7 olgularında izodizomi (n = 11) ile tam/kısmi heterodizominin (n = 12) **hemen hemen eşit sayıda** bildirildiğini ve olguların yaklaşık **yarısının** post-zigotik mitotik segregasyon hatasından kaynaklandığını göstermiştir; yani UPD7'de trizomi kurtarma tek yol değildir (Mergenthaler ve ark., 2000). Pratik çıkarım: bir UPD'nin izo mu hetero mu olduğu, oluşum mekanizmasını *olasılıklı* olarak gösterir, kesin belirlemez.

**Sorulan:** UPD oluşum mekanizmalarının (trizomi kurtarma, monozomi kurtarma, gamet tamamlama) klinik sonuçlara bağlanması doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C15 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 1. Kavramsal tanım · satır 40

> Son olarak iki özel kavram, tabloyu tamamlar. **Letal-mozaik hipotezi**, bazı varyantların konstitüsyonel hâlde embriyoyu öldürdüğünü, ancak mozaik hâlde — sağlam hücrelerle karışık olarak — yaşayabildiğini öne sürer (Happle, 1987); ***bu hipotez, bir grup sendromun neden istisnasız sporadik olduğunu açıklar***. **Revertant mozaiklik** ise ters yöndeki olaydır: konstitüsyonel olarak hastalıklı bir bireyde, bazı hücrelerde ikinci bir olay varyantı düzelterek sağlıklı hücre klonları oluşturur.

**Sorulan:** Happle'ın letal-mozaik hipotezi bugün hâlâ geçerli mi? "Daima sporadik" ifadesi tutuyor mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C16 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 2.2 Hangi bölme tutuldu? Tekrarlanma riskinin tek belirleyicisi · satır 72

> Klinik genetikte mozaikliğin en önemli sonucu, tekrarlanma riskini yeniden tanımlamasıdır. Burada birbirine sürekli karıştırılan iki ayrı soru vardır ve bunları ayırmak zorunludur: *"Hastanın fenotipini ne açıklıyor?"* sorusunun cevabı **somatik bölmededir**; ***"Kardeşinde tekrar eder mi?" sorusunun cevabı ise germ hücresi bölmesindedir***. Şekil 12.2, bu iki bölmenin dört olası kombinasyonundan klinikte anlamlı olan üçünü karşılaştırır.

**Sorulan:** İki sorunun bu şekilde ayrılması danışma pratiğinde doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C17 · Bölüm 12 — Mozaiklik: Postzigotik Varyantlar, VAF ve Tekrarlanma Riski

**Yer:** `Bölüm_12_Mozaiklik.md` · 1. Kavramsal tanım · satır 40

> Son olarak iki özel kavram, tabloyu tamamlar. **Letal-mozaik hipotezi**, bazı varyantların konstitüsyonel hâlde embriyoyu öldürdüğünü, ancak mozaik hâlde — sağlam hücrelerle karışık olarak — yaşayabildiğini öne sürer (Happle, 1987); bu hipotez, bir grup sendromun neden istisnasız sporadik olduğunu açıklar. ***Revertant mozaiklik ise ters yöndeki olaydır***: konstitüsyonel olarak hastalıklı bir bireyde, bazı hücrelerde ikinci bir olay varyantı düzelterek sağlıklı hücre klonları oluşturur.

**Sorulan:** Revertant mozaiklik anlatımı doğru mu? Bu konu bir textbook'ta bu ağırlıkta yer almalı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C18 · Bölüm 13 — Kodlamayan (Noncoding) ve Regülatör Varyantlar

**Yer:** `Bölüm_13_Noncoding_Regulator_Varyantlar.md` ·  · satır 3

> **Bölümün çekirdek tezi:** Genomun protein kodlayan kısmı %2'den azdır; klinik genetiğin neredeyse tamamı ise on yıllardır bu %2'ye bakmıştır. Kodlamayan varyantlar, bu kör noktanın adıdır. Bu bölümün çekirdek iddiası şudur: **kodlamayan bir varyant, proteinin tek bir amino asidini bile değiştirmeden hastalık yapabilir — çünkü hedefi ürünün kendisi değil, ürünün ifade programıdır.** Bir promotör varyantı genin ne kadar üretileceğini, bir enhancer varyantı hangi dokuda üretileceğini, bir 5′UTR varyantı ne kadar verimli çevrileceğini, bir TAD sınırı varyantı ise hangi genin üretileceğini bozar. Buradan üç klinik sonuç doğar: (1) bu varyantları görmek için **ekzom yetmez, WGS gerekir**; (2) ***fenotip çoğu zaman şaşırtıcı biçimde dar ve tek organa sınırlıdır, çünkü etkilenen düzenleyici doku-özgüdür***; (3) yorumlamada **PVS1 uygulanamaz** ve kanıtın ağırlık merkezi hesaplamadan **fonksiyonel deneye** kayar. Bölüm 8'de yapısal varyant ölçeğinde gördüğümüz düzenleyici mimariyi (TAD, enhancer hijacking) bu bölüm **tek nükleotid** ölçeğine indirir.

**Sorulan:** Bu genelleme doğru mu? PVS1'in uygulanamaması ve ağırlığın fonksiyonel deneye kayması ifadesi de değerlendirilsin.

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C20 · Bölüm 15 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_15_Ayni_Gen_Farkli_Hastalik.md` · 2.3 Üçüncü eksen: varyant konumu — domain ve izoform · satır 92

> Aynı doku-seçicilik sorusu daha geniş bir çerçevede de sorulmuştur: laminler bütün hücrelerde ifade edilirken hastalıkların neden büyük ölçüde doku-seçici fenotiplerle ortaya çıktığı hâlâ tam açıklanmış değildir; hastalık yapan varyantların nükleer morfolojiyi bozduğu gösterilmiştir, ancak bu bozulmanın patolojiye nasıl dönüştüğü ancak anlaşılmaya başlanmıştır (Worman, 2012). ⚠️ Dolayısıyla ***domain–fenotip haritaları güçlü örüntüler sunar, ancak birebir öngörü aracı olarak kullanılmamalıdır***.

**Sorulan:** Domain–fenotip haritalarının sınırı doğru çizilmiş mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C21 · Bölüm 15 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_15_Ayni_Gen_Farkli_Hastalik.md` · 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu) · satır 418

> ### 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu)
> "Bu bölümdeki tüm kaynakların PMID/DOI bilgisini kontrol et. PMID veya DOI veremediğin kaynağı çıkar. Kaynağı olmayan iddiayı 'kaynak doğrulaması gerekli' olarak işaretle."
>
> **Bu bölüm için durum:** **22/22 kaynak PMID+DOI doğrulandı** (9'u bu oturumda PubMed MCP ile — Thaxton 2022, Strande 2017, Toydemir 2006, Eriksson 2003, Worman 2012, Bertrand 2011, Marini 2007, Kaler 2011, Mantovani 2018; 12'si Bölüm_00 kaynak kütüğünden yeniden kullanıldı). Bölüm, 27.07.2026 tarihli iddia-düzeyi doğrulama turundan geçmiştir; turda *SCN2A*/otizm atfı Sanders 2018'e taşınmış ve "altı eksen" çerçevesi 🏷️ etiketlenmiştir (bkz. `Dogrulama_Kutugu.md`).
>
> **İşaretlenen iddialar:** (1) ⚠️ Domain–fenotip haritaları güçlü örüntüler sunar ancak birebir öngörü aracı değildir; laminopatilerde nükleer morfoloji bozukluğunun patolojiye nasıl dönüştüğü henüz tam açıklanmamıştır (Worman, 2012). (2) *COL4A3*/*COL4A4* (ince bazal membran nefropatisi ↔ otozomal resesif Alport sendromu) ve *RYR1* (malign hipertermi/santral kor ↔ bialelik konjenital miyopati) örnekleri, kalıtım modu eksenini örneklemek üzere ***yerleşik ders bilgisi düzeyinde verilmiştir; bu bölümde ayrıca PubMed doğrulaması yapılmamıştır***. (3) *FGFR3* varyant–fenotip eşleşmeleri (p.Asn540Lys, p.Gly380Arg, p.Lys650Met, p.Lys650Glu, p.Arg248Cys) yerleşik klinik genetik bilgisidir; bu bölümde doğrudan kaynaklanan noktalar p.Arg621His (Toydemir, 2006) ve p.Gly380Arg'nin konstitütif aktivasyonudur (Webster ve Donoghue, 1996). (3) 🏷️ **"Allelik serinin altı ekseni" çerçevesi kitabın pedagojik sentezidir**; literatürde bu adla yerleşik bir sınıflandırma değildir — eksenlerin bileşenleri kaynaklı, gruplama editöryaldir (§2 girişindeki etikete bkz.).

**Sorulan:** COL4A3/COL4A4 ve RYR1 örneklerinin kaynaksız, ders bilgisi olarak verilmesi kabul edilebilir mi? İçerik doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C22 · Bölüm 15 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_15_Ayni_Gen_Farkli_Hastalik.md` · 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu) · satır 418

> ### 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu)
> "Bu bölümdeki tüm kaynakların PMID/DOI bilgisini kontrol et. PMID veya DOI veremediğin kaynağı çıkar. Kaynağı olmayan iddiayı 'kaynak doğrulaması gerekli' olarak işaretle."
>
> **Bu bölüm için durum:** **22/22 kaynak PMID+DOI doğrulandı** (9'u bu oturumda PubMed MCP ile — Thaxton 2022, Strande 2017, Toydemir 2006, Eriksson 2003, Worman 2012, Bertrand 2011, Marini 2007, Kaler 2011, Mantovani 2018; 12'si Bölüm_00 kaynak kütüğünden yeniden kullanıldı). Bölüm, 27.07.2026 tarihli iddia-düzeyi doğrulama turundan geçmiştir; turda *SCN2A*/otizm atfı Sanders 2018'e taşınmış ve "altı eksen" çerçevesi 🏷️ etiketlenmiştir (bkz. `Dogrulama_Kutugu.md`).
>
> **İşaretlenen iddialar:** (1) ⚠️ Domain–fenotip haritaları güçlü örüntüler sunar ancak birebir öngörü aracı değildir; laminopatilerde nükleer morfoloji bozukluğunun patolojiye nasıl dönüştüğü henüz tam açıklanmamıştır (Worman, 2012). (2) *COL4A3*/*COL4A4* (ince bazal membran nefropatisi ↔ otozomal resesif Alport sendromu) ve *RYR1* (malign hipertermi/santral kor ↔ bialelik konjenital miyopati) örnekleri, kalıtım modu eksenini örneklemek üzere **yerleşik ders bilgisi** düzeyinde verilmiştir; bu bölümde ayrıca PubMed doğrulaması yapılmamıştır. (3) *FGFR3* varyant–fenotip eşleşmeleri (p.Asn540Lys, p.Gly380Arg, p.Lys650Met, p.Lys650Glu, p.Arg248Cys) ***yerleşik klinik genetik bilgisidir***; bu bölümde doğrudan kaynaklanan noktalar p.Arg621His (Toydemir, 2006) ve p.Gly380Arg'nin konstitütif aktivasyonudur (Webster ve Donoghue, 1996). (3) 🏷️ **"Allelik serinin altı ekseni" çerçevesi kitabın pedagojik sentezidir**; literatürde bu adla yerleşik bir sınıflandırma değildir — eksenlerin bileşenleri kaynaklı, gruplama editöryaldir (§2 girişindeki etikete bkz.).

**Sorulan:** Listelenen FGFR3 varyant–fenotip eşleşmelerinin tamamı doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### C23 · Bölüm 15 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_15_Ayni_Gen_Farkli_Hastalik.md` · 6. Varyant yorumlama açısından önemi (ACMG/ClinGen) · satır 227

> **PM1 (mutasyonel hotspot / kritik domain).** ***Hotspot her zaman bir hastalığın hotspot'udur***. Domain-temelli kanıt, ancak hastanın fenotibi o domainle ilişkili hastalık varlığına uyuyorsa geçerlidir.

**Sorulan:** PM1'in bu şekilde koşullanması doğru mu?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### D2 · Bölüm 1 — Genetik Hastalık Mekanizması Nedir?

**Yer:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · 1.I — Penetrans ve ekspresivite: en sık karıştırılan ikili · satır 137

> Penetransla ilgili kritik ve sıkça gözden kaçan bir nokta, onun sabit bir sayı olmadığıdır; çoğu zaman **yaşa bağlı bir eğridir** (Şekil 1.6). Geç başlangıçlı hastalıklarda — özellikle herediter kanser sendromlarında — genç bir taşıyıcı henüz tamamen sağlıklı olabilir, ancak riski yaşla birlikte artar. Penetrans ayrıca cinsiyete de bağlı olabilir. Bunun pratik karşılığı, presemptomatik taramanın ve genetik danışmanın temelini oluşturur: "bu yaşta sağlıklı olması" bir varyantı dışlamaz. Tüm bu olguların — eksik penetransın ve değişken ekspresivitenin — altında yatan moleküler nedenler arasında allel dozu, diferansiyel allelik ekspresyon, kopya sayısı varyasyonu, cis ya da trans konumdaki modifiye edici varyantlar, yaş, cinsiyet ve epigenetik/çevresel etkenler sayılır (Cooper ve ark., 2013). Aklımızda tutmamız gereken basit pusula şudur: **Penetrans** "var mı?" (Presence), **Ekspresivite** "ne kadar?" (Extent) sorusudur — ***🏷️ bu İngilizce baş harflere dayanan bellek desteği kitabın kendi anlatım aracıdır***, yerleşik bir terminoloji kuralı değildir.

**Sorulan:** İngilizce baş harfe dayanan bir bellek desteği Türkçe bir kitapta işe yarar mı? Türkçe bir alternatif önerir misiniz?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### D3 · Bölüm 15 — Aynı Gen, Farklı Hastalık: Allelik Seriler

**Yer:** `Bölüm_15_Ayni_Gen_Farkli_Hastalik.md` · 2. Moleküler mekanizma: allelik seriyi doğuran altı eksen · satır 54

> 🏷️ **Bu altı eksenli çerçeve kitabın pedagojik sentezidir.** Eksenlerin her biri ayrı ayrı kaynaklıdır ve bu kitabın önceki bölümlerinde tek tek işlenmiştir (mekanizma yönü → Bölüm 2–6; rezidüel işlev → Bölüm 2; varyant konumu → Bölüm 2 ve 7; kalıtım modu → Bölüm 1 ve 3; zamanlama → Bölüm 1 ve 12; bağlam → Bölüm 14). Buna karşılık ***"allelik serinin altı ekseni" literatürde bu adla yerleşik bir sınıflandırma değildir***; eksen sayısı ve gruplama editöryaldir ve öğretme kolaylığı için seçilmiştir. Bir raporda veya yayında bu çerçeveye yerleşik bir taksonomiymiş gibi atıf yapılmamalıdır.

**Sorulan:** Altı eksen doğru seçilmiş mi? Eksik/fazla eksen var mı? Çerçeve kitapta kalsın mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### D4 · Bölüm 16 — Mekanizmadan Varyant Yorumuna: ACMG/ClinGen Sentezi

**Yer:** `Bölüm_16_Mekanizmadan_Varyant_Yorumuna.md` · 2.6 Bütün kitabı tek tabloda toplamak · satır 123

> Şekil 16.3, bu bölümün ağırlık merkezidir: ***kitabın on dört mekanizma bölümünün her birinin, sekiz kriter ailesiyle ilişkisini tek matriste özetler***.

**Sorulan:** Matris pedagojik olarak sağlam mı? Normatif tabloyla karıştırılma riski yeterince önlenmiş mi?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

<br>

### D5 · Bölüm 3 — Haploinsufficiency (Yetersiz Doz)

**Yer:** `Bölüm_03_Haploinsufficiency.md` · 4.5. Bir genin haploinsufficient olduğunu nasıl anlarız? Popülasyon metrikleri · satır 148

> ![Şekil 3.4 — ***Dozaj duyarlılığı spektrumu ve onu ölçen metrikler***](assets/sekil_13_dozaj_duyarlilik_spektrumu.svg)

**Sorulan:** Dozaj duyarlılığını bir spektrum olarak sunmak doğru mu? Metriklerin (pLI, LOEUF, pHaplo, pTriplo, HI-indeksi) tek eksene yerleştirilmesi yanıltıcı mı?

**Değerlendirme:**  ☐ D  ☐ Y  ☐ A → 

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

---

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
