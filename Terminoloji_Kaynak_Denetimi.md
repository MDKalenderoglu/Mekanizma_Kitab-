# Terminoloji ve Adlandırma Kaynak Denetimi

**Tarih:** 02.08.2026

**Kapsam:** `kitap/06_Kisaltmalar.md`, `kitap/07_Terminoloji_ve_Yazim_Kurallari.md`, aktif kitap genelindeki terim tutarlılığı ve şekil/algoritma/tablo liste bağlantıları.

**Durum:** Kullanıcı onayıyla uygulandı; Git geçmişi commit düzeyinde korunur, push kullanıcı tarafından yapılır.

Bu kayıt, Türkçe terimlerin yalnız İngilizceden çevrilmediğini; Türkiye'deki kurumsal ve akademik kullanımla karşılaştırıldığını göstermek için tutulur. Türkçe tıp dilinde tek bir bağlayıcı terminoloji otoritesi bulunmayan terimlerde kullanım çeşitliliği saklanmış, tercih gerekçesi açıkça yazılmıştır. Uluslararası adlandırma kuralları Türkçe kullanım kaynaklarından ayrı değerlendirilmiştir.

## 1. Denetim yöntemi

1. İngilizce açılım ve teknik anlam, terimin sahibi veya normatif otoritesi üzerinden doğrulandı: HGVS, HGNC, ClinGen, NCBI ve IUPHAR/BPS.
2. Türkçe karşılıklar için öncelik Tıbbi Genetik Derneği, T.C. Sağlık Bakanlığı, uzmanlık dernekleri, üniversite hastaneleri ve Türkçe hakemli tıp yayınlarına verildi.
3. Tek ve bağlayıcı bir Türkçe karşılık bulunmadığında en az iki kullanım karşılaştırıldı. Kitap tercihi, yerleşiklik, açıklık ve bilimsel anlamı koruma ölçütleriyle seçildi.
4. Kurum adları ve uluslararası veri tabanı adları özgün biçimleriyle korundu; Türkçe sütununda bunların açıklayıcı karşılığı verildi.
5. Kaynakta yerleşik Türkçe karşılığı bulunmayan çok yeni/özgül terimlerde yapay bir “resmî çeviri” iddia edilmedi; karşılığın açıklayıcı çeviri olduğu belirtildi.

## 2. Uygulanan değişiklikler

