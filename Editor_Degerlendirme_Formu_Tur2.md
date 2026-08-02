# Editöryal Değerlendirme Formu — Tur 2

> **Bu form nedir?** Birinci tur (`Uzman_Degerlendirme_Formu.md`) **dış uzmanın** bilimsel değerlendirmesiydi ve A–G maddelerinin tamamı uygulandı. Bu form ise kitabın tamamının **editöryal** bir gözle yeniden taranmasından çıkan bulgulardır: tutarlılık, kapsam, yapı, okuyucu deneyimi ve yayına hazırlık. Bilimsel iddia denetimi değil, **kitap olarak bütünlük** denetimidir.
>
> **Yöntem:** 17 bölüm + ön/arka madde + şablonlar programatik olarak tarandı (numaralandırma sürekliliği, çapraz gönderme geçerliliği, sayım tutarlılığı, terminoloji uyumu, tablo/mermaid yapısı, kaynak kütüğü kapsaması, mutlaklaştırma dili) ve içerik örneklemeyle okundu.
>
> **Gösterim:** **D** = değişiklik gerekmez · **A** = ana fikir doğru, revizyon gerekli · **Y** = değiştirilmeli
>
> **Nasıl doldurulur:** Her maddede önce **nerede** olduğu, sonra **ne gördüğüm**, sonra **soru** var. Kutuya D/Y/A yazıp altına notunuzu düşün; boş bıraktıklarınız "karar verilmedi" sayılır ve uygulanmaz.

---

## Karar oturumu — 2 Ağustos 2026

Bu formun yayın yönünü belirleyen maddeleri kullanıcıyla tek tek görüşüldü. Aşağıdaki kayıtlar **onaylanmış kararı** gösterir; bölüm/dosya değişikliklerinin uygulandığını göstermez. Uygulama, ayrı kapsam ve ayrı kullanıcı onayıyla paketler hâlinde yapılacaktır.

1. Önce HTML + PDF değerlendirme sürümü; bağımsız uzman incelemelerinden sonra dijital ve baskıya hazır nihai sürüm.
2. Birincil hedef kitle: tıbbi genetik ve çocuk genetiği hekimleri/eğitim alanlar, klinik genomik ve varyant yorumlama uzmanları, tıbbi biyoloji uzmanları/araştırmacıları ve moleküler genetik tanı laboratuvarı ekipleri. İkincil hedef: pediatri hekimleri, moleküler biyoloji ve genetik alanında eğitim alanlar, genetik danışmanlık ekipleri ve ileri düzey tıp öğrencileri.
3. Mevcut Bölüm 15 (alelik seri), mevcut Bölüm 14'ten (digenik/oligogenik mimari) önceye alınacak.
4. Kalıtsal kanser yatkınlığı ve ikinci vuruş, mozaiklik içine yerleştirilmeyecek; bağımsız Bölüm 16 olacak. Mevcut Bölüm 16 ve 17 sırasıyla 17 ve 18'e kayacak.
5. Okuyucuya yönelik öz değerlendirme soruları kitabın sonunda bölüm bazında gruplanacak; bölüm sonlarında bağlantı verilecek; yanıt yaklaşımları sorulardan ayrı tutulacak.
6. Ayrıntılı üretim/doğrulama günlükleri proje içinde korunacak; yayımlanan kitapta yalnız kısa, okuyucuya yönelik yöntem açıklaması bulunacak.
7. Türkiye'ye özgü klinik uygulama eki mevcut kapsama alınmayacak; gelecek sürüm için taahhüt edilmeyecek.
8. Uygulama sırası: karar kaydı → düşük riskli teknik temizlik → ayrı bilimsel/yapısal paketler → bağımsız insan değerlendirmesi → yayın kapanışı.

---

## 0. Bu turda zaten düzeltilenler (onayınıza sunulur, soru değildir)

Bunlar tartışmasız olgusal/iç tutarlılık hatalarıydı; sormadan düzelttim. İtirazınız varsa geri alınır.

