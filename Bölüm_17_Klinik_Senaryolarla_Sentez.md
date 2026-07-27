# Bölüm 17 — Klinik Senaryolarla Sentez: Hastadan Mekanizmaya

> **Bölümün çekirdek tezi:** Bu kitap on altı bölüm boyunca tek yönde ilerledi: mekanizmadan kliniğe. Önce moleküler kusuru tanımladık, sonra hücresel sonucunu, sonra fenotibi, sonra testi ve yorumu. Klinik pratik ise **ters yönde** çalışır: karşınızda bir hasta vardır ve mekanizmayı bilmezsiniz. Bu bölüm, kitabın bütün içeriğini bu ters yöne çevirir ve tek bir soruya indirger: **elimdeki klinik tablo, hangi mekanizmayı düşündürüyor ve o mekanizmayı hangi test görebilir?** Bölümün ikinci tezi buradan doğar: genetik tanı bir test sonucu değil, bir **akıl yürütme zinciridir** — fenotip, mekanizma hipotezi, test seçimi, varyant, kanıt, sınıflandırma ve danışma halkalarından oluşur; ve zincirin gücü en zayıf halkası kadardır. Üçüncü tez, gündelik pratiğin en yanlış anlaşılan cümlesiyle ilgilidir: **"genetik test negatif" bir tanı değil, bir zaman damgasıdır.** Negatiflik çoğu zaman "genetik neden yok" anlamına gelmez; "kullandığım yöntemin göremediği bir yerde olabilir" anlamına gelir — ve bu kör noktalar, kitabın önceki bölümlerinde tek tek öğrenildiği için önceden bilinebilir ve sırayla kapatılabilir.

> **Bu bölüm nasıl okunmalı?** Bu bölüm kitabın **kapanış ve tekrar bölümüdür**; yeni bir mekanizma öğretmez, öğrenilenleri hastanın başında kullanılabilir hâle getirir. Tıp öğrencileri için 7. başlıktaki sekiz senaryo, kitabın tamamının somut bir özetidir; her senaryonun sonundaki "öğreti" cümlesi ilgili bölüme geri gönderir. Klinisyenler için 2., 4. ve 5. başlıklar ile Şekil 17.1–17.2 doğrudan poliklinik pratiğine aittir. Uzmanlık öğrencileri ve genetik danışmanlar için 9. başlıktaki ana algoritma, bir olguyu baştan sona götürmenin kontrol listesidir. Kitabı baştan okuyan biri için bu bölüm, bir sınav provası gibi de kullanılabilir: her senaryoda önce kendi mekanizma hipotezinizi kurun, sonra metne bakın.

> 🖼️ **Görseller hakkında not:** Şekil 17.1–17.4 `assets/` klasöründe SVG olarak bulunur. Mermaid diyagramları metin içine gömülüdür.

---

## Öğrenme hedefleri

Bu bölümü tamamlayan okuyucu:
1. Klinik akıl yürütmenin yönünü (fenotip → mekanizma → test → varyant → yorum → danışma) tanımlar ve her halkanın hangi bölüme karşılık geldiğini gösterir.
2. Yaygın klinik ipuçlarını (asimetrik tutulum, anticipasyon, maternal kalıtım, büyüme asimetrisi, aynı ailede değişken ağırlık) aday mekanizmalara çevirir.
3. Derin fenotiplemenin tanısal getiriye katkısını açıklar ve standart fenotip terminolojisinin rolünü belirtir.
4. Ekzom/genom dizilemenin altı kör noktasını sayar ve her biri için doğru ikinci basamak testi seçer.
5. "Negatif sonuç" karşısında basamaklı bir strateji kurar ve yeniden analizin beklenen getirisini sayısal olarak ifade eder.
6. Trio analizinin ve doku seçiminin tanısal getiriye etkisini açıklar.
7. Sekiz farklı pediatrik senaryoda mekanizma hipotezini kurar, uygun testi seçer ve sonucu doğru kriterlerle yorumlar.
8. Tanısal zincirin en sık kırıldığı üç noktayı tanır ve bunları önlemek için pratik önlemleri sıralar.
9. Bir olguyu başvurudan danışmaya kadar götüren bütünleşik bir algoritma uygular.

---

## 1. Kavramsal tanım: akıl yürütmenin yönü

Klinik genetikte iki farklı düşünme biçimi bir arada kullanılır ve ikisi de gereklidir.

**Örüntü tanıma**, deneyimli klinisyenin gücüdür: hastanın yüzü, duruşu, el bulguları ve öyküsü bir araya gelir ve akla belirli bir sendrom gelir. Hızlıdır, çoğu zaman doğrudur ve tanınabilir sendromlarda hâlâ en verimli yoldur. Ancak iki sınırı vardır: tanımadığınız bir sendromu tanıyamazsınız ve örüntü size **hangi testi isteyeceğinizi** her zaman söylemez.

**Mekanizmacı akıl yürütme** ise bu kitabın öğrettiği yoldur ve tam olarak bu iki boşluğu kapatır. Sendromun adını bilmeseniz bile, klinik bulgular size **hangi moleküler mekanizmanın** iş başında olabileceğini söyler; mekanizma da hangi testin o kusuru görebileceğini belirler. Asimetrik, çizgisel bir tutulum gördüğünüzde aklınıza gelen şey bir sendrom adı olmayabilir — ama "postzigotik bir olay olmuş olabilir" düşüncesi, kandan değil **etkilenmiş dokudan** örnek almanızı sağlar ve tanıyı kurtarır.

Şekil 17.1, bu çeviriyi sistematik hâle getirir.

![Şekil 17.1 — Klinik ipucundan mekanizmaya: hastadan geriye doğru okumak](assets/sekil_58_klinik_ipucu_mekanizma.svg)

Bu çevirinin ön koşulu **derin fenotiplemedir**. Fenotibi ne kadar ayrıntılı ve ne kadar standart biçimde kaydederseniz, hem mekanizma hipoteziniz o kadar keskinleşir hem de laboratuvarın varyant önceliklendirmesi o kadar isabetli olur. Bu amaçla geliştirilen İnsan Fenotip Ontolojisi (Human Phenotype Ontology, HPO), insan hastalıklarında görülen fenotipik anormallikleri tanımlamak ve hesaplamalı olarak analiz etmek için kapsamlı ve mantıksal bir standart sunmak üzere 2008'de başlatılmış ve bugün fenotip alışverişinde dünya çapında bir standart hâline gelmiştir; nöroloji, nefroloji, immünoloji, pulmonoloji ve yenidoğan taraması gibi alanlarda kapsamı sürekli genişletilmektedir (Köhler ve ark., 2021). Pratik karşılığı şudur: "gelişme geriliği" gibi genel bir ifade yerine standart terimlerle kaydedilmiş ayrıntılı bir fenotip, varyant önceliklendirme algoritmalarının çalışabileceği bir girdiye dönüşür.

**Tablo 17.1 — Klinik akıl yürütmenin temel kavramları**

| Kavram | Tanım | Pratik karşılığı |
|---|---|---|
| Örüntü tanıma | Bulgu kümesinin bilinen bir sendroma benzetilmesi | Hızlı; tanınabilir sendromlarda en verimli yol |
| **Mekanizmacı akıl yürütme** | Bulgulardan **moleküler mekanizmaya** gitmek | Sendrom tanınmasa bile doğru testi seçtirir |
| Derin fenotipleme | Ayırt edici bulguların sistematik ve standart kaydı | Hipotezi keskinleştirir; varyant önceliklendirmesini besler |
| **Kör nokta** | Kullanılan yöntemin yapısal olarak göremediği varyant sınıfı | Negatif sonucun en sık nedeni |
| Basamaklı strateji | Kör noktaları sırayla kapatan test dizisi | "Her şeyi aynı anda iste" yaklaşımının alternatifi |
| **Yeniden analiz** | Var olan verinin yeni bilgiyle yeniden değerlendirilmesi | Yeni örnek almadan tanı kazandırır |