| Alan | Önce | Sonra | Dayanak / gerekçe |
|---|---|---|---|
| Kısaltma tabloları | İngilizce açılım ile Türkçe karşılık aynı hücrede veya eksik | İngilizce açılım ve Türkçe karşılık/açıklama ayrı sütunlarda | Özgün terim ile çevirinin birbirine karışmasını önler |
| NMD | anlamsız aracılı mRNA yıkımı | nonsense aracılı mRNA yıkımı | Türk tıbbi genetik kullanımında “nonsense aracılı” biçimi görülür; yerleşik teknik terimi yanlış çağrışımdan korur [T1] |
| VAF | varyant alel frekansı (okuma oranı) | varyant alel fraksiyonu; Türkçe yayınlardaki “varyant alel frekansı” kullanımı ayrıca belirtildi | `fraction`, bir örnekteki varyant okuma payını anlatır; “okuma oranı” kaldırıldı [T10] |
| VUS | belirsiz önemde varyant | klinik önemi belirsiz varyant | Kullanıcının belirttiği doğal Türkçe söz dizimi ve Türkiye'deki klinik/akademik kullanım [T2, T3] |
| pLoF | öngörülen işlev kaybı | öngörülen işlev kaybettirici varyant | pLoF çoğu bağlamda etkiyi değil, bu etkiyi oluşturacağı öngörülen varyant sınıfını belirtir |
| WES / WGS | tüm ekzom/genom dizileme | tüm ekzom/genom dizilemesi | Türkçe ad tamlama yapısı standartlaştırıldı [T1] |
| CMA | kromozomal mikroarray | kromozomal mikrodizin analizi | İngilizce araç adı yerine Türkçe açıklama; özgün açılım ayrı sütunda korundu |
| CGH | Türkçe karşılık yok | karşılaştırmalı genomik hibridizasyon | Yerleşik Türkçe teknik kullanım |
| SNP array | Türkçe karşılık yok | tek nükleotid polimorfizmi mikrodizini | Açıklayıcı Türkçe karşılık; özgün açılım ayrı tutuldu |
| MLPA | Türkçe karşılık yok | multipleks ligasyona bağımlı prob amplifikasyonu | Türkçe tıbbi genetik yayınlarındaki kullanım [T9] |
| PCR / ddPCR | Türkçe karşılık yok | polimeraz zincir reaksiyonu / dijital damlacık PCR | Türkçe moleküler tanı kullanımı [T11] |
| MPRA | massively **paralel** reporter assay | massively **parallel** reporter assay; yüksek ölçekli paralel raportör analizi | İngilizce yazım hatası düzeltildi; açıklayıcı Türkçe karşılık eklendi |
| ESE/ESS, ISE/ISS | Yalnız İngilizce açılım | Ekzonik/intronik splicing güçlendiricisi ve baskılayıcısı | Karşılıklar anlamı koruyacak şekilde ayrı sütuna eklendi |
| NAHR | Yalnız İngilizce açılım | alelik olmayan homolog rekombinasyon | “Non-allelic” Türkçe `alelik olmayan` standardıyla eşleştirildi |
| RAN | Eksik İngilizce açılım | repeat-associated non-AUG translation; AUG'den bağımsız, tekrarla ilişkili translasyon | Açılım tamamlandı |
| Hastalık tablosu | Satır başlarında karışık büyük/küçük harf | İlk sözcük ve özel adlar büyük; ortak adlar küçük | Cümle düzeni bütün tabloya uygulandı |
| DMD/BMD | Duchenne / Becker musküler distrofi | Duchenne ve Becker musküler distrofi | Türkçe yayınlardaki ortak kullanım; eğik çizgiyle eksik adlandırma kaldırıldı [T6] |
| CMT1A | Charcot-Marie-Tooth | Charcot–Marie–Tooth hastalığı tip 1A | Eponimler arasındaki bağ en dash ile; hastalık adı Türkiye'deki kurumsal kullanımla uyumlu [T7] |
| HNPP | herediter basınca duyarlı nöropati | Herediter basınca duyarlı nöropati | Yerleşik Türkçe nöroloji kullanımı ve satır başı biçimi [T4] |
| OI | osteogenesis imperfekta | Osteogenezis imperfekta | Türkçe akademik kullanım ve Türkçe sesletim [T5] |
| KF | kistik fibroz | Kistik fibrozis | Sağlık Bakanlığı ve Türkçe klinik kullanım [T8] |
| PWS/AS, BWS/SRS | Sendrom sözcüğü yalnız ikinci ada bağlanabilecek yapı | Her hastalık adı için `sendromu` ayrı yazıldı | Anlam belirsizliği giderildi |
| FXTAS/FXPOI | frajil X ilişkili ... / primer over yetmezliği | Her iki ad da `Frajil X ile ilişkili` biçiminde tamamlandı | İkinci adın da frajil X ilişkisi açıklaştırıldı |
| LHON | Leber herediter optik nöropati | Leber herediter optik nöropatisi | Türkçe ad tamlaması düzeltildi |
| PROS | *PIK3CA* ilişkili | *PIK3CA* ile ilişkili | Gen sembolüne doğrudan Türkçe ek zinciri yerine taşıyıcı sözcük kullanıldı [T10] |
| DIPG | diffüz **intrensek** pontin gliom | Diffüz **intrinsik** pontin gliom | Yazım hatası düzeltildi |
| CATSHL | Kamptodaktili, uzun boy ve işitme kaybı | Kamptodaktili, uzun boy, **skolyoz** ve işitme kaybı | Kısaltmanın `S` bileşeni eksikti; resmî hastalık kaydıyla tamamlandı [U8] |
| WAGR | ... gelişim geriliği | ... zihinsel yetersizlik | `R` bileşeninin güncel anlamı intellectual disability/impaired intellectual development; Türkçe olgu kullanımıyla karşılaştırıldı [U9, T12] |
| ID/DD | zihinsel yetersizlik / gelişimsel gerilik | Zihinsel yetersizlik / gelişimsel gecikme | `disability` ve `delay` birbirinden ayrıldı |
| NaV1.2 | Açıklamasız protein örneği | *SCN2A* geninin kodladığı voltaj kapılı sodyum kanalı α-alt birimi olduğu açıklandı | Gen sembolü ile kanal/protein adının karışmasını önler [U6, U7] |
| HGVS referans dizisi | Transkriptin bölümde bir kez verilmesi HGVS kuralı gibi sunuluyordu | Formal rapor kuralı ile kitap içi tekrar azaltma tercihi ayrıldı | Referans ve sürüm gereği normatif; anlatıdaki tekrar azaltma editöryal tercihtir [U1, U2] |
| `Ter` / `*` | Yalnız `Ter` geçerli izlenimi | HGVS'nin ikisini de kabul ettiği, kitabın `Ter` seçtiği yazıldı | Kural ile kitap tercihi ayrıldı [U1, U4] |
| `in cis` / `in trans` | `[;]` yerine sözel ifade | Formal HGVS faz gösterimi ve düzyazı açıklaması ayrı verildi | Aynı alel `c.[v1;v2]`, farklı aleller `c.[v1];[v2]` [U3] |
| Protein kodu | Üç harfli kod mutlak HGVS zorunluluğu gibi | HGVS'nin üç harfli kodu yeğlediği, kitabın bunu zorunlu tuttuğu belirtildi | Normatif öneri ile yayın stili ayrıldı [U1] |
| İç karar kodları | E5, F6 ve G2.2 okuyucu metninde görünüyordu | Okuyucuya açık metinden kaldırıldı | İç editöryal izler yalnız değerlendirme kayıtlarında kalır |
| Hedef kitle | Eski dört grup; tıbbi biyoloji/laboratuvar alt küme | Onaylı birincil ve ikincil hedef kitle; tıbbi genetik hekimleri ile tıbbi biyoloji/moleküler tanı ekipleri açıkça yazıldı | Kullanıcı kararı ve `CLAUDE.md` proje kimliğiyle eşleştirildi |
| Nesne listeleri | Her satır bölüm başına gidiyordu | Şekil/algoritma/tablonun kendi başlığına doğrudan bağlantı | Her nesne için kararlı ve doğrulanabilir HTML kimliği üretildi |
| Sayfa numarası | Akışkan HTML'de yok | HTML'de bölüm bilgisi; sayfalandırılmış PDF için hedef sayfa sayacı altyapısı | Sayfa numarası ancak sabit sayfalama sonrasında anlamlıdır |

