# Bölüm 15 — Digenik, Oligogenik Kalıtım ve Modifiye Edici Lokuslar

> **Bölümün çekirdek tezi:** Bu kitabın önceki bölümleri, büyük ölçüde tek bir varsayım üzerine kuruluydu: *bir hastalığın bir nedeni vardır.* Bu bölüm o varsayımı gevşetir. **Monogenik ve kompleks kalıtım iki ayrı dünya değil, tek bir eksenin iki ucudur**; arada digenik (iki lokusun ikisi de gerekli), oligogenik (birkaç lokusun eşitsiz katkısı) ve modifiye edici (ana varyantın etkisini hafifleten ya da ağırlaştıran ikinci lokus) senaryoları vardır. Bu eksende bir hastalığı nereye koyduğunuz üç şeyi birden belirler: aileye vereceğiniz **tekrarlanma riskini**, bekleyeceğiniz **penetransı** ve varyantı nasıl **yorumlayacağınızı**. Bölümün ikinci ve klinik olarak daha keskin tezi ise bir uyarıdır: **"iki gende varyant bulmak" ile "hastalık digeniktir" demek aynı şey değildir.** Her sağlıklı genom çok sayıda nadir varyant taşır; digenik iddia, monogenik iddiadan daha yüksek bir kanıt çıtası gerektirir. Bu bölüm ayrıca Bölüm 1'de "eksik penetrans ve değişken ekspresivite" diye adlandırdığımız bulanıklığa somut bir moleküler zemin verir: o bulanıklığın önemli bir kısmı, ana genin etrafındaki **genetik bağlamdır**.

> **📘 Okuma katmanları.** Bu kitabın birincil hedefi **yandal asistanı ve klinik genomik çalışan hekimdir**; genel pediatrist ve tıp öğrencisi ikincil hedef kitledir. Bölümü kendi katmanınızdan okuyabilirsiniz:
> · **① Temel — tıp öğrencisi:** Süreklilik ve eşik modeli (Şekil 15.1) kurulmadan sonraki tartışmalar havada kalır.
> · **② Klinik — pediatrist ve klinisyen:** §4 ve §8 ile Şekil 15.4'ün C paneli; "iki gende varyant bulduk" cümlesinin danışmadaki karşılığı.
> · **③ İleri düzey — yandal asistanı, laboratuvar, varyant yorumlayan:** §6: ACMG/AMP çerçevesinin kapsam sınırı, tek-varyant sınıflandırması ile çift-lokus nedenselliği arasındaki ayrım ve digenik iddianın kanıt basamakları.

> 🖼️ **Görseller hakkında not:** Şekil 15.1–15.4 `assets/` klasöründe SVG olarak bulunur. Mermaid diyagramları metin içine gömülüdür.

---

## Öğrenme hedefleri

