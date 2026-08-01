# Bölüm 16 — Mekanizmadan Varyant Yorumuna: ACMG/ClinGen Sentezi

> **Bölümün çekirdek tezi:** Bu kitabın on dört bölümü boyunca mekanizmaları tek tek öğrendik. Bu bölüm, o bilginin **nereye aktığını** gösterir: klinik laboratuvarda bir varyantın sınıflandırılmasına. ACMG/AMP çerçevesi çoğu zaman bir **kontrol listesi** gibi öğretilir — kriterleri işaretle, kuralı uygula, sınıfı oku. Bu okuma yanlıştır ve bölümün birinci tezi budur: çerçeve bir kontrol listesi değil, bir **kanıt tartma dilidir**; kriterlerin ağırlıkları vardır, ağırlıklar toplanabilir ve toplam ağırlık bir **olasılık** ifade eder. İkinci ve kitabın tamamını bu bölüme bağlayan tez ise şudur: **hangi kriteri hangi güçte kullanabileceğinizi belirleyen şey mekanizmadır.** PVS1'i uygulayabilmek için işlev kaybının o hastalığın mekanizması olduğunu bilmeniz; PM1'i kullanabilmek için hotspot'un hangi mekanizmaya ait olduğunu bilmeniz; PS3'ü kullanabilmek için testin hangi mekanizmayı ölçtüğünü bilmeniz gerekir. Mekanizma bilgisi olmadan yapılan varyant yorumu, doğru kelimeleri yanlış anlamda kullanan bir cümledir. Üçüncü tez pratiktir: **VUS bir sonuç değil, bir eksik-kanıt durumudur** — ve hangi verinin hangi kriteri açtığını bilmek, o durumu çözmenin yoludur.

> **Bu bölüm nasıl okunmalı?** Bu bölüm kitabın **yorumlama sentezidir** ve önceki bölümlere sürekli geri gönderme yapar. Tıp öğrencileri için 1. başlık ile Şekil 16.1 çekirdektir: sınıflandırmanın bir olasılık ifadesi olduğunu kavramak, geri kalanını taşır. Klinisyenler için 4. ve 8. başlıklar ile Şekil 16.4 doğrudan kullanılabilir — özellikle "raporda yazan sınıf ne anlama geliyor?" ve "VUS geldiyse ne yapmalıyım?" soruları. Varyant yorumlayan laboratuvar uzmanları için 2. ve 6. başlıklar ile Şekil 16.3–16.3 bölümün ağırlık merkezidir. 7. başlıktaki beş çözümlü örnek, bütün bölümü tek tek olgular üzerinde tekrar eder; zamanı kısıtlı okuyucu doğrudan oraya gidebilir.

> 🖼️ **Görseller hakkında not:** Şekil 16.1–16.4 `assets/` klasöründe SVG olarak bulunur. Mermaid diyagramları metin içine gömülüdür.

---

## Öğrenme hedefleri

Bu bölümü tamamlayan okuyucu:
1. ACMG/AMP'nin beş sınıflı terminolojisini ve kanıt kategorilerini (popülasyon, hesaplamalı, fonksiyonel, segregasyon, de novo, alelik) tanımlar.
2. Kriter güç düzeylerinin (destekleyici / orta / güçlü / çok güçlü) olasılık oranı ve puan karşılıklarını açıklar ve sınıflandırmanın neden bir olasılık ifadesi olduğunu gerekçelendirir.
3. Mekanizma bilgisinin hangi kriteri açtığını, hangisini zayıflattığını ve hangisini geçersiz kıldığını mekanizma–kriter matrisi üzerinden yorumlar.
4. PVS1'in mekanizma ön koşulunu ve güç düşürme basamaklarını açıklar; verilen bir null varyantta doğru basamağı seçer.
5. Popülasyon frekansı kriterlerinin (PM2/BS1/BA1) neden hastalığa özgü hesaplanması gerektiğini açıklar.
6. Hesaplamalı öngörü kriterlerinin (PP3/BP4) kalibrasyon temelli kullanımını açıklar ve "birden çok araç aynı yönde" yaklaşımının neden yetersiz olduğunu belirtir.
7. Fonksiyonel kanıtın (PS3/BS3) hangi koşullarda ve hangi güçte kullanılabileceğini açıklar; çoklu-varyant (MAVE) verilerinin katkısını yorumlar.
8. Bir VUS karşısında hangi ek verinin hangi kriteri açacağını planlar ve yeniden değerlendirme stratejisi kurar.
9. Gen-özgü/hastalık-özgü uzmanlaştırılmış çerçevelerin (CNV, mtDNA, splice, kodlamayan) neden gerekli olduğunu açıklar.
10. Sınıflandırma sonucunu klinik dile çevirir: raporlama, danışma ve izlem sonuçlarını doğru ifade eder.

---

## 1. Kavramsal tanım

Klinik laboratuvarın ürettiği cümle kısadır: "Bu varyant patojeniktir." Bu cümlenin arkasında ise bir uzlaşı, bir yöntem ve — çoğu okuyucunun fark etmediği — bir **olasılık** vardır.

Bugün kullanılan ortak dil, ACMG ve AMP'nin 2015'te yayımladığı ve College of American Pathologists'in de katkı verdiği uzlaşı belgesiyle kurulmuştur. Belge, Mendel hastalıklarına neden olan genlerde saptanan varyantları tanımlamak için beş standart terim önerir — **patojenik**, **olası patojenik**, **belirsiz önemde (VUS)**, **olası benign**, **benign** — ve varyantları bu beş kategoriye yerleştirmek için tipik kanıt türlerini (popülasyon verisi, hesaplamalı veri, fonksiyonel veri, segregasyon verisi) kullanan bir ölçütler süreci tanımlar (Richards ve ark., 2015). Kritik ayrıntı şudur: kriterler eşit değildir. Her kriterin bir **güç düzeyi** vardır ve sınıf, işaretlenen kriter *sayısından* değil, birikmiş *ağırlıktan* doğar.

Bu ağırlıkların ne anlama geldiği, çerçevenin yayımlanmasından üç yıl sonra matematiksel olarak açıklığa kavuşturuldu. Tavtigian ve arkadaşları, ACMG/AMP ölçütlerini dört kanıt düzeyi ve üstel olarak ölçeklenen patojenite olasılık oranları varsayan **naif Bayes sınıflandırıcısına** çevirdiler ve çerçevenin iç tutarlılığını sınadılar. Sonuç, çerçeveyi büyük ölçüde doğruladı: var olan 18 kanıt kombinasyonundan yalnızca ikisi genel çerçeveyle matematiksel olarak tutarsızdı. Aynı çalışma, karşıt yönlü kanıtların (hem patojenite hem benignlik lehine) bir arada bulunduğu kombinasyonları da modelledi ve bunların olası patojenik, olası benign veya VUS sonucu verebileceğini gösterdi (Tavtigian ve ark., 2018). Yani sınıflandırma, niteliksel bir sezgi değil, **niceliksel bir tartıdır**.

İki yıl sonra aynı grup, bu Bayes formülasyonunun günlük kullanıma uygun bir kısayolunu önerdi: kanıt güç kategorileri **toplanabilir puanlara** soyutlanabilir. Puanlar log(odds) ile orantılıdır ve toplandıklarında Bayes formülasyonunu yeniden üretirler. Sistemin gücü sadeliği ve puan değerleri ile patojenite olasılık oranı arasındaki bağın, her veri türü için kanıt gücünün **ampirik olarak kalibre edilmesine** izin vermesidir; zayıflığı ise dar bir öncül olasılık aralığını sabitlemesi ve Bayes doğasının kullanıcıya görünmez kalmasıdır (Tavtigian ve ark., 2020).

Şekil 16.1 bu mimariyi tek sayfada toplar.

![Şekil 16.1 — ACMG/AMP kanıt mimarisi: kriterler sayılmaz, tartılır](assets/sekil_54_acmg_kanit_mimarisi.svg)

Bu tablodan çıkan üç kavramsal sonuç, bölümün geri kalanını taşır.

**Birincisi, VUS bir "ara tanı" değildir.** VUS, varyantın "biraz patojen" olduğunu söylemez; kanıtın henüz herhangi bir yöne karar verdirecek ağırlığa ulaşmadığını söyler. Bu nedenle VUS klinik karar için kullanılamaz — ama aynı nedenle **çözülebilir** bir durumdur: eksik olan şey varyantın doğası değil, veridir.

**İkincisi, tek bir kriter yetmez — ve bunun sayısal karşılığı sanıldığından katıdır.** Bayes türevi puan sisteminde kanıt ağırlıkları şöyledir: **Çok güçlü = 8, Güçlü = 4, Orta = 2, Destekleyici = 1** (benignlik için sırasıyla −4, −2, −1). Sınıf sınırları ise:

| Toplam puan | Sınıf |
|---:|---|
| **≥10** | Patojenik |
| 6–9 | Olası patojenik |
| 0–5 | VUS |
| −1 ila −5 | Olası benign |
| ≤−6 | Benign |

Buradan çıkan sonuç öğreticidir. **Çok güçlü** düzeyde uygulanan PVS1 **8 puandır** ve patojenik için gereken 10'a **ulaşmaz** — saf puan hesabında *olası patojenik* aralığında kalır. Sık yapılan hata, "yanına bir destekleyici kanıt eklenirse patojenik olur" varsayımıdır: bir destekleyici kriter yalnızca **+1** getirir, toplam **9** olur ve sınıf **hâlâ olası patojeniktir**. Patojenik sınıfa geçmek için **en az +2 puan** gerekir; bu da bir **orta** düzey kriterle ya da **iki bağımsız destekleyici** kriterle sağlanır.

Bazı ulusal uygulama kılavuzları buna bir güvenlik kuralı daha ekler: BA1 istisnası dışında bir varyantı (olası) patojenik ya da (olası) benign sınıflamak için **en az iki bağımsız kanıt kriteri** aranır; dolayısıyla elinde yalnızca PVS1_ÇokGüçlü (8 puan) bulunan bir varyant, ikinci bir doğrulayıcı kanıt gelene kadar **VUS olarak tutulur** (ACGS, 2024).

Son bir uyarı: **PVS1 her zaman 8 puan değildir.** ClinGen'in PVS1 karar ağacı, varyantın konumuna ve öngörülen sonucuna göre kriteri kademeli olarak düşürür — PVS1_Güçlü (4), PVS1_Orta (2), PVS1_Destekleyici (1). NMD'den kaçan, klinik olarak ilgisiz bir izoformu etkileyen ya da proteinin yalnızca küçük bir bölümünü kaybettiren varyantlarda tam güç uygulanamaz (Abou Tayoun ve ark., 2018; §3). Kriterin **adı** aynı kalırken **ağırlığı** değişir — ve sınıfı belirleyen ağırlıktır.

**Üçüncüsü ve bu bölümün asıl konusu: her kriterin uygulanabilirliği ve gücü, mekanizmaya bağlıdır.** Kriterin adı sabittir; anlamı değildir.

Son bir kavramsal ön koşul: varyant sınıflandırması, **gen–hastalık ilişkisinin geçerli olduğu varsayımı üzerine** kurulur. Bölüm 15'te gördüğümüz gibi ClinGen bu ilişkiyi ayrı bir çerçeveyle puanlar ve "Kesin"den "Çelişkili"ye uzanan bir ölçekte sınıflar (Strande ve ark., 2017); değerlendirilecek hastalık varlığının tanımlanması ise ön-küreleme aşamasında yapılır (Thaxton ve ark., 2022). İlişkinin kendisi zayıfsa, o gendeki hiçbir varyant güvenle patojenik ilan edilemez — kanıtın temeli çürüktür (MacArthur ve ark., 2014).