| # | Nerede | Neydi | Ne yapıldı |
|---|---|---|---|
| 0.1 | `assets/` · 4 dosya | "allel → alel" standardizasyonu `.md` içindeki görsel referanslarını değiştirmiş, dosya adları eski kalmıştı. **Şekil 1.4, 6.x, 9.x ve 15.1 HTML kitaba hiç gömülmüyordu** (build sessizce atlıyor, uyarı vermiyor). | Dosyalar yeni adlarına taşındı; artık 66 SVG inline. |
| 0.2 | Böl.01 · Böl.16 öz-denetim | Böl.01 "6 SVG + **4** Mermaid" (gerçek 3), Böl.16 "4 SVG + **3** Mermaid" (gerçek 2). | Gerçek sayılara çekildi. |
| 0.3 | Böl.08 · Böl.09 · Böl.16 doğrulama blokları | Böl.08 "6/6 kaynak" (kaynakçada 7), Böl.09 "10/10" (13), Böl.16 "24/24" (25). Uzman turlarında eklenen kaynaklar sayıma girmemişti. | Üçü de gerçek sayıya çekildi; Böl.08'de Hook 1977'nin DOI'siz künye biçimi ayrıca belirtildi. |
| 0.4 | `Bölüm_00` kaynak kütüğü | Böl.03'te kullanılan **Birchler & Veitia 2012 (PMID 22908297)** kütükte yoktu. | Kütüğe eklendi. Kütük artık 153 PMID'nin tamamını içeriyor, yetim kayıt yok. |
| 0.5 | Böl.15 · Böl.16 | Kendi C21–C24 turlarımızda metne "allelik hastalık", "allelik durum", "nonsens varyant" biçimleri kaçmıştı (kitap standardı: *alelik*, *nonsense*). | Düzeltildi. |
| 0.6 | `kitap/20_Ekler.md` Ek B | Ek B, Şekil 16.3'ün metin hâli. D4 turunda yalnız **şekli** güncellemiştim; Ek B hâlâ "✖ uygulanamaz" diyor ve normatif olmadığı uyarısını taşımıyordu — yani şekille çelişiyordu. | Ek B şekille eşitlendi (pedagojik sentez ibaresi, "genellikle uygulanmaz", VCEP önceliği, PM1_Supporting ve PVS1_Strength(RNA) istisnaları). |

---

## A. Yayına hazırlık — kitabın kendisinde görünen boşluklar

### A1 · Künye, ithaf, teşekkür, özgeçmiş

**Nerede:** `kitap/01_Kunye.md`, `02_Ithaf.md`, `04_Tesekkur.md`, `24_Ozgecmis.md` — ve bunların hepsi üretilen HTML kitaba giriyor.

**Ne gördüm:** Yayımlanan kitapta **11 yerde `[DOLDURULACAK]` ibaresi basılı hâlde duruyor** — kurum, sürüm numarası, basım tarihi, yayıncı, ISBN, ithaf metni, teşekkür metni, yazar özgeçmişi. Bunlar bir okuyucunun ilk gördüğü sayfalar.

**Soru:** Bu alanları siz doldurmak ister misiniz, yoksa **sürüm/tarih gibi otomatikleştirilebilecek olanları `build_book.py` üretim sırasında doldursun** (ör. "Sürüm 0.9 · derleme tarihi 01.08.2026") ve yalnız ithaf/teşekkür/özgeçmiş size mi kalsın? Ayrıca: kitap ISBN'siz mi yayımlanacak?

**Değerlendirme:** ☐ D ☐ Y ☒ A → HTML/PDF değerlendirme sürümü ve ardından dijital + baskıya hazır nihai sürüm kararlaştırıldı. Sürüm numarası, ISBN, yayınevi ve kişisel alanlar yayın kapanışında doldurulacak; otomatik alan üretiminin ayrıntısı teknik paket içinde ayrıca onaylanacak.

<br>

### A2 · "Görseller hakkında not" kutusu — yazım ortamı okuyucuya sızıyor

**Nerede:** 15 bölümün başında, çekirdek tezin hemen altında.

> 🖼️ **Görseller hakkında not:** Şekil 12.1–12.4 `assets/` klasöründe SVG olarak bulunur. Mermaid diyagramları metin içine gömülüdür.

**Ne gördüm:** Bu not, kitabın **kaynak dosyalarıyla** çalışan biri için yazılmış. Ama yayımlanan üründe (tek dosyalık HTML ya da PDF) okuyucunun `assets/` klasörü yok, "Mermaid" diye bir şey görmüyor, tüm görseller zaten gömülü. Not 15 kez basılıyor ve okuyucuya hiçbir şey söylemiyor. Ayrıca Böl.01 ve Böl.02'de bu not hiç yok — yani zaten tutarlı da değil.