---

## 2. Klinik ipucundan mekanizmaya

### 2.1 Ondan az ipucu, kitabın tamamını kapsar

Şekil 17.1'deki listenin gücü, kısalığındadır. Pediatrik genetik pratiğinde karşılaşılan mekanizmaya-özgü ipuçlarının çoğu bir düzineyi geçmez ve bunların her biri kitabın bir bölümüne karşılık gelir.

**Asimetri ve çizgisellik mozaikliği düşündürür.** Blaschko çizgilerini izleyen pigmentasyon, segmental aşırı büyüme veya tek taraflı tutulum, olayın döllenmeden sonra gerçekleştiğini söyler (Bölüm 12). Bu ipucunun tanısal sonucu doğrudandır: kan örneği yanıltıcı olabilir, **etkilenmiş dokudan** örnek gerekir.

**Kuşaklar boyunca erkenleşen ve ağırlaşan tablo tekrar genişlemesini düşündürür.** Anticipasyon, dizileme temelli testlerin yapısal olarak göremediği bir mekanizmanın klinik imzasıdır (Bölüm 9); doğru test hedefli tekrar analizidir.

**Maternal kalıtım örüntüsü ve çok sistemli tutulum mitokondriyal hastalığı düşündürür** (Bölüm 11); ve burada ikinci bir karar daha vardır: hangi dokudan bakılacağı, çünkü heteroplazmi düzeyi dokudan dokuya değişir.

**Büyüme asimetrisi ve ebeveyn kökenine bağlı farklılık imprinting kusurunu düşündürür** (Bölüm 10); dizileme normal çıkabilir, çünkü kusur dizide değil metilasyondadır.

**Aynı ailede çok farklı ağırlıkta tablo, rezidüel işlev ve modifiye edici lokusları düşündürür** (Bölüm 14–15); burada ölçülebilir bir doz varsa (ör. yedek gen kopya sayısı) o doğrudan ölçülmelidir.

Bu ipuçlarının ortak özelliği şudur: hiçbiri bir gen adı söylemez, ama hepsi **hangi testi isteyeceğinizi** söyler.

### 2.2 "Negatif" ne demektir? Altı kör nokta

Klinik pratikte en sık karşılaşılan ve en çok yanlış anlaşılan durum, güçlü bir klinik tanıya rağmen genetik testin negatif gelmesidir. Bu durumu doğru yorumlamak için önce beklentiyi doğru kurmak gerekir.

Şüpheli genetik hastalığı olan çocuklarda tanısal getiriyi karşılaştıran, 37 çalışma ve 20.068 çocuğu kapsayan bir sistematik derleme ve meta-analiz, tüm genom dizilemenin tanısal getirisini 0,41, tüm ekzom dizilemeninkini 0,36 ve kromozomal mikroarray'inkini 0,10 olarak bildirmiştir. Aynı analizde, kohort içi karşılaştırma yapan çalışmalarda **trio** analizinin tek bireye göre tanı olasılığını anlamlı biçimde artırdığı gösterilmiştir (olasılık oranı 2,04). Yazarlar, şüpheli genetik hastalığı olan çocuklarda WGS/WES'in **birinci basamak genomik test** olarak düşünülmesi gerektiği sonucuna varmışlardır (Clark ve ark., 2018).

Bu sayılar iki şey söyler. Birincisi, negatif sonuç **beklenen** bir olaydır — çoğunluk değilse bile büyük bir azınlıktır. İkincisi, aynı hastadan alınacak ek örnek (ebeveynler) tanısal getiriyi belirgin biçimde artırır.

Peki hangi varyantlar kaçar? Şekil 17.2 bu kör noktaları toplar.

![Şekil 17.2 — "Ekzom negatif" ne demektir? Altı kör nokta](assets/sekil_59_negatif_ekzom_kor_noktalar.svg)

Bu kör noktaların gerçek klinik ağırlığı, ulusal ölçekli programlarda görülebilir. Birleşik Krallık'ta 2.183 aileden 4.660 katılımcıyı kapsayan genom dizileme pilot çalışmasında, fenotip verileri HPO terimleriyle toplanmış, sanal gen panelleri ve fenotipe dayalı otomatik varyant önceliklendirmesi uygulanmış ve probandların **%25'inde** genetik tanı konmuştur. Tanısal getiri, tek gen kökenli olması muhtemel bozukluklarda (%35) karmaşık kökenli olması muhtemel bozukluklara (%11) göre çok daha yüksek; entelektüel yetersizlik, işitme ve görme bozukluklarında %40–55 aralığında bulunmuştur. Bu bölüm açısından en öğretici bulgu şudur: konulan tanıların **%14'ü** araştırma ve otomatik yaklaşımların birleşimiyle elde edilmiştir ve bu birleşim özellikle **kodlamayan, yapısal ve mitokondriyal genom varyantları ile ekzom dizilemenin iyi kapsamadığı kodlayan varyantlar** için belirleyici olmuştur. Ayrıca konulan tanıların dörtte biri, hasta ya da yakınları için klinik karar vermede **anında** sonuç doğurmuştur (Smedley ve ark., 2021).

> **🔬 Deep-dive — Yeniden analiz: yeni örnek almadan tanı kazanmak.** Kör noktaların en ucuz çözümü yeni bir test değil, var olan verinin yeniden değerlendirilmesidir. Birleşik Krallık'taki Deciphering Developmental Disorders çalışmasında, 2014'te 1.133 ağır gelişimsel bozukluğu olan çocuk ve ebeveynlerinde ekzom dizilemeyle **%27** tanı oranı bildirilmişti. Aynı veri; geliştirilmiş varyant çağırma yöntemleri, yeni varyant saptama algoritmaları, güncellenmiş varyant anotasyonu, kanıta dayalı filtreleme stratejileri ve **yeni keşfedilen hastalık genleri** ışığında yeniden analiz edildiğinde 182 kişiye daha tanı konabilmiş ve genel tanı oranı **454/1.133'e (%40)** yükselmiştir; ayrıca 43 kişide (%4) klinik önemi belirsiz bir bulgu saptanmıştır (Wright ve ark., 2018). Bu, kliniğe doğrudan çevrilebilecek bir sonuçtur: **negatif raporlanan bir olgu, kapanmış bir dosya değildir.** Yeni gen keşiflerinin hızı düşünüldüğünde, 12–24 ayda bir yeniden değerlendirme makul bir pratiktir ve bu, ailenin yeniden örnek vermesini gerektirmez. Yeniden analizin bir başka boyutu da yorumdur: aynı varyant, yeni popülasyon verileri, yeni fonksiyonel çalışmalar ya da gen–hastalık ilişkisinin güncellenmiş geçerliliği ışığında farklı sınıflandırılabilir (Bölüm 16).

### 2.3 Zincirin bütünü

Şekil 17.3, kitabın tamamını tek bir akış olarak gösterir ve bu bölümün omurgasıdır.

![Şekil 17.3 — Kitabın omurgası: hastadan rapora, rapordan yeniden hastaya](assets/sekil_60_uctan_uca_akis.svg)

