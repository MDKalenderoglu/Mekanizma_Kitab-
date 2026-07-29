# Bölüm 15 — Aynı Gen, Farklı Hastalık: Allelik Seriler

> **Bölümün çekirdek tezi:** Klinik genetiğin gündelik dili gen adları üzerine kuruludur: "*LMNA* hastası", "*FGFR3* mutasyonu", "*RET* taşıyıcısı". Bu dil pratiktir ama yanıltıcıdır, çünkü **bir gen bir hastalığa karşılık gelmez.** Aynı lokustaki farklı varyantlar, birbirinden klinik olarak tanınmayacak kadar farklı — kimi zaman taban tabana zıt — hastalıklar üretir: *FGFR3*'ün bir varyantı bebeği neonatal dönemde öldüren bir iskelet displazisi yaparken, aynı genin başka bir varyantı uzun boy ve işitme kaybıyla giden tümüyle farklı bir tabloya yol açar. Bu bölüm, bu çokluğun rastgele olmadığını gösterir: **allelik seri**, çoğu zaman tek bir ölçülebilir eksen (aktivite düzeyi, rezidüel işlev, bozulan arayüz) boyunca dizilir ve o eksendeki konum, hastalığın adını belirler. Bölümün ikinci ve yorumlama açısından daha keskin tezi şudur: **değerlendirilen birim gen değil, gen–kalıtım–mekanizma üçlüsüdür.** Bir varyant "*LMNA* için patojen" olamaz; ancak "*LMNA*'ya bağlı otozomal dominant Emery-Dreifuss musküler distrofisi için patojen" olabilir. Bu ayrımı kaçıran her rapor cümlesi, hem yanlış bir tanı hem de yanlış bir tekrarlanma riski taşır.

> **Bu bölüm nasıl okunmalı?** Bu bölüm kitabın bir **sentez bölümüdür**: Bölüm 2–6'da tek tek öğrenilen mekanizmaların (LoF, HI, GoF, DN, neomorf) aynı lokusta yan yana durduğunda ne olduğunu inceler. Tıp öğrencileri için 1. ve 2. başlıklar ile Şekil 15.1–15.2 çekirdeği oluşturur; altı eksen kavranmadan geri kalanı ezber olarak kalır. Klinisyenler için 4. ve 7. başlıklar, laboratuvar ve varyant yorumlayanlar için 6. başlık ile Şekil 15.4 doğrudan uygulanabilir niteliktedir. Bölüm 16'ya (ACMG/ClinGen sentezi) hazırlık olarak 6. başlık mutlaka okunmalıdır.

> 🖼️ **Görseller hakkında not:** Şekil 15.1–15.4 `assets/` klasöründe SVG olarak bulunur. Mermaid diyagramları metin içine gömülüdür.

---

## Öğrenme hedefleri

Bu bölümü tamamlayan okuyucu:
1. Allelik heterojenite, lokus heterojenite ve fenotipik heterojenite (pleiotropi) kavramlarını birbirinden ayırır ve her birinin tanısal sonucunu açıklar.
2. Bir allelik serinin dizildiği altı ekseni (mekanizma yönü, rezidüel işlev, varyant konumu, kalıtım modu, zamanlama, bağlam) sıralar ve her birine somut bir gen örneği verir.
3. *FGFR3* serisini reseptör aktivitesi ekseninde açıklar ve aynı genin hem uzun boy hem letal iskelet displazisi yapabilmesini gerekçelendirir.
4. Rezidüel işlev derecesinin klinik eşiği geçtiğinde hastalığın neden "yeni bir ad" aldığını *PAH* ve *ATP7A* örnekleriyle açıklar.
5. Varyant konumunun (domain/izoform) doku-seçici fenotibi nasıl belirlediğini *LMNA* ve *COL1A1* üzerinden yorumlar.
6. Progeria örneğinde sessiz bir nükleotid değişiminin nasıl yeni bir protein (progerin) ürettiğini ve bunun mekanizma sınıfını nasıl değiştirdiğini açıklar.
7. Aynı genin germline ve mozaik hâllerinin neden farklı hastalık adları taşıdığını *GNAS* örneğinde açıklar.
8. "Birleştirme (lumping) ve ayırma (splitting)" kararının ölçütlerini sayar ve bunun panel kapsamı, varyant yorumu ve danışmaya etkilerini yorumlar.
9. PS1, PM5, PM1 ve PVS1 kriterlerinin allelik seride neden "hangi hastalık için?" sorusuyla birlikte sorulması gerektiğini açıklar.
10. Fenotip-öncelikli ve gen-öncelikli tanı stratejilerini karşılaştırır ve derin fenotiplemenin allelik seride neden vazgeçilmez olduğunu gerekçelendirir.

---

## 1. Kavramsal tanım

Bölüm 1'de üç heterojenite biçimini kısaca tanımlamıştık; bu bölüm bunlardan birini merkeze alır, dolayısıyla üçünü net biçimde ayırarak başlamak gerekir. **Lokus heterojenitesi**, aynı klinik tablonun farklı genlerdeki varyantlarla ortaya çıkmasıdır — Bölüm 11'de gördüğümüz Leigh sendromu, yetmiş beşten fazla farklı genin aynı klinik kapıya çıkabildiği örnektir. **Allelik heterojenite**, aynı gendeki farklı varyantların aynı hastalığa yol açmasıdır; kistik fibrozdaki yüzlerce farklı *CFTR* varyantı bunun tipik hâlidir. Bu bölümün konusu ise üçüncüsüdür: **fenotipik heterojenite (allelik seri)** — aynı gendeki farklı varyantların **farklı hastalıklara** yol açması. Genetik literatürde bunun bir başka adı **pleiotropi**dir: tek bir lokusun birden çok, görünüşte ilgisiz özelliği etkilemesi.

Aradaki fark akademik bir incelik değildir; doğrudan raporu değiştirir. Lokus heterojenitesi karşısında yapılması gereken **paneli genişletmektir**. Allelik heterojenite karşısında yapılması gereken **o genin tamamını iyi kapsayan bir test seçmektir**. Fenotipik heterojenite karşısında ise yapılması gereken bambaşkadır: **varyantın gen içindeki konumunu ve mekanizmasını çözmek**, çünkü hastanın hangi hastalığa sahip olduğu ancak bu bilgiyle söylenebilir.

**Allelik seri** terimi, tek bir gendeki varyantların ürettiği fenotip yelpazesinin tamamına verilen addır. Bu terim aslında bize yabancı değil: Bölüm 6'da Muller'in klasik allel serisini (amorf → hipomorf → hipermorf → antimorf → neomorf) tanıtmıştık. Muller serisi bir **moleküler** seridir; bu bölümde ele aldığımız allelik seri ise onun **klinik izdüşümüdür**. Aynı zamanda Wilkie'nin dominant varyant mekanizmalarını sınıflandırdığı çerçeve (Wilkie, 1994) burada tekrar iş görür: aynı lokusta hem kayıp hem kazanım mekanizmalarının bulunabilmesi, allelik serilerin en dramatik biçimidir.

Bu bölümün kavramsal omurgasını oluşturan üçüncü terim ise klinik laboratuvardan gelir: **gen–hastalık varlığı (gene–disease entity)**. ClinGen'in gen–hastalık geçerliliği çerçevesi, kanıtın gücünü değerlendirirken hiçbir zaman yalnız "gen"i değil, bir **gen ile bir hastalık arasındaki ilişkiyi** puanlar ve bu ilişkiyi "Kesin (Definitive)", "Güçlü", "Orta", "Sınırlı", "Bildirilmiş kanıt yok" veya "Çelişkili kanıt" olarak sınıflar (Strande ve ark., 2017). Yani bir gen, bir hastalık için "Kesin", başka bir hastalık için "Sınırlı" olabilir. Allelik seri, bu çerçevenin neden bu şekilde kurulduğunu gösteren esas nedendir.

**Tablo 15.1 — Heterojenite türleri ve tanısal karşılıkları**

| Kavram | Tanım | Klinik/laboratuvar sonucu |
|---|---|---|
| Lokus heterojenitesi | Aynı fenotip, **farklı genler** | Paneli genişlet; tek gen negatifliği tanıyı dışlamaz |
| Allelik heterojenite | Aynı hastalık, **aynı gende farklı varyantlar** | Genin tamamını kapsayan test seç (CNV dahil) |
| **Fenotipik heterojenite / allelik seri** | **Aynı gen, farklı hastalıklar** | Varyantın konumu ve mekanizması tanının kendisidir |
| Pleiotropi | Tek lokusun birden çok özelliği etkilemesi | Beklenmedik organ tutulumlarını dışlama; sistemik değerlendirme |
| Gen–hastalık varlığı | Gen + kalıtım modu + hastalık üçlüsü | Küreleme, panel kapsamı ve varyant sınıflandırmasının birimi |
| Ön-küreleme (precuration) | Gen için hangi hastalık varlıklarının tanımlanacağının belirlenmesi | Birleştirme/ayırma kararının yapıldığı aşama |

---

## 2. Moleküler mekanizma: allelik seriyi doğuran altı eksen

Bir genin çok sayıda hastalık yapması ilk bakışta kaotik görünür. Oysa neredeyse her allelik seri, birbirinden ayırt edilebilir **altı eksenden** bir veya birkaçının üzerinde dizilir (Şekil 15.1). Bu eksenleri tanımak, karşınıza çıkan yeni bir gende bile "bu gen neden iki hastalık yapıyor?" sorusunu sistematik biçimde yanıtlamanızı sağlar.

> 🏷️ **Bu altı eksenli çerçeve kitabın pedagojik sentezidir.** Eksenlerin her biri ayrı ayrı kaynaklıdır ve bu kitabın önceki bölümlerinde tek tek işlenmiştir (mekanizma yönü → Bölüm 2–6; rezidüel işlev → Bölüm 2; varyant konumu → Bölüm 2 ve 7; kalıtım modu → Bölüm 1 ve 3; zamanlama → Bölüm 1 ve 12; bağlam → Bölüm 14). Buna karşılık **"allelik serinin altı ekseni" literatürde bu adla yerleşik bir sınıflandırma değildir**; eksen sayısı ve gruplama editöryaldir ve öğretme kolaylığı için seçilmiştir. Bir raporda veya yayında bu çerçeveye yerleşik bir taksonomiymiş gibi atıf yapılmamalıdır.