**Soru:** Bu not **yayımlanan kitaptan tamamen çıkarılsın** mı (build sırasında filtrelenir, `.md` kaynaklarında kalır), yoksa okuyucuya gerçekten hitap eden bir şeye mi dönüştürülsün (ör. "Şekiller yüksek çözünürlüklü ve vektöreldir; yazdırmada bozulmaz")?

**Değerlendirme:** ☐ D ☒ Y ☐ A → Kaynak dosyasında yararlıysa korunabilir; yayımlanan HTML/PDF'de kaynak ortamı/Mermaid/assets dili gösterilmeyecek. Okuyucuya yararlı bir erişilebilirlik veya vektör görsel notu gerekiyorsa yayın tasarımı aşamasında tek ve genel bir not olarak değerlendirilecek.

<br>

### A3 · Önsöz ile yeni okuma katmanları çelişiyor

**Nerede:** `kitap/03_Onsoz.md` satır 15 ve 39 vs. 17 bölümün başındaki yeni **📘 Okuma katmanları** bloğu.

**Ne gördüm:** Önsöz *"Kitap, dört okuyucu grubunu aynı anda gözeterek yazıldı"* diyor ve dördünü eşit ağırlıkta sayıyor. Uzman turunun F6/G5 kararı ise farklıydı ve bölüm başlarına şu şekilde işlendi: **birincil hedef = yandal asistanı ve klinik genomik çalışan hekim; genel pediatrist ve tıp öğrencisi ikincil.** Ayrıca önsözün "Her bölüm bir çekirdek tez ve öğrenme hedefleriyle açılır" cümlesi artık eksik — arada okuma katmanları bloğu var.

**Soru:** Önsöz bu hiyerarşiyi açıkça yazsın mı ("birincil / ikincil hedef kitle"), yoksa dört grubu eşit sunan mevcut nazik dil mi korunsun? İkisi aynı kitapta duramaz; hangisi sizin tercihiniz?

**Değerlendirme:** ☐ D ☒ Y ☐ A → Önsöz birincil/ikincil hedef kitleyi açıkça yazacak. Birincil: tıbbi genetik, çocuk genetiği, klinik genomik/varyant yorumlama, tıbbi biyoloji ve moleküler tanı ekipleri. İkincil: pediatri, moleküler biyoloji ve genetik eğitimi, genetik danışmanlık ekipleri ve ileri düzey tıp öğrencileri. Üç katmanlı okuma sistemi bu farklı deneyim düzeylerini destekleyecek.

<br>

### A4 · Kısaltmalar listesi yeni terimleri kapsamıyor

**Nerede:** `kitap/06_Kisaltmalar.md`