**Tablo 16.1 — Varyant yorumlamanın temel kavramları**

| Kavram | Tanım | Pratik karşılığı |
|---|---|---|
| Beş sınıf | Patojenik · Olası patojenik · VUS · Olası benign · Benign | Rapor dili; klinik eylem yalnız ilk iki ve son iki sınıfa dayanır |
| Kanıt gücü | Destekleyici / Orta / Güçlü / Çok güçlü | Her düzey bir olasılık oranına karşılık gelir |
| Puan sistemi | Kanıt gücünün toplanabilir sayıya çevrilmesi | Sınıf sınırları puan eşikleriyle tanımlanır |
| Öncül olasılık | Değerlendirme öncesi patojenite beklentisi | Bayes formülasyonunun girdisi |
| **VUS** | Kanıtın karar verdirecek ağırlığa ulaşmaması | Bir sonuç değil, **eksik veri durumu** |
| Gen–hastalık geçerliliği | Genin belirli bir hastalıkla ilişkisinin kanıt gücü | Sınıflandırmanın ön koşulu |
| Uzmanlaştırma (spesifikasyon) | Kriterlerin gen/hastalık grubuna göre yeniden tanımlanması | CNV, mtDNA, splice, kodlamayan için ayrı kurallar |

---

## 2. Moleküler mekanizma: kanıt türleri ve mekanizmayla bağları

Bu bölümde "mekanizma" iki anlamda kullanılır: kitabın öğrettiği **biyolojik mekanizmalar** ve çerçevenin kendi **kanıt mekaniği**. İkisi arasındaki köprüyü kurmak, bu başlığın işidir.

### 2.1 Popülasyon kanıtı: "nadir" hastalığa göre tanımlanır

Popülasyon frekansı, varyant yorumlamanın en güçlü ve en çok suistimal edilen kanıtıdır. Sezgi basittir: hastalık nadirse, varyant da nadir olmalıdır. Ancak "nadir"in eşiği çoğu zaman keyfî seçilir — ve fazlasıyla gevşek seçilir.

