# Önsöz — Bu kitap neden yazıldı, nasıl okunmalı?

## Kitabın tezi

Tıbbi genetik eğitiminin çoğu, hastalık adları üzerine kuruludur: hangi sendromun hangi geni, hangi genin hangi fenotibi. Bu bilgi gereklidir ama tek başına kırılgandır, çünkü hızla eskir ve tanımadığınız bir tabloyla karşılaştığınızda size yol göstermez.

Bu kitap başka bir omurga önerir: **mekanizma**. Bir varyantın hastalığa nasıl yol açtığını — proteini yok mu ediyor, azaltıyor mu, bozuyor mu, ona yeni bir iş mi yaptırıyor, komşu genin ifadesini mi değiştiriyor — anladığınızda üç şey birden çözülür. Hastanın **hangi test**e ihtiyacı olduğu, laboratuvarın bulduğu varyantın **nasıl yorumlanacağı** ve aileye verilecek **riskin nasıl hesaplanacağı**. Kitabın her bölümü bu nedenle aynı zinciri kurar:

> **mekanizma → varyant tipi → hücresel sonuç → klinik fenotip → tanısal test → varyant yorumu**

Bu zincir, kitabın hem içindekiler listesini hem de her bölümün iç yapısını belirler.

## Kimler için?

Kitap, dört okuyucu grubunu aynı anda gözeterek yazıldı:

**Tıp öğrencileri** için her zor kavram, önce sezgisel bir girişle ve benzetmeyle açılır; ardından tanımlanır, sonra klinikte neden önemli olduğu gösterilir. Terimler ilk geçtikleri yerde cümle içinde tanımlanır; ayrı bir sözlük ezberi gerekmez.

**Genel pediatri hekimleri** için her bölümde "hangi klinik ipucu bu mekanizmayı düşündürür" ve "bu şüpheyle hangi testi isterim" soruları açıkça yanıtlanır; 17. bölüm bunu sekiz uçtan uca senaryoyla tekrar eder.

**Çocuk genetiği uzmanları ve yandal asistanları** için mekanizmalar nüanslarıyla, tartışmalı noktalarıyla ve landmark çalışmalara dayandırılarak ele alınır; deep-dive kutuları bu okuyucu için yazılmıştır.

**Genomik veri yorumlayanlar** (laboratuvar uzmanları, biyoinformatikçiler, genetik danışmanlar) için her bölümün 6. başlığı ACMG/ClinGen çerçevesiyle doğrudan bağ kurar; 16. bölüm bu bağların tamamını tek bir matriste toplar.

## Kitap nasıl okunmalı?

**Baştan sona okuma** en çok kazandıran yoldur, çünkü bölümler birbirinin üzerine kurulur: Bölüm 2'deki işlev kaybı kavramı olmadan Bölüm 3'teki doz–eşik mantığı, o olmadan Bölüm 5'teki dominant-negatif matematiği anlaşılmaz.

Zamanı kısıtlı okuyucular için üç kısayol vardır:

- **Klinik kısayol:** Bölüm 1 → Bölüm 17 → oradan senaryoların gönderdiği bölümler.
- **Laboratuvar kısayolu:** Bölüm 2 → Bölüm 16 → Bölüm 15 → ilgilendiğiniz mekanizma bölümü.
- **Sınav kısayolu:** her bölümün başındaki *çekirdek tez* ve *öğrenme hedefleri*, sonundaki *öz-denetim tablosu* ve *sık yapılan hatalar* kutusu.

## Her bölümün yapısı

Bölümler aynı iskeleti izler; bu, aradığınızı nerede bulacağınızı bilmenizi sağlar.

Her bölüm bir **çekirdek tez** ve **öğrenme hedefleriyle** açılır. Ardından on standart başlık gelir: kavramsal tanım, moleküler mekanizma, varyant tipleri, klinik fenotipe dönüşüm, tanısal testlerle ilişkisi, varyant yorumlama açısından önemi, pediatrik klinik örnekler, sık yapılan hatalar, klinik karar algoritması ve kaynaklar. Bölüm, bir **öz-denetim tablosu** ve **kaynak doğrulama durumuyla** kapanır.

Metin içinde dört kutu türü kullanılır: **🔬 deep-dive** (mekanizmanın derinine inen, ileri düzey tartışma), **🟦 klinikte dikkat** (pratik uyarı), **🔴 sık yapılan hata** (yaygın yanlışların listesi) ve **🧠 hatırlatıcı** (mnemonik). Doğrulanamamış ya da tartışmalı iddialar **⚠️** ile işaretlenir.

## Kaynak politikası

Bu kitaptaki her mekanizma ve yorumlama iddiası, bibliyografik verisi **PubMed üzerinden tek tek doğrulanmış** kaynaklara dayanır; her kaynağın PMID'si ve DOI bağlantısı verilir. Metin içinde yazar-yıl biçimi kullanılır, tam künyeler bölüm sonlarındaki kaynakçalarda ve kitabın sonundaki **toplu kaynakçada** yer alır.

GeneReviews, OMIM, ClinVar ve gnomAD gibi ikincil kaynaklar yalnızca destekleyici bilgi olarak anılır; hiçbiri ana mekanizma kaynağı olarak kullanılmaz. Bir iddia doğrulanamadığında ya çıkarılmış ya da açıkça işaretlenmiştir.

## Görseller hakkında

Kitaptaki şekiller dekorasyon değil, anlatının taşıyıcısıdır; her biri tek başına okunabilecek biçimde tasarlandı: başlık, panel yapısı ve tek cümlelik bir "öğreti" satırı içerir. Renkler anlam taşır — mavi işlev kaybı ve normal-kontrollü durumu, kırmızı işlev kazanımı ve patojen ağırlığı, amber klinik dikkat noktalarını, sarı yıldız ise "varyant burada" işaretini gösterir.

Karar ağaçları ve algoritmalar Mermaid diyagramı olarak gömülmüştür; kitabın HTML sürümü çevrimdışı olarak da bunları çizer.

## Sınırlar ve sorumluluk

Bu bir **eğitim metnidir**, klinik kılavuz değildir. Tanısal ve tedaviye yönelik kararlar; hastanın kendi klinik bağlamına, merkezin olanaklarına ve **güncel ulusal/uluslararası kılavuzlar ile ilgili uzman panel önerilerine** göre verilmelidir. Varyant sınıflandırma kuralları ve gen–hastalık ilişkileri zamanla değişir; kitapta verilen eşikler, puanlar ve örnek yorumlar öğretici amaçlıdır.

Klinik senaryolar ve çözümlü örnekler **kurgudur**; gerçek hasta verisi içermez.

---

> **Bir cümlede kitap:** Gen adlarını ezberlemek yerine mekanizmayı anlayın; mekanizma size testi de, yorumu da, aileye söyleyeceğiniz cümleyi de verir.