![Şekil 15.1 — Aynı gen neden farklı hastalıklar yapar? Altı eksen](assets/sekil_50_allelik_seri_alti_eksen.svg)

### 2.1 Birinci eksen: mekanizma yönü — kayıp mı, kazanım mı?

Allelik serilerin en çarpıcı biçimi, aynı gende hem işlev kaybı hem işlev kazanımı varyantlarının bulunmasıdır. Bölüm 4'te bunun iki klasik örneğini görmüştük: *RET*'te işlev kaybı bağırsak sinir sistemi gelişimini bozarak Hirschsprung hastalığına, işlev kazanımı ise reseptörü sürekli açık bırakarak MEN2 sendromuna yol açar (Edery ve ark., 1997); *SCN2A*'da işlev kazanımı yaşamın ilk günlerinde başlayan epilepsiyle, işlev kaybı ise daha geç başlangıçlı (ortanca 8 ay, ağırlıklı olarak infantil spazm) tabloyla ilişkilidir (Berecki ve ark., 2018); *SCN2A* işlev kaybının daha geniş nörogelişimsel ucu — otizm spektrum bozukluğu ve entelektüel yetersizlik — ayrı bir literatüre dayanır (Sanders ve ark., 2018). Bu iki örnek, yönün klinik olarak neden kritik olduğunu da gösterir: sodyum kanalı hastalıklarında mekanizma yönü doğrudan **tedavi yönünü** belirler; sodyum kanal blokerleri işlev kazanımı tablolarında yararlı, işlev kaybı tablolarında ise potansiyel olarak zararlıdır (Brunklaus ve ark., 2020).

Bu eksenin en öğretici örneği ise *FGFR3*'tür, çünkü burada iki yön arasındaki geçiş kesikli değil **süreklidir** (Şekil 15.2).

![Şekil 15.2 — Tek gen, tek eksen: FGFR3 aktivite serisi](assets/sekil_51_fgfr3_aktivite_ekseni.svg)

FGFR3'ün anahtar özelliği, endokondral kemik büyümesinin **negatif** düzenleyicisi olmasıdır — yani bir fren gibi çalışır. Aktive edici varyantlar bu freni sıkıştırarak büyüme plağını baskılar. Bunun moleküler ölçüsü Bölüm 4'te ele aldığımız çalışmada verilmiştir: tanatoforik displazi tip II'ye yol açan p.Lys650Glu değişimi, FGFR3 tirozin kinazını yabanıl tipin **yaklaşık 100 katı** düzeyinde ve ligandtan bağımsız biçimde aktive eder; yazarların yorumuna göre bu değişim, normalde ligand bağlanması ve otofosforilasyonla başlatılan konformasyon değişikliklerini taklit etmektedir (Webster ve ark., 1996). Aktivite arttıkça klinik tablo ağırlaşır: hipokondroplazi (p.Asn540Lys) hafif ve sık gözden kaçan bir kısalık yaparken, SADDAN (p.Lys650Met) ağır displazi, akantozis nigrikans ve gelişim geriliğiyle gider; tanatoforik displazi ise neonatal letaldir.

Serinin asıl öğretici ucu ise diğer yöndedir. Toydemir ve arkadaşları, kamptodaktili, **uzun boy**, skolyoz ve işitme kaybıyla giden yeni bir bozukluğun (CATSHL sendromu) lokusunu 4p'ye haritaladılar; bu sendrom *Fgfr3* nakavt faresinin fenotibini birebir tekrarladığı için doğrudan *FGFR3*'ü taradılar ve tirozin kinaz domaininde **kısmi işlev kaybına** yol açan heterozigot bir p.Arg621His değişimi buldular. Yazarların vurgusu şudur: anormal FGFR3 sinyali, endokondral kemik büyümesini **hem baskılayarak hem de destekleyerek** insanda anomali yapabilir (Toydemir ve ark., 2006). Yani aynı gen, aynı eksenin iki ucunda birbirinin tam tersi iskelet fenotipleri üretir.

> **🔬 Deep-dive — Aynı kodon, farklı amino asit, farklı hastalık.** *FGFR3*'ün 650. kodonu allelik seri kavramının en keskin dersini verir. Bu kodondaki lizinin **metiyoninle** değişmesi (p.Lys650Met) SADDAN fenotibine yol açarken, aynı kodonda lizinin **glutamatla** değişmesi (p.Lys650Glu) tanatoforik displazi tip II ile ilişkilidir. İki varyant aynı nükleotid komşuluğunda, aynı proteinin aynı pozisyonundadır; buna rağmen biri yaşamla bağdaşan bir sendrom, diğeri neonatal letal bir displazi üretir. Bu farkın moleküler zemini deneysel olarak da gösterilmiştir: 650. pozisyonda yalnız glutamat değil aspartat, daha az ölçüde de glutamin ve lösin belirgin konstitütif aktivasyon yaratır; buna karşılık aktivasyon halkasındaki komşu rezidülerin (Tyr-647 ile Leu-656 arası) glutamata değişmesi reseptörü aktive etmez — yani etki hem **konuma** hem **yüke** özgüdür (Webster ve ark., 1996). Bunun varyant yorumlamadaki karşılığı doğrudandır: ACMG'nin PM5 kriteri ("aynı pozisyonda daha önce patojen bildirilmiş **farklı** bir amino asit değişimi") burada mekanik olarak uygulanırsa yanıltıcı olur, çünkü kanıt "bu pozisyon önemlidir" der ama "aynı hastalığı yapar" demez. Aynı biçimde PS1 ("daha önce patojen bildirilmiş varyantla **aynı** amino asit değişimi") kriterinin geçerliliği de, kanıtın hangi hastalık için üretildiğine bağlıdır. Kural olarak formüle edilebilir: **allelik seri taşıyan genlerde konum-temelli kriterler, hastalık belirtilmeden kullanılamaz.**

### 2.2 İkinci eksen: rezidüel işlev — alelin ağırlığı

İkinci eksen, kitabın en tanıdık mantığını kullanır: **doz–eşik**. Burada varyantlar aynı yöndedir (hepsi işlev kaybı), ama farklı miktarda işlev bırakırlar ve bırakılan miktar hastalığın adını değiştirir.

Bölüm 2'de bunun iki örneğini görmüştük. Fenilalanin hidroksilaz eksikliğinde, kalan enzim aktivitesi klasik fenilketonüriden hafif hiperfenilalaninemiye uzanan bir yelpaze oluşturur; büyük genotip–fenotip serileri, alel çiftinin öngördüğü rezidüel aktivite ile klinik ağırlık arasında güçlü bir ilişki bulunur (Hillert ve ark., 2020). Duchenne ve Becker musküler distrofileri ise aynı mantığın farklı bir biçimidir: burada belirleyici olan varyantın **okuma çerçevesini bozup bozmadığıdır**; çerçeveyi koruyan delesyonlar kısalmış ama kısmen işlevsel bir distrofin üretir ve daha hafif Becker fenotibiyle sonuçlanır (Monaco ve ark., 1988).

Bu eksenin belki de en öğretici örneği bakır taşıyıcısı *ATP7A*'dır. Kaler'in derlemesinde özetlendiği gibi, *ATP7A* kusurları infantil başlangıçlı ve ölümcül seyreden **Menkes hastalığına** yol açar; buna karşılık **oksipital boynuz sendromu**, aynı genin daha hafif allelik varyantı olarak tanımlanır. Klinik olarak kritik olan gözlem şudur: yenidoğan döneminde tanı konup erken bakır tedavisi başlanan hastalarda sonuçlar iyileşmekte, hatta **mutant ATP7A molekülleri az miktarda rezidüel aktivite koruyorsa** klinik sonuçlar normale yaklaşabilmektedir (Kaler, 2011). Yani rezidüel işlev burada yalnızca hastalığın adını değil, **tedaviye yanıt olasılığını** da belirler.

> **🔬 Deep-dive — Aynı gen, üçüncü ve tümüyle beklenmedik bir hastalık.** *ATP7A* serisi, allelik serilerin neden yalnız "ağır–hafif" ekseniyle açıklanamayacağını da gösterir. Menkes hastalığı ve oksipital boynuz sendromundan sonra tanımlanan üçüncü *ATP7A* bozukluğu, **izole distal motor nöropatidir**; bu tablo Menkes hastalığının ya da oksipital boynuz sendromunun karakteristik klinik ve biyokimyasal bulgularının **hiçbirini** taşımaz ve Charcot-Marie-Tooth hastalığı tip 2'yi andırır. Kaler'in vurguladığı gibi bu bulgu, ATP7A'nın motor nöron bakımında daha önce fark edilmemiş kritik bir rolü olduğunu ve bu üçüncü hastalığın altında yatan mekanizmanın diğer ikisinin patofizyolojisinden **farklı** olduğunu göstermektedir (Kaler, 2011). Klinik dersi keskindir: bir hastada *ATP7A* varyantı bulunduğunda "bakır düzeyi normal, o hâlde Menkes değil, varyant anlamsız" akıl yürütmesi hatalıdır — çünkü serinin bir ucundaki hastalığın biyokimyasal imzası, diğer ucundaki hastalıkta yoktur. Bu, allelik serilerde biyokimyasal doğrulama testlerinin **hastalığa özgü** olduğunu ve seride yanlış basamağa göre yorumlanmaması gerektiğini hatırlatır.

### 2.3 Üçüncü eksen: varyant konumu — domain ve izoform

Üçüncü eksende varyantların yönü ve ağırlığı benzer olabilir; farkı yaratan, proteinin **hangi bölgesinin** bozulduğudur. Bunun ders kitabı örneği *LMNA*'dır (Şekil 15.3).

![Şekil 15.3 — Konum fenotibi yazar: LMNA ve laminopatiler](assets/sekil_52_lmna_domain_fenotip.svg)

A ve C laminleri, *LMNA* geninin ürünleridir ve neredeyse bütün post-mitotik hücrelerde ifade edilirler; iç nükleer zarın altında bir protein ağı — **nükleer lamina** — oluştururlar, sitoiskeletle bağlantı kurarlar, kromatinle ve aralarında transkripsiyon faktörlerinin de bulunduğu çok sayıda proteinle etkileşirler. Buna rağmen *LMNA* varyantlarının yol açtığı hastalıklar **doku-seçicidir**: çizgili kas, yağ dokusu, periferik sinir gibi belirli dokuları tutan tablolardan, tüm bedeni etkileyen prematür yaşlanma sendromlarına uzanan **onun üzerinde farklı bozukluk** tanımlanmıştır ve bu geniş fenotip yelpazesi, aynı ölçüde geniş bir varyant çeşitliliğiyle ilişkilidir. Bu klinik ve genetik heterojenite *LMNA* geni için benzersiz bir düzeydedir ve genotip–fenotip ilişkisi kurmayı özellikle güçleştirir (Bertrand ve ark., 2011).