Zincirin en sık kırıldığı üç yer, üç farklı bölüme karşılık gelir. **İkinci halka atlandığında** (mekanizma hipotezi kurulmadan geniş test istendiğinde), negatif sonuç gelir ve nedeni anlaşılmaz; oysa kaçan şey, seçilen testin kör noktasıdır. **Beşinci halka mekanizmasız yapıldığında** (kriterler bir kontrol listesi gibi işaretlendiğinde), PVS1 kapısı ya da hastalık varlığı seçimi atlanır ve sınıf yanlış çıkar (Bölüm 16). **Geri besleme kurulmadığında** ise VUS veya negatif sonuç raporlanır, dosya kapanır ve tanı yıllarca gecikir. Üçünün ortak özelliği, teknolojiyle değil **akıl yürütmeyle** ilgili olmalarıdır.

---

## 3. Varyant tipleri

Bu bölümde varyant tipi sorusu klinikten başlar: **hangi başvuru tablosunda hangi varyant tipini beklemeliyim ve o tipi hangi yöntem görür?**

**Tablo 17.2 — Klinik tablodan beklenen varyant tipine ve yönteme**

| Klinik tablo | Beklenen varyant tipi | Görebilen yöntem | İlgili bölüm |
|---|---|---|---|
| Çoklu anomali + gelişimsel gerilik | Büyük delesyon/duplikasyon | CMA · CNV çözünürlüklü WGS | 3, 8 |
| İzole, ağır, resesif metabolik tablo | Biallelik null/missense | Panel/WES + biyokimyasal doğrulama | 2 |
| Erken başlangıçlı ağır epilepsi | De novo missense (çoğu GoF) | Trio panel/WES + fonksiyonel veri | 4, 16 |
| Kemik kırılganlığı, bağ doku tablosu | Glisin missense (DN) vs null | Panel; mekanizma ayrımı şart | 5 |
| Tipik fenotip, panel negatif | Derin intronik/kriptik splice | WGS + **RNA analizi** | 7, 13 |
| Segmental/asimetrik tutulum | Düşük VAF postzigotik varyant | Etkilenmiş dokudan derin dizileme | 12 |
| Kuşaklar boyunca erkenleşme | Tekrar genişlemesi | Hedefli tekrar analizi · uzun-okuma | 9 |
| Çok sistemli + laktat artışı | mtDNA varyantı (heteroplazmik) | Uygun dokudan mtDNA dizileme | 11 |
| Büyüme asimetrisi/aşırı büyüme | Metilasyon kusuru · UPD | Metilasyon analizi · SNP array | 10 |
| Aynı ailede değişken ağırlık | Modifiye edici doz farkı | Hedefli kopya sayısı ölçümü | 14 |
| Aynı gen, atipik fenotip | Serinin başka basamağı | Domain/izoform analizi + fenotip derinleştirme | 15 |

Tablonun okunma biçimi şudur: sol sütun **klinik**, sağ sütun **yöntem**dir; ikisini bağlayan orta sütun ise mekanizmadır. Mekanizma sütunu atlandığında, sol sütundan sağ sütuna doğrudan geçilmeye çalışılır ve tanısal hatalar tam burada doğar.

---

## 4. Klinik fenotipe dönüşüm: ilk basamakta ne isteyeceğim?

### 4.1 Testi hipotez seçer, hipotezi fenotip kurar

Genomik testlerin yaygınlaşması, "hangi testi isteyeyim?" sorusunu ortadan kaldırmadı; yalnızca sorunun biçimini değiştirdi. Bugün asıl soru, **hangi testi ilk sırada isteyeceğim ve negatif gelirse sırada ne var?** biçimindedir.

**Algoritma 17.1 — İlk basamak test seçimi akışı**

```mermaid
flowchart TD
  A["Klinik değerlendirme + derin fenotipleme"] --> B{"Tanınabilir spesifik bir<br/>sendrom/mekanizma var mı?"}

  B -->|"Evet — mekanizmaya özgü"| C{"Hangi mekanizma?"}
  C -->|"Tekrar genişlemesi<br/>(anticipasyon)"| D["HEDEFLİ tekrar analizi<br/>— dizileme ile başlama"]
  C -->|"İmprinting<br/>(büyüme asimetrisi)"| E["METİLASYON analizi<br/>± UPD testi"]
  C -->|"Mozaiklik<br/>(segmental/çizgisel)"| F["ETKİLENMİŞ DOKUDAN<br/>derin dizileme"]
  C -->|"Mitokondriyal<br/>(maternal, çok sistemli)"| G["Uygun dokudan mtDNA<br/>+ nükleer panel"]
  C -->|"Bilinen tek gen<br/>(ör. doz modifier'ı olan)"| H["Hedefli gen testi<br/>+ gerekiyorsa kopya sayısı"]

  B -->|"Hayır / geniş ayırıcı tanı"| I{"Çoklu anomali veya<br/>gelişimsel gerilik ön planda mı?"}
  I -->|"Evet"| J["CMA (veya CNV çözünürlüklü WGS)<br/>+ TRİO dizileme"]
  I -->|"Hayır — organ/sistem odaklı"| K["Hedefli panel veya<br/>TRİO WES/WGS"]

  D --> L{"Sonuç tanısal mı?"}
  E --> L
  F --> L
  G --> L
  H --> L
  J --> L
  K --> L

  L -->|"Evet"| M["Bölüm 16: kanıtı tart, sınıflandır,<br/>raporla → danışma ve izlem"]
  L -->|"Hayır"| N["KÖR NOKTA basamağına geç<br/>(Şekil 17.2): WGS · RNA · tekrar ·<br/>metilasyon · doku · mtDNA"]
  N --> O["Hâlâ negatif → veriyi paylaş,<br/>TAKVİMLİ yeniden analiz planla<br/>(12–24 ay)"]
```

### 4.2 Trio mu, tek birey mi?

Bu, pratikte en çok maliyet tartışması yaratan ve en çok yanlış kararın verildiği sorudur. Kanıt nettir: kohort içi karşılaştırmalarda trio analizi, tek bireye göre tanı olasılığını yaklaşık iki katına çıkarmaktadır (Clark ve ark., 2018); ulusal ölçekli genom programında da tanısal getiri aile yapısına göre değişmiş ve **trio ile daha geniş pedigrili ailelerde en yüksek** bulunmuştur (Smedley ve ark., 2021). Bunun mekanik nedeni Bölüm 16'da açıklanmıştı: trio, de novo kanıtını (PS2/PM6) ve faz bilgisini (PM3) doğrudan üretir; ikisi de tek bireyden elde edilemez.

### 4.3 Doku seçimi: bazen testten daha önemli

Kitabın üç bölümü aynı uyarıyı verir. Mozaiklikte etkilenmiş doku (Bölüm 12), mitokondriyal hastalıkta heteroplazminin yüksek olduğu doku (Bölüm 11) ve RNA analizinde ilgili genin ifade edildiği doku (Bölüm 13) gereklidir. Yanlış dokudan yapılan doğru test, negatif sonuç verir — ve bu negatiflik, mekanizmayı dışlamaz.

---

## 5. Tanısal testlerle ilişkisi

Bu bölümde tablo, **basamaklı strateji** olarak okunmalıdır: hangi test hangi sırada ve hangi kör noktayı kapatmak için istenir.

**Tablo 17.3 — Basamaklı test stratejisi ve kör noktalar**