## 3. Değişmeden korunan temel tercihler

`işlev kaybı`, `işlev kazanımı`, `yapısal varyant`, `kopya sayısı varyantı`, `tek nükleotid varyantı`, `uniparental dizomi`, `homozigotluk bölgesi`, `Fenilketonüri`, `Spinal musküler atrofi`, `Frajil X sendromu`, `Huntington hastalığı`, `Friedreich ataksisi`, `Prader–Willi sendromu`, `Angelman sendromu`, `MELAS`, `MEN2`, `Fokal kortikal displazi` ve `Tanatoforik displazi` karşılıkları Türkçe kurumsal/akademik kullanımla uyumlu bulundu; yalnız tablo biçimi ve satır başı büyük harfi standardize edildi.

`haploinsufficiency`, `triplosensitivity`, `splicing`, `hotspot` ve `nonsense` için tek bir bağlayıcı Türkçe karşılık bulunmadığından kitabın önceden onaylanmış terminoloji politikası korundu: teknik terim ilk kullanımda açıklanır, sonra tek biçimde sürdürülür.

## 4. Kaynaklar

### Uluslararası ve normatif

- **[U1]** HGVS Nomenclature, *General Recommendations*, sürüm 21.1.4 (11.05.2026): https://hgvs-nomenclature.org/21.1.4/recommendations/general/
- **[U2]** HGVS Nomenclature, *Reference Sequences*, sürüm 21.1.4: https://hgvs-nomenclature.org/stable/background/refseq/
- **[U3]** HGVS Nomenclature, *DNA Alleles*: https://hgvs-nomenclature.org/stable/recommendations/DNA/alleles/
- **[U4]** HGVS Nomenclature, *Protein Frameshift*: https://hgvs-nomenclature.org/stable/recommendations/protein/frameshift/
- **[U5]** HUGO Gene Nomenclature Committee, *Frequently Asked Questions*: https://www.genenames.org/help/faq/
- **[U6]** NCBI Gene, *SCN2A sodium voltage-gated channel alpha subunit 2*: https://www.ncbi.nlm.nih.gov/gene/6326
- **[U7]** IUPHAR/BPS Guide to Pharmacology, *NaV1.2*: https://www.guidetopharmacology.org/GRAC/ObjectDisplayForward?familyId=82&objectId=579
- **[U8]** NCBI Genetic Testing Registry, *Camptodactyly–tall stature–scoliosis–hearing loss syndrome*: https://www.ncbi.nlm.nih.gov/gtr/conditions/C1864852/
- **[U9]** NCBI GeneReviews, *WAGR Spectrum Disorder*: https://www.ncbi.nlm.nih.gov/books/NBK621298/