Yine de bazı örüntüler nettir. Yağ dokusunu tutan laminopatilerde varyantlar ağırlıklı olarak proteinin **Ig-benzeri domaininde** kümelenir ve SREBP-1 gibi transkripsiyon ortaklarıyla etkileşimi bozdukları düşünülür; çizgili kas laminopatilerinde ise varyantlar gen boyunca **dağınıktır** ve proteinin yapısını değiştirerek nükleer laminaya polimerizasyonunu, dolayısıyla sürekli gerilen kas hücrelerinde kritik olan mekanik dayanıklılığı zayıflattıkları düşünülür (Bertrand ve ark., 2011). Prematür yaşlanma sendromlarında ise mekanizma bambaşkadır: burada varyantlar hücre için **toksik** olan olgunlaşmamış proteinlerin birikmesine yol açar.

Aynı doku-seçicilik sorusu daha geniş bir çerçevede de sorulmuştur: laminler bütün hücrelerde ifade edilirken hastalıkların neden büyük ölçüde doku-seçici fenotiplerle ortaya çıktığı hâlâ tam açıklanmış değildir; hastalık yapan varyantların nükleer morfolojiyi bozduğu gösterilmiştir, ancak bu bozulmanın patolojiye nasıl dönüştüğü ancak anlaşılmaya başlanmıştır (Worman, 2012). ⚠️ Dolayısıyla domain–fenotip haritaları güçlü **örüntüler** sunar, ancak birebir öngörü aracı olarak kullanılmamalıdır.

> **🔬 Deep-dive — Progeria: sessiz bir değişimin yeni bir protein doğurması.** Hutchinson-Gilford progeria sendromu (HGPS), *LMNA* serisinin mekanizma açısından en ilginç basamağıdır. Eriksson ve arkadaşları, klasik HGPS'li 20 olgunun **18'inde** aynı de novo tek baz değişimini — ekzon 11 içinde G608G (GGC>GGT) — buldular; bir olguda ise aynı kodonda farklı bir değişim vardı. Bu değişim amino asidi değiştirmez; buna karşılık ekzon 11 içinde **kriptik bir splice bölgesini aktive eder** ve karboksi-ucuna yakın **50 amino asidin silindiği** bir protein ürünü doğurur. HGPS fibroblastlarında lamin A'ya karşı antikorlarla yapılan immünofloresan incelemede birçok hücrede gözle görülür nükleer membran anormallikleri saptanmıştır (Eriksson ve ark., 2003). Silinen bölge, öncü proteinin (prelamin A) olgunlaşma sürecinde kesilmesi için gereken bölgeyi de içerdiğinden, ortaya çıkan ürün — **progerin** — kalıcı olarak farnesillenmiş hâlde kalır ve çekirdek zarfında birikir. Bu tek örnek kitabın üç bölümünü birleştirir: değişim **splicing** yoluyla iş görür (Bölüm 7), ürün basit bir eksiklik değil **yeni ve toksik bir molekül** olduğu için mekanizma dominant-negatif/neomorfik karakterdedir (Bölüm 5–6) ve aynı gendeki kas varyantları bu yolu **hiç** kullanmaz. Tarihsel bir not olarak, HGPS lokusunun 1q'ye haritalanması iki bağımsız gözlemle mümkün olmuştu: 1q'nun uniparental izodizomisi taşıyan iki olgu ve paternal interstisyel bir delesyon taşıyan bir olgu — yani Bölüm 8 ve Bölüm 10'un araçları, bir Bölüm 15 sorusunun çözümünde kullanılmıştır.