| Test | Bu mekanizmayı yakalar mı? | Sınırlılığı |
|------|----------------------------|-------------|
| **WES (tercihen trio)** | Kodlayan varyantların çoğunu; birinci basamak genomik test olarak uygundur | CNV, tekrar, derin intronik, metilasyon ve çoğu zaman mtDNA kör noktada kalır; kapsama boşlukları vardır |
| **Short-read WGS** | Kodlayan + kodlamayan + çoğu yapısal varyant; tek testte en geniş kapsam | Uzun tekrarlar ve karmaşık bölgeler sınırlı; yorum yükü yüksek |
| **Long-read WGS** | Tekrar genişlemeleri, karmaşık SV ve **faz** için üstün | Maliyet/erişim; her merkezde rutin değil |
| **Array-CGH / SNP array** | Dozaj CNV'leri; SNP array ayrıca UPD ve homozigotluk bölgelerini gösterir | Dengeli SV'leri ve tek nükleotid varyantlarını görmez |
| **MLPA** | Hedefli delesyon/duplikasyon ve **kopya sayısı** (ör. yedek gen dozu) | Yalnız tasarlanan lokus |
| **RNA-seq (doğru dokudan)** | Kriptik splice sonuçlarını, alel dengesizliğini ve ifade kaybını doğrudan gösterir | Doğru doku şart; ifade edilmeyen gende bilgi vermez |
| **Methylation array / MS-MLPA** | İmprinting kusurları, UPD ve epimutasyonlar; bazı sendromlarda episignature | Yalnız ilgili mekanizmalarda anlamlı |
| **Karyotip** | Dengeli translokasyon/inversiyon; tekrarlayan düşük öyküsünde değerli | Çözünürlük düşük |
| **(stratejiye özgü) Hedefli tekrar analizi · mtDNA dizileme · doku örneklemesi** | **Evet — kör noktaları kapatan asıl testler bunlardır** | Her biri hipotez gerektirir; hipotezsiz istenmezler |

> **Bu mekanizmayı hangi test yakalar? (özet):** Basamaklı strateji şudur: **(1)** derin fenotipleme ile mekanizma hipotezi kur; **(2)** mekanizmaya özgü bir ipucu varsa doğrudan o testi iste (tekrar · metilasyon · doku · mtDNA); **(3)** geniş ayırıcı tanıda trio WES/WGS ile başla (çoklu anomali varsa CNV çözünürlüğünü garanti et); **(4)** negatifse kör noktaları sırayla kapat (WGS → RNA → tekrar → metilasyon → doku → mtDNA); **(5)** hâlâ negatifse veriyi paylaş ve **takvimli yeniden analiz** planla.

> **🟦 Klinikte dikkat — "Her şeyi aynı anda isteyelim" yaklaşımının bedeli:** Geniş testi hipotezsiz istemek yalnız maliyetli değil, aynı zamanda **yanıltıcıdır**: her genomda çok sayıda nadir varyant bulunur ve hipotez yoksa bunların hangisinin anlamlı olduğunu söyleyecek çapa yoktur. Sonuç, artan VUS yükü ve aileye taşınan gereksiz belirsizliktir. Doğru yaklaşım geniş testi reddetmek değil, onu **fenotiple çerçevelemektir**.

---

## 6. Varyant yorumlama açısından önemi

Bu bölümün varyant yorumlamaya katkısı, Bölüm 16'nın çerçevesini **klinik girdiyle beslemektir**. Üç bağlantı özellikle önemlidir.

**Birincisi, fenotip kriterin kendisidir.** Derin fenotipleme, PP4'ün kullanılabilirliğini belirler; ama daha önemlisi, Bölüm 15'te gördüğümüz gibi **hangi hastalık varlığı için** değerlendirme yapılacağını seçtirir. Allelik seri taşıyan bir gende bu seçim, bütün kriterlerin anlamını değiştirir.

**İkincisi, aile örneği kriter üretir.** Trio ve genişletilmiş aile örneklemesi, laboratuvarın kendi başına üretemeyeceği kanıtı (PS2/PM6, PP1/BS4, PM3) sağlar. Bu nedenle "aile örneği alınamadı" cümlesi teknik bir ayrıntı değil, **kanıt kaybıdır**.

**Üçüncüsü, doku seçimi kanıtın geçerliliğini belirler.** Yanlış dokudan yapılan RNA analizi kullanılabilir bir kanıt üretmez (splice bulgusu için **PVS1_Strength**, etkisizlik için BP7 — Bölüm 7); yanlış dokudan bakılan heteroplazmi düzeyi yanlış yorumlanır; kandan yapılan analiz mozaik bir varyantı hiç göstermez ve varyant "yok" sayılır.

**Algoritma 17.2 — Klinik senaryodan kanıt üretimine**

```mermaid
flowchart TD
  A["Klinik senaryo"] --> B["Mekanizma hipotezi"]
  B --> C{"Bu mekanizma hangi<br/>kanıtı ÜRETEBİLİR?"}

  C -->|"İşlev kaybı"| D["PVS1 kapısı açık →<br/>basamak seç (Şekil 16.2)"]
  C -->|"İşlev kazanımı / DN"| E["PVS1 KAPALI →<br/>PM1 (hotspot) + PS3 (yön gösteren test)"]
  C -->|"Splice"| F["RNA analizi planla →<br/>PVS1 karar ağacı +<br/>RNA kanıtı = PVS1_Strength"]
  C -->|"Doz / CNV"| G["CNV puanlama çerçevesi"]
  C -->|"Mozaiklik"| H["Doku + VAF; segregasyon YOK,<br/>PS2/PM6 dikkatle"]
  C -->|"İmprinting"| I["Metilasyon kanıtı + ebeveyn kökeni"]
  C -->|"Mitokondriyal"| J["mtDNA spesifikasyonu:<br/>heteroplazmi + doku + haplogrup"]

  D --> K["Hastalık varlığını SEÇ (Bölüm 15)"]
  E --> K
  F --> K
  G --> K
  H --> K
  I --> K
  J --> K

  K --> L["Kriterleri seç, güçlerini belirle,<br/>TOPLAM AĞIRLIĞI hesapla (Bölüm 16)"]
  L --> M{"Sınıf?"}
  M -->|"P / LP"| N["Raporla + mekanizma cümlesi<br/>→ izlem/tarama/aile testi"]
  M -->|"VUS"| O["Eksik kanıtı üret:<br/>aile örneği · RNA · fonksiyonel test<br/>→ takvimli yeniden değerlendirme"]
  M -->|"LB / B"| P["Nedensel değil —<br/>ama TANI DIŞLANMADI:<br/>kör noktalara dön (Şekil 17.2)"]
```

---

## 7. Pediatrik genetikten klinik örnekler: sekiz senaryo

Aşağıdaki sekiz senaryo, kitabın bütün bölümlerini hastanın başında tekrar eder. Her senaryo aynı yapıyı izler: **başvuru → mekanizma hipotezi → test → sonuç → yorum → öğreti.** Şekil 17.4 bu sekiz senaryonun omurgasını tek sayfada toplar.

![Şekil 17.4 — Sekiz senaryo panosu: başvurudan mekanizmaya, mekanizmadan teste](assets/sekil_61_senaryo_panosu.svg)