### Türkçe kullanım doğrulaması

- **[T1]** Tıbbi Genetik Derneği, *Yeni Nesil Dizi Analizinde Algoritmalar Çalışma Grubu*: https://www.tibbigenetik.org.tr/upload/2018581083.pdf
- **[T2]** Çitli ve ark., “VUS = Önemi Belirsiz Varyant”, *Eskişehir Medical Journal* (2023): https://dergipark.org.tr/tr/pub/eskisehirmedj/issue/76478/1232725
- **[T3]** Canbek ve ark., “Klinik Önemi Belirsiz varyant”, *Osmangazi Tıp Dergisi* (2024): https://dergipark.org.tr/tr/download/issue-full-file/86310
- **[T4]** Bayrak ve ark., “Herediter Basınca Duyarlı Nöropati”, *Türk Nöroloji Dergisi* (2010): https://tjn.org.tr/abstract/870/tur
- **[T5]** Dokuz Eylül Üniversitesi, “Osteogenezis imperfekta” uzmanlık tezi kaydı: https://avesis.deu.edu.tr/tezler/58ab62af-c0ab-4200-bd2f-2fe2639552d4/cocuk-genetik-hastaliklari-poliklinigimize-2000-2015-yillarinda-basvuran-osteogenezis-imperfektali-hastalarin-retrospektif-degerlendirilmesi-ve-genetik-danismanlik-verilmesi
- **[T6]** Köken ve ark., “Duchenne ve Becker Musküler Distrofi”, *Güncel Pediatri* (2021): https://dergipark.org.tr/tr/pub/pediatri/article/912014
- **[T7]** Ankara Etlik Şehir Hastanesi, “Charcot–Marie–Tooth”: https://etliksehir.saglik.gov.tr/TR-1535211/klinik-hakkinda.html
- **[T8]** T.C. Sağlık Bakanlığı Halk Sağlığı Genel Müdürlüğü, *Kistik Fibrozis Yenidoğan Tarama Testi ile Tanı Alan Hastaları İzleme Rehberi*: https://hsgm.saglik.gov.tr/depo/birimler/cocuk-ergen-sagligi-db/Dokumanlar/Kitaplar/KF_Rehberi.pdf
- **[T9]** Öztürk ve ark., MLPA Türkçe kullanımı, *Osmangazi Tıp Dergisi* (2024): https://dergipark.org.tr/tr/pub/otd/article/1317452
- **[T10]** “Clinical and Molecular Spectrum of PIK3CA-Related Overgrowth Syndrome: A Turkish Cohort”, düşük VAF ve PROS Türkçe kullanımı, *Dicle Tıp Dergisi* (2026): https://dergipark.org.tr/tr/pub/dicletip/article/1906487
- **[T11]** *Klinik Biyokimyada Moleküler Tanı: Sıvı Biyopsi*, dijital damlacık PCR kullanımı, *Kocatepe Tıp Dergisi* (2025): https://dergipark.org.tr/tr/pub/kocatepetip/article/1628346
- **[T12]** Koçak ve Ceylaner, “WAGR Sendromu”, *Fırat Tıp Dergisi* (2009): https://dergipark.org.tr/tr/pub/firattip/issue/6356/84823

Tüm çevrim içi kaynaklara erişim tarihi **02.08.2026**'dır. Bu kayıt, Türkçe terim kullanımını belgeleme ve editöryal kararın izini koruma amacındadır; bağımsız Türkçe bilimsel editör incelemesinin yerine geçmez.