**Ne gördüm:** Uzman turlarında kitaba giren iki kısaltmanın listede karşılığı yok: **pLoF** (öngörülen işlev kaybı — LoF'tan ayrı bir kavram, sözlüğe eklendi ama kısaltma listesinde yok) ve **CSpec** (ClinGen Criteria Specification Registry). Ayrıca listede `allel` yazımı iki yerde eski biçimde duruyor.

**Soru:** Kısaltmalar listesini sözlükle **otomatik senkron** tutmak ister misiniz (build sırasında sözlükten üretilir), yoksa elle bakım yeterli mi?

**Değerlendirme:** ☐ D ☐ Y ☐ A → Karar verilmedi. pLoF/CSpec ve eski `allel` yazımları teknik temizlik kapsamına adaydır; otomatik senkron ile elle bakım arasında ayrıca karar verilecektir.

---

## B. Yapısal tutarlılık

### B1 · Bölüm 1'in öğrenme hedefleri diğer 16 bölümden farklı biçimde

**Nerede:** `Bölüm_01_Genetik_Hastalık_Mekanizması.md` · "## Öğrenme hedefleri"

> Bu bölümü bitiren okuyucu; genetik bilginin DNA'dan kromozoma uzanan fiziksel organizasyonunu ve bunun gen ifadesiyle ilişkisini açıklayabilmeli; bir genin yapısal ögelerini tanıyıp… (tek paragraf, noktalı virgüllerle, altı hedef iç içe)

**Ne gördüm:** Diğer **16 bölümün tamamı** numaralı liste kullanıyor (1., 2., 3. …). Bölüm 1 tek bir uzun paragraf. Öz-denetim tablosu ve sınav kısayolu okuma yolu (önsöz: "her bölümün başındaki öğrenme hedefleri") madde madde okunabilirlik varsayıyor.

**Soru:** Bölüm 1 de numaralı listeye çevrilsin mi? (İçerik aynı kalır, yalnız biçim değişir.)

**Değerlendirme:** ☐ D ☐ Y ☐ A →

<br>

### B2 · Bölüm 4'ün test tablosunda "Methylation array" satırı yok

**Nerede:** `Bölüm_04_Gain_of_Function.md` · §5 tanısal testler tablosu

**Ne gördüm:** `CLAUDE.md` standart test tablosunu sekiz sabit satır olarak tanımlıyor (WES · short-read WGS · long-read WGS · array · MLPA · RNA-seq · **Methylation array** · Karyotip). Bölüm 4 bu satırı çıkarmış, yerine "Fonksiyonel test (*in vitro*)" koymuş. Diğer 16 bölümün tamamı sekiz satırı koruyup **ek** satır ekliyor (ör. Böl.12 "derin panel/ddPCR", Böl.11 "mtDNA dizileme").

**Soru:** Bölüm 4'e de "Methylation array — ⚠️ bu mekanizmayı yakalamaz" satırı eklensin ve fonksiyonel test **dokuzuncu** satır olarak mı kalsın? (Tutarlılık lehine bunu öneriyorum; alternatif, standardı "sekiz satır zorunlu değil, ilgisiz olan çıkarılabilir" diye gevşetmek.)

**Değerlendirme:** ☐ D ☐ Y ☐ A →

<br>

### B3 · Kaynakça "atıf/doğrulama notu" üç farklı metinle yazılmış

**Nerede:** Her bölümün "## 10. Kaynaklar" başlığının hemen altı.

**Ne gördüm:** Böl.02–04 bir metin, Böl.01 başka bir metin, Böl.09 sonrası üçüncü bir metin kullanıyor. Hepsi aynı şeyi söylüyor ama farklı cümlelerle; kitabın en tekrarlayan yapısal ögesi bu.

**Soru:** Tek bir standart cümleye indirilsin mi? Ayrıca: yeni kaynak politikası (01.08.2026) hakemli makale dışındaki kaynak türlerini de kabul ettiğine göre, bu notun **"PubMed üzerinden doğrulanmıştır"** ifadesi de güncellenmeli mi ("kaynak türüne uygun kalıcı kimlikle doğrulanmıştır" gibi)?

**Değerlendirme:** ☐ D ☐ Y ☐ A →

---

## C. İçerik ve kapsam

### C1 · Öz-denetim tabloları artık kitabın bir parçası — okuyucuya mı, size mi ait?

**Nerede:** Her bölümün sonundaki "✅ Bölüm öz-denetim tablosu" + "🔎 Bölüm sonu kaynak doğrulama komutu" blokları — **hepsi yayımlanan kitapta basılı.**

**Ne gördüm:** Bu bloklar artık çok uzadı. Örneğin Bölüm 12'de doğrulama bloğu 6 paragraf ve her uzman turunun ne düzelttiğini tek tek anlatıyor ("C15 — …, C16 — …, C17 — …"). Bunlar **yazım süreci kayıtları**; kitabın denetlenebilirlik iddiasının kanıtı olarak değerli, ama okuyucu için mi yazılmışlar belirsiz. Bir okuyucu Bölüm 12'yi bitirdiğinde son okuduğu şey, o bölümün editöryal geçmişi oluyor.

**Soru:** Üç seçenek var, hangisi?
1. **Olduğu gibi kalsın** — şeffaflık kitabın kimliğidir.
2. **Kitabın sonuna toplu bir "Doğrulama kaydı" eki**ne taşınsın; bölüm sonunda yalnız kısa öz-denetim tablosu kalsın.
3. **Yayımlanan sürümden çıkarılsın**, `.md` kaynaklarında ve `Dogrulama_Kutugu.md`'de tutulsun.

**Değerlendirme:** ☐ D ☒ Y ☐ A → Ayrıntılı öz-denetim ve kaynak doğrulama/uzman turu günlükleri yayımlanan sürümden çıkarılacak; proje kaynaklarında ve `Dogrulama_Kutugu.md` içinde korunacak. Okuyucuya yönelik öz değerlendirme soruları ayrı `kitap/19_Oz_Degerlendirme.md` hedefinde bölüm bazında toplanacak; bölüm sonunda yalnız bağlantı bulunacak. Bu dosya ve build davranışı henüz uygulanmadı.

<br>

### C2 · Uzmanın "en zayıf bölüm" dediği Bölüm 14 için kanıt hiyerarşisi metin içinde, ayrı bir kutu değil

**Nerede:** `Bölüm_14_Digenik_Oligogenik_Modifier.md` · §6 · 🟦 kutusu

**Ne gördüm:** Uzman G3'te Bölüm 14'ü kitabın epistemik olarak en kırılgan bölümü ilan etti ve altı basamaklı bir **kanıt hiyerarşisi** istedi. Bölümde bu içeriğin neredeyse tamamı var (beş gereklilik + fonksiyonel ortak-etki modeli + "üç durumu ayırın" uyarısı), ama **numaralandırılmış bir kontrol listesi olarak değil**, bir 🟦 kutusunun içinde akan metin olarak. Uzmanın istediği "bir digenik iddiayı savunmadan önce şu altı basamağı geç" biçimi değil.

**Soru:** Bu içerik, §6'da numaralı bir **"Digenik iddia kontrol listesi"** kutusuna (veya Şekil 14.4'ün yanına bir Mermaid akışına) çevrilsin mi? İçerik yeni kaynak gerektirmez, yalnız biçim değişir.