Bu bölümü tamamlayan okuyucu:
1. Monogenik–digenik–oligogenik–poligenik sürekliliğini tanımlar ve lokus sayısı ile etki büyüklüğü arasındaki ters ilişkiyi açıklar.
2. Digenik kalıtımı tanımlar, klasik örneğini (*RDS*/*ROM1*) açıklar ve otozomal resesif kalıtımdan neye bakarak ayırt edileceğini bilir.
3. Trialelik kalıtım kavramını açıklar ve Bardet-Biedl sendromu örneğinde kalıtım modelinin nasıl sorgulandığını yorumlar.
4. Modifiye edici lokusun tanımını verir ve dört ana mekanizmasını (yedek/paralog doz, aynı yolakta ikinci lokus, düzenleyici varyant, çevre/cinsiyet) sıralar.
5. *SMN2* kopya sayısının SMA fenotipini nasıl belirlediğini açıklar ve bunu doz–eşik mantığıyla ilişkilendirir.
6. Kistik fibrozda aynı *CFTR* genotipinin neden farklı akciğer hastalığı ağırlığı ürettiğini modifiye edici lokuslarla açıklar.
7. Eşik (yük) modelini açıklar ve aynı fenotipe farklı genetik mimarilerle ulaşılabileceğini gerekçelendirir.
8. Digenik/oligogenik bir iddiayı desteklemek için gereken kanıt basamaklarını sıralar ve "iki nadir varyant" gözleminin neden yetersiz olduğunu açıklar.
9. ACMG/AMP çerçevesinin kapsam sınırını, tek-varyant sınıflandırması ile çift-lokus nedenselliği arasındaki ayrımı ve bunların raporlama/danışma sonuçlarını açıklar.

---

## 1. Kavramsal tanım

Mendel genetiğinin gücü, sadeliğinden gelir: bir gen, bir hastalık, hesaplanabilir bir risk. Bu kitabın buraya kadarki bölümleri de bu sadeliği korudu — mekanizmalar değişti (kayıp, kazanım, dominant-negatif, imprinting, mozaiklik), ama sorumlu lokus hep bir taneydi. Klinik pratikte ise sık sık bu modele oturmayan durumlarla karşılaşırız: patojen varyantı taşıdığı hâlde sağlıklı akrabalar, aynı varyantı taşıyan iki kardeşte çok farklı ağırlıkta hastalık, ya da tek bir gende bulunan varyantın fenotipi tam olarak açıklayamaması. Bu bölüm, bu boşluğun genetik mimariyle ilgili kısmını ele alır.

Kavramları netleştirerek başlayalım. **Bu bölümde “zorunlu digenik” diye adlandırılan dar modelde** hastalık, iki *farklı* lokustaki varyantların birlikte bulunmasını gerektirir; her iki varyant da gereklidir, hiçbiri tek başına yeterli değildir. “Digenik” sözcüğü literatürde daha geniş iki-lokuslu mimariler için de kullanılabildiğinden, bir iddia kurulurken hangi modelin kastedildiği ayrıca yazılmalıdır. Zorunlu digenik model, otozomal resesif kalıtımdan kritik biçimde farklıdır: resesifte iki varyant **aynı** genin iki alelindedir; digenikte ise **farklı genlerde**, çoğu zaman farklı kromozomlardadır. **Oligogenik kalıtımda** katkıda bulunan lokus sayısı ikiden fazladır (tipik olarak birkaç tane) ve katkılar eşit değildir: genellikle bir "ana" lokus ile ona eşlik eden daha küçük etkili lokuslar bulunur. **Poligenik** uçta ise yüzlerce–binlerce lokus vardır, her birinin etkisi tek başına çok küçüktür ve hastalık toplam yükle belirlenir.

**Modifiye edici lokus (modifier)** ise bu spektrumun içinde ama ayrı bir kavramdır: modifier, hastalığı **tek başına yapmaz**; ana varyantın yarattığı tabloyu hafifletir veya ağırlaştırır. Yani modifier'ın işlevi hastalığı *başlatmak* değil, *renklendirmektir*. Bu ayrım klinik olarak önemlidir, çünkü modifier bir lokusta bulunan varyant tek başına raporlanacak bir "neden" değildir; ama prognozu ve bazen tedaviyi etkileyebilir.

Şekil 15.1'de gösterildiği gibi bu dört durak arasında keskin bir biyolojik sınır yoktur; ayrım pratik ve tanısaldır. Eksende sağa doğru gidildikçe lokus sayısı artar, lokus başına etki büyüklüğü azalır ve kalıtım Mendel oranlarından uzaklaşır.

![Şekil 15.1 — Monogenikten poligeniğe: tek bir süreklilik, dört durak](assets/sekil_50_monogenik_poligenik_sureklilik.svg)

Bu sürekliliği anlamanın en yararlı aracı **eşik (yük) modelidir**. Model şunu varsayar: hastalık, bireyin taşıdığı genetik (ve çevresel) yükün belli bir eşiği aşmasıyla ortaya çıkar. Bu bakış, aynı fenotipe **farklı genetik mimarilerle** ulaşılabileceğini doğal biçimde açıklar: bir birey tek büyük etkili bir varyantla eşiği aşarken, bir başkası çok sayıda küçük katkının toplamıyla aşabilir. Aynı model, neden bazı taşıyıcıların hasta olmadığını da açıklar — o birey eşiğin altında kalmıştır. Bu, Bölüm 3'te doz–eşik, Bölüm 11'de heteroplazmi–eşik olarak gördüğümüz mantığın **lokuslar arası** karşılığıdır.

**Tablo 15.1 — Digenik, oligogenik kalıtım ve modifiye edicilerin temel kavramları**

| Kavram | Tanım | Klinik anlamı |
|---|---|---|
| Monogenik | Tek lokus; büyük etki | Mendel oranları geçerli; risk hesaplanabilir |
| **Zorunlu digenik** | İki farklı lokus; **ikisi de gerekli**, biri yetmez | Tek-lokus için kullanılan evrensel bir oran yoktur; ebeveyn genotiplerinden iki-lokuslu ortak aktarım olasılığı hesaplanabilir |
| **Trialelik** | Bir lokusta iki + ikinci lokusta bir varyant | "Resesif" tablo aslında üçüncü alele bağımlı olabilir |
| **Oligogenik** | Birkaç lokus; eşitsiz katkı (± ana lokus) | Eksik penetrans sık görülebilir; düzenlenmeye özgü ampirik veri yoksa genel oran verilmez |
| Poligenik | Yüzlerce–binlerce lokus; her biri çok küçük | Ampirik risk; toplam yük belirleyici |
| **Modifier** | Hastalığı yapmaz; ağırlığını değiştirir | Prognoz ve bazen tedavi hedefi; tek başına "neden" değildir |
| Eşik (yük) modeli | Hastalık, toplam yük eşiği aşınca ortaya çıkar | Aynı fenotipe farklı mimarilerle ulaşılabilir |
| Epistazi | Bir lokusun etkisinin başka lokusa bağlı olması | Digenik/modifier etkilerin ortak istatistiksel adı |

---

## 2. Moleküler mekanizma

### 2.1 Digenik kalıtım: 1 + 1 = hastalık

Digenik kalıtımın ders kitabı örneği, tıbbi genetikte bu kavramın ilk net gösterimidir. Kajiwara, Berson ve Dryja, retinitis pigmentosalı üç ailede, birbiriyle bağlantısız iki fotoreseptör geninde — *peripherin/RDS* ve *ROM1* — varyantlar saptadılar ve kritik gözlemi yaptılar: **yalnızca her iki varyantı birden taşıyan (çift heterozigot) bireyler hastalanıyordu**; tek bir varyant taşıyan akrabalar sağlıklıydı (Kajiwara ve ark., 1994).

Şekil 15.2, bu örüntünün pedigrideki görünümünü ve neden kafa karıştırıcı olduğunu gösterir. Ailede iki sağlıklı ebeveynden hasta bir çocuk doğmuştur — bu, otozomal resesif kalıtımın klasik imzasıdır. Ancak burada iki varyant aynı genin iki alelinde değil, **iki ayrı gendedir**; dolayısıyla risk, tek-lokuslu resesif kalıtımdaki %25 oranı otomatik olarak kopyalanarak değil, ebeveynlerin iki lokustaki genotiplerinden hesaplanır. Şekildeki temsili eşleşmede baba yalnız *RDS*, anne yalnız *ROM1* heterozigotudur; lokuslar bağımsızsa her iki varyantın birlikte aktarım olasılığı 1/2 × 1/2 = 1/4, yani %25 çıkar. Sayının otozomal resesif örnekle aynı olması **hesap modelinin aynı olduğu anlamına gelmez**; başka ebeveyn genotiplerinde sonuç değişir ve klinik yineleme riski ayrıca penetrans, bağlantı ve diğer aileye özgü etkenlere bağlıdır.

![Şekil 15.2 — Digenik kalıtımın pedigri imzası](assets/sekil_51_digenik_pedigri.svg)

Mekanizma açısından bu örnek özellikle öğreticidir, çünkü rastgele iki gen değildir: peripherin/RDS ve ROM1, fotoreseptör dış segment disklerinin kenar yapısında **birlikte** görev alan proteinlerdir. Yani iki lokus aynı yapısal komplekste buluşur ve o kompleksin toplam işlevi için ortak bir doz eşiği vardır. Her iki alelin de yarı yarıya azalması, tek birinin azalmasının yapamadığı şeyi yapar: kompleksi eşiğin altına düşürür. **Digenik kalıtımın mekanik özü budur — iki lokus, ortak bir işlevsel havuzda toplanır.**

Bu gözlem, bir sonraki bölümde tekrar karşımıza çıkacak bir kanıt ölçütünü de doğurur: iki gen arasında gösterilebilir bir **biyolojik bağ** (aynı kompleks, aynı yolak, protein–protein etkileşimi) yoksa, digenik iddia zayıftır.

### 2.2 Trialelik kalıtım: kalıtım modelinin kendisi sorgulanınca

Digenik kavramının bir adım ötesi, Bardet-Biedl sendromunda (BBS) ortaya çıktı. BBS — pigmenter retina distrofisi, polidaktili, obezite, gelişim geriliği ve böbrek anomalileriyle giden bir siliyopati — klasik olarak otozomal resesif kabul ediliyordu. Katsanis ve arkadaşları 163 BBS ailesini *BBS2* ve *BBS6* için tarayınca beklenmedik bir tablo buldular: dört ailede etkilenmiş bireyler **üç mutant alel** taşıyordu; buna karşılık iki ailede *BBS2*'de iki mutant alel taşıyan ancak *BBS6* varyantı olmayan bireyler **etkilenmemişti**. Yazarlar buradan, BBS'nin tek-gen resesif bir hastalık olmayabileceğini ve en azından bazı ailelerde fenotibin ortaya çıkması için **üç mutant alel** gerekebileceğini öne sürdüler (Katsanis ve ark., 2001).

Bu bulgunun kavramsal ağırlığı, tek bir hastalığın ötesindedir. Burada sorgulanan şey bir genin patojenitesi değil, **kalıtım modelinin kendisidir**: bir lokusta iki patojen alel taşıyan bir bireyin sağlıklı kalabilmesi, "resesif" etiketinin her zaman yeterli olmadığını düşündürür.

⚠️ **Ancak modelin bugünkü durumu net biçimde kaydedilmelidir.** BBS'de trialelik kalıtım **tarihsel olarak önemli, güncel olarak ciddi biçimde tartışmalı** bir modeldir. Sonraki geniş genetik çalışmalar **zorunlu** trialelik modeli tutarlı biçimde doğrulamamıştır; güncel uzlaşı BBS'yi, **aynı gendeki bialelik** patojen/olası patojen varyantlarla oluşan otozomal resesif bir hastalık olarak kabul eder. Buna karşılık ikinci bir BBS genindeki ek varyantların **fenotip şiddetini, organ tutulumunu veya ekspresiviteyi** değiştirebileceğine dair veriler vardır.

Bu nedenle iki kavram **kesin biçimde ayrılmalıdır**: *"zorunlu üçüncü alel"* bugün rutin tanıda ve tekrarlanma riski hesabında **kullanılmamaktadır**; *"ikinci-lokus modifiye edici etkisi"* ise araştırılmaya devam eden, ancak klinik yorum standardı henüz oluşmamış bir mekanizmadır. Pratik uyarı da buradan çıkar: bir BBS geninde **trans** yerleşimli iki gerçek patojen varyant taşıdığı hâlde sağlıklı görünen bir birey, doğrudan trialelizm kanıtı sayılmamalıdır. Önce daha sıradan açıklamalar elenmelidir — varyant sınıflandırmasının doğruluğu, **faz**, yaşa bağlı fenotip, **hipomorfik** etki olasılığı, gözden kaçan CNV ve intronik varyantlar, ve eksik klinik değerlendirme. Korunması gereken ilke, trialelizmin kendisi değil, **kalıtım modelinin sorgulanabilir olduğudur**.

### 2.3 Modifiye edici lokuslar: aynı varyant, farklı ağırlık

Klinik pratikte en sık karşılaşılan durum ne saf digenik ne saf oligogeniktir; **ana bir varyant vardır ve fenotibin ağırlığı beklenenden farklıdır.** Bu farkın önemli bir kısmını modifiye edici lokuslar açıklar. Şekil 15.3, modifier'ın dört ana çalışma yolunu ve iki ders kitabı örneğini bir arada gösterir.

![Şekil 15.3 — Modifiye edici lokuslar: aynı varyant, farklı hastalık ağırlığı](assets/sekil_52_modifier_mekanizmalari.svg)

**Birinci yol, yedek/paralog doz.** Ana genin işini kısmen görebilen ikinci bir gen varsa, o genin kopya sayısı veya etkinliği fenotibi doğrudan belirler. Bunun en temiz örneği spinal musküler atrofidir (SMA) ve aşağıda ayrıntılandırılacaktır.

**İkinci yol, aynı yolakta ikinci bir lokus.** Ana kusurun bulunduğu biyolojik yolağın başka bir bileşenindeki varyasyon, sistemi tamponlayabilir ya da yükü artırabilir. Bu, digenik kalıtımla süreklidir; fark, ikinci lokusun *gerekli* olması ile yalnızca *etkileyici* olması arasındadır.

**Üçüncü yol, düzenleyici varyantlardır** ve Bölüm 13 ile doğrudan köprü kurar. Bir enhancer veya promotör varyantı, hedef genin ifade dozunu azaltarak ya da artırarak modifier gibi davranır. Bunun en iyi belgelenmiş örneği Hirschsprung hastalığındaki *RET* lokusudur: Emison ve arkadaşları, *RET*'in **intron 1'inde**, korunmuş bir enhancer-benzeri dizideki yaygın bir kodlamayan varyantın hastalık yatkınlığıyla anlamlı biçimde ilişkili olduğunu ve riske katkısının nadir kodlayan alellerinkinden **20 kat daha büyük** olduğunu gösterdiler. Bu varyant *in vitro* enhancer aktivitesini belirgin biçimde azaltıyor, düşük penetrans gösteriyor ve erkeklerle kadınlarda farklı genetik etkiler yaratıyordu — yani Hirschsprung'un karmaşık kalıtım örüntüsünün birkaç özelliğini birden açıklıyordu (Emison ve ark., 2005).

**Dördüncü yol genetik değildir ama unutulmamalıdır:** çevre, cinsiyet ve rastlantısal (stokastik) gelişimsel olaylar da modifier'dır. Emison çalışmasındaki cinsiyete bağlı etki farkı bunun somut bir örneğidir.

> **🔬 Deep-dive — *SMN2* kopya sayısı: modifier'ın en ölçülebilir hâli.** Spinal musküler atrofinin ana kusuru bütün hastalarda aynıdır: *SMN1*'in bialelik kaybı. Buna rağmen klinik tablo, doğumda solunum yetmezliğiyle giden Tip I'den, yürüyebilen ve erişkinliğe ulaşan Tip III'e kadar geniş bir aralıkta değişir. Bu değişkenliğin ana açıklayıcısı, insan genomunda *SMN1*'in neredeyse özdeş bir kopyası olarak bulunan **SMN2**'dir. *SMN2*, Bölüm 7'de ayrıntılandırdığımız sessiz bir C>T değişimi nedeniyle ekzon 7'yi büyük ölçüde atlar ve çoğunlukla kısa, işlevsiz bir protein üretir; ancak transkriptlerin küçük bir bölümü tam-boy SMN'e dönüşür. Dolayısıyla **her *SMN2* kopyası, hastaya az miktarda çalışan protein katar** — ve kopya sayısı arttıkça toplam doz eşiğe yaklaşır, fenotip hafifler. Calucho ve arkadaşları 625 ilişkisiz İspanyol hastayı analiz edip 1999'dan itibaren yayımlanmış çalışmalardaki 2.834 olguyu derleyerek toplam 3.459 hastalık bir veri seti oluşturdular ve *SMN2* kopya sayısı ile SMA tipi arasındaki ilişkiyi daha evrensel prognostik kurallar hâlinde ortaya koydular (Calucho ve ark., 2018). Bu örnek üç açıdan öğreticidir: **(1)** modifier burada bir dizi varyantı değil, bir **kopya sayısıdır** — yani Bölüm 8'deki doz mantığı modifier olarak iş görmektedir; **(2)** mekanizma splicing üzerinden çalışır (Bölüm 7), yani modifier etkiler kitabın önceki mekanizmalarını kullanır; **(3)** kopya sayısı bugün yalnızca prognoz için değil, **klinik çalışmalara hasta katmanlandırması ve yenidoğan taraması sonrası tedavi kararları** için de kullanılmaktadır — modifier bilgisinin doğrudan klinik karar değiştirdiği ender ve net bir örnektir.

### 2.4 Modifier'lar tek gende kalmaz: kistik fibrozis

Kistik fibroz, "aynı genotip, farklı fenotip" sorusunun en iyi çalışılmış zeminidir. Bölüm 2'de gördüğümüz gibi *CFTR* genotipi, pankreas yetmezliği gibi bazı özellikleri iyi öngörür (Sosnay ve ark., 2013). Ancak hastalığın başlıca mortalite nedeni olan **akciğer hastalığının ağırlığı**, aynı *CFTR* genotipini taşıyan hastalar arasında bile çarpıcı biçimde değişkendir.

Corvol ve arkadaşları, 6.365 KF hastasını kapsayan bir genom çapında ilişkilendirme meta-analiziyle akciğer hastalığı değişkenliğiyle anlamlı biçimde ilişkili **beş lokus** tanımladılar: 3q29 (*MUC4/MUC20*), 5p15.3 (*SLC9A3*), 6p21.3 (HLA sınıf II), Xq22-q23 (*AGTR2/SLC6A14*) ve daha önce de bildirilmiş olan 11p12-p13 (*EHF/APIP*) (Corvol ve ark., 2015). Bu lokusların hiçbiri *CFTR* değildir ve hiçbiri tek başına kistik fibrozis yapmaz; yaptıkları şey, var olan hastalığın seyrini değiştirmektir.

Buradan iki klinik sonuç çıkar. Birincisi, **genotip prognozu tam belirlemez** — aynı mutasyonu taşıyan iki hastaya aynı seyri vaat etmek yanlıştır. İkincisi ve daha umut verici olanı, modifiye edici lokusların **tedavi hedefi** olabilmesidir; hastalığın kendisini değil ama ağırlığını değiştiren yolaklar, farmakolojik müdahale için mantıklı adaylardır.

---

## 3. Varyant tipleri

Bu bölümde "varyant tipi" sorusu farklı sorulur: önemli olan varyantın moleküler sınıfı değil, **kalıtım mimarisindeki rolüdür**. Aşağıdaki tablo bu rolleri ve her birinin kanıt gereksinimini toplar.

**Tablo 15.2 — Varyantın kalıtım mimarisindeki rolü ve kanıt gereksinimi**

| Rol | Tanım | Tek başına hastalık yapar mı? | Kanıt gereksinimi | Örnek |
|---|---|---|---|---|
| Tek nedensel varyant (monogenik) | Fenotibi tek başına açıklar | Evet | Standart ACMG | Kitabın Bölüm 2–13'ü |
| **Digenik çift** | İki lokus; ikisi de gerekli | Hayır (hiçbiri) | Biyolojik bağ + birlikte ayrışma + tekrarlanma | *RDS* + *ROM1* (Kajiwara 1994) |
| **Üçüncü alel (trialelik)** | Resesif çifte eklenen üçüncü varyant | Hayır | Aynı lokusta iki alelli sağlıklı bireylerin gösterilmesi | *BBS2* + *BBS6* (Katsanis 2001) |
| **Oligogenik katkı** | Birkaç lokusun eşitsiz katkısı | Hayır | Yük analizi; ana lokus + katkı lokusları | Siliyopatiler, bazı nörogelişimsel tablolar |
| **Modifier — paralog doz** | Yedek genin kopya sayısı/etkinliği | Hayır | Doz–fenotip korelasyonu (büyük seri) | *SMN2* kopya sayısı (Calucho 2018) |
| **Modifier — yolak lokusu** | Aynı yolakta tamponlayan/ağırlaştıran lokus | Hayır | GWAS veya aile-temelli ilişkilendirme | KF akciğer modifier'ları (Corvol 2015) |
| **Modifier — düzenleyici varyant** | İfade dozunu değiştiren kodlamayan varyant | Hayır (düşük penetrans) | Fonksiyonel (enhancer aktivitesi) + ilişkilendirme | *RET* intron 1 (Emison 2005) |
| **Poligenik yük** | Çok sayıda küçük etkili varyant toplamı | Hayır (tek tek) | Poligenik skor; ampirik risk | Kompleks hastalıklar |

Tablonun okunma biçimi şudur: yukarıdan aşağı inildikçe her bir varyantın tek başına taşıdığı bilgi azalır, buna karşılık iddiayı kurmak için gereken **popülasyon düzeyinde kanıt** artar. İkinci ve üçüncü satırlar için aile-temelli kanıt (birlikte ayrışma) belirleyiciyken, alt satırlar için büyük kohortlar ve istatistiksel ilişkilendirme gerekir. Klinik laboratuvar pratiğinde ilk satır rutin olarak raporlanır; ortadaki satırlar dikkatli bir gerekçeyle raporlanabilir; son satırlar ise tanısal rapordan çok araştırma ve prognoz bağlamına aittir.

---

## 4. Klinik fenotipe dönüşüm

### 4.1 Tekrarlanma riski: tek bir evrensel oran neden yetmez?

Bu bölümün genetik danışmaya en doğrudan etkisi, **tekrarlanma riskinin hesaplanma biçimidir**. Tam penetranslı klasik tek-lokus modellerinde ebeveyn genotipleri biliniyorsa aktarım olasılığı çoğu kez kısa bir oranla özetlenebilir; örneğin iki heterozigot ebeveynden doğan otozomal resesif bir çocuk için hastalık genotipi olasılığı %25'tir. Zorunlu digenik kalıtım da Mendel ayrışmasının dışında değildir, fakat hesap **iki lokusun birlikte oluşması gereken genotipine** göre kurulur; bu nedenle bütün digenik ailelere uygulanabilecek tek bir yüzde yoktur. Şekil 15.2'deki temsili senaryoda iki bağımsız 1/2 aktarımın çarpımı %25 eder. Bu yalnız o ebeveyn düzeninin genotipik aktarım olasılığıdır; klinik yineleme riski penetrans, iki lokus arasındaki bağlantı ve fenokopi gibi etkenler hesaba katılmadan bu sayıya eşitlenmemelidir.

Oligogenik ve modifier'a bağlı tablolarda ise durum daha zordur: **bütün ailelere uygulanabilecek genel bir oran yoktur.** Düzenlenmeye özgü, tam metinden doğrulanmış ampirik veri varsa koşullarıyla birlikte kullanılabilir; yoksa belirsizlik açıkça söylenir ve risk aile öyküsü ile uygun kohort verileri üzerinden nitel ya da aralıklı biçimde tartışılır.

### 4.2 Penetrans: taşıyıcı olmak hasta olmak değildir

Oligogenik mimarinin en tipik klinik yansıması **eksik penetranstır**. Ana lokusta patojen varyantı taşıyan bir birey, ek katkılar eşiğe ulaşmadığı için sağlıklı kalabilir. Bölüm 1'de bu olguyu tanımlamış ve Cooper ve arkadaşlarının derlemesine dayanmıştık (Cooper ve ark., 2013); bu bölüm o tanımın altına mekanizma koyar — penetransın bir kısmı, ana genin dışındaki genetik bağlamdır.

Aynı olgu monogenik diyabet tablolarında da iyi belgelenmiştir. Monogenik diyabet formlarında eksik penetrans ve değişken ekspresivite yaygın olarak görülür; bu, hem tanıyı hem hastalık yönetimini zorlaştırır. Ancak bu değişkenliği yaratan modifiye edici varyantların tanımlanması yalnızca bir sorun değil, aynı zamanda bir fırsattır: **koruyucu** genetik varyantların belirlenmesi, daha yaygın diyabet formlarının mekanizmalarını aydınlatabilir ve yeni tedavi stratejilerine işaret edebilir (Li ve ark., 2023).

### 4.3 Ekspresivite: "aynı varyant, neden kardeşimde daha hafif?"

Klinikte en sık sorulan sorulardan biridir ve ailelerin en çok zorlandığı belirsizliktir. Cevabın bir kısmı Bölüm 12'de gördüğümüz mozaikliktir, bir kısmı Bölüm 11'deki heteroplazmidir; ama nükleer, konstitüsyonel bir varyantın söz konusu olduğu durumlarda cevap çoğu zaman **modifiye edici genetik bağlamdır**. SMA'da bu bağlam ölçülebilir bir sayıya (*SMN2* kopya sayısı) indirgenebildiği için istisnai biçimde nettir; çoğu hastalıkta ise henüz böyle bir "sayaç" yoktur.

**Algoritma 15.1 — Beklenmedik fenotip ağırlığında modifiye edici arayışı**

```mermaid
flowchart TD
  A["Hastada ana lokusta patojen varyant var<br/>ama fenotip beklenenden FARKLI"] --> B{"Fark hangi yönde?"}
  B -->|"Beklenenden HAFİF"| C{"Ölçülebilir bir<br/>modifier var mı?"}
  B -->|"Beklenenden AĞIR"| D["Ek yük ara:<br/>ikinci lokus, düzenleyici varyant,<br/>çevresel faktör"]
  B -->|"Taşıyıcı ama SAĞLIKLI"| E["Eksik penetrans:<br/>toplam yük eşiğin altında"]

  C -->|"Evet — ör. SMN2 kopya sayısı"| F["Ölç ve prognoza kat<br/>(tedavi kararını etkileyebilir)"]
  C -->|"Hayır"| G["Bilinen modifier lokusları tara<br/>(ör. KF'de akciğer modifier'ları)"]

  D --> H["Fenotibi TEK varyantla açıklamakta<br/>ısrar etme: ikinci lokus olasılığını<br/>açıkça değerlendir"]
  E --> I["Aileye: 'taşıyıcı ≠ hasta'<br/>+ izlem planı"]

  F --> J["Danışma: belirsizliği<br/>açıkça ifade et; genel oran verme"]
  G --> J
  H --> J
  I --> J
```

### 4.4 Ne zaman digenik/oligogenik düşünmeli?

Şüpheyi tetikleyen örüntüler şunlardır: klinik olarak güçlü bir tanıda tek gende bulunan varyantın **fenotibi tam açıklayamaması**; ailede kalıtım kalıbının hiçbir Mendel modeline oturmaması; aynı varyantı taşıyan akrabalar arasında **açıklanamayan penetrans farkı**; bilinen bir resesif hastalıkta iki patojen alel taşıyan sağlıklı bireylerin gösterilmesi; ve fenotibin bilinen tabloya göre olağandışı biçimde ağır olması. Bu örüntüler tek başlarına tanı koydurmaz, ancak analiz stratejisini genişletmeyi gerektirir.

Aşağıdaki akış, eldeki gözlemlerden hangi mimarinin düşünülmesi gerektiğini ayırt etmeye yarar. Dikkat edilmesi gereken nokta, ilk dallanmanın **varyantların aynı gende mi farklı genlerde mi olduğu** sorusu olmasıdır; pedigri görüntüsü tek başına ayırt edici değildir.

**Algoritma 15.2 — Digenik ve oligogenik kalıtımın ayırt edilmesi**

```mermaid
flowchart TD
  A["İki sağlıklı ebeveyn,<br/>hasta çocuk"] --> B{"Patojen varyantlar<br/>NEREDE?"}
  B -->|"AYNI genin iki alelinde"| C["Otozomal resesif<br/>→ tekrarlanma riski %25"]
  B -->|"FARKLI genlerde"| D{"Her biri tek başına<br/>hastalık yapıyor mu?"}
  B -->|"Aynı gende 2 + başka gende 1"| E["TRİALELİK olasılığı<br/>(ör. BBS)"]

  D -->|"Evet, biri yeterli"| F["Rastlantısal ikinci bulgu<br/>→ tek gen nedensel;<br/>diğeri ikincil bulgu"]
  D -->|"Hayır, hiçbiri yetmez"| G["DİGENİK olasılığı<br/>→ altı basamaklı kontrol listesine geç"]

  H["Ana lokusta patojen varyant VAR<br/>ama fenotip beklenenden farklı"] --> I{"Fark yönü?"}
  I -->|"Taşıyıcı ama sağlıklı"| J["Eksik penetrans<br/>→ OLİGOGENİK / modifier yükü"]
  I -->|"Hasta ama hafif/ağır"| K["Değişken ekspresivite<br/>→ MODIFIER perspektifi"]

  C --> L["Doğrulama: ailede segregasyon"]
  E --> L
  G --> L
  J --> L
  K --> L
  L --> M["Uyarı: pedigri görüntüsü<br/>digenik ile resesifi AYIRT ETMEZ;<br/>ayrım lokus konumundan gelir"]
```

---

## 5. Tanısal testlerle ilişkisi

Bu bölümde testin kendisinden çok **analiz stratejisi** belirleyicidir: aynı WES/WGS verisi, tek-gen varsayımıyla analiz edildiğinde negatif, çift-lokus/yük perspektifiyle analiz edildiğinde bilgilendirici olabilir. Ayrıca aile örneklerinin (trio veya genişletilmiş aile) değeri bu bölümde diğer bütün bölümlerden daha yüksektir.

**Tablo 15.3 — Çok-lokuslu mimarileri hangi test yakalar?**

| Test | Bu mekanizmayı yakalar mı? | Sınırlılığı |
|------|----------------------------|-------------|
| **WES** | Kısmen — iki farklı gendeki kodlayan varyantları aynı anda görebilir; digenik keşiflerin çoğu bu yolla yapılmıştır | Analiz tek-gen filtreleriyle yapılırsa çift-lokus örüntüsü gözden kaçar; kodlamayan modifier'ları göremez |
| **Short-read WGS** | Evet — kodlayan + kodlamayan modifier'ları (ör. *RET* intron 1) kapsar | Yorum sorunu büyür: her genomda çok sayıda nadir varyant vardır; seçicilik şart |
| **Long-read WGS** | Evet; ayrıca kopya sayısı/paralog ayrımını (ör. *SMN1* vs *SMN2*) daha güvenilir çözer | Maliyet ve erişim |
| **Array-CGH / SNP array** | Kısmen — modifier olarak iş gören CNV'leri ve kopya sayısı farklarını yakalar | Tek nükleotid düzeyindeki modifier'ları göremez |
| **MLPA** | **Evet — hedefliyse çok değerli.** *SMN2* kopya sayısı tayininde standart yaklaşımdır | Yalnız tasarlanan lokus; genom geneli bilgi vermez |
| **RNA-seq** | Dolaylı — modifier'ın ifade üzerindeki etkisini ve alel dengesizliğini gösterebilir | Doğru doku gerekir (Bölüm 13); nedensellik kurmaz |
| **Methylation array** | Genellikle hayır | Bu mekanizmalar için yerleşik tanısal rolü yoktur |
| **Karyotip** | Hayır | Çözünürlük yetersiz |
| **(mimariye özgü) Aile analizi ± hedefli doz testi** | **Evet — belirleyici.** Genişletilmiş aile segregasyonu digenik iddianın omurgasıdır; *SMN2* gibi doz modifier'ları hedefli ölçülür | Aile üyelerine erişim gerekir; tek olgu (singleton) analizinde en zayıf nokta budur |

> **Bu mekanizmayı hangi test yakalar? (özet):** Digenik/oligogenik şüphesinde belirleyici olan yeni bir cihaz değil, **veriye bakış biçimi ve aile örnekleridir**. Pratik sıra: WES/WGS verisini tek-gen filtresinin ötesinde (aday gen çiftleri, ortak yolak, yük analizi) yeniden değerlendir; **genişletilmiş aileden örnek** al ve birlikte ayrışmayı test et; ölçülebilir bir doz modifier'ı varsa (ör. *SMN2*) hedefli olarak ölç.

> **🟦 Klinikte dikkat — Aile örneği burada lükse değil, zorunluluğa yakındır:** Digenik bir iddianın en güçlü klinik kanıtı, **yalnızca çift-taşıyıcıların hasta, tek-taşıyıcı akrabaların sağlıklı olduğunun gösterilmesidir**. Tek bir hastadan (singleton) elde edilen veriyle bu gösterilemez. Bu nedenle çift-lokus şüphesi doğduğunda, mümkün olan en geniş aile örneklemesi hedeflenmelidir.

---

## 6. Varyant yorumlama açısından önemi (ACMG/ClinGen)

ACMG/AMP önerileri, klinik laboratuvarda saptanan varyantların özellikle **Mendelci hastalıklar** bağlamında sınıflandırılması için geliştirilmiştir; kılavuz, çok-genli Mendelci olmayan kompleks hastalıklarla ilişkili genlerdeki varyantların yorumlanmasını kendi amaç kapsamı dışında bırakır ve aday genlerde kuralların dikkatle uygulanmasını ister (Richards ve ark., 2015). Dolayısıyla iki varyantın her birine ayrı ACMG/AMP etiketi vermek, varyant çiftinin zorunlu digenik nedenselliğini kendiliğinden kanıtlamaz. Aşağıdaki “tek-lokus baskısı” anlatımı kılavuzun kendi terimi değil, bu kapsam sınırının digenik olguda yarattığı sorunu görünür kılan **pedagojik bir çıkarımdır** (Şekil 15.4).

![Şekil 15.4 — "Bu hastalık digenik" demek için ne gerekir?](assets/sekil_53_digenik_kanit_hiyerarsisi.svg)

**Birinci sıkışma sınıflandırmadadır.** Digenik bir çiftte hiçbir varyant tek başına yeterli olmayabilir; buna karşılık bir varyant, aynı genin başka hastalıkları için tek başına sınıflandırılabilir. Bu nedenle tek tek varyant sınıfları ile **varyant çiftinin belirli fenotipteki nedenselliği** aynı önerme değildir. Pratik çözüm, her varyantın sınıfını ve gen–hastalık bağlamını ayrı vermek; ardından çift-lokus hipotezini, kanıt basamakları ve belirsizlik düzeyiyle ayrı bir sonuç cümlesinde açıklamaktır.

**İkinci sıkışma segregasyon kriterindedir.** Tek gene odaklanan bir segregasyon analizi, zorunlu digenik bir ailede tek-varyant taşıyıcılarını “uyumsuz” gösterebilir. Bu gözlem tek başına varyantın masum olduğunu da ikinci lokusun nedensel olduğunu da kanıtlamaz; iki lokusun genotipi, yaşa bağlı penetrans, fenokopi ve eksik genotipleme birlikte değerlendirilmelidir. Digenik hipotezin aile içi sınaması, yalnız etkilenmişleri değil mümkün olduğunca çok etkilenmemiş birinci derece akrabayı da iki lokus bakımından karşılaştırmalıdır (Schäffer, 2013).

Bu zorluklar karşısında dayanılacak ilke, gen–hastalık ilişkisinin geçerliliğini değerlendirmek için geliştirilen genel standartlardan gelir: nedensellik iddiası tek bir gözleme dayandırılmamalı; olgu–kontrol karşılaştırması, segregasyon, bağımsız tekrar ve biyolojik olarak uygun fonksiyonel kanıt birlikte tartılmalıdır (MacArthur ve ark., 2014). Digenik iddia için bu genel ilkeler, aşağıdaki altı basamakta somutlaştırılmıştır.

> **🏷️ Pedagojik sentez — Digenik iddia için altı basamaklı kontrol listesi.** Bu altı basamak resmî bir ACMG/ClinGen sınıflandırması veya puanlama sistemi değildir. Bileşenleri digenik kalıtım derlemesindeki kanıt alanları ile nadir varyant nedenselliği için önerilen genel ilkelerden türetilmiş; sıralama ve gruplama bu kitabın editöryal sentezi olarak yapılmıştır (Schäffer, 2013; MacArthur ve ark., 2014; Richards ve ark., 2015). **“İki gende varyant bulduk” bir gözlemdir, digenik tanı değildir.** Güçlü bir zorunlu digenik iddia kurulmadan önce şu altı sorunun her biri yanıtlanmalıdır:
>
> 1. **Her iki genin hastalıkla ilişkisi geçerli mi?** Her gen için, iddia edilen fenotip ve allelik gereksinim bağlamında bağımsız gen-düzeyi kanıt aranır. Yalnız ağ yakınlığı veya *in silico* öngörü, bir geni hastalık geni yapmaz.
> 2. **Tek-lokuslu açıklama neden yetersiz?** Bilinen genler ve uygun transkriptler yeterli kapsamayla incelenmiş; faz, CNV/yapısal varyant, kodlamayan veya splice değişikliği, mozaiklik, mitokondriyal neden ve fenokopi gibi daha yalın açıklamalar sistematik biçimde değerlendirilmiş olmalıdır.
> 3. **Çift genotip popülasyon ve aile verisiyle destekleniyor mu?** Varyantların ve çiftin soyla uyumlu kontrol popülasyonlarındaki sıklığı, rastlantısal birlikte bulunma olasılığı ve iki-lokuslu segregasyon incelenir. Model zorunlu digenikse çift genotipin etkilenmişlerle birlikte ayrışması, tek-varyant taşıyıcılarının ise modelin öngördüğü fenotipi göstermesi beklenir; yaş ve penetrans hesaba katılır.
> 4. **Bağımsız tekrar var mı?** Aynı gen çifti ve uyumlu fenotip, akraba olmayan aile veya kohortlarda yeniden gösterilmelidir. Tek aile, özellikle küçük ve eksik örneklenmişse, kesin nedensellik için kırılgan kalır.
> 5. **Ortak etki doğrudan sınandı mı?** Hastalıkla ilgili bir sistemde **yabanıl tip, yalnız A, yalnız B ve A+B** koşulları karşılaştırılır. Deney, yalnız her varyantın zararını değil, birleşimin iddia edilen modele özgü ek veya eşik-aşan etkisini göstermelidir; biyolojik yakınlık tek başına ortak nedensellik değildir.
> 6. **Rakip iki-lokus açıklamaları dışlandı mı?** Tek bir hastalığın zorunlu digenik modeli; **monogenik hastalık + modifier**, **iki bağımsız/örtüşen tanı (dual veya blended diagnosis)**, poligenik arka plan ve rastlantısal ikinci VUS ile açıkça karşılaştırılır.
>
> Bu liste bir “altı kutudan altısı işaretlenirse kesin tanı” kuralı değildir; kanıtın niteliği ve modelle uyumu tartılır. Özellikle yeni veya yalnız küçük ailelere dayanan bir iddiada, karşılaştırmalı ortak-etki ve bağımsız tekrar eksikse sonuç **“aday/olası digenik model”** düzeyinde tutulmalı; “kesin digenik tanı” diye raporlanmamalıdır. Schäffer'in tam metin derlemesi, ikna edici örneklerde pedigri, protein–protein/protein–DNA ilişkisi ve özgül fonksiyonel ya da hayvan modeli kanıtının önemini; yüksek verimli dizilemenin tek başına kalıtım biçimini kanıtlamadığını vurgular.

> **🔬 Deep-dive — Yüksek verimli dizileme neden digenik keşfi otomatik olarak kolaylaştırmadı?** Sezgisel beklenti şuydu: bir örnekte aynı anda iki gendeki varyantları görebilen bir teknoloji, digenik kalıtımın kanıtlanmasını da kolaylaştırmalıydı. Schäffer, 2012 sonuna kadarki literatürü tarayarak bu beklentinin gerçekleşmediğini gösterdi: dar bir tanım kullanıldığında insan digenik kalıtımı için kanıt taşıyan fenotip sayısı, monogenik hastalıklardaki binlerce bildirimin yanında yalnızca birkaç düzineyle sınırlıydı; üstelik yüksek verimli dizilemenin kullanıldığı örnek sayısı son derece azdı (Schäffer, 2013). Nedeni istatistikseldir: monogenik bir keşifte aranan şey "bir gende beklenenden fazla varyant birikimi"dir; digenik keşifte ise **gen çiftleri** aranır ve olası çift sayısı gen sayısının karesiyle büyür. Bu, çoklu karşılaştırma yükünü ve rastlantısal birlikteliği dramatik biçimde artırır. Bu yüzden alanın ilerlemesi ham dizileme gücünden çok, **arama uzayını daraltan önsel bilgiden** (bilinen etkileşim ağları, ortak yolaklar, aday gen listeleri) gelmektedir. Klinik karşılığı nettir: bir digenik hipotezi, önce biyolojiyle daraltılmalı, sonra veriyle sınanmalıdır — tersi değil.

---

## 7. Pediatrik genetikten klinik örnekler

**Digenik retinitis pigmentosa — kavramın doğduğu yer.** Üç ilgisiz ailede, birbirine bağlantısız *peripherin/RDS* ve *ROM1* genlerinde varyantlar saptanmış; yalnızca her iki varyantı birden taşıyan çift heterozigotlar retinitis pigmentosa geliştirmiştir (Kajiwara ve ark., 1994). **Öğreti:** iki proteinin aynı yapısal komplekste buluşması, digenik iddiayı mekanik olarak anlaşılır kılan şeydir; biyolojik bağ olmadan digenik iddia zayıftır.

**Bardet-Biedl sendromu — kalıtım modelinin sorgulanması.** 163 aileden oluşan bir kohortta dört ailede etkilenmiş bireylerin *BBS2* ve *BBS6*'da toplam üç mutant alel taşıdığı; buna karşılık iki ailede *BBS2*'de iki mutant alel taşıyan bireylerin **etkilenmemiş** olduğu gösterilmiştir (Katsanis ve ark., 2001). **Öğreti:** "iki patojen alel = hasta" denklemi her resesif hastalıkta otomatik geçerli değildir; sağlıklı iki-alelli bireylerin varlığı, ek bir lokusun aranması gerektiğinin en güçlü işaretidir.

**Spinal musküler atrofi — ölçülebilir modifier.** Ana kusur bütün hastalarda *SMN1* kaybıdır; klinik tipi belirleyen esas değişken *SMN2* kopya sayısıdır. 625 İspanyol hastanın analizi ve 2.834 bildirilmiş olgunun derlenmesiyle oluşturulan 3.459 hastalık veri seti, kopya sayısı ile SMA tipi arasındaki ilişkiyi prognostik kurallar hâlinde ortaya koymuştur (Calucho ve ark., 2018). **Öğreti:** modifier her zaman soyut bir "genetik bağlam" değildir; bazen doğrudan ölçülebilen ve klinik kararı değiştiren bir sayıdır. SMA'da kopya sayısı tayini, yenidoğan taraması sonrası tedavi kararlarında ve klinik çalışma katmanlandırmasında kullanılmaktadır.

**Kistik fibroz — aynı genotip, farklı akciğer.** 6.365 hastalık GWAS meta-analizinde akciğer hastalığı ağırlığıyla ilişkili beş lokus tanımlanmıştır: *MUC4/MUC20*, *SLC9A3*, HLA sınıf II, *AGTR2/SLC6A14* ve *EHF/APIP* (Corvol ve ark., 2015). **Öğreti:** hastalığı **başlatan** gen ile hastalığın **seyrini belirleyen** genler farklıdır; bu ayrım hem prognoz konuşmasını hem tedavi hedefi arayışını değiştirir.

**Hirschsprung hastalığı — kodlamayan modifier ve düşük penetrans.** *RET*'in intron 1'indeki korunmuş enhancer-benzeri dizide yer alan yaygın bir kodlamayan varyant, hastalık yatkınlığıyla anlamlı biçimde ilişkilidir ve riske katkısı nadir kodlayan alellerden yaklaşık 20 kat büyüktür; varyant *in vitro* enhancer aktivitesini azaltır, düşük penetrans gösterir ve cinsiyete göre farklı etki yaratır (Emison ve ark., 2005). **Öğreti:** bu örnek Bölüm 4 (RET'in iki yüzü), Bölüm 13 (kodlamayan/enhancer) ve bu bölümü (modifier/düşük penetrans) tek bir lokusta birleştirir — ve yaygın, düşük penetranslı varyantların hem sık hem nadir hastalıkların temelinde yatabileceğini gösterir.

**Monogenik diyabet — modifiye edici varyantlar fırsat olarak.** Monogenik diyabet formlarında eksik penetrans ve değişken ekspresivite yaygındır; bunları belirleyen genetik modifiye edicilerin tanımlanması hem tanı zorluğunu açıklar hem de **koruyucu** varyantların keşfi yoluyla yeni tedavi hedeflerine işaret edebilir (Li ve ark., 2023). **Öğreti:** modifier araştırması yalnızca "neden bu hasta farklı?" sorusunu yanıtlamaz; koruyucu yönü bulmak, doğanın kendi tedavi denemesini okumaktır.

---

## 8. Sık yapılan hatalar ve klinikte dikkat

> **🔴 Sık yapılan hata kutusu**
> 1. **"İki gende VUS bulundu, hastalık digeniktir."** Bu bir gözlemdir, sonuç değil. Her genomda çok sayıda nadir varyant vardır; biyolojik bağ, birlikte ayrışma ve tekrarlanma gösterilmeden digenik denemez.
> 2. **"Ebeveynler sağlıklı, o hâlde otozomal resesif."** Digenik kalıtımın pedigri imzası resesifle **birebir aynıdır**. Ayrım pedigriden değil, varyantların farklı lokuslarda olmasından ve tek başlarına hastalık yapmadıklarının gösterilmesinden gelir.
> 3. **"Varyantı taşıyan sağlıklı akraba var, demek ki varyant patojen değil."** Eksik penetrans oligogenik mimarilerde kuraldır. Segregasyon uyumsuzluğu, ikinci bir lokusun varlığına işaret ediyor olabilir.
> 4. **"Digenik hastalıkta risk her zaman %25'tir."** Değildir. Risk, ebeveynlerin iki lokustaki genotiplerine, bağlantıya ve penetransa göre aileye özgü hesaplanır; bazı eşleşmelerde genotipik aktarım olasılığı tesadüfen %25 çıkabilir.
> 5. **"Modifier bulundu, bu hastalığın nedeni."** Modifier hastalığı **yapmaz**; ağırlığını değiştirir. Tanısal raporda "neden" olarak sunulması yanlıştır.
> 6. **"Aynı *CFTR* genotipi, aynı seyir."** Akciğer hastalığı ağırlığı modifiye edici lokuslarla belirgin biçimde değişir; genotipten kesin prognoz vaat edilmemelidir.
> 7. **"SMA tanısı kondu, *SMN2* kopya sayısına gerek yok."** Kopya sayısı prognozu ve tedavi kararlarını doğrudan etkiler; SMA'da modifier ölçümü tanının ayrılmaz parçasıdır.
> 8. **"Tek hastadan digenik kalıtım kesinleştirilebilir."** Kesinleştirilemez. Tek olgu bir aday model doğurabilir; birlikte ayrışmayı göstermek için aile örnekleri, iddiayı sağlamlaştırmak için bağımsız aileler ve modele uygun işlevsel kanıt gerekir.

> **🟦 Klinikte dikkat kutusu**
> - Klinik tanı güçlü ama tek gendeki varyant fenotibi tam açıklamıyorsa, veriyi **tek-gen filtresinin ötesinde** yeniden değerlendirin (aday gen çiftleri, ortak yolak, yük perspektifi).
> - Çift-lokus şüphesinde **genişletilmiş aile örneklemesi** planlayın; singleton veriyle bu iddia kurulamaz.
> - SMA'da *SMN2* kopya sayısı, KF'de bilinen modifiye edici bilgiler prognoz konuşmasına dâhil edilmelidir.
> - Danışmada belirsizliği açıkça ifade edin: oligogenik/modifier tablolarda düzenlenmeye özgü, tam metinden doğrulanmış ampirik veri yoksa **genel bir tekrarlanma yüzdesi vermeyin**.
> - "Taşıyıcı ≠ hasta" mesajı, eksik penetranslı ailelerde en sık gereken ve en sık atlanan cümledir; izlem planıyla birlikte verilmelidir.
> - Modifiye edici bulgular tanısal rapordan ayrı, **prognoz/araştırma** başlığı altında sunulmalı; ailenin bunu "ikinci bir hastalık" olarak algılamaması sağlanmalıdır.

---

## 9. Klinik pratikte karar algoritması

**Algoritma 15.3 — Çok-lokus şüphesinde klinik karar akışı**

```mermaid
flowchart TD
  A["Güçlü klinik tanı<br/>+ genetik sonuç fenotibi TAM AÇIKLAMIYOR"] --> B{"Ana lokusta patojen<br/>varyant var mı?"}

  B -->|"Var ama fenotip<br/>beklenenden farklı"| C["MODIFIER perspektifi"]
  B -->|"Yok / yetersiz<br/>(ör. tek heterozigot)"| D["ÇOK-LOKUS perspektifi"]

  C --> E{"Ölçülebilir modifier<br/>biliniyor mu?"}
  E -->|"Evet (ör. SMN2 kopya sayısı)"| F["Hedefli ölç (MLPA) →<br/>prognoza ve tedavi kararına kat"]
  E -->|"Hayır"| G["Bilinen modifier lokuslarını<br/>değerlendir; yoksa belirsizliği<br/>açıkça raporla"]

  D --> H["WES/WGS verisini YENİDEN analiz et:<br/>aday gen çiftleri · ortak yolak ·<br/>protein–protein etkileşim ağları"]
  H --> I{"İki lokusta aday<br/>varyant çifti var mı?"}
  I -->|"Hayır"| J["Diğer kör noktalar:<br/>kodlamayan (Böl. 13), CNV (Böl. 8),<br/>mozaiklik (Böl. 12) → yeniden analiz"]
  I -->|"Evet"| K["ALTI BASAMAKLI KONTROL:<br/>gen ilişkisi · tek-lokus dışlama ·<br/>popülasyon/segregasyon · tekrar ·<br/>WT/A/B/A+B işlev · rakip model"]

  K --> L{"Kanıt eksenleri birlikte<br/>zorunlu digenik modeli<br/>yeterince destekliyor mu?"}
  L -->|"Hayır / test edilemedi"| P["Aday/olası digenik model —<br/>eksik kanıtı açıkla,<br/>yeniden analiz/araştırma planla"]
  L -->|"Evet"| Q["Güçlü digenik model:<br/>varyantları ayrı sınıflandır,<br/>çift-lokus kanıtını ayrıca sun"]

  F --> R["GENETİK DANIŞMA"]
  G --> R
  P --> R
  Q --> R
  R --> S["Digenik: aileye özgü iki-lokus aktarımı<br/>+ penetransla risk hesapla; evrensel oran verme<br/>Oligogenik/modifier: doğrulanmış ampirik veri yoksa<br/>kesin oran verme; izlem planı kur"]
```

---

## 10. Kaynaklar

> **Atıf / doğrulama notu:** Bu bölümün bibliyografik verileri PubMed üzerinden doğrulanmıştır; her kaynağın PMID ve DOI'si tek tek teyit edilmiştir. (Metin içinde yazar-yıl, kaynakçada DOI-link kullanılır.)

1. **Schäffer AA (2013).** Digenic inheritance in medical genetics. *Journal of Medical Genetics* 50(10):641–652. **PMID: 23785127** · DOI: [10.1136/jmedgenet-2013-101713](https://doi.org/10.1136/jmedgenet-2013-101713) — *Kullanım amacı: Bölümün ana çerçeve kaynağı; digenik kalıtımın tanımı, kanıt türleri, aday gen ve protein–protein etkileşim bilgisinin rolü, HTS'nin beklenen katkıyı neden sağlamadığı.*

2. **Kajiwara K, Berson EL, Dryja TP (1994).** Digenic retinitis pigmentosa due to mutations at the unlinked peripherin/RDS and ROM1 loci. *Science* 264(5165):1604–1608. **PMID: 8202715** · DOI: [10.1126/science.8202715](https://doi.org/10.1126/science.8202715) — *Kullanım amacı: Landmark — insan digenik kalıtımının ilk net gösterimi; yalnızca çift heterozigotların etkilenmesi.*

3. **Katsanis N, Ansley SJ, Badano JL, ve ark. (2001).** Triallelic inheritance in Bardet-Biedl syndrome, a Mendelian recessive disorder. *Science* 293(5538):2256–2259. **PMID: 11567139** · DOI: [10.1126/science.1063525](https://doi.org/10.1126/science.1063525) — *Kullanım amacı: Landmark — trialelik kalıtım; iki patojen alel taşıyan sağlıklı bireylerin gösterilmesi ve kalıtım modelinin sorgulanması.*

4. **Calucho M, Bernal S, Alías L, ve ark. (2018).** Correlation between SMA type and SMN2 copy number revisited: An analysis of 625 unrelated Spanish patients and a compilation of 2834 reported cases. *Neuromuscular Disorders* 28(3):208–215. **PMID: 29433793** · DOI: [10.1016/j.nmd.2018.01.003](https://doi.org/10.1016/j.nmd.2018.01.003) — *Kullanım amacı: Klinik/modifier — *SMN2* kopya sayısının SMA tipini belirlemesi; 3.459 hastalık derleme; prognostik ve tedavi kararına etkisi.*

5. **Corvol H, Blackman SM, Boëlle PY, ve ark. (2015).** Genome-wide association meta-analysis identifies five modifier loci of lung disease severity in cystic fibrosis. *Nature Communications* 6:8382. **PMID: 26417704** · DOI: [10.1038/ncomms9382](https://doi.org/10.1038/ncomms9382) — *Kullanım amacı: Klinik/modifier — 6.365 hastada beş modifiye edici lokus; aynı *CFTR* genotipinde değişken akciğer hastalığı.*

6. **Emison ES, McCallion AS, Kashuk CS, ve ark. (2005).** A common sex-dependent mutation in a RET enhancer underlies Hirschsprung disease risk. *Nature* 434(7035):857–863. **PMID: 15829955** · DOI: [10.1038/nature03467](https://doi.org/10.1038/nature03467) — *Kullanım amacı: Mekanizma/klinik — kodlamayan modifier; düşük penetrans; cinsiyete bağlı etki; nadir alellere göre ~20 kat büyük risk katkısı (Bölüm 13 köprüsü).*

7. **Li M, Popovic N, Wang Y, Chen C, Polychronakos C (2023).** Incomplete penetrance and variable expressivity in monogenic diabetes; a challenge but also an opportunity. *Reviews in Endocrine and Metabolic Disorders* 24(4):673–684. **PMID: 37165203** · DOI: [10.1007/s11154-023-09809-1](https://doi.org/10.1007/s11154-023-09809-1) — *Kullanım amacı: Klinik/kavramsal — monogenik hastalıkta eksik penetrans ve değişken ekspresivitenin modifiye edicilerle ilişkisi; koruyucu varyant fırsatı.*

8. **Cooper DN, Krawczak M, Polychronakos C, Tyler-Smith C, Kehrer-Sawatzki H (2013).** Where genotype is not predictive of phenotype: towards an understanding of the molecular basis of reduced penetrance in human inherited disease. *Human Genetics* 132(10):1077–1130. **PMID: 23820649** · DOI: [10.1007/s00439-013-1331-2](https://doi.org/10.1007/s00439-013-1331-2) — *Kullanım amacı: Kavramsal — eksik penetrans ve değişken ekspresivitenin moleküler temelleri. Kaynak kütüğünden yeniden kullanılmıştır (Bölüm 1 köprüsü).*

9. **MacArthur DG, Manolio TA, Dimmock DP, ve ark. (2014).** Guidelines for investigating causality of sequence variants in human disease. *Nature* 508(7497):469–476. **PMID: 24759409** · DOI: [10.1038/nature13127](https://doi.org/10.1038/nature13127) — *Kullanım amacı: Metodoloji — uygun kontrol popülasyonu, aile segregasyonu, bağımsız tekrar ve modele uygun fonksiyonel deneyle nedensellik iddiasının sınanması. Kaynak kütüğünden yeniden kullanılmıştır.*

10. **Richards S, Aziz N, Bale S, ve ark. (2015).** Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. *Genetics in Medicine* 17(5):405–424. **PMID: 25741868** · DOI: [10.1038/gim.2015.30](https://doi.org/10.1038/gim.2015.30) — *Kullanım amacı: Kılavuz — ACMG/AMP varyant sınıflandırmasının özellikle Mendelci hastalıklar için geliştirilmiş kapsamı; çok-genli Mendelci olmayan kompleks hastalıklar ve aday genler için açık kapsam/sakınım sınırı. Kaynak kütüğünden yeniden kullanılmıştır.*

11. **Sosnay PR, Siklosi KR, Van Goor F, ve ark. (2013).** Defining the disease liability of variants in the cystic fibrosis transmembrane conductance regulator gene. *Nature Genetics* 45(10):1160–1167. **PMID: 23974870** · DOI: [10.1038/ng.2745](https://doi.org/10.1038/ng.2745) — *Kullanım amacı: Klinik örnek — *CFTR* genotip–fenotip ilişkisinin sınırları. Kaynak kütüğünden yeniden kullanılmıştır (Bölüm 2 köprüsü).*

> **İkincil/destekleyici kaynak notu:** OMIM, ClinVar, gnomAD ve DIDA benzeri digenik varyant veri tabanları bu bölümde yalnızca destekleyici/başvuru kaynağı olarak anılmıştır; hiçbiri ana mekanizma kaynağı olarak kullanılmamıştır.

---

## ✅ Bölüm öz-denetim tablosu

**Tablo 15.4 — Bölüm 15 öz-denetim tablosu**

| Kriter | Durum | Not |
|--------|-------|-----|
| Mekanizma doğru anlatıldı mı? | ✅ | Süreklilik → eşik/yük modeli → digenik (ortak işlevsel havuz) → trialelik → modifier'ın dört yolu zinciri kuruldu |
| Klinik bağlantı kuruldu mu? | ✅ | Tekrarlanma riski, penetrans ve ekspresivite üzerinden; "taşıyıcı ≠ hasta" mesajı |
| Varyant tipi ile mekanizma ilişkilendirildi mi? | ✅ | 8 satırlık **rol** tablosu (nedensel/digenik/trialelik/oligogenik/3 tip modifier/poligenik) + kanıt gereksinimi |
| Pediatrik örnek verildi mi? | ✅ | Digenik RP, BBS, SMA (*SMN2*), KF modifier'ları, Hirschsprung (*RET*), monogenik diyabet — hepsi kaynaklı |
| Test seçimi açıklandı mı? | ✅ | Standart 8 satırlık tablo + aile analizi/hedefli doz satırı; "belirleyici olan analiz stratejisi ve aile örneği" vurgusu |
| ACMG/ClinGen bağlantısı doğru mu? | ✅ | Richards 2015'in gerçek kapsam cümlesi ayrıldı; “tek-lokus baskısı” kılavuz alıntısı değil pedagojik çıkarım olarak etiketlendi |
| Kaynaklar PMID/DOI ile verildi mi? | ✅ | 11/11 kaynak PMID + DOI-link + kullanım amacı ile (7 yeni doğrulama + 4 kütükten yeniden kullanım) |
| Spekülatif iddialar işaretlendi mi? | ✅ | Trialelik kalıtımın BBS'deki kapsamı/genelleştirilebilirliği ⚠️ ile işaretlendi |
| Kaynak uydurma riski var mı? | ✅ Yok | 7 yeni PMID/DOI bu oturumda PubMed MCP ile tek tek doğrulandı; 4'ü daha önce doğrulanmış kütük kaydı |
| Görsel/şema/algoritma desteği yeterli mi? (≥3 SVG, ≥2 Mermaid) | ✅ | **4 SVG + 3 Mermaid**; tüm SVG'ler PNG'ye render edilip gözle denetlendi (eşik paneli yeniden tasarlandı) |

---

### 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu)
> "Bu bölümdeki her kaynağın **türüne uygun kalıcı kimliğini** kontrol et: hakemli makalede PMID + DOI; kılavuz/uzman panel spesifikasyonunda kurum + sürüm + tarih + kalıcı bağlantı; veri tabanında veri sürümü + sorgu tarihi. Kimliği doğrulanamayan kaynağı çıkar. Kaynağı olmayan spesifik iddiayı 'kaynak doğrulaması gerekli' olarak işaretle. Kitabın kendi pedagojik çerçevesini doğrulamaya çalışma — 🏷️ ile etiketle." *(Politika 01.08.2026 uzman turunda güncellendi: eski 'PMID veya DOI veremediğin kaynağı çıkar' kuralı HGVS, ClinGen/CSpec, gnomAD sürüm notları gibi PMID'siz ama yetkili kaynakları dışlıyordu.)*
>
> **Bibliyografik:** **11/11 hakemli makalenin PMID+DOI künyesi doğrulandı.**
>
> **İddia düzeyi:** Bölüm 03.08.2026'da yeniden denetlendi. Altı basamaklı kontrol listesini taşıyan Schäffer 2013, MacArthur 2014 ve Richards 2015 ana metinleri incelendi; toplam 11 kaynağın altısı için PMC ana metni erişilebildi, beş telifli makalenin NCBI/PMC ana metni erişilemedi. Yeni kontrol listesi erişilemeyen bir tam metne dayandırılmadı. Denetimde digenik riskin “%25 değildir” diye mutlaklaştırıldığı gerçek bir hesap hatası bulundu ve metin/şekil/algoritmalarda düzeltildi (bkz. `Dogrulama_Kutugu.md`).
>
> **İşaretlenen iddialar:** (1) Trialelik kalıtımın Bardet-Biedl sendromundaki kapsamı ve genelleştirilebilirliği ⚠️ tartışmalıdır; modelin her ailede geçerli olduğu varsayılmamalıdır. (2) Monogenik–digenik–oligogenik–poligenik ayrımının “keskin biyolojik sınırı olmadığı” kavramsal bir çerçevedir. (3) 🏷️ Altı basamaklı digenik iddia kontrol listesi resmî ACMG/ClinGen standardı değil, bileşenleri kaynaklı editöryal sentezdir. (4) Digenik genotipik aktarım olasılığı aileye özgü hesaplanmalı; klinik yineleme riski penetrans ve bağlantı hesaba katılmadan buna eşitlenmemelidir.