Whiffin ve arkadaşları buna niceliksel bir çözüm getirdiler: aday hastalık nedeni varyantların frekansa göre filtrelenmesi için, **hastalık prevalansını, genetik ve alelik heterojeniteyi, kalıtım modunu, penetransı ve referans veri kümesindeki örnekleme varyansını** hesaba katan istatistiksel bir çerçeve. Kardiyomiyopati örneğinde bu yaklaşım, ortalama bir ekzomda değerlendirilmesi gereken aday varyant sayısını **üçte iki oranında azaltmış**, bunu gerçek patojenik varyantları eleme pahasına yapmamıştır (yanlış pozitif oranı 0,001'in altında) (Whiffin ve ark., 2017).

Bu, bu kitabın mekanizma bölümleriyle doğrudan bağlanır. Penetrans eksikse (Bölüm 1, 14) izin verilen frekans yükselir; hastalık resesifse alel frekansı eşiği baskın kalıtıma göre farklıdır; alelik heterojenite yüksekse (ör. *CFTR*) tek bir varyantın taşıyabileceği pay küçülür. Aynı gnomAD frekansı, bir hastalık için "çok sık — BS1", başka bir hastalık için "beklenen düzeyde — PM2" olabilir.

> **🟦 Klinikte dikkat — Bir varyantın "gnomAD'de yok" olması ne kadar kanıttır?** Popülasyon veri tabanlarında yokluk ya da hastalık için beklenenden düşük frekans **PM2'yi destekleyebilir**, ama tek başına patojeniteyi göstermez. Kriterin gücü konusunda iki katmanlı düşünmek gerekir: **ClinGen SVI'nin genel çerçevesinde PM2, orta değil destekleyici güçte (PM2_Supporting) uygulanır** — gerekçe, popülasyonda yokluğun 2015 çerçevesinde olduğundan fazla ağırlıklandırılmış olması ve tek başına orta düzey kanıtın öngörülen olasılık oranını karşılamamasıdır. Buna karşılık ilgili gen–hastalık ilişkisi için **onaylanmış bir VCEP spesifikasyonu varsa, frekans eşiğini ve kriter gücünü o spesifikasyon belirler.** VCEP'ler üç şeyi birden değiştirebilir: kanıt gücünü (destekleyici / orta / uygulanamaz), frekans eşiğini ("tümüyle yok" yerine hastalığa özgü çok düşük bir PopMax/FAF değeri) ve teknik koşulları (kalıtım biçimi, penetrans, prevalans, kurucu varyantlar, değerlendirilecek popülasyon alt grubu). Yani **PM2_Supporting bir varsayılandır, evrensel bir sabit değil**; güncel ve onaylı bir VCEP kuralı varsa o uygulanır.
>
> **"gnomAD'de yok" ifadesi de otomatik olarak PM2 anlamına gelmez.** Kriteri uygulamadan önce şunlar doğrulanmalıdır: o pozisyonda **yeterli kapsama ve çağrılabilirlik** var mı; ilgili **varyant tipi** kullanılan veri kümesinde güvenilir biçimde saptanabiliyor mu; hastalıkla ilişkili **atasal popülasyonlar** yeterince temsil edilmiş mi; kullanılan **sürüm ve genom yapısı** hangisi; ve varyant gerçekten yok mu, yoksa **filtrelenmiş ya da düşük kaliteli** mi? Her insan genomunda çok sayıda özel veya son derece nadir ama zararsız varyant bulunduğundan, yalnız yokluk **zayıf bir pozitif kanıttır**.
>
> **Kısıt ölçütlerinin yeri de dikkatle tanımlanmalıdır.** **pLI** ExAC veri kümesiyle tanımlanmış (Lek ve ark., 2016), **LOEUF** ise gnomAD ile getirilmiştir (Karczewski ve ark., 2020). Bu ölçütler bilgiyi **bağlamlandırır**, ancak *bağımsız bir ACMG kanıtı ya da PM2'nin güç yükselticisi değildir*. Yüksek LoF intoleransı, genin heterozigot protein-kesici varyantlara karşı seçilim altında olduğunu düşündürür — o kadar. Tek başına ne genin belirli bir hastalıkla ilişkili olduğunu, ne haploinsufficiency'nin o hastalığın mekanizması olduğunu, ne de eldeki varyantın gerçekten işlev kaybı yaptığını kanıtlar. Nadir bir kesici varyant ancak şu üçü sağlandığında güçlü patojenite kanıtına dönüşür: **gen–hastalık ilişkisinin geçerliliği**, o ilişkide **LoF'un hastalık mekanizması** olduğunun gösterilmesi ve **transkript/NMD değerlendirmesinin PVS1 ile uyumlu** olması (§3).

### 2.2 Hesaplamalı kanıt: "araçlar hemfikir" yeterli değildir

*In silico* öngörü araçları, varyant yorumlamanın en kolay ulaşılan ve en yanlış kullanılan kanıtıdır. 2015 çerçevesi bu araçları PP3/BP4 ile **destekleyici** düzeyde ve genellikle birden çok aracın uyuşması koşuluyla kullanır. Pejaver ve arkadaşları, bu yaklaşımın niceliksel dayanağı olmadığını gösterdiler: hem araç geliştiricilerinin tanımladığı skor aralıkları hem de "birden çok öngörücünün uzlaşması" gerekliliği niceliksel destekten yoksundu.

Bunun yerine, ACMG/AMP önerileri içindeki kanıt güçlerini niceliklendiren olasılıksal çerçeveyi hesaplamalı öngörücülere genişlettiler ve bir aracın skorlarını PP3/BP4 kanıt güçlerine çeviren yeni bir standart tanımladılar. Yaklaşım, **yerel pozitif öngörü değerinin** kestirimine dayanır ve herhangi bir hesaplamalı aracı (ya da başka herhangi bir sürekli ölçekli kanıtı) her varyant tipi için kalibre edebilir. On üç missense yorumlama aracı için, patojenite ve benignlik lehine her kanıt gücüne karşılık gelen skor eşikleri kestirildi. Sonuçlar öğreticidir: araçların çoğu yeni eşiklerle hem patojenik hem benign sınıflandırma için **destekleyici** düzeye ulaştı; birden fazla araç **orta**, birkaçı **güçlü** düzeye erişti; bir araç bazı varyantlarda benign sınıflandırma için **çok güçlü** düzeye ulaştı (Pejaver ve ark., 2022).

Pratik sonuç iki cümledir. **Bir:** üç aracın aynı yönü göstermesi kanıtın gücünü artırmaz — araçlar birbirinden bağımsız değildir. **İki:** kalibre edilmiş tek bir aracı, tanımlanmış eşik aralığıyla kullanmak, kalibre edilmemiş beş aracı oylamaktan üstündür.

> **🔬 Deep-dive — Hesaplamalı araçlar mekanizmayı bilmez.** Bu, kitabın 4., 5. ve 6. bölümleriyle doğrudan bağlanan kritik bir sınırlılıktır. Missense öngörü araçları, temelde "bu amino asit değişimi tolere edilebilir mi?" sorusunu yanıtlar; bu soru işlev **kaybı** için anlamlıdır. Oysa dominant-negatif, işlev kazanımı ve neomorfik varyantlar için doğru soru "protein bozuluyor mu?" değil, "protein **ne yapıyor**?"dur. Nitekim bu mekanizmaları ayırt etmeye yönelik analizler, mevcut patojenite tahmin araçlarının dominant-negatif ve işlev kazanımı varyantlarını tanımakta belirgin biçimde zayıf kaldığını göstermiştir (Gerasimavicius ve ark., 2022). Bunun yorumlamadaki karşılığı nettir: bir GoF hastalığında düşük bir öngörü skoru, varyantı temize çıkarmaz; benzer biçimde yüksek bir skor da varyantın **hangi yönde** iş gördüğünü söylemez. Splicing tarafında ise durum daha iyidir: derin öğrenme temelli splice öngörüsü, sessiz ve derin intronik varyantların kriptik splice etkilerini yakalayabilmekte ve kalibre edilmiş eşiklerle daha güçlü kanıt üretebilmektedir (Jaganathan ve ark., 2019).

### 2.3 Fonksiyonel kanıt: hangi testin, hangi mekanizmayı ölçtüğü

PS3/BS3, mekanizmayla en doğrudan bağlantılı kriterdir — ve bu yüzden bu kitabın odağıdır. ClinGen'in fonksiyonel kanıt çerçevesi, bir analizin klinik yorumlamada kullanılabilmesi için önce **hastalık mekanizmasının tanımlanmış** olmasını, analizin bu mekanizmayı ölçtüğünün gösterilmesini, bilinen patojenik ve benign varyant kontrolleriyle **doğrulanmış** olmasını ve son olarak kanıt gücünün OddsPath benzeri bir ölçüyle **hesaplanmasını** ister (Brnich ve ark., 2019). Yani PS3 otomatik olarak "güçlü" değildir; gücü, analizin performansından türetilir.

Son yıllarda bu alan niteliksel bir sıçrama yaptı: **çoklu-varyant (multiplexed) fonksiyonel analizler**, binlerce varyantın işlevsel etkisini aynı anda ölçebiliyor. Gelman ve arkadaşları, mevcut ACMG/AMP ve ClinGen standartlarının fonksiyonel verinin rolünü tanımladığını ancak çoklu-varyant analizlerinin kendine özgü zorluk ve avantajlarını ele almadığını belirterek, hem deneycilere (veri üretimi ve raporlama) hem klinisyenlere (veri kalitesinin değerlendirilmesi ve ACMG/AMP çerçevesine dâhil edilmesi) yönelik öneriler geliştirdiler (Gelman ve ark., 2019).

Bu yaklaşımın pediatrik genetikteki somut karşılığı çarpıcıdır. Lo ve arkadaşları, X'e bağlı üre döngüsü bozukluğu olan OTC eksikliği için yüksek verimli bir fonksiyonel analiz geliştirip **1.570 varyantın** — tek nükleotid değişimiyle ulaşılabilir missense mutasyonların %84'ü — etkisini tek tek ölçtüler. Analiz yalnızca bilinen benign ve patojenik varyantları ayırt etmekle kalmadı; **neonatal başlangıçlı** olguların varyantlarını **geç başlangıçlı** olgularınkinden de ayırdı ve klinik olarak anlamlı işlev kaybı düzeylerine karşılık gelen skor aralıklarının tanımlanmasına izin verdi. Verinin mevcut ACMG kılavuzları altında PS3 kanıtı olarak dâhil edilmesiyle yapılan pilot yeniden sınıflandırmada, işlevi tümüyle kaybettiren 34 varyanttan **22'si belirsiz önemden olası patojenik sınıfına** geçti (Lo ve ark., 2023).

Bu tek çalışma, bölümün üç tezini birden örnekler: kanıt tartılır (skor aralıkları güç belirler), mekanizma bilgisi kriteri açar (analiz OTC enzim işlevini ölçer, yani LoF mekanizmasına uygundur) ve VUS çözülebilir bir durumdur.

### 2.4 Aile kanıtı: segregasyon, de novo ve faz

Aile verisi, laboratuvarın kendi başına üretemeyeceği ama klinisyenin sağlayabileceği kanıttır — bu yüzden klinik-laboratuvar iş birliğinin en verimli noktasıdır.

**Segregasyon (PP1/BS4)** niceliksel bir kanıttır, ancak 2015 çerçevesi bunu nicel olarak tanımlamamıştı. Dokuz laboratuvarın çerçeveyi birlikte uyguladığı bir değerlendirmede, tutarlı kullanımın önündeki engellerden birinin tam olarak bu tanım eksikliği olduğu belirlendi; buradan hareketle kolay uygulanabilir nicel ölçütler önerildi (Jarvik ve Browning, 2016). Pratikte anlamı şudur: "ailede birlikte gidiyor" ifadesi tek başına bir kanıt değildir; kaç bilgilendirici menzilde gittiği sayılmalı ve kanıt gücü buna göre belirlenmelidir.

**De novo kanıtı (PS2/PM6)**, ebeveynlik doğrulanmışsa güçlü, doğrulanmamışsa orta düzeydedir. Ancak Bölüm 12'nin uyarısı burada devreye girer: "de novo" görünen bir varyant, ebeveynlerden birinde **düşük düzeyde mozaik** olabilir; bu hem kanıtın gücünü hem — daha önemlisi — aileye verilecek tekrarlanma riskini değiştirir (Campbell ve ark., 2014).

**Faz bilgisi (PM3)** resesif hastalıklarda belirleyicidir: iki varyantın *in trans* olduğunun gösterilmesi kanıt üretir, *in cis* olduğunun gösterilmesi ise tersine kanıttır. Ebeveyn örneği yoksa uzun-okuma dizileme bu bilgiyi verebilir.

### 2.5 Mekanizmaya özgü kriter: PVS1

PVS1, çerçevenin tek "çok güçlü" patojenik kriteridir ve adı yanıltıcıdır: "çok güçlü" olan kriterin *kendisi* değil, koşulları sağlandığında taşıdığı ağırlıktır. 2015 kılavuzu bu kriteri tanımlarken farklı işlev kaybı varyant tiplerine özgü değerlendirmeleri ayrıntılandırmamış; varyantın tipi, konumu ve gerçek bir null etki olasılığına ilişkin ek kanıtı birleştiren karar yolları sunmamıştı. ClinGen'in Sekans Varyant Yorumlama çalışma grubu bu boşluğu doldurmak üzere ayrıntılı öneriler geliştirdi; yedi hastalık-özgü grubun 56 heterojen işlev kaybı varyantı üzerinde yaptığı değerlendirmede yeni önerilerle **%89 uyum** sağlandı ve uyumsuz kalan altı varyanttaki (%11) farklılıklar, hastalığa özgü uyarlamalardan kaynaklandı (Abou Tayoun ve ark., 2018).

Şekil 16.2, bu akışın iki katmanını gösterir: önce **mekanizma kapısı**, sonra **güç basamakları**.

![Şekil 16.2 — PVS1: önce mekanizma kapısı, sonra güç basamakları](assets/sekil_56_pvs1_mekanizma_kapisi.svg)

Kapı sorusu bölümün özetidir: *işlev kaybı, değerlendirilen gen–hastalık ilişkisinin bilinen mekanizması mı?* Bölüm 15'te gördüğümüz gibi bu soru gen düzeyinde değil, **gen–hastalık üçlüsü** düzeyinde sorulur: *RET*'te bir null varyant Hirschsprung hastalığı için mekanizmaya uygundur, MEN2 için değildir. Kapı kapalıysa basamaklara hiç bakılmaz.

Kapı açıksa varyantın gen içindeki konumu gücü belirler. NMD'ye giren erken sonlanma kodonları ve tüm gen delesyonları tam güçle değerlendirilirken (Bölüm 2), NMD'den kaçan kesilmeler, son ekzondaki küçük kayıplar, alternatif başlangıç kodonuyla kısmen kurtarılabilen varyantlar ve klinik olarak ilgisiz izoformları etkileyen değişimler için güç kademeli olarak düşürülür. Splice bölgesi varyantları ise doğrudan "null" sayılmaz: önce öngörülen transkript sonucu (ekzon atlanması, intron tutulumu, kriptik bölge kullanımı), sonra bunun okuma çerçevesine ve NMD'ye etkisi belirlenir; PVS1'in gücü buna göre ayarlanır ve RNA verisi mevcutsa hem bu basamak netleşir hem PS3 devreye girebilir (Walker ve ark., 2023).

### 2.6 Bütün kitabı tek tabloda toplamak

Şekil 16.3, bu bölümün sentez haritasıdır: kitabın on dört mekanizma bölümünde ele alınan biyolojik mekanizmaların, sekiz geniş kanıt ailesiyle hangi noktalarda ve hangi koşullarda kesişebildiğini tek matriste gösterir. **Bu matris bir ACMG/AMP uygulama algoritması ya da resmî bir ClinGen eşleştirmesi değildir**; yorumlama sırasında hangi kanıt alanlarının sorgulanmaya değer olduğunu gösteren pedagojik bir yönlendirme aracıdır. Matrisin **iki ekseni de editöryaldir**: soldaki on dört satır bu kitabın mekanizma bölümlendirmesidir, üstteki sekiz sütun ise ACMG/AMP kriter kodlarını öğretim kolaylığı için daha geniş kanıt aileleri altında toplayan bir gruplamadır — ClinGen'in kendi rehberleri bu kriterleri (PVS1, PS2/PM6, PS3/BS3, PM2, PM3, PP1/BS4, PP4, PP3/BP4 ve splice kanıtı) ayrı metodolojik sorunlar olarak ele alır.

![Şekil 16.3 — Mekanizma → kriter matrisi: kitabın on dört bölümü tek tabloda](assets/sekil_55_mekanizma_kriter_matrisi.svg)

Matrisin okunma biçimi şudur. **İşlev kaybı ve yetersiz doz** satırı, çerçevenin varsayılan hâlidir — kriterler tasarlandıkları gibi çalışır. **İşlev kazanımı, dominant-negatif ve neomorfik** satırlarında PVS1 kapısı kapalıdır; buna karşılık hotspot/arayüz kümelenmesi PM1'i güçlendirir ve mekanizmayı doğrudan ölçen fonksiyonel testler PS3'ü değerli kılar; hesaplamalı öngörünün gücü ise düşer. **Splicing** satırında hem PVS1 (uyarlanmış akışla) hem PS3 (RNA analizi) hem PP3 (kalibre splice öngörüsü) güçlenir — bu, kitapta kanıtın en zengin olduğu mekanizmadır. **CNV, mitokondriyal ve tekrar genişlemesi** satırlarında çerçevenin kendisi yetersizdir ve özel puanlama sistemleri devreye girer. **Mozaiklik** satırında segregasyon anlamını yitirir ve de novo kanıtı dikkatle kullanılmalıdır. **Kodlamayan** satırında kriterlerin çoğu ya uygulanamaz ya zayıflar; ağırlık fonksiyonel kanıta kayar. **Digenik** satırında tek-lokus segregasyon analizi yanıltıcıdır. **Alelik seri** satırında ise bütün konum-temelli kriterler "hangi hastalık için?" sorusuyla koşullanır.

> **⚠️ Matris nasıl okunmaz — üç yanlış anlama.** **(1) İşaret, kriterin kazanıldığı anlamına gelmez.** Bir hücredeki ● ya da ▲, o mekanizmada ilgili kanıt ailesinin sıklıkla sorgulandığını söyler; varyantın o kriteri karşıladığını değil. **(2) ✖ ya da boşluk, kriterin kesinlikle uygulanamayacağı anlamına gelmez.** "Genellikle uygulanmaz" ile "yasaktır" aynı şey değildir; Bölüm 13'te gördüğümüz gibi saf düzenleyici varyantta PVS1 yoktur ama mekanizması splicing olan intronik bir varyantta PVS1_Strength(RNA) vardır. **(3) Aynı hücre her gen için aynı gücü göstermez.** Kriterin uygulanabilirliği ve ağırlığı; gen–hastalık ilişkisine, kalıtım biçimi ve alelik gereksinime, varyant sınıfına, klinik olarak anlamlı transkripte, ölçülen işlevsel sonuca, deneyin validasyonuna ve — varsa — güncel VCEP spesifikasyonuna göre belirlenir. Çakışma hâlinde **VCEP spesifikasyonu bu matrisin önündedir.**
>
> **Örnek bir okuma.** Yetersiz doz satırında null etki, popülasyon sıklığı, de novo/segregasyon ve fenotip kanıtları "sıklıkla sorgulanır" olarak işaretlidir. Bu, o gende bulunan nonsens bir varyanta otomatik olarak PVS1 + PM2 + PS2 verileceği anlamına **gelmez**: önce ilgili gen–hastalık ilişkisinde işlev kaybının yerleşik mekanizma olup olmadığı, varyantın klinik olarak anlamlı transkripte etkisi, popülasyon verisinin o hastalık için uygunluğu ve de novo kanıtının kalitesi ayrı ayrı doğrulanır. Matris size **hangi soruları soracağınızı** verir, cevapları değil.

---

## 3. Varyant tipleri

Önceki bölümlerde "varyant tipi → mekanizma" yönünde ilerledik. Burada zinciri tamamlıyoruz: **varyant tipi → hangi kriterle başlanır.**

**Tablo 16.2 — Varyant tipine göre öncelikle değerlendirilecek kanıt alanları**

| Varyant tipi | Öncelikle değerlendirilecek kanıt alanları | Mekanizma kontrolü | En sık yanlış uygulama |
|---|---|---|---|
| Nonsens / çerçeve kayması (NMD'ye giren) | PVS1 (karar ağacıyla), PM2_Supporting, PP1/PS2 | LoF, bu hastalığın mekanizması mı? | Gen–hastalıkta LoF mekanizmasını, klinik olarak anlamlı transkripti ve NMD beklentisini değerlendirmeden PVS1 uygulamak — PVS1 yalnız varyant tipine bakılarak verilmez |
| Son ekzon / NMD kaçışı | PVS1 karar ağacı (güç varyanta göre belirlenir), PM2_Supporting | Kalan protein işlev görebilir mi? Mekanizma LoF mu, DN/GoF mu? | **İki yönlü hata:** tam güçle uygulayıp sınıfı şişirmek *veya* "son ekzon" diye otomatik bir düşürülmüş PVS1 vermek. Kesilen bölgenin kritikliği, aynı bölgede bilinen patojenik kesici varyantlar ve protein stabilitesi incelenmeden güç belirlenemez |
| Tam gen delesyonu | CNV puanlama çerçevesi, doz duyarlılığı kürasyonu | Doz duyarlılığı kanıtlanmış mı? | Dizi varyantı kriterlerini CNV'ye uygulamak; ya da aynı doz kaybını hem CNV puanında hem PVS1'de **iki kez saymak** |
| Missense — hotspot/arayüzde | PM1 (hastalık-spesifik), PS3 (validasyonu incelenmiş), PM2_Supporting, PP3 | GoF/DN mi, LoF mi? | Deneyin **ölçtüğü yönün** hastalık mekanizmasıyla uyumunu ve deneyin validasyonunu kontrol etmeden PS3 vermek — aktivite azalması, hastalık GoF ile oluşuyorsa PS3'ü desteklemez |
| Missense — dağınık konumda | PM2_Supporting, PP3 (kalibre tek araç), PS3 | Genin mekanizması ne? | Birden çok kalibre edilmemiş aracın **çoğunluk oyunu** kullanmak veya her aracı ayrı PP3 kanıtı gibi saymak |
| Kanonik splice (±1,2) | PVS1 splice karar ağacı; gözlenen LoF RNA sonucu **PVS1_Strength(RNA)** | Çerçeve korunuyor mu? NMD bekleniyor mu? | Kanonik konumu otomatik PVS1_VeryStrong saymak · **saf RNA-splicing sonucunu** PS3 ile kodlamak (RNA'dan bağımsız protein/hücresel işlev deneyleri yine PS3 olabilir) |
| Derin intronik / sessiz | PP3 (splice öngörüsü), gözlenen LoF RNA sonucu **PVS1_Strength(RNA)**; etki yoksa koşullu **BP7** | Kriptik bölge aktive oluyor mu? | "Sessiz = zararsız" saymak · saf RNA-splicing sonucunu PS3 ile kodlamak · **uygun olmayan dokudaki negatif RNA sonucunu otomatik BP7/BS3 saymak** |
| Kodlamayan / düzenleyici | PS3 (element–hedef gen bağlantısı kurulmuşsa), PM2_Supporting; PVS1 saf düzenleyici varyantta uygulanmaz, PM1 yalnız iyi tanımlanmış hastalık-spesifik motif/hotspotta **PM1_Supporting** düzeyinde düşünülebilir | Element ve hedef gen tanımlı mı? | Kodlayan kriterleri olduğu gibi taşımak · düzenleyici eleman–hedef gen bağlantısı gösterilmeden herhangi bir reporter sonucunu PS3 saymak |
| Tekrar genişlemesi | Ayrı çerçeve: alel boyu eşikleri, motif yapısı ve kesintiler, metilasyon, instabilite | Tekrar tipi, eşikler ve penetrans aralıkları biliniyor mu? | Kısa varyantlar için tasarlanmış ACMG/AMP kanıt kodlarını tekrar aleline **mekanik olarak** uygulamak; yalnız tekrar sayısına bakıp motif bütünlüğü, kesintiler, metilasyon ve somatik instabiliteyi atlamak |
| mtDNA varyantı | mtDNA'ya özgü ACMG/AMP spesifikasyonu | Heteroplazmi düzeyi ve doku? | Nükleer kriterleri değişiklik yapmadan kullanmak; heteroplazmi, doku dağılımı, maternal segregasyon, haplogrup ve mtDNA'ya özgü popülasyon verisini hesaba katmamak |
| Düşük VAF (mozaik) | **Önce** analitik doğrulama ve dokusal dağılım; ardından — de novo durumu gerçekten karşılanıyorsa — PS2/PM6 | Gerçek postzigotik mozaik mi, artefakt mı? Mozaik olan proband mı, ebeveyn mi? | Düşük VAF'yi tek başına mozaiklik/de novo kanıtı sayıp doğrudan PS2/PM6 uygulamak · kan VAF'ini mutant hücre oranı ya da aktarım riskiyle eşitlemek · segregasyonu klasik biçimde yorumlamak |

> **⚠️ Bu tablo bir ACMG/AMP uygulama algoritması değildir.** Sütunlardaki sıra bir işlem sırası değil, kontrol listesidir; kanıt kodları varyant tipine göre otomatik verilmez. Her kriter gen–hastalık ilişkisi, kalıtım biçimi, hastalık mekanizması, klinik olarak anlamlı transkript, deneyin validasyonu ve — varsa — güncel VCEP spesifikasyonu bağlamında uygulanır. Üç nokta özellikle vurgulanmalıdır: **PM2** genel varsayılan olarak *Supporting* düzeyinde kullanılır (§2'deki kutuya bkz.); **PS3** hiçbir varyant tipi için otomatik "ilk kriter" değildir — deney sınıfının uygunluğu ve validasyonu ayrıca incelenir (Brnich ve ark., 2019); **yalnız splicing sonucunu ölçen RNA deneyleri** PS3/BS3 yerine ClinGen SVI splicing çerçevesiyle değerlendirilir (Walker ve ark., 2023).

Tablonun ortak dersi şudur: **ilk adım kriter seçmek değil, mekanizmayı ve hastalık varlığını belirlemektir.** Kriter seçimi bunun sonucudur, öncülü değil. Son sütun da bunu doğrular: listelenen yanlış uygulamaların neredeyse tamamı, kriterin *kendisinden* değil, mekanizma/bağlam sorusu sorulmadan kriter uygulanmasından doğar.

---

## 4. Klinik fenotipe dönüşüm

### 4.1 Rapordaki sınıf klinikte ne anlama gelir?

Beş sınıfın klinik karşılığı, çoğu zaman sanıldığından daha nüanslıdır.

**Patojenik ve olası patojenik** sınıflar klinik eylem için kullanılabilir. Ancak "olası patojenik" mutlak bir kesinlik değildir: Bayes çerçevesinde bu sınıf yaklaşık %90–99 arası bir patojenite olasılığına karşılık gelir (Tavtigian ve ark., 2018). Yani her yüz "olası patojenik" varyanttan birkaçının zamanla yeniden sınıflandırılması beklenen bir olaydır, bir hata değil.

**VUS**, klinik karar için kullanılamaz. Bu, bir aileye söylenmesi gereken en zor ama en dürüst cümlelerden biridir: "Bir değişim bulduk, ancak bunun hastalığa neden olup olmadığını söyleyecek yeterli veri yok." VUS'a dayanarak izlem başlatmak, ameliyat kararı vermek ya da akrabalara test önermek yanlıştır.

**Olası benign ve benign** sınıflar, o varyantın nedensel olmadığını söyler; ancak tanının dışlandığını söylemez. Bölüm 8, 12 ve 13'te gördüğümüz kör noktalar (CNV, mozaiklik, kodlamayan varyantlar) hâlâ açıktır.

### 4.2 Yeniden sınıflandırma: raporun son sözü değildir

Varyant sınıfları zamanla değişir, çünkü kanıt birikir. Bu, klinik genomiğin en önemli ama en az konuşulan gerçeklerinden biridir. ClinGen'in tanıtım makalesi bunu bir vaka anlatısıyla açar: hipertrofik kardiyomiyopatili bir ailede "olası patojenik" bulunan bir varyanta göre aile üyeleri test edilir, negatif olanlara risk taşımadıkları söylenir; beş yıl sonra aynı varyantın, daha yeni popülasyon frekansı verilerine dayanan başka bir laboratuvar tarafından "olası benign" olarak yorumlandığı görülür ve yeni bir panelde ailede gerçek nedensel varyant bulunur — daha önce "negatif" denen bir aile üyesi bu kez pozitif çıkar ve incelemede kardiyomiyopati saptanarak koruyucu bir müdahale yapılır (Rehm ve ark., 2015).

Bu anlatının dersi, tek bir laboratuvarın hatası değil, sistemin doğasıdır: **varyant yorumu, veri paylaşımı ve periyodik yeniden değerlendirme olmadan güvenli değildir.**

### 4.3 VUS geldiğinde ne yapılır?

Bu, bu bölümün klinisyene en doğrudan katkısıdır. VUS bir çıkmaz değil, bir adres listesidir (Şekil 16.4).

![Şekil 16.4 — VUS'u çözme haritası: hangi ek veri hangi kriteri açar?](assets/sekil_57_vus_cozme_haritasi.svg)

**Algoritma 16.1 — VUS geldiğinde eksik kanıtı üretme akışı**

```mermaid
flowchart TD
  A["Sonuç: VUS"] --> B{"Fenotip bu gen–hastalık<br/>varlığıyla gerçekten uyumlu mu?"}
  B -->|"Hayır / zayıf"| C["Rastlantısal bulgu olabilir:<br/>ayırıcı tanıyı ve diğer kör noktaları<br/>(CNV · mozaiklik · kodlamayan) yeniden aç"]
  B -->|"Evet"| D["ADIM 1 — Aile örneği:<br/>de novo mu? faz nedir?<br/>(PS2/PM6 · PM3)"]

  D --> E{"Ek etkilenmiş akraba var mı?"}
  E -->|"Evet"| F["ADIM 2 — Segregasyon çalış:<br/>bilgilendirici menzil sayısına göre<br/>PP1'in gücünü belirle"]
  E -->|"Hayır"| G["ADIM 3 — Laboratuvar kanıtı üret"]
  F --> G

  G --> H{"Varyant splice etkisi<br/>düşündürüyor mu?"}
  H -->|"Evet"| I["RNA analizi (doğru doku):<br/>PVS1 basamağı + PS3"]
  H -->|"Hayır"| J{"Gen için doğrulanmış<br/>fonksiyonel analiz var mı?"}
  J -->|"Var"| K["Fonksiyonel/MAVE verisi:<br/>PS3 veya BS3 (gücü kalibrasyondan)"]
  J -->|"Yok"| L["Kalibre in silico eşiği + hastalığa özgü<br/>frekans eşiği yeniden hesapla"]

  I --> M["ADIM 4 — Yeniden sınıflandır"]
  K --> M
  L --> M
  M --> N{"Sınıf değişti mi?"}
  N -->|"Evet"| O["Raporu güncelle;<br/>aileyi ve izlem planını yeniden bilgilendir"]
  N -->|"Hayır"| P["VUS olarak bırak + ClinVar'a bildir<br/>+ TAKVİMLİ yeniden değerlendirme planla<br/>(ör. 12–24 ay)"]
  C --> P
```

### 4.4 Danışmada dil

Sınıflandırmanın olasılık doğası, aileye anlatılırken kaybolmamalıdır. "Patojenik" kelimesi ailede "kesinlik" olarak yankılanır; "belirsiz" kelimesi ise çoğu zaman "kötü bir şey ama söylemiyorlar" biçiminde anlaşılır. Bu iki yanlış anlamanın panzehiri aynıdır: **kanıt dilini kullanmak.** "Bu değişimin hastalığa yol açtığını gösteren güçlü kanıtlar var" ve "Bu değişimin ne anlama geldiğini söyleyecek yeterli veri henüz yok; bunu şu adımlarla araştırmayı planlıyoruz" cümleleri, hem doğrudur hem de ailenin belirsizliği yönetmesini kolaylaştırır.

---

## 5. Tanısal testlerle ilişkisi

Bu bölümde test tablosu farklı bir soruyla okunur: **hangi test hangi kanıtı (dolayısıyla hangi kriteri) üretir?**

**Tablo 16.3 — Hangi test hangi kanıtı (kriteri) üretir?**

| Test | Bu mekanizmayı yakalar mı? | Sınırlılığı |
|------|----------------------------|-------------|
| **WES** | Kodlayan varyantları bulur; PM2, PP3, PVS1 için ham veriyi sağlar | Kriterleri kendisi uygulamaz; kapsama boşlukları PM2 ve PVS1 yorumunu bozabilir; CNV ve kodlamayan alanı zayıf |
| **Short-read WGS** | Kodlayan + kodlamayan + çoğu SV; PM2 ve PP3 için en geniş zemin | Yorum yükü büyür; tekrar bölgeleri ve büyük genişlemeler sınırlı |
| **Long-read WGS** | **Faz bilgisi (PM3) ve karmaşık SV çözümü için üstün** | Maliyet/erişim; rutin varyant yorumlamada henüz standart değil |
| **Array-CGH / SNP array** | CNV çerçevesine girdi verir; bölge büyüklüğü ve gen içeriği puanlanır | Dizi varyantı kriterleri uygulanamaz; dengeli SV'leri görmez |
| **MLPA** | Hedefli delesyon/duplikasyon; ekzon düzeyinde çerçeve hesabı → PVS1 basamağı | Yalnız tasarlanan lokus |
| **RNA-seq** | Splice sonucu ve alel dengesizliği için **doğrudan kanıt** üretir. Kod seçimi: splicing bulgusu **PVS1_Strength** (etki yoksa BP7); PS3 ise RNA-splicing testinin ölçmediği işlevsel etki içindir | Doğru doku şart; ifade edilmeyen dokuda bilgi vermez |
| **Methylation array** | İmprinting/epimutasyon tablolarında ayırt edici; episignature desteği | Yalnız ilgili mekanizmalarda anlamlı |
| **Karyotip** | Dengeli translokasyon/inversiyon; CNV çerçevesine dolaylı katkı | Çözünürlük düşük |
| **(çerçeveye özgü) Aile örneklemesi ± fonksiyonel test** | **Evet — kriter üreten asıl kaynak.** PS2/PM6, PP1/BS4, PM3, PS3/BS3 buradan doğar | Zaman, erişim ve maliyet gerektirir; her gen için doğrulanmış analiz yoktur |

> **Bu mekanizmayı hangi test yakalar? (özet):** Varyant yorumlamada belirleyici olan tek bir test değil, **kanıt üretme sırasıdır**: (1) genin ve hastalık varlığının doğru seçilmesi, (2) varyantın tipine göre uygun kriter ailesinin belirlenmesi, (3) eksik kanıtı üretecek testin hedefli olarak istenmesi (aile örneği · RNA · fonksiyonel analiz), (4) sonucun ilgili uzman panel spesifikasyonuyla puanlanması.

---

## 6. Varyant yorumlama açısından önemi: uzmanlaştırma ve tuzaklar

### 6.1 Genel çerçeve neden yetmez?

2015 çerçevesi genel amaçlıdır ve bu onun hem gücü hem sınırıdır. Kitabın önceki bölümlerinde gördüğümüz mekanizmaların çoğu, çerçevenin varsayımlarını kırar; bu nedenle ClinGen ve ilgili uzman grupları bir dizi **uzmanlaştırılmış çerçeve** geliştirmiştir:

- **Kopya sayısı varyantları** için bölge/gen içeriği temelli ayrı bir puanlama sistemi kullanılır; dizi varyantı kriterleri doğrudan uygulanmaz (Riggs ve ark., 2020 — Bölüm 8).
- **Mitokondriyal DNA varyantları** için haplogrup bağlamını, heteroplazmi düzeyini ve tek-lif çalışmalarını hesaba katan mtDNA'ya özgü bir spesifikasyon geliştirilmiştir (McCormick ve ark., 2020 — Bölüm 11).
- **Splice varyantları** için PVS1'in gen-özgü karar ağacıyla uyarlanması, **RNA kanıtının PVS1_Strength koduyla** (PS3 ile değil) yakalanması, etkisizlik gösteren RNA sonucunun **BP7** ile kodlanması ve PP3/BP4'ün splice öngörüsüyle kullanımı ayrıca tanımlanmıştır; PS3/BS3, RNA-splicing testlerinin doğrudan ölçmediği işlevsel etkiye ayrılmıştır (Walker ve ark., 2023 — Bölüm 7).
- **Kodlamayan varyantlar** için, düzenleyici elementin ve hedef geninin tanımlanmasını şart koşan bir uyarlama önerilmiştir (Ellingford ve ark., 2022 — Bölüm 13).
- **Gen-özgü uzman panelleri (VCEP)**, kendi genlerinde kriterleri yeniden tanımlar: bir gende PM2 destekleyiciye indirilirken, başka bir gende PS3 için kabul edilen analiz listesi belirlenir.

Pratik kural şudur: **ilgili gen veya hastalık grubu için yayımlanmış bir spesifikasyon varsa, genel çerçeve değil o kullanılır.**

### 6.2 Kanıtın çift sayılması: en sinsi hata

Bayes çerçevesinin en önemli varsayımı, kanıt parçalarının **birbirinden bağımsız** olmasıdır. Uygulamada bu varsayım kolayca ihlal edilir ve sonuç, sınıfın yapay olarak şişmesidir. Tipik çift sayımlar şunlardır: aynı splice öngörüsünü hem PP3 hem PVS1 gerekçesi yapmak; aynı fonksiyonel çalışmayı hem PS3 hem PM1 için kullanmak; aynı ailedeki de novo bulgusunu hem PS2 hem PP1 saymak; nadirliği hem PM2 hem PS4 gerekçesine dönüştürmek. Kural basittir: **her veri parçası yalnız bir kez, en uygun kriterde sayılır.**

### 6.3 Karşıt kanıtı görmezden gelmemek

Çerçeve, hem patojenite hem benignlik lehine kanıtın bir arada bulunabileceğini kabul eder ve bu durumların olası patojenik, olası benign veya VUS sonucu verebileceği gösterilmiştir (Tavtigian ve ark., 2018). Uygulamadaki eğilim ise karşıt kanıtı görmezden gelmektir — özellikle fenotip güçlü olduğunda. Oysa karşıt kanıt, toplam ağırlıktan düşülmelidir; aksi hâlde rapor, elindeki veriden daha kesin görünür.

> **🟦 Klinikte dikkat — "Fenotip çok uyuyor, o hâlde patojenik olmalı" refleksi:** Fenotip uyumu PP4 ile sınırlı ve destekleyici bir kanıttır; sınıflandırmayı tek başına taşıyamaz. Üstelik Bölüm 15'te gördüğümüz gibi, alelik seri taşıyan genlerde fenotip uyumu **hangi hastalık varlığının** değerlendirildiğini belirlemek için kullanılmalı, kanıtı büyütmek için değil. Fenotibin güçlü olması, eksik kanıtın yerine geçmez; yalnızca hangi ek veriyi üretmeniz gerektiğini söyler.

---

## 7. Pediatrik genetikten klinik örnekler (çözümlü)

Aşağıdaki beş örnek, bölümün bütün araçlarını tek tek olgular üzerinde uygular. Puanlar, doğal ölçekli puan sistemine göre verilmiştir (Tavtigian ve ark., 2020); gerçek olgularda ilgili uzman panel spesifikasyonu esastır.

**Örnek 1 — Yenidoğanda dirençli nöbet; *SCN2A* p.Arg1882Gln (de novo).** Doğumun ilk gününde fokal nöbetlerle başvuran bebekte trio WES ile heterozigot bir missense varyant saptanır. Kanıt zinciri şöyle kurulur.

**De novo kanıtı (PS2).** Burada en sık yapılan hata, "trio negatif → PS2 tam güç" kısayoludur. Kriterin ön koşulu ebeveynliğin **doğrulanmış** olmasıdır (doğrulanmamışsa PM6 kullanılır) — ama asıl nokta güç düzeyidir: gen-özgü uzman panel spesifikasyonları de novo kanıtını **olgu sayısına göre** ölçekler. **Tek** doğrulanmış de novo olgu tipik olarak **PS2_Orta (+2)** eder; güç düzeyine çıkabilmek için bağımsız ikinci bir doğrulanmış de novo olgu gerekir. **Popülasyon kanıtı (PM2_Destekleyici, +1):** varyant uygun veri tabanlarında yok ve o pozisyonda kapsama yeterli (§2.1'deki koşullar). **Bölge kanıtı (PM1_Orta, +2):** bu kriteri "bu kodon tekrarlayan bir varyant konumudur" gerekçesiyle vermek **teknik olarak yanlıştır** — tekrarlayan olgularda görülme **PS4**'ün alanıdır. PM1, varyantın uzman panelin tanımladığı **patojenik varyanttan zengin bölge** içinde bulunmasına dayanır; dolayısıyla p.Arg1882'nin güncel PM1 tablosunda yer aldığı doğrulanmalıdır.

**Fonksiyonel kanıt (PS3_Güçlü, +4).** Bu, örneğin en sağlam ayağıdır ve dayanağı **nicel voltage-clamp** verisidir: yabanıl tipte toplam akımın %1,18 ± 0,13'ü olan persistan sodyum akımı, R1882Q'da **%2,92 ± 0,25**'e çıkar — yaklaşık 2,5 katlık bir artış — ve aktivasyon/inaktivasyon voltaj eğrilerinde de kayma gösterilmiştir (Berecki ve ark., 2018). Dinamik aksiyon potansiyeli clamp çalışması ise bu biyofiziksel değişikliklerin net sonucunun **artmış nöronal ateşleme** olduğunu ortaya koyar; yani yönü **işlev kazanımı** olarak netleştirir.

**Toplam: +9 → olası patojenik.** Dört kriterin toplamı patojenik için gereken 10'a ulaşmaz (§1). Sınıfın patojeniğe çıkması için ek kanıt gerekir ve iki yol vardır: *(a)* varyantın **bağımsız** hastalarda tekrarlandığının **PS4** kapsamında değerlendirilmesi — bir ek uygun olgu +1, iki-üç olgu +2, dört ve üzeri +4; ya da *(b)* ikinci bir doğrulanmış de novo olgunun bulunması, ki bu PS2'yi güç düzeyine (+4) çıkarır ve toplamı 11 yapar. ⚠️ **Aynı probandı hem PS2 hem PS4 için iki kez saymamak gerekir.** Nitekim p.Arg1882Gln tek olguya dayanan bir varyant değildir; kaynak çalışma bu varyantı taşıyan birden çok bireyi tanımlar — dolayısıyla gerçek bir olguda PS4 çoğunlukla uygulanabilir durumdadır.

**Öğreti:** Bu örnek iki ayrı dersi birden verir. Birincisi **puan disiplinidir**: kriterin adını doğru seçmek yetmez, **güç düzeyini** olgu sayısına ve panel kuralına göre ölçeklemek gerekir; "de novo + hotspot + fonksiyonel test" üçlüsü sezgisel olarak "patojenik" hissettirse de sayı 9'da kalabilir. İkincisi **mekanizma yönünün değeridir** — ama bunu doğru konumlandırmak şarttır: PS3'ün *puanı*, doğrulanmış ve nicel bir analizin hastalık mekanizmasıyla uyumlu anormal işlevi göstermesinden gelir. İşlev kazanımı yönünün belirlenmesi ise ACMG puanına ek bir ağırlık katmaz; değeri **klinik** düzlemdedir: fenotip korelasyonu, mekanizma sınıflaması ve tedavi seçimi. Erken başlangıçlı, işlev kazanımı yönündeki sodyum kanalı tablolarında sodyum kanal blokerlerinden yarar görülebilirken işlev kaybı tablolarında aynı yaklaşım uygun değildir (Brunklaus ve ark., 2020) — ancak bu bir garanti değildir; ilaç yanıtı bireyseldir ve fonksiyon yönü tek başına tedavi sonucunu vaat etmez.

**Örnek 2 — Yenidoğan hiperamonyemisi; *OTC* missense VUS.** Üçüncü günde ağır hiperamonyemi ile başvuran erkek bebekte *OTC*'de daha önce bildirilmemiş bir missense varyant bulunur. Başlangıçta kanıt zayıftır: popülasyonda yok (PM2, +1), hesaplamalı öngörü destekleyici (PP3, +1), hemizigot ve fenotip uyumlu (PP4, +1) → +3 → **VUS**. Ancak bu gen için 1.570 varyantın işlevsel etkisini ölçen çoklu-varyant analizi mevcuttur; varyant, klinik olarak anlamlı işlev kaybına karşılık gelen skor aralığındadır ve analiz neonatal başlangıçlı olguların varyantlarını geç başlangıçlılardan ayırt edebilmektedir (PS3, +4) (Lo ve ark., 2023). Toplam +7 → **olası patojenik**. **Öğreti:** aynı çalışmada, işlevi tümüyle kaybettiren 34 varyanttan 22'si tam bu yolla VUS'tan olası patojeniğe geçmiştir; fonksiyonel veri, VUS'u çözmenin en güçlü tek aracıdır.

**Örnek 3 — Son ekzonda nonsense varyant: PVS1 tuzağı.** Klinik olarak uyumlu bir olguda, ilgili genin **son ekzonunda** bir nonsense varyant bulunur. Refleks yorum "null varyant → PVS1 (+8)" der ve ek bir destekle sınıf hemen patojeniğe çıkar. Doğru yorum ise şudur: varyant NMD'den kaçar, yalnızca proteinin son birkaç rezidüsünü kaldırır ve bilinen işlevsel bir domaini etkilemez; bu durumda PVS1 destekleyiciye indirilir (+1) veya hiç uygulanmaz. PM2 (+1) ile birlikte toplam +2 → **VUS**. **Öğreti:** PVS1'in gücü varyant tipinden değil, kaybedilen protein bölgesinin işlevsel öneminden gelir; hastalık-özgü uyarlamalar tam bu noktada devreye girer (Abou Tayoun ve ark., 2018).

**Örnek 4 — "Nadir" ama aslında sık: frekans eşiğinin hastalığa göre hesaplanması.** Kardiyomiyopati paneli yapılan bir çocukta, gnomAD'de %0,05 frekansında bir missense varyant bulunur. "%1'in altı, o hâlde nadir" kestirmesi PM2'yi tetikler. Hastalığa özgü hesap ise farklı sonuç verir: hastalığın prevalansı, kalıtım modu, penetransı ve alelik heterojenitesi göz önüne alındığında bu genin tek bir varyantı için izin verilen en yüksek popülasyon frekansı çok daha düşüktür; %0,05 bu eşiğin üzerindedir ve BS1 (−4) uygulanır (Whiffin ve ark., 2017). Varyant **olası benign** olarak sınıflandırılır. **Öğreti:** aynı frekans, farklı hastalıklarda zıt yönde kanıttır; frekans eşiği hesaplanır, ezberlenmez.

**Örnek 5 — İki laboratuvar, iki farklı sınıf.** Bir ailede daha önce "olası patojenik" raporlanan bir varyant, yıllar sonra başka bir laboratuvar tarafından "olası benign" olarak yorumlanır; aile bu iki raporla kliniğe başvurur. Doğru yaklaşım, hangi raporun "haklı" olduğunu tartışmak değil, iki sınıflandırmanın **hangi kanıta dayandığını** karşılaştırmaktır: yeni popülasyon verisi frekans kriterini mi değiştirmiştir? Yeni segregasyon verisi eklenmiş midir? Fonksiyonel çalışma yayımlanmış mıdır? Bu tür bir uyuşmazlığın klinik sonuçları ağır olabilir; ClinGen'in kuruluş gerekçesini anlattığı vaka anlatısında, benzer bir yeniden yorumlama zinciri sonunda ailede gerçek nedensel varyantın bulunmasına ve daha önce "risk taşımıyor" denen bir bireyde koruyucu müdahaleye yol açmıştır (Rehm ve ark., 2015). **Öğreti:** varyant sınıfı bir zaman damgası taşır; veri paylaşımı ve takvimli yeniden değerlendirme, yorumlamanın parçasıdır.

---

## 8. Sık yapılan hatalar ve klinikte dikkat

> **🔴 Sık yapılan hata kutusu**
> 1. **Kriterleri saymak.** "Beş kriter işaretlendi, demek ki patojenik." Sınıf, kriter sayısından değil toplam ağırlıktan doğar; beş destekleyici kriter (+5) VUS sınırında kalır.
> 2. **PVS1'i mekanizma kapısını kontrol etmeden uygulamak.** İşlev kaybı, değerlendirilen **hastalığın** mekanizması değilse PVS1 hiç kullanılamaz.
> 3. **Splice varyantlarına otomatik tam güç vermek.** Kanonik ±1,2 pozisyonları bile öngörülen transkript sonucuna ve çerçeve etkisine göre değerlendirilmelidir.
> 4. **Kalibre edilmemiş araçları "oylatmak".** "Beş araçtan dördü zararlı diyor" ifadesinin niceliksel karşılığı yoktur; kalibre edilmiş tek bir aracın eşik aralığı tercih edilir (Pejaver ve ark., 2022).
> 5. **Hesaplamalı öngörüden mekanizma yönü çıkarmak.** Araçlar dominant-negatif ve işlev kazanımı varyantlarını ayırt etmekte zayıftır (Gerasimavicius ve ark., 2022); düşük skor, GoF varyantını temize çıkarmaz.
> 6. **Fonksiyonel çalışmayı otomatik olarak PS3 saymak.** Analiz mekanizmayı ölçmeli, kontrollerle doğrulanmış olmalı ve gücü hesaplanmalıdır (Brnich ve ark., 2019).
> 7. **Aynı kanıtı iki kriterde saymak.** Aynı splice öngörüsünü hem PP3 hem PVS1 gerekçesi yapmak, sınıfı yapay olarak yükseltir.
> 8. **Frekans eşiğini genel bir sayı olarak kullanmak.** Eşik, hastalığın prevalansı, kalıtımı, penetransı ve alelik heterojenitesinden hesaplanır (Whiffin ve ark., 2017).
> 9. **"De novo" bulgusunu sorgulamadan kabul etmek.** Ebeveyn mozaikliği hem kanıt gücünü hem tekrarlanma riskini değiştirir (Campbell ve ark., 2014).
> 10. **Karşıt kanıtı görmezden gelmek.** Benign yöndeki kanıt toplam ağırlıktan düşülmelidir; atlanması raporu olduğundan kesin gösterir.
> 11. **VUS'a dayanarak klinik karar vermek.** VUS izlem başlatmak, cerrahi karar vermek veya akrabalara test önermek için kullanılamaz.
> 12. **Sınıflandırmayı kalıcı saymak.** Yeni veri sınıfı değiştirebilir; takvimli yeniden değerlendirme planlanmalıdır (Rehm ve ark., 2015).

> **🟦 Klinikte dikkat kutusu**
> - Rapor cümlesini **gen + kalıtım + hastalık** üçlüsüyle kurun ve bir **mekanizma cümlesi** ekleyin ("beklenen etki işlev kaybıdır ve bu, X hastalığının bilinen mekanizmasıyla uyumludur").
> - İlgili gen için yayımlanmış bir uzman panel spesifikasyonu varsa, genel çerçeve yerine onu kullanın ve raporda belirtin.
> - VUS raporlarken **bir sonraki adımı** yazın: hangi ek veri hangi kriteri açacak (aile örneği · RNA · fonksiyonel analiz).
> - Aile örneği istemek laboratuvarın değil, çoğu zaman klinisyenin elindedir; segregasyon ve de novo kanıtı en ucuz kanıt kaynaklarıdır.
> - Belirsizliği aileye kanıt diliyle anlatın; "patojenik" kelimesini kesinlik, "belirsiz" kelimesini kötü haber olarak duyma eğilimi bu dille yumuşar.
> - Varyantlarınızı ve gerekçelerinizi paylaşılan veri tabanlarına bildirin; yeniden sınıflandırmanın altyapısı budur.

---

## 9. Klinik pratikte karar algoritması

**Algoritma 16.2 — Mekanizmadan sınıflandırmaya: ana yorumlama akışı**

```mermaid
flowchart TD
  A["Dizileme sonucu: aday varyant"] --> B["ADIM 0 — Gen–hastalık ilişkisi geçerli mi?<br/>ClinGen geçerlilik sınıfı + hastalık VARLIĞINI seç"]
  B -->|"Sınırlı / Çelişkili"| C["Kanıt temeli zayıf:<br/>tanısal iddia kurma; araştırma bağlamında değerlendir"]
  B -->|"Kesin / Güçlü"| D["ADIM 1 — Bu hastalığın MEKANİZMASI ne?<br/>(LoF · GoF · DN · splice · doz · mozaik · imprint…)"]

  D --> E{"Gen/hastalık için yayımlanmış<br/>ÖZEL spesifikasyon var mı?"}
  E -->|"Var"| F["O spesifikasyonu kullan<br/>(CNV · mtDNA · splice · kodlamayan · VCEP)"]
  E -->|"Yok"| G["Genel ACMG/AMP çerçevesi"]

  F --> H["ADIM 2 — Kriter ailelerini MEKANİZMAYA göre seç<br/>(Şekil 16.3 matrisi)"]
  G --> H

  H --> I{"Null varyant mı?"}
  I -->|"Evet"| J["PVS1 kapısı → basamak seç<br/>(Şekil 16.2)"]
  I -->|"Hayır"| K["PM1 · PS1/PM5 · PP3 (kalibre) ·<br/>PS3 (mekanizmayı ölçüyorsa)"]

  J --> L["ADIM 3 — Popülasyon + aile + fonksiyonel kanıtı ekle<br/>Her veri YALNIZ BİR kriterde sayılır"]
  K --> L

  L --> M["ADIM 4 — Karşıt kanıtı da topla ve<br/>TOPLAM AĞIRLIĞI hesapla"]
  M --> N{"Toplam ağırlık hangi sınıfa düşüyor?"}

  N -->|"P / LP"| O["Raporla: gen + kalıtım + hastalık + mekanizma cümlesi<br/>→ izlem, tarama, aile testi planı"]
  N -->|"LB / B"| P["Raporla: nedensel değil<br/>→ ancak TANI DIŞLANMADI; kör noktaları hatırlat"]
  N -->|"VUS"| Q["Eksik kanıtı belirle (Şekil 16.4)<br/>→ hedefli veri üret → TAKVİMLİ yeniden değerlendir"]

  O --> R["Veriyi paylaş (ClinVar) ·<br/>yeniden değerlendirme takvimi kur"]
  P --> R
  Q --> R
  C --> R
```

---

## 10. Kaynaklar

> **Atıf / doğrulama notu:** Bu bölümün bibliyografik verileri PubMed üzerinden doğrulanmıştır; her kaynağın PMID ve DOI'si tek tek teyit edilmiştir. (Metin içinde yazar-yıl, kaynakçada DOI-link kullanılır.)

1. **Richards S, Aziz N, Bale S, ve ark. (2015).** Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. *Genetics in Medicine* 17(5):405–424. **PMID: 25741868** · DOI: [10.1038/gim.2015.30](https://doi.org/10.1038/gim.2015.30) — *Kullanım amacı: Bölümün temel çerçevesi; beş sınıflı terminoloji, kanıt kategorileri ve kriter tanımları. Kaynak kütüğünden yeniden kullanılmıştır.*

2. **Tavtigian SV, Greenblatt MS, Harrison SM, ve ark. (2018).** Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework. *Genetics in Medicine* 20(9):1054–1060. **PMID: 29300386** · DOI: [10.1038/gim.2017.210](https://doi.org/10.1038/gim.2017.210) — *Kullanım amacı: Kanıt güçlerinin olasılık oranlarına çevrilmesi; 18 kombinasyondan yalnız 2'sinin tutarsız olması; karşıt yönlü kanıtların sonucu.*

3. **Tavtigian SV, Harrison SM, Boucher KM, Biesecker LG (2020).** Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines. *Human Mutation* 41(10):1734–1737. **PMID: 32720330** · DOI: [10.1002/humu.24088](https://doi.org/10.1002/humu.24088) — *Kullanım amacı: Toplanabilir puan sistemi; puanların log(odds) ile orantılı olması; sistemin güçlü ve zayıf yanları.*

4. **Pejaver V, Byrne AB, Feng BJ, ve ark. (2022).** Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. *American Journal of Human Genetics* 109(12):2163–2177. **PMID: 36413997** · DOI: [10.1016/j.ajhg.2022.10.013](https://doi.org/10.1016/j.ajhg.2022.10.013) — *Kullanım amacı: PP3/BP4'ün kalibrasyon temelli kullanımı; "çoklu araç uzlaşması" gerekliliğinin niceliksel dayanağının olmaması; 13 araç için eşikler.*

5. **Whiffin N, Minikel E, Walsh R, ve ark. (2017).** Using high-resolution variant frequencies to empower clinical genome interpretation. *Genetics in Medicine* 19(10):1151–1158. **PMID: 28518168** · DOI: [10.1038/gim.2017.26](https://doi.org/10.1038/gim.2017.26) — *Kullanım amacı: Frekans eşiğinin prevalans, heterojenite, kalıtım ve penetranstan hesaplanması; kardiyomiyopatide aday varyantların üçte iki azaltılması.*

6. **Jarvik GP, Browning BL (2016).** Consideration of Cosegregation in the Pathogenicity Classification of Genomic Variants. *American Journal of Human Genetics* 98(6):1077–1081. **PMID: 27236918** · DOI: [10.1016/j.ajhg.2016.04.003](https://doi.org/10.1016/j.ajhg.2016.04.003) — *Kullanım amacı: Segregasyonun nicel bir kanıt olması; ACMG/AMP'de tanım eksikliğinin tutarsızlık kaynağı olması; uygulanabilir nicel ölçütler.*

7. **Gelman H, Dines JN, Berg J, ve ark. (2019).** Recommendations for the collection and use of multiplexed functional data for clinical variant interpretation. *Genome Medicine* 11(1):85. **PMID: 31862013** · DOI: [10.1186/s13073-019-0698-7](https://doi.org/10.1186/s13073-019-0698-7) — *Kullanım amacı: Çoklu-varyant fonksiyonel verilerin üretimi, raporlanması ve ACMG/AMP çerçevesine dâhil edilmesi.*

8. **Lo RS, Cromie GA, Tang M, ve ark. (2023).** The functional impact of 1,570 individual amino acid substitutions in human OTC. *American Journal of Human Genetics* 110(5):863–879. **PMID: 37146589** · DOI: [10.1016/j.ajhg.2023.03.019](https://doi.org/10.1016/j.ajhg.2023.03.019) — *Kullanım amacı: Pediatrik örnek — OTC eksikliğinde çoklu-varyant analizi; neonatal ve geç başlangıçlı olguların ayrılması; PS3 ile 34 varyanttan 22'sinin VUS'tan olası patojeniğe geçmesi.*

9. **Rehm HL, Berg JS, Brooks LD, ve ark. (2015).** ClinGen — the Clinical Genome Resource. *The New England Journal of Medicine* 372(23):2235–2242. **PMID: 26014595** · DOI: [10.1056/NEJMsr1406261](https://doi.org/10.1056/NEJMsr1406261) — *Kullanım amacı: Yeniden sınıflandırmanın klinik sonuçları; veri paylaşımının gerekçesi; ClinGen'in kuruluş çerçevesi.*

10. **Abou Tayoun AN, Pesaran T, DiStefano MT, ve ark. (2018).** Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. *Human Mutation* 39(11):1517–1524. **PMID: 30192042** · DOI: [10.1002/humu.23626](https://doi.org/10.1002/humu.23626) — *Kullanım amacı: PVS1'in mekanizma ön koşulu ve güç basamakları; yedi hastalık-özgü grupta %89 uyum. Kaynak kütüğünden yeniden kullanılmıştır.*

11. **Walker LC, de la Hoya M, Wiggins GAR, ve ark. (2023).** Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup. *American Journal of Human Genetics* 110(7):1046–1067. **PMID: 37352859** · DOI: [10.1016/j.ajhg.2023.06.002](https://doi.org/10.1016/j.ajhg.2023.06.002) — *Kullanım amacı: Splice varyantlarında PVS1'in uyarlanması ve RNA verisinin PS3 ile ilişkilendirilmesi. Kaynak kütüğünden yeniden kullanılmıştır.*

12. **Brnich SE, Abou Tayoun AN, Couch FJ, ve ark. (2019).** Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework. *Genome Medicine* 12(1):3. **PMID: 31892348** · DOI: [10.1186/s13073-019-0690-2](https://doi.org/10.1186/s13073-019-0690-2) — *Kullanım amacı: PS3/BS3'ün mekanizma tanımı, analiz doğrulaması ve güç hesabı koşulları. Kaynak kütüğünden yeniden kullanılmıştır.*

13. **Riggs ER, Andersen EF, Cherry AM, ve ark. (2020).** Technical standards for the interpretation and reporting of constitutional copy-number variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics (ACMG) and the Clinical Genome Resource (ClinGen). *Genetics in Medicine* 22(2):245–257. **PMID: 31690835** · DOI: [10.1038/s41436-019-0686-8](https://doi.org/10.1038/s41436-019-0686-8) — *Kullanım amacı: CNV'ler için ayrı puanlama çerçevesi. Kaynak kütüğünden yeniden kullanılmıştır.*

14. **McCormick EM, Lott MT, Dulik MC, ve ark. (2020).** Specifications of the ACMG/AMP standards and guidelines for mitochondrial DNA variant interpretation. *Human Mutation* 41(12):2028–2057. **PMID: 32906214** · DOI: [10.1002/humu.24107](https://doi.org/10.1002/humu.24107) — *Kullanım amacı: mtDNA'ya özgü uzmanlaştırma; haplogrup, heteroplazmi ve tek-lif çalışmalarının kritere çevrilmesi. Kaynak kütüğünden yeniden kullanılmıştır.*

15. **Ellingford JM, Ahn JW, Bagnall RD, ve ark. (2022).** Recommendations for clinical interpretation of variants found in non-coding regions of the genome. *Genome Medicine* 14(1):73. **PMID: 35850704** · DOI: [10.1186/s13073-022-01073-3](https://doi.org/10.1186/s13073-022-01073-3) — *Kullanım amacı: Kodlamayan varyantlarda çerçevenin uyarlanması; element ve hedef gen tanımı şartı. Kaynak kütüğünden yeniden kullanılmıştır.*

16. **Strande NT, Riggs ER, Buchanan AH, ve ark. (2017).** Evaluating the Clinical Validity of Gene-Disease Associations: An Evidence-Based Framework Developed by the Clinical Genome Resource. *American Journal of Human Genetics* 100(6):895–906. **PMID: 28552198** · DOI: [10.1016/j.ajhg.2017.04.015](https://doi.org/10.1016/j.ajhg.2017.04.015) — *Kullanım amacı: Sınıflandırmanın ön koşulu olarak gen–hastalık geçerliliği. Kaynak kütüğünden yeniden kullanılmıştır (Bölüm 15 köprüsü).*

17. **Thaxton C, Goldstein J, DiStefano M, ve ark. (2022).** Lumping versus splitting: How to approach defining a disease to enable accurate genomic curation. *Cell Genomics* 2(5):100131. **PMID: 35754516** · DOI: [10.1016/j.xgen.2022.100131](https://doi.org/10.1016/j.xgen.2022.100131) — *Kullanım amacı: Değerlendirilecek hastalık varlığının tanımlanması (ön-küreleme). Kaynak kütüğünden yeniden kullanılmıştır (Bölüm 15 köprüsü).*

18. **MacArthur DG, Manolio TA, Dimmock DP, ve ark. (2014).** Guidelines for investigating causality of sequence variants in human disease. *Nature* 508(7497):469–476. **PMID: 24759409** · DOI: [10.1038/nature13127](https://doi.org/10.1038/nature13127) — *Kullanım amacı: Nedensellik iddiasının kanıt gücüne göre derecelendirilmesi. Kaynak kütüğünden yeniden kullanılmıştır.*

19. **Karczewski KJ, Francioli LC, Tiao G, ve ark. (2020).** The mutational constraint spectrum quantified from variation in 141,456 humans. *Nature* 581(7809):434–443. **PMID: 32461654** · DOI: [10.1038/s41586-020-2308-7](https://doi.org/10.1038/s41586-020-2308-7) — *Kullanım amacı: **LOEUF** kısıt ölçütünün tanımlandığı çalışma; popülasyon kanıtının gen düzeyinde bağlamlandırılması. Kaynak kütüğünden yeniden kullanılmıştır.*

20. **Jaganathan K, Kyriazopoulou Panagiotopoulou S, McRae JF, ve ark. (2019).** Predicting Splicing from Primary Sequence with Deep Learning. *Cell* 176(3):535–548.e24. **PMID: 30661751** · DOI: [10.1016/j.cell.2018.12.015](https://doi.org/10.1016/j.cell.2018.12.015) — *Kullanım amacı: Splice öngörüsünün hesaplamalı kanıt olarak gücü. Kaynak kütüğünden yeniden kullanılmıştır.*

21. **Gerasimavicius L, Livesey BJ, Marsh JA (2022).** Loss-of-function, gain-of-function and dominant-negative mutations have profoundly different effects on protein structure. *Nature Communications* 13(1):3895. **PMID: 35794153** · DOI: [10.1038/s41467-022-31686-6](https://doi.org/10.1038/s41467-022-31686-6) — *Kullanım amacı: Tahmin araçlarının dominant-negatif ve işlev kazanımı varyantlarında zayıflığı. Kaynak kütüğünden yeniden kullanılmıştır.*

22. **Campbell IM, Yuan B, Robberecht C, ve ark. (2014).** Parental somatic mosaicism is underrecognized and influences recurrence risk of genomic disorders. *American Journal of Human Genetics* 95(2):173–182. **PMID: 25087610** · DOI: [10.1016/j.ajhg.2014.07.003](https://doi.org/10.1016/j.ajhg.2014.07.003) — *Kullanım amacı: De novo kanıtının (PS2/PM6) ebeveyn mozaikliğiyle sınırlanması ve tekrarlanma riskine etkisi. Kaynak kütüğünden yeniden kullanılmıştır.*

23. **Berecki G, Howell KB, Deerasooriya YH, ve ark. (2018).** Dynamic action potential clamp predicts functional separation in mild familial and severe de novo forms of *SCN2A* epilepsy. *Proceedings of the National Academy of Sciences USA* 115(24):E5516–E5525. **PMID: 29844171** · DOI: [10.1073/pnas.1800077115](https://doi.org/10.1073/pnas.1800077115) — *Kullanım amacı: Çözümlü örnek 1'de fonksiyonel kanıtın (PS3) mekanizma yönünü göstermesi. Kaynak kütüğünden yeniden kullanılmıştır.*

24. **Brunklaus A, Du J, Steckler F, ve ark. (2020).** Biological concepts in human sodium channel epilepsies and their relevance in clinical practice. *Epilepsia* 61(3):387–399. **PMID: 32090326** · DOI: [10.1111/epi.16438](https://doi.org/10.1111/epi.16438) — *Kullanım amacı: Mekanizma yönünün tedavi kararına çevrilmesi. Kaynak kütüğünden yeniden kullanılmıştır.*

25. **Lek M, Karczewski KJ, Minikel EV, ve ark. (2016).** Analysis of protein-coding genetic variation in 60,706 humans. *Nature* 536(7616):285–291. **PMID: 27535533** · DOI: [10.1038/nature19057](https://doi.org/10.1038/nature19057) — *Kullanım amacı: **pLI** metriğinin tanımlandığı çalışma (ExAC); PM2'nin kısıtlılık bağlamında yorumlanması. Kaynak kütüğünden yeniden kullanılmıştır.*

> **Kılavuz belgesi (§1).** **Association for Clinical Genomic Science (ACGS) (2024).** *ACGS Best Practice Guidelines for Variant Classification in Rare Disease*, v1.2; 2024. [Belge (PDF)](https://www.genomicseducation.hee.nhs.uk/wp-content/uploads/2024/08/ACGS-2024_UK-practice-guidelines-for-variant-classification.pdf) — *Kullanım amacı: Bayes türevi kanıt puanları (Çok güçlü 8 · Güçlü 4 · Orta 2 · Destekleyici 1) ve sınıf eşikleri (≥10 · 6–9 · 0–5 · −1…−5 · ≤−6); BA1 istisnası dışında **en az iki bağımsız kriter** kuralı ve yalnızca PVS1_ÇokGüçlü bulunan varyantın ikinci kanıt gelene kadar VUS tutulması.* ⚠️ PubMed'de indekslenmeyen, sürüme bağlı normatif bir belgedir; alıntılanan puan ve eşikler belge metniyle birebir eşleştirilmiştir (29.07.2026).

> **İkincil/destekleyici kaynak notu:** ClinVar, ClinGen VCEP spesifikasyonları, gnomAD ve OMIM bu bölümde yalnızca destekleyici/başvuru kaynağı olarak anılmıştır. Puan eşikleri ve olasılık aralıkları, ilgili yöntem makalelerinde tanımlanan değerlerdir; gerçek olgularda ilgili uzman panel spesifikasyonu esas alınmalıdır.

---

## ✅ Bölüm öz-denetim tablosu

**Tablo 16.4 — Bölüm 16 öz-denetim tablosu**

| Kriter | Durum | Not |
|--------|-------|-----|
| Mekanizma doğru anlatıldı mı? | ✅ | Kanıt mimarisi (güç → olasılık oranı → puan → sınıf) kuruldu; kriter aileleri tek tek mekanizmayla ilişkilendirildi |
| Klinik bağlantı kuruldu mu? | ✅ | Sınıfların klinik anlamı, yeniden sınıflandırma, VUS yönetimi ve danışma dili |
| Varyant tipi ile mekanizma ilişkilendirildi mi? | ✅ | 11 satırlık "varyant tipine göre öncelikle değerlendirilecek kanıt alanları" tablosu (algoritma olmadığı dipnotla belirtildi) + mekanizma–kriter matrisi |
| Pediatrik örnek verildi mi? | ✅ | Beş çözümlü örnek: *SCN2A* (yenidoğan epilepsisi), *OTC* (hiperamonyemi), son-ekzon PVS1 tuzağı, frekans eşiği, iki laboratuvar uyuşmazlığı |
| Test seçimi açıklandı mı? | ✅ | Standart 8 satırlık tablo + "aile örneklemesi/fonksiyonel test" satırı; testler kriter üretimi açısından okundu |
| ACMG/ClinGen bağlantısı doğru mu? | ✅ | PVS1 (Abou Tayoun 2018), PS3/BS3 (Brnich 2019), PP3/BP4 (Pejaver 2022), PM2/BS1 (Whiffin 2017), PP1 (Jarvik 2016), spesifikasyonlar (Riggs/McCormick/Walker/Ellingford) |
| Kaynaklar PMID/DOI ile verildi mi? | ✅ | 24/24 kaynak PMID + DOI-link + kullanım amacı ile (8 yeni doğrulama + 16 kütükten yeniden kullanım) |
| Spekülatif iddialar işaretlendi mi? | ✅ | Mekanizma–kriter matrisinin pedagojik (normatif olmayan) niteliği ⚠️ ile işaretlendi; puan eşiklerinin kaynağı açıkça belirtildi |
| Kaynak uydurma riski var mı? | ✅ Yok | 8 yeni PMID/DOI bu oturumda PubMed MCP ile doğrulandı; 16'sı daha önce doğrulanmış kütük kaydı |
| Görsel/şema/algoritma desteği yeterli mi? (≥3 SVG, ≥2 Mermaid) | ✅ | **4 SVG + 3 Mermaid**; tüm SVG'ler tarayıcıda render edilip gözle denetlendi |

---

### 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu)
> "Bu bölümdeki her kaynağın **türüne uygun kalıcı kimliğini** kontrol et: hakemli makalede PMID + DOI; kılavuz/uzman panel spesifikasyonunda kurum + sürüm + tarih + kalıcı bağlantı; veri tabanında veri sürümü + sorgu tarihi. Kimliği doğrulanamayan kaynağı çıkar. Kaynağı olmayan spesifik iddiayı 'kaynak doğrulaması gerekli' olarak işaretle. Kitabın kendi pedagojik çerçevesini doğrulamaya çalışma — 🏷️ ile etiketle." *(Politika 01.08.2026 uzman turunda güncellendi: eski 'PMID veya DOI veremediğin kaynağı çıkar' kuralı HGVS, ClinGen/CSpec, gnomAD sürüm notları gibi PMID'siz ama yetkili kaynakları dışlıyordu.)*
>
> **Bu bölüm için durum:** **24/24 kaynak PMID+DOI doğrulandı** (8'i bu oturumda PubMed MCP ile — Tavtigian 2018, Tavtigian 2020, Pejaver 2022, Whiffin 2017, Jarvik & Browning 2016, Gelman 2019, Lo 2023, Rehm 2015; 16'sı Bölüm_00 kaynak kütüğünden yeniden kullanıldı). Bölüm, 27.07.2026 tarihli iddia-düzeyi doğrulama turundan geçmiştir; turda **RNA-splicing kanıtının kodlanması** dört ayrı yerde düzeltilmiştir (PS3 değil **PVS1_Strength**; etkisizlik için **BP7**) — Walker ve ark., 2023 (bkz. `Dogrulama_Kutugu.md`).
>
> **İşaretlenen iddialar:** (1) ⚠️ Şekil 16.3'deki mekanizma–kriter matrisi **pedagojik bir özettir**; normatif değildir ve ilgili gen/hastalık için yayımlanmış uzman panel spesifikasyonunun yerini almaz. (2) Puan karşılıkları (destekleyici +1, orta +2, güçlü +4, çok güçlü +8) ve sınıf eşikleri, doğal ölçekli puan sisteminde tanımlanan değerlerdir (Tavtigian ve ark., 2020); olasılık oranları ve sonsal olasılık aralıkları Bayes formülasyonundan gelir (Tavtigian ve ark., 2018). Uzman panelleri kendi genlerinde farklı eşikler tanımlayabilir. (3) 7. başlıktaki çözümlü örneklerin puanlamaları **öğretici amaçlıdır**; gerçek olgularda güncel spesifikasyon ve tam kanıt kümesi kullanılmalıdır.
>
> **Uzman değerlendirmesi turu C24 (01.08.2026).** Tablo 16.2'nin "sık hata" sütunu satır satır denetlendi; 11 satırın 5'i revize edildi ve tablonun **algoritma gibi okunma riski** giderildi. Yapısal değişiklikler: başlık "ilk bakılacak kriterler" → **"öncelikle değerlendirilecek kanıt alanları"**, son sütun "tipik tuzak" → **"en sık yanlış uygulama"**, kriterler arasındaki **oklar virgülle** değiştirildi (ok, kriterlerin sırayla ve otomatik uygulanacağı izlenimi veriyordu) ve tablonun altına normatif olmadığını söyleyen bir ⚠️ dipnotu eklendi. İçerik düzeltmeleri: **(1) Son ekzon/NMD kaçışı** — hata tek yönlü yazılmıştı; "son ekzon" diye **otomatik düşürülmüş PVS1** vermenin de aynı ölçüde yanlış olduğu, gücün kesilen bölgenin kritikliğine ve mekanizmaya (LoF mu, DN/GoF mu) göre belirlendiği eklendi. **(2–3) İki splice satırı** — "RNA bulgusunu PS3 ile kodlamak" uyarısı yalnız **saf splicing sonucu** için geçerlidir; RNA'dan bağımsız protein/hücresel işlev deneylerinin yine PS3 oluşturabileceği belirtildi. Ayrıca "etki yoksa BP7" koşullandırıldı: uygun olmayan dokudaki negatif RNA sonucu otomatik BP7/BS3 sayılamaz. **(4) Tekrar genişlemesi** — "dizileme temelli kriter uygulamaya çalışmak" ifadesi çıkarıldı (genişlemeler bugün NGS ve uzun-okuma ile de saptanır); hata, **kısa varyantlar için tasarlanmış kanıt kodlarını tekrar aleline mekanik uygulamak** ve motif bütünlüğü/kesinti/metilasyon/instabiliteyi atlamak olarak yeniden yazıldı. **(5) Düşük VAF** — "PS2/PM6 dikkatle" sırası yanlıştı; ilk soru de novo kriteri değil **varyantın gerçekliği ve dokusal dağılımıdır**. Ayrıca üç genel düzeltme yapıldı: tablodaki bütün **PM2**'ler **PM2_Supporting**'e çevrildi (§2'deki kutuyla uyumlu), kodlamayan satırındaki "PM1 genellikle yok" ifadesi **PM1_Supporting**'in iyi tanımlanmış hastalık-spesifik motiflerde kullanılabileceği biçiminde daraltıldı, ve PS3'ün hiçbir satırda otomatik "ilk kriter" olmadığı dipnota yazıldı. Yeni kaynak gerekmedi; düzeltmeler bölümün mevcut kaynaklarına (Abou Tayoun 2018 · Walker 2023 · Brnich 2019 · Riggs 2020 · McCormick 2020 · Ellingford 2022 · Pejaver 2022) dayanır.
>
> **Uzman değerlendirmesi turu D4 (01.08.2026).** Şekil 16.3'ün **normatif bir ACMG/ClinGen eşleştirme tablosu sanılma riski** giderildi. Şekil başlığı "Mekanizma → kriter matrisi" → **"Mekanizma × kanıt ailesi ilişki matrisi (pedagojik sentez · NORMATİF DEĞİLDİR)"**; alt yazıya "semboller kriter gücü veya ACMG puanı göstermez, işaret = kriter kazanıldı değildir" eklendi; lejantta **✖ "UYGULANAMAZ" → "genellikle UYGULANMAZ"** olarak yumuşatıldı. Metinde matrisin **iki ekseninin de editöryal** olduğu yazıldı: on dört satır bu kitabın mekanizma bölümlendirmesi, sekiz sütun ise ACMG kriter kodlarını öğretim amacıyla gruplayan bir sınıflamadır — ClinGen'in kendi rehberleri bu kriterleri ayrı metodolojik sorunlar olarak ele alır. Şeklin altına **üç yanlış anlamayı** açıkça reddeden bir uyarı kutusu (işaret ≠ kriter kazanıldı · boşluk/✖ ≠ yasak · aynı hücre ≠ her gende aynı güç) ve VCEP spesifikasyonunun matrisin önünde geldiği notu eklendi; ayrıca matrisin **nasıl okunacağını** gösteren somut bir örnek okuma yazıldı (yetersiz doz satırı → nonsens varyanta otomatik PVS1+PM2+PS2 verilmez). Yeni kaynak gerekmedi.