**Değerlendirme:** ☐ D ☐ Y ☐ A →

<br>

### C3 · Uzmanın F4'ü: klinik örnekler dominant nörogelişimsel/iskelet lehine eğilimli

**Nerede:** Kitap geneli §7 "Pediatrik genetikten klinik örnekler" başlıkları.

**Ne gördüm:** Bunu sayarak doğruladım. Kitabın omurga örnekleri: *FGFR3, PAX6, TBX5, SCN2A, PTPN11, COL1A1, AKT1, GNAQ, GNAS, LMNA, IDH1, NF1/NF2*. Buna karşılık: **otozomal resesif metabolik hastalık** yalnız *PAH* üzerinden ve kısa; **X'e bağlı** hastalık *DMD* ve *ATP7A* ile sınırlı; **renal** yalnız yeni eklenen *COL4A3/4*; **işitme** neredeyse yok; **kanser predispozisyonu** *TP53* dışında yok; **anöploidi/kromozom hastalığı** (21, 22q11.2, Turner) bir mekanizma örneği olarak hemen hiç geçmiyor.

**Soru:** Hangi eksikler kapatılsın? Yeni bölüm açmadan, mevcut bölümlerin §7'lerine birer örnek eklenebilir:
- ☐ AR metabolik/enzim (ör. *GALT* veya *ASS1* — rezidüel aktivite ekseni, Böl.2/15)
- ☐ X'e bağlı (ör. *OTC* — zaten Böl.16'da var, Böl.1'e kalıtım örneği olarak taşınabilir)
- ☐ İşitme (ör. *GJB2* — hem AR hem dominant, hem de kurucu varyant örneği)
- ☐ Kanser predispozisyonu (ör. *RB1* iki-vuruş — Böl.2'ye)
- ☐ Anöploidi (ör. 22q11.2 delesyon sendromu — Böl.8'e; kısmen var mı kontrol edilmeli)

**Değerlendirme:** ☐ D ☐ Y ☐ A →

<br>

### C4 · Bölüm 8'de anöploidi ve kromozom segregasyonu görünmez

**Nerede:** `Bölüm_08_CNV_Yapisal_Varyantlar.md` başlık yapısı.

**Ne gördüm:** Uzman F2'de bunu istemişti ve haklı: bölüm CNV ve yapısal varyantı çok iyi anlatıyor ama **nondisjunction, trizomi/monozomi, mozaik anöploidi ve kromozom segregasyonu** ana alt başlık olarak yok. Konu Böl.10 (trizomi kurtarma → UPD) ve Böl.12 (mozaik anöploidi) içinde parça parça geçiyor. Bir pediatrik genetik kitabında Down sendromunun mekanizması hiçbir bölümün ana başlığı değil.

**Soru:** Bölüm 8'e "Sayısal anomaliler: nondisjunction ve anöploidi" diye bir alt başlık (§2.x) eklensin mi? Yoksa bu bilinçli bir kapsam kararı mı — kitap "mekanizma" kitabı olduğu için klasik sitogenetik dışarıda mı bırakıldı?

**Değerlendirme:** ☐ D ☐ Y ☐ A →

---

## D. Kalan uzman kalemleri (birinci turdan devredenler)

Bunlar uzmanın istediği ama **sizin kararınızı beklediğim** kalemler. Kolay cevaplanabilsin diye tek tabloya topladım.

| # | Uzman maddesi | Ne gerektirir | Karar |
|---|---|---|---|
| D1 | **F1(a)** — Bölüm 15 (Alelik seri), Bölüm 14'ten (Digenik) önce gelmeli | Dosya adları, iki bölümün numaraları, ~40 çapraz gönderme, kütükteki "kullanıldığı bölümler" sütunu, Ek B ve Şekil 16.3 satır sırası. Yapılabilir ama geniş tarama. | ☒ Yap ☐ Yapma — ayrı yapısal paket |
| D2 | **F2** — "Kanser yatkınlığı ve somatik ikinci vuruş" bölümü | Tam bir textbook bölümü: *RB1, TP53, DICER1, APC*, MMR, *TSC1/2*, *NF1* üzerinden two-hit, LOH, doku seçiciliği, mozaiklik kesişimi + PubMed doğrulamalı kaynaklar + SVG/Mermaid. Uzun iş. | ☒ Yap ☐ Yapma — bağımsız Bölüm 16; mozaiklik içine yerleştirilmez |
| D3 | **F3** — Zorunlu 10 başlık → 6 sabit çekirdek + esnek | `CLAUDE.md` ve şablon değişir; mevcut bölümler olduğu gibi kalabilir. Yalnız **bundan sonra** yazılacak bölümleri etkiler. | ☐ Yap ☐ Yapma |
| D4 | **F5** — Türkiye eki (sürümlendirilmiş) | Sabit içerik (akrabalık, endogami, kurucu varyant, ROH, resesif test stratejisi) + değişken içerik (SGK, test menüsü) ayrı; tarih ve sürüm numaralı. | ☐ Yap ☒ Yapma — mevcut kapsam dışında; gelecek sürüm taahhüdü yok |
| D5 | **G2.7** — Bağımsız dış hakem okuması | Klinik genetik uzmanı · moleküler tanı laboratuvarı uzmanı · sitogenetik/CNV uzmanı · Türkçe bilimsel editör. **Bunu ben yapamam**; uzman da modelin bunun yerine geçemeyeceğini açıkça yazdı. | ☒ Planlandı ☐ Değil — bilimsel/yapısal paketlerden sonra |

---

## E. Genel sorular

**E1 — Kitabın sürüm numarası ne olsun ve bunu kim/nasıl artıracağız?** Şu an sürüm alanı boş. Uzman turlarından sonra kitap belirgin biçimde değişti; bir sürüm politikası (ör. "0.9 — dış hakem öncesi", "1.0 — hakem sonrası") kitabın denetlenebilirlik iddiasını tamamlar.

> **Kısmi karar:** Değerlendirme sürümü, bağımsız inceleme ve nihai yayın sırası kabul edildi. Kesin sürüm numaraları ve artırma politikası yayın kapanışı öncesinde ayrıca kararlaştırılacak.
>

**E2 — Yayım formatı nihai olarak ne? ** Şu an tek dosyalık HTML → tarayıcıdan PDF. Basılı kitap, e-kitap (EPUB) veya web sürümü hedefleniyorsa bazı kararlar (görsel çözünürlüğü, sayfa kırılımı, iç bağlantılar, renk-körlüğü uyumu) şimdiden değişir.

> **Karar:** Önce HTML + PDF değerlendirme sürümü; bağımsız uzman incelemelerinden sonra dijital ve baskıya hazır nihai sürüm. EPUB/web dağıtım ayrıntısı yayın kapanışında ayrıca değerlendirilecek.
>

**E3 — Hangi bulguları önce ele alalım?** Bu formdaki maddeleri sıraya koymamı ister misiniz, yoksa siz mi seçeceksiniz?

> **Karar:** Kararların kalıcı kaydı → düşük riskli teknik temizlik → ayrı bilimsel/yapısal paketler → bağımsız insan değerlendirmesi → yayın kapanışı.
>

---

### Form döndükten sonra ne olacak?

- **Y** ve **A** işaretli maddeler uygulanır; bir kural değişiyorsa **kitap genelinde** aranır.
- **D** işaretli maddeler için metin değişmez; `Dogrulama_Kutugu.md`'ye "editöryal tur — değişiklik gerekmedi" kaydı düşülür.
- Düzeltmelerden sonra `python3 build_book.py` ile kitap yeniden derlenir.