**Senaryo 1 — Yenidoğan, ağır hipotoni ve solunum yetmezliği.** Doğumdan itibaren belirgin hipotoni, zayıf ağlama, dil fasikülasyonları ve derin tendon reflekslerinin alınamaması. **Mekanizma hipotezi:** ön boynuz motor nöronunda işlev kaybı; klasik olarak biallelik *SMN1* kaybı. **Test:** *SMN1* delesyon analizi (MLPA) — ve kritik olarak **aynı testte *SMN2* kopya sayısı**. **Yorum:** ana kusur bütün hastalarda aynıdır; klinik ağırlığı belirleyen esas değişken yedek genin kopya sayısıdır (Bölüm 14), ve bu etki Bölüm 7'de anlatılan bir splicing farkı üzerinden çalışır (Lorson ve ark., 1999). Büyük serilerde kopya sayısı ile hastalık tipi arasındaki ilişki prognostik kurallar hâlinde ortaya konmuştur (Calucho ve ark., 2018). **Öğreti:** modifier ölçümü burada akademik bir ayrıntı değil, prognoz ve tedavi kararının parçasıdır — dizileme yapmadan önce doğru doz testini istemek gerekir.

**Senaryo 2 — Altı aylık bebek, dirençli nöbetler.** Yaşamın ilk günlerinde başlayan, çoklu antiepileptiğe dirençli nöbetler; EEG'de ağır örüntü; gelişimsel duraklama. **Mekanizma hipotezi:** iyon kanalı hastalığı; başlangıç yaşı erken olduğunda **işlev kazanımı** yönü ön planda. **Test:** trio panel/WES; saptanan de novo missense varyantın **yönü** için fonksiyonel veri. **Yorum:** *SCN2A*'da tekrarlayan varyantların bir kısmı işlev kazanımı, bir kısmı işlev kaybı yönündedir ve bu ayrım elektrofizyolojik olarak gösterilebilir (Berecki ve ark., 2018). Yorumlamada bu, PS3'ün yalnızca "işlev bozulmuş" demek için değil **yönü göstermek** için kullanılması demektir (Bölüm 16). **Öğreti:** mekanizma yönü doğrudan tedaviyi değiştirir; erken başlangıçlı ve işlev kazanımı yönündeki sodyum kanalı tablolarında sodyum kanal blokerleri gündeme gelirken, işlev kaybı tablolarında aynı yaklaşım uygun değildir (Brunklaus ve ark., 2020).

**Senaryo 3 — İki yaşında çocuk, gelişimsel gerilik ve dismorfik bulgular.** Çoklu minör anomali, büyüme geriliği, tanınabilir bir sendrom örüntüsü yok. **Mekanizma hipotezi:** dozaj dengesizliği — bitişik gen delesyonu ya da tek gen yetersiz dozu (Bölüm 3, 8). **Test:** kromozomal mikroarray (ya da CNV çözünürlüğü güvenilir bir WGS) + trio dizileme. **Yorum:** açıklanamayan gelişimsel gerilik/çoklu konjenital anomali tablolarında mikroarray birinci basamak test olarak yerleşmiştir (Miller ve ark., 2010); saptanan CNV, dizi varyantı kriterleriyle değil kendi puanlama çerçevesiyle değerlendirilir (Riggs ve ark., 2020). **Öğreti:** "ekzom yaptık, negatif" cümlesi bu senaryoda yetersizdir; ekzom verisinden CNV çağrısı güvenilir değildir ve kör nokta tam buradadır.

**Senaryo 4 — Süt çocuğu, asimetrik aşırı büyüme.** Bir ekstremitede aşırı büyüme, ciltte damarsal malformasyon, keskin sınırlı ve orta hatta duran bir dağılım. **Mekanizma hipotezi:** postzigotik (mozaik) aktive edici varyant (Bölüm 12). **Test:** **etkilenmiş dokudan** (deri/yumuşak doku) derin dizileme; kandan bakılan analiz negatif olabilir. **Yorum:** bu grup bozukluklar, mozaik aktive edici varyantların yol açtığı bir spektrum olarak tanımlanmış ve tanı ölçütleri buna göre düzenlenmiştir (Keppler-Noreuil ve ark., 2015); mozaikliğin klinik ve moleküler sınıfları ile saptama zorlukları ayrıntılı biçimde ele alınmıştır (Biesecker ve Spinner, 2013). **Öğreti:** bu senaryoda testten daha önemli olan karar **doku seçimidir**; yanlış dokudan yapılan doğru test yanlış sonuç verir.

**Senaryo 5 — Beş yaşında çocuk, hipotoni ve laktat yüksekliği.** Egzersiz intoleransı, pitozis ve oftalmopleji, işitme kaybı, anne tarafında benzer yakınmalar. **Mekanizma hipotezi:** mitokondriyal hastalık; maternal kalıtım örüntüsü mtDNA'yı düşündürür (Bölüm 11). **Test:** uygun dokudan (idrar epiteli, gerekirse kas) mtDNA dizileme + nükleer gen paneli. **Yorum:** mitokondriyal hastalıklar iki genomdan da kaynaklanabilir ve heteroplazmi düzeyi dokudan dokuya değişir; tanı ve yönetim bu ikili yapıyı hesaba katmalıdır (Gorman ve ark., 2016; Stewart ve Chinnery, 2015). Varyant yorumlaması ise mtDNA'ya özgü uzmanlaştırılmış çerçeveyle yapılır (Bölüm 16). **Öğreti:** kandan bakılan normal bir heteroplazmi düzeyi tanıyı dışlamaz; doku ve eşik bilgisi olmadan sonuç yorumlanamaz.

**Senaryo 6 — Yenidoğan, makrozomi ve hipoglisemi.** Doğum tartısı yüksek, makroglossi, karın duvarı defekti öyküsü, hemihipertrofi. **Mekanizma hipotezi:** imprinting kusuru (Bölüm 10). **Test:** ilgili imprintli bölgenin **metilasyon analizi**; dizileme tek başına yetersizdir. **Yorum:** bu tablo, alt tipleri farklı moleküler mekanizmalara dayanan ve alt tipe göre tümör riski değişen bir bozukluktur; uluslararası uzlaşı, tanının moleküler alt tipe göre netleştirilmesini ve **tarama planının alt tipe göre kurulmasını** önerir (Brioude ve ark., 2018). **Öğreti:** burada moleküler tanı yalnız etiket değildir; doğrudan izlem protokolünü belirler.

**Senaryo 7 — Sekiz yaşında çocuk, kas güçsüzlüğü ve yüksek kreatin kinaz; panel ve ekzom negatif.** Klinik olarak konjenital kas hastalığı düşünülüyor; geniş panel ve ekzom sonuçsuz. **Mekanizma hipotezi:** kodlayan bölge dışında kalan bir splicing kusuru (Bölüm 7, 13). **Test:** **kas dokusundan RNA dizileme** (± WGS). **Yorum:** genetik tanısı konmamış nadir kas hastalıkları kohortunda transkriptom dizileme, aday splice-bozucu varyantların doğrulanmasını ve hem ekzonik hem **derin intronik** bölgelerdeki splice-değiştirici varyantların saptanmasını sağlamış, genel tanı oranı **%35** olmuştur; ayrıca sık tekrarlayan bir de novo intronik varyantın, kollajen VI benzeri distrofi düşünülen ve önceki genetik analizleri negatif olan hastaların yaklaşık dörtte birini açıkladığı gösterilmiştir (Cummings ve ark., 2017). **Öğreti:** RNA analizi burada iki iş birden yapar — tanıyı koyar ve Bölüm 16'da gördüğümüz gibi öngörüyü ölçüme çevirerek PS3'ü açar.