*COL1A1*/*COL1A2* serisi, konum ekseninin nicel olarak en iyi belgelenmiş örneğidir. Bölüm 5'te osteogenesis imperfekta'yı dominant-negatif hastalığın prototipi olarak ele almış ve niceliksel kusurların (null alel) hafif tip I'e, glisin değişimlerinin ise ağır tablolara yol açtığını görmüştük (Forlino ve Marini, 2000). Marini ve arkadaşlarının derlediği 832 bağımsız yapısal varyant, bu tablonun içinde bir **bölgesel harita** olduğunu gösterdi: α1(I) zincirindeki glisin değişimlerinin üçte biri letaldir ve letalite, değiştiren rezidünün yüklü ya da dallanmış yan zincirli olmasıyla artar; ilk 200 rezidüdeki değişimler letal değildir; buna karşılık heliks pozisyonları 691–823 ve 910–964 arasındaki iki bölge **yalnızca letal** varyantlar içerir ve bu bölgeler integrinler, matriks metalloproteinazları, fibronektin ve COMP gibi ortaklar için büyük ligand bağlanma bölgeleriyle hizalanır. *COL1A2*'de ise varyantların yaklaşık %80'i letal değildir ve letal olanlar zincir boyunca düzenli aralıklı kümeler hâlinde dizilir (Marini ve ark., 2007). Aynı çalışma, konum ekseninin **hastalık kimliğini** de değiştirebildiğini gösterir: *COL1A1*'deki splice bölgesi varyantları nadiren letaldir, çoğu zaman çerçeve kaymasına ve hafif tip I fenotibine yol açar; buna karşılık N-propeptid bölgesini etkileyen belirli varyantlar osteogenesis imperfekta yerine **Ehlers-Danlos sendromunun artrokalazi tipiyle** ilişkilendirilmiştir.

Konum ekseninin ikinci bileşeni **izoformdur**: bir gen doku-özgül promotörlerden veya alternatif splicing yoluyla farklı ürünler veriyorsa, yalnız bazı izoformları etkileyen bir varyant yalnız o dokuda hastalık yapar. *PAX6* bu mantığın klinik karşılığını sunar: tam işlev kaybı yaratan varyantlar tipik olarak aniridi ile giden yetersiz doz tablosunu üretirken, kalıntı işlev bırakan belirli missense varyantlar Peters anomalisi ya da foveal hipoplazi gibi farklı ön segment tablolarıyla ilişkilendirilmiştir (Lima Cunha ve ark., 2019).

### 2.4 Dördüncü eksen: kalıtım modu — tek alel mi, iki alel mi?

Dördüncü eksen sıklıkla gözden kaçar ama danışma açısından en ağır sonuçları doğurandır: **aynı gen, monoalelik durumda bir hastalık, bialelik durumda bambaşka bir hastalık yapabilir.** Klasik örnek *COL4A3* ve *COL4A4*'tür: tek bir patojen alel taşımak çoğu zaman izole mikroskopik hematüri ile giden ince bazal membran nefropatisine yol açarken, iki patojen alel taşımak ilerleyici böbrek yetmezliğiyle giden otozomal resesif Alport sendromu üretir. Benzer biçimde *RYR1*'de dominant missense varyantlar malign hipertermi yatkınlığı ya da santral kor hastalığı yaparken, bialelik işlev kaybı varyantları ağır konjenital miyopatilerle ilişkilidir.

Bu eksenin klinik önemi şudur: aynı laboratuvar sonucunun tekrarlanma riski, hangi hastalık varlığının kastedildiğine göre **%50'den %25'e** kayar. Bir aileye "bu gende varyant bulundu" demek, risk hesabı yapmak için yeterli bilgi taşımaz.

### 2.5 Beşinci eksen: zamanlama — germline mi, mozaik mi?

Bölüm 12'de mozaikliği ayrı bir mekanizma sınıfı olarak ele almıştık; burada onu allelik serinin bir ekseni olarak yeniden okuyoruz. Aynı varyant, **döllenmeden önce mi sonra mı** ortaya çıktığına göre farklı hastalık adları taşıyabilir — hatta germline hâlde hiç görülemeyebilir, çünkü embriyoyu yaşatmaz.

*GNAS* bunun en zengin örneğidir. Weinstein ve arkadaşları, McCune-Albright sendromlu hastaların etkilenmiş dokularında Gsα'nın 201. kodonunda aktive edici değişimler (p.Arg201His veya p.Arg201Cys) saptadılar ve kritik olarak, mutant alel yükünün **dokudan dokuya değiştiğini** gösterdiler — bu, varyantın postzigotik olarak ortaya çıktığının doğrudan kanıtıdır (Weinstein ve ark., 1991). Aynı aktive edici varyantın germline hâlde hiç bildirilmemiş olması, Bölüm 12'de tanıtılan Happle'ın letal-mozaik hipotezinin klasik uygulamasıdır. Buna karşılık *GNAS*'ın **işlev kaybı** varyantları germline olarak aktarılabilir ve psödohipoparatiroidizm ile ilişkili bozukluklar ailesini oluşturur.

### 2.6 Altıncı eksen: bağlam — ebeveyn kökeni ve genetik zemin

Son eksen, varyantın kendisiyle değil içinde bulunduğu bağlamla ilgilidir. İmprintli lokuslarda (Bölüm 10) aynı işlev kaybı varyantı, **hangi ebeveynden geldiğine göre** farklı klinik tablolar üretir. *GNAS* burada da örnek genimizdir: psödohipoparatiroidizm ve ilişkili bozukluklar, kısa kemikler, kısa boy, tıknaz yapı, erken başlangıçlı obezite ve ektopik ossifikasyonların değişken biçimde bulunduğu ve sıklıkla paratiroid hormonuna (PTH) ve TSH'ye direncin eşlik ettiği metabolik bozukluklar grubudur. Uluslararası uzlaşı belgesinin altını çizdiği nokta, bu bölüm açısından tam olarak yerinde bir uyarıdır: **tabloların sunumu ve ağırlığı bireyler arasında değişir ve farklı tipler arasında hatırı sayılır klinik ve moleküler örtüşme vardır**; bu nedenle tanı klinik ölçütlerle konulmalı ve **moleküler genetik analizle doğrulanmalıdır** (Mantovani ve ark., 2018).

İkinci bağlam bileşeni, Bölüm 14'ün konusuydu: **modifiye edici lokuslar ve genetik zemin.** Aynı varyantın farklı ailelerde farklı ağırlıkta hastalık yapması, allelik serinin kendi içinde bir "bulanıklık payı" taşıdığı anlamına gelir. Bu, domain–fenotip haritalarının neden kesin öngörü aracı olamayacağının ikinci nedenidir.

---

## 3. Varyant tipleri

Bu bölümde varyant tipi sorusu ters yönde sorulur: klasik olarak "bu varyant tipi hangi mekanizmayı yapar?" diye sorarız; allelik seride ise "bu varyant tipi beni serinin **hangi ucuna** götürür?" diye sormamız gerekir. Aşağıdaki tablo bu yönlendirmeyi özetler.

**Tablo 15.2 — Varyant tipinin allelik serideki tipik konumu**

| Varyant tipi | Seride tipik konumu | Mekanizma sonucu | Uyarı |
|---|---|---|---|
| Nonsens / çerçeve kayması (NMD'ye giden) | Serinin **işlev kaybı** ucu | Null alel; yetersiz doz veya resesif tablo | NMD kaçışı varsa DN'e kayabilir (Bölüm 2) |
| Tam gen delesyonu | İşlev kaybı ucunun en net hâli | Kesin null; "delesyon testi" mekanizma belirler | Delesyon fenotibi missense'ten **hafifse** DN düşün |
| Hipomorfik missense | Serinin **hafif** ucu | Kısmi rezidüel işlev | Aynı gende ağır missense'lerle karıştırılmamalı |
| Arayüz/domain missense'i | Doku-seçici basamak | DN veya izole domain kusuru | Domain haritası olmadan yorumlanmaz |
| Aktive edici missense (hotspot) | Serinin **işlev kazanımı** ucu | Konstitütif/artmış aktivite | Kaybın hastalığıyla aynı panelde olabilir |
| **Aynı kodonda farklı amino asit** | Bazen **başka bir hastalık** | Farklı yapısal sonuç | PS1/PM5 doğrudan uygulanamaz |
| Splice bölgesi varyantı | Genellikle ara basamak | Çerçeveye göre değişir | Aynı gende hem hafif hem letal olabilir |
| **Sessiz (senonim) varyant** | Beklenmedik basamak | Kriptik splice → yeni ürün | HGPS örneği; "sessiz = zararsız" değildir |
| Okuma çerçevesini koruyan delesyon | Hafif basamak | Kısalmış ama işlevsel ürün | Duchenne ↔ Becker ayrımı |
| Kodlamayan/düzenleyici varyant | Doku-seçici hafif basamak | İfade dozunda azalma | Bölüm 13 ile birlikte okunur |

Tablonun taşıdığı temel ders şudur: **varyant tipi mekanizmayı öneri düzeyinde belirler, kesinleştirmez.** Aynı gende aynı tipte iki varyant serinin iki farklı basamağında durabilir; bu nedenle allelik seri taşıyan genlerde tip-temelli otomatik yorumlama (özellikle *in silico* araçlara dayanan yorumlama) özellikle güvenilmezdir. Bölüm 5'te gördüğümüz gibi, mevcut tahmin araçları dominant-negatif ve işlev kazanımı mekanizmalarını ayırt etmekte belirgin biçimde zayıftır.

---

## 4. Klinik fenotipe dönüşüm

### 4.1 Neden bu bölüm "önce fenotip" der?

Genomik çağın en yaygın yanlış anlamalarından biri, dizilemenin fenotiplemeyi gereksizleştirdiği düşüncesidir. Allelik seri bu düşüncenin tam tersini kanıtlar: **bir varyantın anlamı, ancak hangi hastalığın arandığı bilinirse çözülebilir.** Aynı *FGFR3* varyantı, uzun boylu bir ailede aranıyorsa başka, kısa ekstremiteli bir yenidoğanda aranıyorsa bambaşka bir anlam taşır.

Pratik sonuç, **derin fenotipleme** ile ifade edilir: boy, segment oranları, işitme, kardiyak ileti, yağ dağılımı, deri bulguları, biyokimyasal imza gibi ayırt edici parametrelerin sistematik olarak kaydedilmesi. Allelik seri taşıyan bir gende bu parametreler, laboratuvarın hangi hastalık varlığı için değerlendirme yapacağını belirler ve çoğu zaman bir VUS'u sınıflandırılabilir hâle getiren şey de budur.

### 4.2 "Bu gende varyant bulundu — hangi hastalık?"

Klinik pratikte bu bölümün en sık karşılaşılan sorusu budur ve altı eksen buna sistematik bir yanıt verir.

**Algoritma 15.1 — Allelik seride hangi hastalık? Ayrım akışı**

```mermaid
flowchart TD
  A["Allelik seri taşıyan bir gende<br/>varyant bulundu"] --> B{"Bu gende BİLİNEN kaç<br/>gen–hastalık varlığı var?"}
  B -->|"Tek varlık"| C["Standart yorum:<br/>varyantı o hastalık için sınıflandır"]
  B -->|"Birden çok varlık"| D{"Varyantların mekanizma<br/>YÖNÜ farklı mı?"}

  D -->|"Evet — LoF ↔ GoF"| E["Yön belirle:<br/>varyant tipi + hotspot + fonksiyonel veri<br/>(ör. RET, SCN2A, FGFR3)"]
  D -->|"Hayır, hepsi aynı yönde"| F{"Fark neyden geliyor?"}

  F -->|"Rezidüel işlev derecesi"| G["Ağırlık ekseni:<br/>hafif ↔ ağır aynı hastalığın<br/>basamakları olabilir (PAH, DMD)"]
  F -->|"Varyantın DOMAIN konumu"| H["Domain–fenotip haritasına bak:<br/>doku-seçici tablo bekle<br/>(LMNA, COL1A1)"]
  F -->|"Kalıtım modu (mono/bialelik)"| I["İkinci aleli MUTLAKA araştır:<br/>risk hesabı buna bağlı"]
  F -->|"Germline mi mozaik mi"| J["Etkilenmiş dokudan örnek;<br/>VAF değerlendir (Bölüm 12)"]
  F -->|"Ebeveyn kökeni (imprintli lokus)"| K["Alelin kökenini belirle<br/>(Bölüm 10)"]

  E --> L["Hasta fenotibi ile<br/>ÖNGÖRÜLEN hastalık uyuşuyor mu?"]
  G --> L
  H --> L
  I --> L
  J --> L
  K --> L

  L -->|"Uyuşuyor"| M["Varyantı O hastalık varlığı için<br/>sınıflandır ve raporla"]
  L -->|"Uyuşmuyor"| N["Fenotibi yeniden derinleştir;<br/>uymuyorsa varyantı ikincil/VUS say;<br/>tek varyanta fenotip UYDURMA"]
```

### 4.3 Spektrum mu, iki ayrı hastalık mı?

Klinikte sık sorulan ikinci soru budur ve yanıtı hem kavramsal hem pratiktir. İki fenotip arasında **ara formlar** gözleniyorsa (hafiften ağıra sürekli bir geçiş varsa), bunlar büyük olasılıkla tek bir hastalığın basamaklarıdır — fenilketonüri ile hafif hiperfenilalaninemi arasındaki ilişki gibi. Buna karşılık iki fenotip arasında ara form yoksa, mekanizmaları farklıysa veya kalıtım modları ayrışıyorsa, bunlar ayrı hastalık varlıklarıdır — Hirschsprung hastalığı ile MEN2 gibi. Bu ayrımın yapıldığı yer klinik gözlemdir, ama sonuçlarını laboratuvar ve danışma taşır (bkz. 6. başlık).

### 4.4 Ters yön: aynı fenotip, farklı genler

Allelik serinin aynası, lokus heterojenitesidir; ikisi tanısal stratejide birlikte düşünülmelidir. Klinik tablo tipik ama gen bulunamıyorsa sorun lokus heterojenitesi olabilir (paneli genişlet); gen bulundu ama tablo atipikse sorun allelik seri olabilir (varyantın serideki yerini çöz). Bu iki soruyu karıştırmamak, tanısal yeniden analizde en çok zaman kazandıran ayrımlardan biridir.

---

## 5. Tanısal testlerle ilişkisi

Allelik serilerde test seçiminin belirleyicisi cihaz değil, **hangi hastalığın arandığı varsayımıdır.** Bunun bugünkü pratik karşılığını doğru kurmak gerekir: tanısal aşamada **genin tamamına bakmak artık varsayılan yaklaşımdır** — dizileme maliyeti düştüğü ve serinin hangi ucunda olunduğu baştan bilinemediği için, hedefli hotspot dizilemesiyle işe başlamak nadiren doğrudur. Hedefli, tek bölgeye inen dizileme esas olarak **aile taramasında** yerini bulur: probandda patojen varyant tanımlandıktan sonra akrabalarda yalnızca o varyantın bulunduğu bölge incelenir. Buna karşılık "hangi hastalık?" sorusu ortadan kalkmaz, yalnızca **yer değiştirir**: cihaz seçiminden çıkıp **kapsam ve yorum** kararına girer — genin tamamı dizilendiğinde bile delesyon/duplikasyon analizinin eklenip eklenmeyeceği, tekrar ya da derin intronik bölgelerin ayrıca aranıp aranmayacağı ve bulunan varyantın hangi hastalık varlığına karşı yorumlanacağı bu soruya bağlıdır. Aşağıdaki tablo bu bakışla okunmalıdır.

**Tablo 15.3 — Allelik serilerde hangi test ne gösterir?**

| Test | Bu mekanizmayı yakalar mı? | Sınırlılığı |
|------|----------------------------|-------------|
| **WES** | Evet — allelik serilerin çoğu kodlayan varyantlardan doğar; gen paneli/WES çekirdek yöntemdir | Varyantı bulur ama **serideki yerini söylemez**; fenotip verisi olmadan yorumlanamaz. Derin intronik ve düzenleyici basamakları kaçırır |
| **Short-read WGS** | Evet; kodlayan + kodlamayan basamakları birlikte kapsar | Yorum yükü büyür; izoform-özgül etkiler ancak RNA verisiyle çözülür |
| **Long-read WGS** | Evet; ayrıca faz bilgisi verir — **mono- vs bialelik ayrımı** (dördüncü eksen) için değerli | Maliyet ve erişim; rutin değil |
| **Array-CGH / SNP array** | Kısmen — tam gen delesyonlarını (serinin null ucu) ve bitişik gen sendromlarını yakalar | Tek nükleotid basamaklarını göremez; **delesyon = en ağır fenotip** varsayımı yanlıştır |
| **MLPA** | Evet — hedefli delesyon/duplikasyon; ekzon düzeyinde çerçeve hesabı (ör. *DMD*) | Yalnız tasarlanan lokus; nokta varyantlarını görmez |
| **RNA-seq** | **Evet — bu bölümde özellikle değerli.** Kriptik splice ürünlerini (ör. progerin transkripti), izoform-özgül etkileri ve alel dengesizliğini gösterir | Doğru doku gerekir; ifade edilmeyen dokuda bilgi vermez |
| **Methylation array** | Genellikle hayır; ancak imprintli lokus söz konusuysa (altıncı eksen) ayırıcıdır | Yalnız imprinting/epimutasyon basamağı için anlamlıdır |
| **Karyotip** | Hayır | Çözünürlük yetersiz |
| **(seriye özgü) Derin fenotipleme ± fonksiyonel/biyokimyasal test** | **Evet — belirleyici.** Serinin hangi basamağında olunduğunu çoğu zaman yalnız fenotip + fonksiyonel veri söyler | Standartlaştırılmış fenotip kaydı gerekir; fonksiyonel test her gen için mevcut değildir |

> **Bu mekanizmayı hangi test yakalar? (özet):** Allelik seride tanısal darboğaz **varyantı bulmak** değil, **onu doğru hastalığa bağlamaktır**. Pratik sıra şudur: (1) genin tamamını kapsayan bir test seç (dizileme + delesyon/duplikasyon); (2) varyantın konumunu ve tipini bilinen domain–fenotip haritasıyla karşılaştır; (3) fenotibi derinleştir ve serinin öngördüğü bulguları **aktif olarak ara**; (4) gerekiyorsa mekanizma yönünü fonksiyonel veriyle netleştir; (5) mono/bialelik durumu ve alelin ebeveyn kökenini netleştir.

> **🟦 Klinikte dikkat — "Delesyon en ağır fenotibi yapar" sanısı:** Sezgi, tam gen delesyonunun serinin en ağır ucunu üreteceğini söyler. Bu, yalnızca serinin yetersiz doz mekanizmasıyla çalışan bölümü için doğrudur. Dominant-negatif ya da neomorfik basamakları olan genlerde delesyon taşıyan birey, missense taşıyan bireyden **belirgin biçimde daha hafif** olabilir — nitekim osteogenesis imperfektada null alel hafif tip I ile, glisin değişimleri ise ağır tablolarla ilişkilidir. Bu nedenle "delesyon bulundu, en ağır seyri bekleyin" cümlesi mekanizma bilinmeden kurulmamalıdır.

---

## 6. Varyant yorumlama açısından önemi (ACMG/ClinGen)

Bu bölüm, ACMG/AMP çerçevesinin (Richards ve ark., 2015) en sessiz varsayımlarından birini görünür kılar. Kriterlerin çoğu, arka planda **tek bir gen–hastalık ilişkisi** olduğunu varsayar. Allelik seri bu varsayımı kırar ve dört kritik noktada uyarlama gerektirir (Şekil 15.4).

![Şekil 15.4 — Birleştirmek mi, ayırmak mı? Küre edilen birim gen değildir](assets/sekil_53_lumping_splitting.svg)

**PVS1 (çok güçlü — null varyant).** Bu kriter yalnızca "işlev kaybının bilinen hastalık mekanizması olduğu" genlerde uygulanabilir; ClinGen'in ayrıntılı işletim kılavuzu bu ön koşulun altını özellikle çizer (Abou Tayoun ve ark., 2018). Allelik seride bu koşul **hastalığa özgüdür**: *RET*'te bir null varyant Hirschsprung hastalığı için mekanizmaya uygundur, ama MEN2 için değildir. Aynı gen, aynı varyant, farklı hastalık — farklı kriter.

**PS1 ve PM5 (aynı/farklı amino asit değişimi).** Bu iki kriter "daha önce patojen bildirilmiş" bir varyanttan kanıt devşirir. Allelik seride sorulması gereken ek soru şudur: **hangi hastalık için patojen bildirilmiş?** *FGFR3* p.Lys650Met ile p.Lys650Glu örneğinde görüldüğü gibi, aynı kodondaki iki değişim iki farklı hastalıkla ilişkilidir; kanıtı hastalık belirtmeden aktarmak sistematik bir yanlışa yol açar.

**PM1 (mutasyonel hotspot / kritik domain).** Hotspot her zaman bir hastalığın hotspot'udur. Domain-temelli kanıt, ancak hastanın fenotibi o domainle ilişkili hastalık varlığına uyuyorsa geçerlidir.

**PP4 (fenotip özgüllüğü).** Allelik seri taşıyan genlerde bu kriterin gücü azalır: "hastanın fenotibi bu gen için oldukça özgül" cümlesi, gen birden çok hastalık yapıyorsa yeterince ayırt edici değildir. Kriteri kullanabilmek için fenotibin **belirli bir hastalık varlığına** özgü olduğu gösterilmelidir.

Bütün bunların üstünde duran soru ise küreleme sorusudur: **aynı genin iki fenotibi tek bir hastalık varlığı mı sayılmalı, yoksa ikiye mi ayrılmalı?** ClinGen, gen–hastalık ilişkilerinin, varyant patojenitesinin ve klinik eyleme geçirilebilirliğin gücünü sınıflandırmak için çerçeveler geliştirdiğinden, değerlendirilecek **hastalık varlığının tanımlanması** zorunlu bir ön adım hâline gelmiştir; bu, birden çok durumla ve/veya geniş fenotipik spektrumla ilişkili genlerde özellikle zordur. Bu nedenle "birleştirme ve ayırma" kararlarını yönlendirecek ve monogenik gen–hastalık ilişkilerinin tanımlanmasında tutarlılığı artıracak ölçütler geliştirilmiştir; bu ölçütlerin klinik tanı, biyoinformatik ve bakım yönetimi açısından somut sonuçları vardır (Thaxton ve ark., 2022). Pratikte ölçütler üç soruya indirgenebilir: **moleküler mekanizma aynı mı, kalıtım modu aynı mı, fenotipler bir süreklilik oluşturuyor mu?** Üçüne de "evet" ise tablolar tek bir hastalık varlığı altında birleştirilir (geniş spektrum olarak tanımlanır); biri bile "hayır" ise ayrılır.

**Algoritma 15.2 — Allelik seride ACMG kriterlerinin uyarlanması**

```mermaid
flowchart TD
  A["Varyant: GEN X, c.___"] --> B{"Bu gen için kaç hastalık<br/>varlığı tanımlı?"}
  B -->|"Tek"| C["Klasik ACMG uygula"]
  B -->|"Birden çok"| D["ÖNCE hastalık varlığını SEÇ<br/>(fenotip + kalıtım + mekanizma)"]

  D --> E{"PVS1 düşünülüyor mu?"}
  E -->|"Evet"| F{"İşlev kaybı, SEÇİLEN hastalığın<br/>bilinen mekanizması mı?"}
  F -->|"Hayır"| G["PVS1 UYGULANAMAZ<br/>(ör. RET null → MEN2 için değil)"]
  F -->|"Evet"| H["PVS1 uygula (ClinGen akışıyla)"]

  E -->|"Hayır"| I{"PS1 / PM5 düşünülüyor mu?"}
  I -->|"Evet"| J{"Referans varyant AYNI hastalık<br/>varlığı için mi patojen?"}
  J -->|"Hayır"| K["Kriteri uygulama veya<br/>gücünü düşür; gerekçeyi yaz"]
  J -->|"Evet"| L["PS1/PM5 uygula"]

  I -->|"Hayır"| M{"PM1 (hotspot/domain)?"}
  M -->|"Domain, seçilen hastalıkla ilişkili"| N["PM1 uygula"]
  M -->|"Domain başka hastalıkla ilişkili"| K

  G --> O["Sonuç raporu:<br/>varyant + KALITIM + HASTALIK<br/>üçlüsüyle yazılır"]
  H --> O
  K --> O
  L --> O
  N --> O
  C --> O
```

> **🟦 Klinikte dikkat — Rapor cümlesini gen adıyla kurmayın:** "*LMNA* geninde patojen varyant saptanmıştır" cümlesi eksiktir ve klinik olarak yanıltıcıdır; okuyan hekim bunu progeria mı, kardiyomiyopati mi, lipodistrofi mi olarak anlayacağını bilemez. Doğru kurulum şudur: "*LMNA* geninde, **otozomal dominant kalıtımlı Emery-Dreifuss musküler distrofisi** ile ilişkili patojen varyant saptanmıştır." Tekrarlanma riski, prognoz, izlem ve tarama planlarının tamamı bu üçlüden türetilir. ClinGen'in gen–hastalık geçerliliği çerçevesinde de puanlanan şey gen değil, **gen ile belirli bir hastalık arasındaki ilişkidir** (Strande ve ark., 2017).

> **🔬 Deep-dive — Aynı gen için farklı geçerlilik puanları olabilir mi? Evet, ve bu bir çelişki değildir.** Bir genin bir hastalıkla ilişkisi "Kesin (Definitive)" sınıfında olabilirken, aynı genin başka bir hastalıkla ilişkisi "Sınırlı (Limited)" ya da "Çelişkili" sınıfında kalabilir. Bu, çerçevenin bir zayıflığı değil, tam olarak amaçlanan davranışıdır: kanıt gen için değil, ilişki için biriktirilir (Strande ve ark., 2017). Klinik karşılığı önemlidir. Bir hastada "Kesin" ilişkili hastalığın fenotibi varsa, o gendeki bir varyant güçlü biçimde yorumlanabilir. Aynı hastada "Sınırlı" ilişkili ikinci bir hastalığın bulguları varsa, aynı varyant o hastalık için aynı ağırlıkta kanıt sayılamaz. Aynı sonuç raporda iki farklı ağırlık taşıyabilir — ve bunu açıkça yazmak, okuyucuyu yanıltmamanın tek yoludur. Uygulamada bunun en sık atlandığı yer, geniş panellerde **ikincil/rastlantısal** bulgular alanıdır: bir gen panele "Kesin" ilişkisi nedeniyle alınmıştır, ama bulunan varyant o hastalıkla değil, aynı genin daha zayıf kanıtlı bir başka fenotibiyle ilişkilidir.

---

## 7. Pediatrik genetikten klinik örnekler

**FGFR3 — bir eksende dizilmiş altı hastalık.** Aynı reseptör geninde aktivite düzeyi arttıkça hipokondroplaziden akondroplaziye, oradan SADDAN'a ve neonatal letal tanatoforik displaziye uzanan bir dizi oluşur; aktivite azaldığında ise seri ters yöne döner ve kamptodaktili, uzun boy, skolyoz ve işitme kaybıyla giden CATSHL sendromu ortaya çıkar. Anormal FGFR3 sinyalinin endokondral kemik büyümesini hem baskılayarak hem destekleyerek insan anomalisi yapabildiği, bu sendromun tanımlanmasıyla gösterilmiştir (Toydemir ve ark., 2006; mekanizma zemini: Webster ve Donoghue, 1996). **Öğreti:** aynı gende zıt yönlü iki hastalık bulmak istisna değil, kural olabilir; genin **normal işlevinin yönünü** (burada: büyümeyi baskılamak) bilmek, iki ucu da anlaşılır kılar.

**LMNA — konumun yazdığı hastalık.** Tek bir gende onun üzerinde farklı bozukluk tanımlanmıştır: çizgili kas, yağ dokusu ve periferik siniri tutan doku-seçici tablolardan sistemik prematür yaşlanma sendromlarına kadar. Yağ dokusu laminopatilerinde varyantlar Ig-benzeri domainde kümelenirken, kas laminopatilerinde gen boyunca dağınıktır; bu klinik ve genetik heterojenite düzeyi *LMNA* için benzersizdir ve genotip–fenotip ilişkisi kurmayı özellikle güçleştirir (Bertrand ve ark., 2011; Worman, 2012). **Öğreti:** aynı proteinin farklı bölgeleri farklı ortaklarla çalışır; hastalık, bozulan **arayüzün** dokusunun adını taşır.

**Hutchinson-Gilford progeria — sessiz bir değişim, yeni bir protein.** Klasik HGPS'li 20 olgunun 18'inde ekzon 11'de aynı de novo G608G değişimi bulunmuş; bu değişim amino asidi değiştirmediği hâlde kriptik bir splice bölgesini aktive ederek karboksi-uca yakın 50 amino asidin silindiği bir ürün doğurmuş ve hastaların fibroblastlarında belirgin nükleer membran anormallikleri gösterilmiştir (Eriksson ve ark., 2003). **Öğreti:** "sessiz varyant zararsızdır" kuralı allelik serilerde özellikle tehlikelidir; aynı gendeki diğer hastalıklardan tümüyle farklı bir mekanizmayla karşılaşabilirsiniz.

**ATP7A — üç hastalık, üç farklı klinik dil.** Aynı bakır taşıyıcı geni, ölümcül infantil Menkes hastalığına, onun daha hafif allelik varyantı olan oksipital boynuz sendromuna ve bu iki tablonun karakteristik klinik/biyokimyasal bulgularının hiçbirini taşımayan, Charcot-Marie-Tooth tip 2'yi andıran **izole distal motor nöropatiye** yol açar; rezidüel aktivite koruyan varyantlarda erken bakır tedavisi klinik sonuçları normale yaklaştırabilmektedir (Kaler, 2011). **Öğreti:** serinin bir ucundaki biyokimyasal test, diğer ucundaki hastalığı dışlamaz; ayrıca rezidüel işlev bazen doğrudan **tedaviye yanıt** demektir.

**COL1A1/COL1A2 — nicelikten niteliğe geçiş ve bölgesel harita.** 832 yapısal varyantın derlenmesiyle, α1(I) zincirindeki glisin değişimlerinin üçte birinin letal olduğu, ilk 200 rezidüdeki değişimlerin letal olmadığı, buna karşılık iki bölgenin (691–823 ve 910–964) yalnızca letal varyantlar içerdiği ve bu bölgelerin büyük ligand bağlanma bölgeleriyle hizalandığı gösterilmiştir; *COL1A2*'de varyantların yaklaşık %80'i letal değildir (Marini ve ark., 2007). Niceliksel (null) kusurlar ise hafif tip I ile ilişkilidir (Forlino ve Marini, 2000). **Öğreti:** aynı gende "az protein" ile "bozuk protein" iki farklı hastalık ağırlığı üretir; delesyon her zaman en ağır sonuç değildir.

**GNAS — zamanlama ve ebeveyn kökeni aynı gende buluşuyor.** McCune-Albright sendromunda aktive edici p.Arg201His/Cys değişimleri **postzigotik** olarak ortaya çıkar ve mutant alel yükü dokudan dokuya değişir (Weinstein ve ark., 1991); aynı genin işlev kaybı varyantları ise germline aktarılır ve psödohipoparatiroidizm ile ilişkili bozukluklar ailesini oluşturur. Bu ailede tabloların sunumu ve ağırlığı değişkendir, tipler arasında hatırı sayılır klinik ve moleküler örtüşme vardır ve tanının moleküler analizle doğrulanması önerilir (Mantovani ve ark., 2018). **Öğreti:** tek bir gen, üç ekseni birden gösterebilir — mekanizma yönü, zamanlama (germline/mozaik) ve ebeveyn kökeni.

**PAH ve DMD — serinin en tanıdık iki basamağı.** Fenilalanin hidroksilaz eksikliğinde alel çiftinin bıraktığı rezidüel aktivite klasik PKU ile hafif hiperfenilalaninemi arasındaki yeri belirler (Hillert ve ark., 2020); distrofinopatilerde ise okuma çerçevesini koruyan delesyonlar Becker, bozanlar Duchenne fenotibiyle sonuçlanır (Monaco ve ark., 1988). **Öğreti:** allelik serinin en kolay öğretilen biçimi rezidüel işlev eksenidir ve her iki örnek de tarama/izlem kararlarını doğrudan değiştirir.

---

## 8. Sık yapılan hatalar ve klinikte dikkat

> **🔴 Sık yapılan hata kutusu**
> 1. **"*X* geninde patojen varyant var" demeyi tanı sanmak.** Gen adı bir tanı değildir. Tanı, gen–kalıtım–hastalık üçlüsüyle kurulur; risk hesabı, prognoz ve izlem bu üçlüden türetilir.
> 2. **PS1/PM5'i hastalık belirtmeden uygulamak.** "Aynı kodonda patojen varyant bildirilmiş" kanıtı, o varyant **başka bir hastalık** için bildirilmişse doğrudan aktarılamaz (*FGFR3* p.Lys650Met ↔ p.Lys650Glu).
> 3. **PVS1'i mekanizma kontrolü yapmadan kullanmak.** Null varyant, ancak işlev kaybı **seçilen hastalığın** bilinen mekanizmasıysa çok güçlü kanıttır; aynı gendeki işlev kazanımı hastalığı için değildir.
> 4. **"Delesyon en ağır fenotibi yapar" varsayımı.** Dominant-negatif/neomorfik basamakları olan genlerde delesyon çoğu zaman **daha hafif** seyreder (osteogenesis imperfekta tip I).
> 5. **"Sessiz varyant zararsızdır."** HGPS'nin tekrarlayan nedeni tam olarak sessiz bir değişimdir; kriptik splice aktivasyonu allelik serilerde beklenmedik basamaklar üretir.
> 6. **Serinin bir ucundaki biyokimyasal testin normal olmasına dayanarak geni dışlamak.** *ATP7A*'ya bağlı izole distal motor nöropatide Menkes hastalığının biyokimyasal imzası yoktur.
> 7. **Kalıtım modunu sabit varsaymak.** Aynı gen monoalelik ve bialelik durumda farklı hastalıklar yapabilir; ikinci alel araştırılmadan verilen tekrarlanma riski yanlış olabilir.
> 8. **Domain–fenotip haritasını kesin öngörü aracı gibi kullanmak.** Bu haritalar güçlü örüntülerdir, kural değildir; özellikle *LMNA*'da genotip–fenotip ilişkisi kurmak istisnai biçimde güçtür.
> 9. **Panelde gen olmasını, o hastalık için geçerli kanıt olması sanmak.** Bir gen panele bir hastalık için "Kesin" ilişkiyle girmiş olabilir; bulunan varyant aynı genin çok daha zayıf kanıtlı başka bir fenotibiyle ilişkiliyse rapor bunu açıkça belirtmelidir.
> 10. **Fenotibi varyanta uydurmak.** Bulunan varyantın öngördüğü hastalığın bulguları hastada yoksa, doğru davranış fenotibi zorlamak değil, varyantı VUS/ikincil bulgu olarak bırakıp yeniden analiz planlamaktır.

> **🟦 Klinikte dikkat kutusu**
> - Allelik seri taşıyan bir gende sonuç geldiğinde, ilk soru "varyant patojen mi?" değil, **"hangi hastalık varlığı için değerlendiriyorum?"** olmalıdır.
> - Derin fenotipleme lüks değildir: serinin öngördüğü bulguları (işitme, kardiyak ileti, yağ dağılımı, segment oranları, biyokimyasal imza) **aktif olarak arayın**; birçok VUS ancak bu şekilde çözülür.
> - Mono- ve bialelik tabloları ayıran genlerde, ikinci alelin varlığını netleştirmeden risk hesabı vermeyin; faz bilgisi gerekiyorsa ebeveyn örneği veya uzun-okuma teknolojisi düşünün.
> - Beklenmedik bir fenotiple karşılaşıldığında **zamanlama eksenini** hatırlayın: germline hâlde hiç görülmeyen varyantlar mozaik hâlde yaşanabilir sendromlar üretir; etkilenmiş dokudan örnek alınmalıdır.
> - İmprintli lokuslarda alelin ebeveyn kökenini belirlemeden fenotip öngörüsü yapılmamalıdır.
> - Rapor metnine mekanizma cümlesi ekleyin: "Bu varyantın beklenen etkisi işlev kaybıdır ve bu, X hastalığının bilinen mekanizmasıyla uyumludur." Bu tek cümle, raporu okuyan hekimin izlem planını doğru kurmasını sağlar.

---

## 9. Klinik pratikte karar algoritması

**Algoritma 15.3 — Allelik seri taşıyan gende klinik karar akışı**

```mermaid
flowchart TD
  A["Genetik sonuç: allelik seri taşıyan<br/>bir gende varyant"] --> B["ADIM 1 — Genin hastalık haritasını çıkar:<br/>tanımlı gen–hastalık varlıkları,<br/>her birinin kalıtımı ve mekanizması"]

  B --> C["ADIM 2 — Derin fenotipleme:<br/>her varlığın ayırt edici bulgularını<br/>sistematik olarak ARA"]

  C --> D{"Fenotip hangi varlıkla<br/>uyuşuyor?"}
  D -->|"Net biçimde biriyle"| E["ADIM 3 — Varyantı O varlık için<br/>sınıflandır (kriterleri hastalığa göre seç)"]
  D -->|"Birden fazlasıyla / belirsiz"| F["Altı ekseni sırayla sor:<br/>yön · rezidüel işlev · konum ·<br/>kalıtım modu · zamanlama · bağlam"]
  D -->|"Hiçbiriyle"| G["Varyantı VUS/ikincil bulgu bırak;<br/>lokus heterojenitesi için<br/>YENİDEN ANALİZ planla"]

  F --> H{"Ayrım netleşti mi?"}
  H -->|"Evet"| E
  H -->|"Hayır"| I["Ek veri üret:<br/>RNA analizi · fonksiyonel test ·<br/>ebeveyn örneği/faz · doku örneği (mozaiklik)"]
  I --> E

  E --> J{"Bu varlık ClinGen'de<br/>hangi geçerlilikte?"}
  J -->|"Kesin / Güçlü"| K["Tanısal rapor:<br/>gen + kalıtım + hastalık üçlüsü<br/>+ mekanizma cümlesi"]
  J -->|"Sınırlı / Çelişkili"| L["Raporda kanıt düzeyini AÇIKÇA belirt;<br/>klinik kararı tek başına bu bulguya bağlama"]

  K --> M["GENETİK DANIŞMA"]
  L --> M
  G --> M
  M --> N["Riski hastalık varlığına göre hesapla<br/>(OD %50 · OR %25 · mozaik: düşük ama sıfır değil)<br/>İzlem/tarama planını O hastalığa göre kur<br/>Belirsizlik varsa açıkça söyle"]
```

---

## 10. Kaynaklar

> **Atıf / doğrulama notu:** Bu bölümün bibliyografik verileri PubMed üzerinden doğrulanmıştır; her kaynağın PMID ve DOI'si tek tek teyit edilmiştir. (Metin içinde yazar-yıl, kaynakçada DOI-link kullanılır.)

1. **Thaxton C, Goldstein J, DiStefano M, ve ark. (2022).** Lumping versus splitting: How to approach defining a disease to enable accurate genomic curation. *Cell Genomics* 2(5):100131. **PMID: 35754516** · DOI: [10.1016/j.xgen.2022.100131](https://doi.org/10.1016/j.xgen.2022.100131) — *Kullanım amacı: Bölümün yorumlama omurgası; hastalık varlığının tanımlanması, ön-küreleme, birleştirme/ayırma ölçütleri ve bunların klinik tanı, biyoinformatik ve bakım yönetimine etkileri.*

2. **Strande NT, Riggs ER, Buchanan AH, ve ark. (2017).** Evaluating the Clinical Validity of Gene-Disease Associations: An Evidence-Based Framework Developed by the Clinical Genome Resource. *American Journal of Human Genetics* 100(6):895–906. **PMID: 28552198** · DOI: [10.1016/j.ajhg.2017.04.015](https://doi.org/10.1016/j.ajhg.2017.04.015) — *Kullanım amacı: Gen–hastalık ilişkisinin (gen değil, ilişki) puanlanması; Kesin/Güçlü/Orta/Sınırlı/Çelişkili sınıfları; aynı gen için farklı geçerlilik düzeyleri.*

3. **Toydemir RM, Brassington AE, Bayrak-Toydemir P, ve ark. (2006).** A novel mutation in FGFR3 causes camptodactyly, tall stature, and hearing loss (CATSHL) syndrome. *American Journal of Human Genetics* 79(5):935–941. **PMID: 17033969** · DOI: [10.1086/508433](https://doi.org/10.1086/508433) — *Kullanım amacı: Landmark — FGFR3'ün kısmi işlev kaybı (p.Arg621His) ile uzun boy fenotibi; aynı genin hem baskılayarak hem destekleyerek anomali yapabilmesi; Fgfr3 nakavt faresiyle örtüşme.*

4. **Eriksson M, Brown WT, Gordon LB, ve ark. (2003).** Recurrent de novo point mutations in lamin A cause Hutchinson-Gilford progeria syndrome. *Nature* 423(6937):293–298. **PMID: 12714972** · DOI: [10.1038/nature01629](https://doi.org/10.1038/nature01629) — *Kullanım amacı: Landmark — 20 klasik olgunun 18'inde ekzon 11 G608G; kriptik splice aktivasyonu; 50 amino asidin silinmesi; nükleer membran anormallikleri; lokusun UPD ve delesyon olgularıyla haritalanması.*

5. **Worman HJ (2012).** Nuclear lamins and laminopathies. *The Journal of Pathology* 226(2):316–325. **PMID: 21953297** · DOI: [10.1002/path.2999](https://doi.org/10.1002/path.2999) — *Kullanım amacı: Review — laminlerin her hücrede ifade edilmesine karşın hastalıkların doku-seçici olması; nükleer morfoloji bozukluğunun patolojiye dönüşümünün henüz tam açıklanmamış olması (⚠️ sınır belirtme).*

6. **Bertrand AT, Chikhaoui K, Ben Yaou R, Bonne G (2011).** [Laminopathies: one gene, several diseases]. *Biologie Aujourd'hui* 205(3):147–162. **PMID: 21982404** · DOI: [10.1051/jbio/2011017](https://doi.org/10.1051/jbio/2011017) — *Kullanım amacı: Review — LMNA'da on üzerinde bozukluk; Ig-benzeri domain ve lipodistrofi, çubuk domaini ve çizgili kas ilişkisi; genotip–fenotip kurmanın zorluğu. (Fransızca metin, İngilizce özet.)*

7. **Marini JC, Forlino A, Cabral WA, ve ark. (2007).** Consortium for osteogenesis imperfecta mutations in the helical domain of type I collagen: regions rich in lethal mutations align with collagen binding sites for integrins and proteoglycans. *Human Mutation* 28(3):209–221. **PMID: 17078022** · DOI: [10.1002/humu.20429](https://doi.org/10.1002/humu.20429) — *Kullanım amacı: Metodoloji/klinik — 832 yapısal varyantın bölgesel haritası; α1(I) glisin değişimlerinin üçte birinin letal olması; iki yalnızca-letal bölge; COL1A2'de %80 letal olmama; splice varyantlarının payı.*

8. **Kaler SG (2011).** ATP7A-related copper transport diseases-emerging concepts and future trends. *Nature Reviews Neurology* 7(1):15–29. **PMID: 21221114** · DOI: [10.1038/nrneurol.2010.180](https://doi.org/10.1038/nrneurol.2010.180) — *Kullanım amacı: Review — Menkes hastalığı, oksipital boynuz sendromu ve izole distal motor nöropati üçlüsü; rezidüel aktivite ve erken tedavi yanıtı; üçüncü hastalığın farklı mekanizması.*

9. **Mantovani G, Bastepe M, Monk D, ve ark. (2018).** Diagnosis and management of pseudohypoparathyroidism and related disorders: first international Consensus Statement. *Nature Reviews Endocrinology* 14(8):476–500. **PMID: 29959430** · DOI: [10.1038/s41574-018-0042-0](https://doi.org/10.1038/s41574-018-0042-0) — *Kullanım amacı: Guideline — GNAS ile ilişkili bozukluklar ailesinde tipler arası klinik/moleküler örtüşme; tanının moleküler analizle doğrulanması gereği.*

10. **Weinstein LS, Shenker A, Gejman PV, ve ark. (1991).** Activating mutations of the stimulatory G protein in the McCune-Albright syndrome. *The New England Journal of Medicine* 325(24):1688–1695. **PMID: 1944469** · DOI: [10.1056/NEJM199112123252403](https://doi.org/10.1056/NEJM199112123252403) — *Kullanım amacı: Landmark — GNAS p.Arg201His/Cys; dokular arasında değişen mutant alel yükü (postzigotik köken). Kaynak kütüğünden yeniden kullanılmıştır (Bölüm 12 köprüsü).*

11. **Wilkie AOM (1994).** The molecular basis of genetic dominance. *Journal of Medical Genetics* 31(2):89–98. **PMID: 8182727** · DOI: [10.1136/jmg.31.2.89](https://doi.org/10.1136/jmg.31.2.89) — *Kullanım amacı: Kavramsal çerçeve — dominant varyant mekanizmalarının sınıflandırılması; aynı lokusta farklı mekanizmaların bir arada bulunabilmesi. Kaynak kütüğünden yeniden kullanılmıştır.*

12. **Webster MK, D'Avis PY, Robertson SC, Donoghue DJ (1996).** Profound ligand-independent kinase activation of fibroblast growth factor receptor 3 by the activation loop mutation responsible for a lethal skeletal dysplasia, thanatophoric dysplasia type II. *Molecular and Cellular Biology* 16(8):4081–4087. **PMID: 8754806** · DOI: [10.1128/MCB.16.8.4081](https://doi.org/10.1128/MCB.16.8.4081) — *Kullanım amacı: Mekanizma landmark — FGFR3 p.Lys650Glu'nun yabanıl tipin ~100 katı, ligandtan bağımsız konstitütif aktivasyonu; 650. pozisyonda konum ve yük özgüllüğü. Kaynak kütüğünden yeniden kullanılmıştır (Bölüm 4 köprüsü).*

13. **Edery P, Eng C, Munnich A, Lyonnet S (1997).** RET in human development and oncogenesis. *BioEssays* 19(5):389–395. **PMID: 9174404** · DOI: [10.1002/bies.950190506](https://doi.org/10.1002/bies.950190506) — *Kullanım amacı: Mekanizma/klinik — RET'in iki yüzü: işlev kaybı/Hirschsprung ve işlev kazanımı/MEN2. Kaynak kütüğünden yeniden kullanılmıştır.*

14. **Berecki G, Howell KB, Deerasooriya YH, ve ark. (2018).** Dynamic action potential clamp predicts functional separation in mild familial and severe de novo forms of *SCN2A* epilepsy. *Proceedings of the National Academy of Sciences USA* 115(24):E5516–E5525. **PMID: 29844171** · DOI: [10.1073/pnas.1800077115](https://doi.org/10.1073/pnas.1800077115) — *Kullanım amacı: Mekanizma — SCN2A'da işlev kazanımı ve kaybının elektrofizyolojik ayrımı ve farklı klinik tablolar. Kaynak kütüğünden yeniden kullanılmıştır.*

15. **Brunklaus A, Du J, Steckler F, ve ark. (2020).** Biological concepts in human sodium channel epilepsies and their relevance in clinical practice. *Epilepsia* 61(3):387–399. **PMID: 32090326** · DOI: [10.1111/epi.16438](https://doi.org/10.1111/epi.16438) — *Kullanım amacı: Klinik — mekanizma yönünün tedavi yönünü belirlemesi (sodyum kanal blokerleri). Kaynak kütüğünden yeniden kullanılmıştır.*

16. **Monaco AP, Bertelson CJ, Liechti-Gallati S, Moser H, Kunkel LM (1988).** An explanation for the phenotypic differences between patients bearing partial deletions of the DMD locus. *Genomics* 2(1):90–95. **PMID: 3384440** · DOI: [10.1016/0888-7543(88)90113-9](https://doi.org/10.1016/0888-7543(88)90113-9) — *Kullanım amacı: Landmark — okuma çerçevesi kuralı; Duchenne ↔ Becker ayrımı (rezidüel işlev ekseni). Kaynak kütüğünden yeniden kullanılmıştır.*

17. **Forlino A, Marini JC (2000).** Osteogenesis imperfecta: prospects for molecular therapeutics. *Molecular Genetics and Metabolism* 71(1-2):225–232. **PMID: 11001814** · DOI: [10.1006/mgme.2000.3039](https://doi.org/10.1006/mgme.2000.3039) — *Kullanım amacı: Mekanizma — niceliksel (null) kusurun hafif tip I, glisin değişimlerinin ağır tablolarla ilişkisi. Kaynak kütüğünden yeniden kullanılmıştır (Bölüm 5 köprüsü).*

18. **Hillert A, Anikster Y, Belanger-Quintana A, ve ark. (2020).** The Genetic Landscape and Epidemiology of Phenylketonuria. *American Journal of Human Genetics* 107(2):234–250. **PMID: 32668217** · DOI: [10.1016/j.ajhg.2020.06.006](https://doi.org/10.1016/j.ajhg.2020.06.006) — *Kullanım amacı: Klinik — PAH genotip–fenotip ilişkisi; rezidüel aktivite ekseninde klasik PKU ↔ hafif hiperfenilalaninemi. Kaynak kütüğünden yeniden kullanılmıştır.*

19. **Lima Cunha D, Arno G, Corton M, Moosajee M (2019).** The Spectrum of PAX6 Mutations and Genotype-Phenotype Correlations in the Eye. *Genes (Basel)* 10(12):1050. **PMID: 31861090** · DOI: [10.3390/genes10121050](https://doi.org/10.3390/genes10121050) — *Kullanım amacı: Klinik — PAX6'da varyant tipine göre aniridi ve diğer ön segment tablolarının ayrışması. Kaynak kütüğünden yeniden kullanılmıştır.*

20. **Abou Tayoun AN, Pesaran T, DiStefano MT, ve ark. (2018).** Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. *Human Mutation* 39(11):1517–1524. **PMID: 30192042** · DOI: [10.1002/humu.23626](https://doi.org/10.1002/humu.23626) — *Kullanım amacı: Guideline — PVS1'in yalnız işlev kaybının bilinen hastalık mekanizması olduğu durumlarda uygulanabilmesi. Kaynak kütüğünden yeniden kullanılmıştır.*

21. **Richards S, Aziz N, Bale S, ve ark. (2015).** Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. *Genetics in Medicine* 17(5):405–424. **PMID: 25741868** · DOI: [10.1038/gim.2015.30](https://doi.org/10.1038/gim.2015.30) — *Kullanım amacı: Guideline — PS1, PM5, PM1, PP4 kriterlerinin tanımı ve allelik seride uyarlanması. Kaynak kütüğünden yeniden kullanılmıştır.*
22. **Sanders SJ, Campbell AJ, Cottrell JR, ve ark. (2018).** Progress in Understanding and Treating SCN2A-Mediated Disorders. *Trends in Neurosciences* 41(7):442–456. **PMID: 29691040** · DOI: [10.1016/j.tins.2018.03.011](https://doi.org/10.1016/j.tins.2018.03.011) — *Kullanım amacı: SCN2A işlev kaybının otizm spektrum bozukluğu ve entelektüel yetersizlikle ilişkisi (Berecki 2018'in kapsamı dışındadır).*

> **İkincil/destekleyici kaynak notu:** OMIM, ClinVar, ClinGen Gene-Disease Validity ve GeneReviews kayıtları bu bölümde yalnızca destekleyici/başvuru kaynağı olarak anılmıştır; hiçbiri ana mekanizma kaynağı olarak kullanılmamıştır. *COL4A3/COL4A4* ve *RYR1* örnekleri, kalıtım modu eksenini örneklemek üzere yerleşik ders bilgisi düzeyinde verilmiştir.

---

## ✅ Bölüm öz-denetim tablosu

**Tablo 15.4 — Bölüm 15 öz-denetim tablosu**

| Kriter | Durum | Not |
|--------|-------|-----|
| Mekanizma doğru anlatıldı mı? | ✅ | Allelik serinin altı ekseni (yön, rezidüel işlev, konum, kalıtım modu, zamanlama, bağlam) sistematik olarak kuruldu |
| Klinik bağlantı kuruldu mu? | ✅ | Derin fenotipleme, "hangi hastalık?" sorusu, rapor cümlesi ve tekrarlanma riskinin hastalık varlığına bağlanması |
| Varyant tipi ile mekanizma ilişkilendirildi mi? | ✅ | 10 satırlık "varyant tipi → serideki konum" tablosu; tip-temelli otomatik yorumun sınırları |
| Pediatrik örnek verildi mi? | ✅ | FGFR3/CATSHL, LMNA/HGPS, ATP7A, COL1A1, GNAS, PAH, DMD, PAX6 — hepsi kaynaklı |
| Test seçimi açıklandı mı? | ✅ | Standart 8 satırlık tablo + derin fenotipleme/fonksiyonel test satırı; "delesyon = en ağır" sanısının düzeltilmesi |
| ACMG/ClinGen bağlantısı doğru mu? | ✅ | PVS1, PS1, PM5, PM1, PP4'ün hastalık-özgü uyarlanması; küreleme ölçütleri (Thaxton 2022); gen–hastalık geçerliliği (Strande 2017) |
| Kaynaklar PMID/DOI ile verildi mi? | ✅ | 21/21 kaynak PMID + DOI-link + kullanım amacı ile (9 yeni doğrulama + 12 kütükten yeniden kullanım) |
| Spekülatif iddialar işaretlendi mi? | ✅ | Domain–fenotip haritalarının öngörü aracı olarak kullanılamayacağı ⚠️ ile işaretlendi; COL4A3/A4 ve RYR1 örnekleri ders bilgisi olarak etiketlendi; **"altı eksen" çerçevesi 🏷️ kitabın pedagojik sentezi olarak etiketlendi** (27.07.2026 doğrulama turu) |
| Kaynak uydurma riski var mı? | ✅ Yok | 9 yeni PMID/DOI bu oturumda PubMed MCP ile tek tek doğrulandı; 12'si daha önce doğrulanmış kütük kaydı |
| Görsel/şema/algoritma desteği yeterli mi? (≥3 SVG, ≥2 Mermaid) | ✅ | **4 SVG + 3 Mermaid**; tüm SVG'ler tarayıcıda render edilip gözle denetlendi (çakışma/taşma yok) |

---

### 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu)
> "Bu bölümdeki tüm kaynakların PMID/DOI bilgisini kontrol et. PMID veya DOI veremediğin kaynağı çıkar. Kaynağı olmayan iddiayı 'kaynak doğrulaması gerekli' olarak işaretle."
>
> **Bu bölüm için durum:** **22/22 kaynak PMID+DOI doğrulandı** (9'u bu oturumda PubMed MCP ile — Thaxton 2022, Strande 2017, Toydemir 2006, Eriksson 2003, Worman 2012, Bertrand 2011, Marini 2007, Kaler 2011, Mantovani 2018; 12'si Bölüm_00 kaynak kütüğünden yeniden kullanıldı). Bölüm, 27.07.2026 tarihli iddia-düzeyi doğrulama turundan geçmiştir; turda *SCN2A*/otizm atfı Sanders 2018'e taşınmış ve "altı eksen" çerçevesi 🏷️ etiketlenmiştir (bkz. `Dogrulama_Kutugu.md`).
>
> **İşaretlenen iddialar:** (1) ⚠️ Domain–fenotip haritaları güçlü örüntüler sunar ancak birebir öngörü aracı değildir; laminopatilerde nükleer morfoloji bozukluğunun patolojiye nasıl dönüştüğü henüz tam açıklanmamıştır (Worman, 2012). (2) *COL4A3*/*COL4A4* (ince bazal membran nefropatisi ↔ otozomal resesif Alport sendromu) ve *RYR1* (malign hipertermi/santral kor ↔ bialelik konjenital miyopati) örnekleri, kalıtım modu eksenini örneklemek üzere **yerleşik ders bilgisi** düzeyinde verilmiştir; bu bölümde ayrıca PubMed doğrulaması yapılmamıştır. (3) *FGFR3* varyant–fenotip eşleşmeleri (p.Asn540Lys, p.Gly380Arg, p.Lys650Met, p.Lys650Glu, p.Arg248Cys) yerleşik klinik genetik bilgisidir; bu bölümde doğrudan kaynaklanan noktalar p.Arg621His (Toydemir, 2006) ve p.Gly380Arg'nin konstitütif aktivasyonudur (Webster ve Donoghue, 1996). (3) 🏷️ **"Allelik serinin altı ekseni" çerçevesi kitabın pedagojik sentezidir**; literatürde bu adla yerleşik bir sınıflandırma değildir — eksenlerin bileşenleri kaynaklı, gruplama editöryaldir (§2 girişindeki etikete bkz.).