**Senaryo 8 — On iki yaşında çocuk, ilerleyici ataksi; ailede erkenleşme.** Dedede erişkin yaşta başlayan yürüme bozukluğu, babada otuzlu yaşlarda, çocukta on iki yaşında; her kuşakta daha erken ve daha ağır. **Mekanizma hipotezi:** tekrar genişlemesi ve anticipasyon (Bölüm 9). **Test:** hedefli tekrar analizi; standart dizileme bu mekanizmayı görmez. **Yorum:** tekrar genişlemesi hastalıkları, tekrar tipine ve konumuna göre farklı patojenik mekanizmalar (işlev kaybı, RNA toksisitesi, protein toksisitesi) üzerinden çalışır ve anticipasyon bu grubun tanımlayıcı klinik imzasıdır (Paulson, 2018). **Öğreti:** aile öyküsündeki tek bir örüntü, doğru testi doğrudan seçtirebilir; burada dizileme ile başlamak zaman ve kaynak kaybıdır.

---

## 8. Sık yapılan hatalar ve klinikte dikkat

> **🔴 Sık yapılan hata kutusu**
> 1. **Mekanizma hipotezi kurmadan geniş test istemek.** Test hipotezle çerçevelenmezse, negatif sonuç yorumlanamaz ve VUS yükü artar.
> 2. **"Ekzom negatif = genetik neden yok" saymak.** Ekzomun altı yapısal kör noktası vardır (CNV, kodlamayan, tekrar, mozaiklik, imprinting, mtDNA).
> 3. **Yanlış dokudan örnek almak.** Mozaiklikte kan, mitokondriyal hastalıkta kan, RNA analizinde ilgisiz doku — hepsi yanlış negatif üretir.
> 4. **Trio'yu maliyet gerekçesiyle atlamak.** Trio, tanı olasılığını yaklaşık iki katına çıkarır ve tek bireyden elde edilemeyen kanıt (de novo, faz) üretir.
> 5. **Anticipasyon öyküsünü atlayıp dizilemeyle başlamak.** Tekrar genişlemeleri hedefli test gerektirir; dizileme bu mekanizmayı görmez.
> 6. **Büyüme asimetrisinde metilasyon analizi istememek.** İmprinting kusurlarında dizi normaldir; kusur metilasyondadır.
> 7. **Negatif dosyayı kapatmak.** Aynı verinin yeniden analizi, yeni örnek almadan tanı oranını belirgin biçimde artırabilir.
> 8. **Fenotibi genel terimlerle kaydetmek.** "Gelişme geriliği" gibi ifadeler ne hipotez kurdurur ne de varyant önceliklendirmesini besler.
> 9. **Modifiye edici doz testini atlamak.** Bazı hastalıklarda (ör. yedek gen kopya sayısı) bu ölçüm doğrudan prognoz ve tedavi kararıdır.
> 10. **Sonucu mekanizma cümlesi olmadan raporlamak/okumak.** "Patojenik varyant saptandı" cümlesi, hangi mekanizma ve hangi hastalık için olduğu yazılmadan klinik karara çevrilemez.

> **🟦 Klinikte dikkat kutusu**
> - Her olguda önce **tek bir cümlelik mekanizma hipotezi** yazın: "Bu tabloda en olası mekanizma …, çünkü ….". Bu cümle testi seçtirir.
> - Fenotibi standart terimlerle ve **ayırt edici** bulgular üzerinden kaydedin; laboratuvara gönderilen fenotip bilgisi, varyant önceliklendirmesinin yakıtıdır.
> - Mekanizmaya özgü bir ipucu varsa (anticipasyon, asimetri, maternal kalıtım, büyüme asimetrisi) **doğrudan o testi** isteyin; geniş testle başlamak zaman kaybıdır.
> - Negatif sonucu raporlarken **hangi kör noktanın açık kaldığını** yazın; bu, bir sonraki hekimin işini kolaylaştırır.
> - Yeniden değerlendirmeyi takvime bağlayın (ör. 12–24 ay) ve aileye bunu açıkça söyleyin; "haber olursa ararız" belirsiz bir vaattir.
> - Tanı konduğunda mekanizmayı aileye anlatın: mekanizma, tekrarlanma riskini, izlem planını ve gerektiğinde tedavi seçeneklerini anlaşılır kılan tek dildir.

---

## 9. Klinik pratikte karar algoritması

**Algoritma 17.3 — Başvurudan danışmaya: ana klinik algoritma**

```mermaid
flowchart TD
  A["HASTA — başvuru"] --> B["1. DERİN FENOTİPLEME<br/>ayırt edici bulgular · aile öyküsü · pedigri ·<br/>başlangıç yaşı · seyir · standart terimler"]

  B --> C["2. MEKANİZMA HİPOTEZİ<br/>Şekil 17.1: klinik ipucu → aday mekanizma"]

  C --> D{"Mekanizmaya ÖZGÜ<br/>bir ipucu var mı?"}
  D -->|"Var"| E["3a. HEDEFLİ TEST<br/>tekrar analizi · metilasyon · doku örneği ·<br/>mtDNA · kopya sayısı"]
  D -->|"Yok / geniş ayırıcı tanı"| F["3b. GENİŞ TEST<br/>TRİO WES/WGS<br/>(çoklu anomali varsa CNV çözünürlüğü şart)"]

  E --> G{"Tanısal sonuç var mı?"}
  F --> G

  G -->|"Var"| H["4. VARYANTI TANI<br/>tip · konum · faz · VAF · kalıtım · ebeveyn kökeni"]
  G -->|"Yok"| I["KÖR NOKTA BASAMAĞI (Şekil 17.2)<br/>WGS → RNA → tekrar → metilasyon →<br/>doku (mozaiklik) → mtDNA"]

  I --> J{"Şimdi tanısal mı?"}
  J -->|"Evet"| H
  J -->|"Hayır"| K["Veriyi paylaş · araştırma/olgu eşleştirme ·<br/>TAKVİMLİ yeniden analiz (12–24 ay)"]

  H --> L["5. YORUM (Bölüm 15–16)<br/>hastalık varlığını seç → kriterleri mekanizmaya göre seç →<br/>toplam ağırlığı hesapla"]

  L --> M{"Sınıf?"}
  M -->|"P / LP"| N["6. DANIŞMA VE İZLEM<br/>risk hastalık varlığına göre ·<br/>izlem/tarama planı · tedavi ve üreme seçenekleri"]
  M -->|"VUS"| O["Eksik kanıtı üret (Şekil 16.4):<br/>aile örneği · RNA · fonksiyonel test<br/>→ yeniden değerlendirme"]
  M -->|"LB / B"| K

  O --> P{"Sınıf değişti mi?"}
  P -->|"Evet"| N
  P -->|"Hayır"| K
  K --> Q["Aileye: dosya KAPANMADI;<br/>ne zaman ve neden tekrar bakılacağını söyle"]
  N --> R["Kayıt: mekanizma cümlesi + kanıt gerekçesi<br/>+ yeniden değerlendirme tarihi"]
  Q --> R
```

---

## 10. Kaynaklar

> **Atıf / doğrulama notu:** Bu bölümün bibliyografik verileri PubMed üzerinden doğrulanmıştır; her kaynağın PMID ve DOI'si tek tek teyit edilmiştir. (Metin içinde yazar-yıl, kaynakçada DOI-link kullanılır.)

1. **Clark MM, Stark Z, Farnaes L, ve ark. (2018).** Meta-analysis of the diagnostic and clinical utility of genome and exome sequencing and chromosomal microarray in children with suspected genetic diseases. *npj Genomic Medicine* 3:16. **PMID: 30002876** · DOI: [10.1038/s41525-018-0053-8](https://doi.org/10.1038/s41525-018-0053-8) — *Kullanım amacı: Tanısal getiri beklentisinin kurulması (WGS 0,41 · WES 0,36 · CMA 0,10); trio'nun tek bireye üstünlüğü (OR 2,04); WGS/WES'in birinci basamak test önerisi.*

2. **Wright CF, McRae JF, Clayton S, ve ark. (2018).** Making new genetic diagnoses with old data: iterative reanalysis and reporting from genome-wide data in 1,133 families with developmental disorders. *Genetics in Medicine* 20(10):1216–1223. **PMID: 29323667** · DOI: [10.1038/gim.2017.246](https://doi.org/10.1038/gim.2017.246) — *Kullanım amacı: Yeniden analizin getirisi; 1.133 ailede tanı oranının %27'den %40'a çıkması; yeni gen bilgisi ve yöntemlerin katkısı.*

3. **Smedley D, Smith KR, Martin A, ve ark. (2021).** 100,000 Genomes Pilot on Rare-Disease Diagnosis in Health Care — Preliminary Report. *The New England Journal of Medicine* 385(20):1868–1880. **PMID: 34758253** · DOI: [10.1056/NEJMoa2035790](https://doi.org/10.1056/NEJMoa2035790) — *Kullanım amacı: Ulusal ölçekli genom programında tanısal getiri (%25 proband); tek gen kökenli (%35) ve karmaşık (%11) tablolar arasındaki fark; tanıların %14'ünün kodlamayan/yapısal/mitokondriyal varyantlar için araştırma yaklaşımlarını gerektirmesi; aile yapısının etkisi.*

4. **Köhler S, Gargano M, Matentzoglu N, ve ark. (2021).** The Human Phenotype Ontology in 2021. *Nucleic Acids Research* 49(D1):D1207–D1217. **PMID: 33264411** · DOI: [10.1093/nar/gkaa1043](https://doi.org/10.1093/nar/gkaa1043) — *Kullanım amacı: Derin fenotiplemenin standart dili; HPO'nun kapsamı ve fenotipe dayalı varyant önceliklendirmesindeki rolü.*

5. **Cummings BB, Marshall JL, Tukiainen T, ve ark. (2017).** Improving genetic diagnosis in Mendelian disease with transcriptome sequencing. *Science Translational Medicine* 9(386):eaal5209. **PMID: 28424332** · DOI: [10.1126/scitranslmed.aal5209](https://doi.org/10.1126/scitranslmed.aal5209) — *Kullanım amacı: Senaryo 7 — tanısı konmamış kas hastalıklarında RNA dizilemenin %35 tanı sağlaması; ekzonik ve derin intronik splice-değiştirici varyantların saptanması.*

6. **Miller DT, Adam MP, Aradhya S, ve ark. (2010).** Consensus statement: chromosomal microarray is a first-tier clinical diagnostic test for individuals with developmental disabilities or congenital anomalies. *American Journal of Human Genetics* 86(5):749–764. **PMID: 20466091** · DOI: [10.1016/j.ajhg.2010.04.006](https://doi.org/10.1016/j.ajhg.2010.04.006) — *Kullanım amacı: Senaryo 3 — gelişimsel bozukluk/konjenital anomalide mikroarray'in birinci basamak testi olması. Kaynak kütüğünden yeniden kullanılmıştır.*

7. **Riggs ER, Andersen EF, Cherry AM, ve ark. (2020).** Technical standards for the interpretation and reporting of constitutional copy-number variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics (ACMG) and the Clinical Genome Resource (ClinGen). *Genetics in Medicine* 22(2):245–257. **PMID: 31690835** · DOI: [10.1038/s41436-019-0686-8](https://doi.org/10.1038/s41436-019-0686-8) — *Kullanım amacı: CNV'lerin ayrı çerçeveyle puanlanması. Kaynak kütüğünden yeniden kullanılmıştır.*

8. **Calucho M, Bernal S, Alías L, ve ark. (2018).** Correlation between SMA type and SMN2 copy number revisited: An analysis of 625 unrelated Spanish patients and a compilation of 2834 reported cases. *Neuromuscular Disorders* 28(3):208–215. **PMID: 29433793** · DOI: [10.1016/j.nmd.2018.01.003](https://doi.org/10.1016/j.nmd.2018.01.003) — *Kullanım amacı: Senaryo 1 — yedek gen kopya sayısının prognostik değeri. Kaynak kütüğünden yeniden kullanılmıştır.*

9. **Lorson CL, Hahnen E, Androphy EJ, Wirth B (1999).** A single nucleotide in the SMN gene regulates splicing and is responsible for spinal muscular atrophy. *Proceedings of the National Academy of Sciences USA* 96(11):6307–6311. **PMID: 10339583** · DOI: [10.1073/pnas.96.11.6307](https://doi.org/10.1073/pnas.96.11.6307) — *Kullanım amacı: Senaryo 1 — modifiye edici etkinin splicing üzerinden çalışması. Kaynak kütüğünden yeniden kullanılmıştır.*

10. **Berecki G, Howell KB, Deerasooriya YH, ve ark. (2018).** Dynamic action potential clamp predicts functional separation in mild familial and severe de novo forms of *SCN2A* epilepsy. *Proceedings of the National Academy of Sciences USA* 115(24):E5516–E5525. **PMID: 29844171** · DOI: [10.1073/pnas.1800077115](https://doi.org/10.1073/pnas.1800077115) — *Kullanım amacı: Senaryo 2 — mekanizma yönünün fonksiyonel olarak ayrılması. Kaynak kütüğünden yeniden kullanılmıştır.*

11. **Brunklaus A, Du J, Steckler F, ve ark. (2020).** Biological concepts in human sodium channel epilepsies and their relevance in clinical practice. *Epilepsia* 61(3):387–399. **PMID: 32090326** · DOI: [10.1111/epi.16438](https://doi.org/10.1111/epi.16438) — *Kullanım amacı: Senaryo 2 — mekanizma yönünün tedavi kararına çevrilmesi. Kaynak kütüğünden yeniden kullanılmıştır.*

12. **Biesecker LG, Spinner NB (2013).** A genomic view of mosaicism and human disease. *Nature Reviews Genetics* 14(5):307–320. **PMID: 23594909** · DOI: [10.1038/nrg3424](https://doi.org/10.1038/nrg3424) — *Kullanım amacı: Senaryo 4 — mozaikliğin klinik/moleküler sınıfları ve saptama zorlukları. Kaynak kütüğünden yeniden kullanılmıştır.*

13. **Keppler-Noreuil KM, Rios JJ, Parker VER, ve ark. (2015).** PIK3CA-related overgrowth spectrum (PROS): diagnostic and testing eligibility criteria, differential diagnosis, and evaluation. *American Journal of Medical Genetics Part A* 167A(2):287–295. **PMID: 25557259** · DOI: [10.1002/ajmg.a.36836](https://doi.org/10.1002/ajmg.a.36836) — *Kullanım amacı: Senaryo 4 — mozaik aşırı büyüme spektrumunda tanı ve test uygunluk ölçütleri. Kaynak kütüğünden yeniden kullanılmıştır.*

14. **Gorman GS, Chinnery PF, DiMauro S, ve ark. (2016).** Mitochondrial diseases. *Nature Reviews Disease Primers* 2:16080. **PMID: 27775730** · DOI: [10.1038/nrdp.2016.80](https://doi.org/10.1038/nrdp.2016.80) — *Kullanım amacı: Senaryo 5 — çift genom, heteroplazmi ve tanısal yaklaşım. Kaynak kütüğünden yeniden kullanılmıştır.*

15. **Stewart JB, Chinnery PF (2015).** The dynamics of mitochondrial DNA heteroplasmy: implications for human health and disease. *Nature Reviews Genetics* 16(9):530–542. **PMID: 26281784** · DOI: [10.1038/nrg3966](https://doi.org/10.1038/nrg3966) — *Kullanım amacı: Senaryo 5 — heteroplazminin dokular arası değişkenliği ve eşik kavramı. Kaynak kütüğünden yeniden kullanılmıştır.*

16. **Brioude F, Kalish JM, Mussa A, ve ark. (2018).** Clinical and molecular diagnosis, screening and management of Beckwith-Wiedemann syndrome: an international consensus statement. *Nature Reviews Endocrinology* 14(4):229–249. **PMID: 29377879** · DOI: [10.1038/nrendo.2017.166](https://doi.org/10.1038/nrendo.2017.166) — *Kullanım amacı: Senaryo 6 — imprinting alt tipine göre tanı ve tümör tarama planı. Kaynak kütüğünden yeniden kullanılmıştır.*

17. **Paulson H (2018).** Repeat expansion diseases. *Handbook of Clinical Neurology* 147:105–123. **PMID: 29325606** · DOI: [10.1016/B978-0-444-63233-3.00009-9](https://doi.org/10.1016/B978-0-444-63233-3.00009-9) — *Kullanım amacı: Senaryo 8 — tekrar genişlemesi mekanizmaları ve anticipasyonun klinik imzası. Kaynak kütüğünden yeniden kullanılmıştır.*

18. **Walker LC, de la Hoya M, Wiggins GAR, ve ark. (2023).** Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup. *American Journal of Human Genetics* 110(7):1046–1067. **PMID: 37352859** · DOI: [10.1016/j.ajhg.2023.06.002](https://doi.org/10.1016/j.ajhg.2023.06.002) — *Kullanım amacı: Senaryo 7 — RNA verisinin kritere çevrilmesi. Kaynak kütüğünden yeniden kullanılmıştır.*

19. **Richards S, Aziz N, Bale S, ve ark. (2015).** Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. *Genetics in Medicine* 17(5):405–424. **PMID: 25741868** · DOI: [10.1038/gim.2015.30](https://doi.org/10.1038/gim.2015.30) — *Kullanım amacı: Bütün senaryolarda sınıflandırma çerçevesi. Kaynak kütüğünden yeniden kullanılmıştır.*

20. **Campbell IM, Yuan B, Robberecht C, ve ark. (2014).** Parental somatic mosaicism is underrecognized and influences recurrence risk of genomic disorders. *American Journal of Human Genetics* 95(2):173–182. **PMID: 25087610** · DOI: [10.1016/j.ajhg.2014.07.003](https://doi.org/10.1016/j.ajhg.2014.07.003) — *Kullanım amacı: Trio yorumunda "de novo" bulgusunun sınırları ve tekrarlanma riski. Kaynak kütüğünden yeniden kullanılmıştır.*

> **İkincil/destekleyici kaynak notu:** GeneReviews, OMIM, ClinVar ve ClinGen kayıtları bu bölümde yalnızca destekleyici/başvuru kaynağı olarak anılmıştır. Senaryolar **öğretici amaçla** kurgulanmış tipik tablolardır; gerçek olgularda tanısal yol, merkezin olanaklarına, ulusal kılavuzlara ve güncel uzman panel önerilerine göre belirlenmelidir.

---

## ✅ Bölüm öz-denetim tablosu

**Tablo 17.4 — Bölüm 17 öz-denetim tablosu**

| Kriter | Durum | Not |
|--------|-------|-----|
| Mekanizma doğru anlatıldı mı? | ✅ | Klinik ipucu → mekanizma çevirisi sistematik hâle getirildi (12 ipucu); kitabın 2–16. bölümleri tek akışta birleştirildi |
| Klinik bağlantı kuruldu mu? | ✅ | Sekiz uçtan uca pediatrik senaryo; ilk basamak test seçimi; doku ve trio kararları; danışma dili |
| Varyant tipi ile mekanizma ilişkilendirildi mi? | ✅ | 11 satırlık "klinik tablo → beklenen varyant tipi → görebilen yöntem" tablosu |
| Pediatrik örnek verildi mi? | ✅ | Sekiz senaryonun tamamı pediatrik ve kaynaklı (SMA, *SCN2A*, CNV, mozaik aşırı büyüme, mitokondriyal, BWS, RNA/kas, tekrar genişlemesi) |
| Test seçimi açıklandı mı? | ✅ | Standart 8 satırlık tablo + basamaklı strateji; altı kör nokta ve her biri için ikinci basamak test |
| ACMG/ClinGen bağlantısı doğru mu? | ✅ | Fenotip → hastalık varlığı seçimi; aile örneğinin kanıt üretmesi; doku seçiminin kanıt geçerliliğine etkisi (Bölüm 16 ile köprü) |
| Kaynaklar PMID/DOI ile verildi mi? | ✅ | 20/20 kaynak PMID + DOI-link + kullanım amacı ile (5 yeni doğrulama + 15 kütükten yeniden kullanım) |
| Spekülatif iddialar işaretlendi mi? | ✅ | Senaryoların öğretici kurgu olduğu ve yerel/güncel kılavuzların esas alınması gerektiği açıkça belirtildi |
| Kaynak uydurma riski var mı? | ✅ Yok | 5 yeni PMID/DOI bu oturumda PubMed MCP ile doğrulandı; 15'i daha önce doğrulanmış kütük kaydı |
| Görsel/şema/algoritma desteği yeterli mi? (≥3 SVG, ≥2 Mermaid) | ✅ | **4 SVG + 3 Mermaid**; tüm SVG'ler tarayıcıda render edilip gözle denetlendi |

---

### 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu)
> "Bu bölümdeki tüm kaynakların PMID/DOI bilgisini kontrol et. PMID veya DOI veremediğin kaynağı çıkar. Kaynağı olmayan iddiayı 'kaynak doğrulaması gerekli' olarak işaretle."
>
> **Bu bölüm için durum:** **20/20 kaynak PMID+DOI doğrulandı** (5'i bu oturumda PubMed MCP ile — Clark 2018, Wright 2018, Smedley 2021, Köhler 2021, Cummings 2017; 15'i Bölüm_00 kaynak kütüğünden yeniden kullanıldı).
>
> **İşaretlenen iddialar:** (1) 7. başlıktaki sekiz senaryo **öğretici amaçla kurgulanmış tipik tablolardır**; gerçek olgu değildir. Her senaryodaki mekanizma–test eşleşmesi kaynaklıdır, ancak tanısal yol merkezin olanaklarına ve güncel ulusal kılavuzlara göre değişebilir. (2) Yeniden değerlendirme için önerilen 12–24 aylık aralık, yeni gen keşif hızına dayanan **pratik bir öneridir**; tek bir kılavuzda tanımlanmış bağlayıcı bir süre değildir. (3) Şekil 17.1 ve 17.2'deki eşleştirmeler pedagojik özetlerdir; ayırıcı tanı listesinin tamamını değil, en sık ve en ayırt edici örüntüleri kapsar.
