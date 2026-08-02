# Terminoloji ve Yazım Kuralları

Bu bölüm, kitap boyunca kullanılan gösterim ve yazım kurallarını toplar. Amacı yalnızca tutarlılık değildir: **klinik genetikte gösterim biçimi, bilginin kendisidir.** Yanlış yazılmış bir varyant gösterimi, yanlış bir varyanttır.

---

## 1. Gen ve protein adlandırma

Gen adları **HGNC** (HUGO Gene Nomenclature Committee) onaylı sembollerle ve **italik** yazılır: *LMNA*, *FGFR3*, *SCN2A*. Protein ve kanal adları **düz** yazılır: lamin A/C, fibroblast büyüme faktörü reseptörü 3 ve Na<sub>V</sub>1.2. Son örnek bir gen sembolü değildir: **Na<sub>V</sub>1.2, *SCN2A* geninin kodladığı voltaj kapılı sodyum kanalı α-alt biriminin kanal/protein adıdır.**

İnsan gen sembolleri **büyük harfle**, fare gen sembolleri **yalnız ilk harfi büyük** olacak biçimde yazılır: insan *FGFR3*, fare *Fgfr3*. Bu ayrım kitapta özellikle hayvan modeli tartışmalarında anlam taşır.

Eski/alternatif sembol kullanılması gerektiğinde güncel sembol parantez içinde verilir. Gen ailesi ya da lokus adı gerektiğinde italik kullanılmaz (ör. HLA sınıf II bölgesi).

## 2. Varyant gösterimi (HGVS)

Varyantlar **HGVS** standardına göre yazılır. Her gösterim üç bileşen içerir: **referans dizi**, **koordinat tipi** ve **değişim**.

| Ön ek | Neyi gösterir | Örnek |
|---|---|---|
| `c.` | kodlayan DNA dizisi | `NM_000138.5:c.7754G>A` |
| `g.` | genomik dizi | `NC_000015.10:g.48470535C>T` |
| `m.` | mitokondriyal DNA | `NC_012920.1:m.3243A>G` |
| `n.` | kodlamayan RNA geni | `NR_002196.1:n.76A>G` |
| `r.` | RNA düzeyi (gözlenen transkript) | `NM_004006.3:r.(124a>u)` |
| `p.` | protein düzeyi | `NP_000133.1:p.(Gly380Arg)` |

### 2.1. HGVS/HGNC kuralları

- Klinik rapordaki varyant gösterimi, kullanılan **referans diziyi erişim ve sürüm numarasıyla** içermeli veya rapor içinde tartışmasız biçimde tanımlamalıdır: `NM_000138.5:c.7754G>A`. RefSeq ve Ensembl gibi sürümlendirilen dizilerde sürüm numarası olmayan gösterim geçerli değildir.
- Protein değişiminde üç harfli amino asit kodu HGVS tarafından yeğlenir ve bu kitapta zorunlu yazım biçimidir: `p.Gly380Arg` (`p.G380R` değil).
- Protein sonucu yalnız DNA/RNA bulgusundan **öngörülüyorsa** parantez kullanılır: `p.(Gly380Arg)`. Protein düzeyindeki sonuç doğrudan deneysel olarak gösterilmişse parantezsiz yazılır.
- Delesyon `del`, duplikasyon `dup`, insersiyon `ins`, delesyon-insersiyon `delins` ile gösterilir: `c.76_78del`, `c.76_77dup`.
- HGVS sonlanma kodonu için hem `Ter` hem `*` kullanımını kabul eder: `p.(Arg1162Ter)` ve `p.(Arg1162*)` eşdeğer gösterimlerdir.
- Çerçeve kayması `fs` ile gösterilir: `p.(Arg97ProfsTer23)`.
- Aynı aleldeki iki varyantın resmî HGVS gösterimi `c.[varyant1;varyant2]`, farklı alellerdeki iki varyantın gösterimi `c.[varyant1];[varyant2]` biçimindedir. Düzyazıda bunlar sırasıyla ***in cis*** ve ***in trans*** olarak açıklanır; sözel anlatım formal gösterimin yerine geçirilmez.

### 2.2. Bu kitabın editöryal tercihleri

- Klinik raporda tam gösterim korunur. Kitabın akıcı metninde referans transkript bir paragraf veya alt bölümde tam biçimiyle tanımlandıktan sonra, aynı bağlam içinde açıkça hangi transkriptin kullanıldığı belli olduğu sürece tekrar edilmeyebilir.
- HGVS iki biçimi de kabul etse de kitap genelinde sonlanma kodonu için `Ter` kullanılır; `*` yalnız tarihsel alıntı veya özgün veri aktarımı gerektiriyorsa korunur.
- Literatürde kökleşmiş kısa gösterimler (ör. akondroplazide `p.Gly380Arg`, MELAS'ta `m.3243A>G`, progeriada `c.1824C>T`) anlatı içinde korunabilir; ancak bunlar tek başlarına eksiksiz HGVS gösterimi değildir ve ilgili referans dizi bağlamda tanımlanır.

> **⚠️ Sık yapılan gösterim hatası:** "G380R mutasyonu" gibi referans dizisiz, ön eksiz ve tek harfli gösterim, değişimin hangi diziye göre yazıldığını belirsiz bırakır. Bu kitapta böyle bir gösterim yalnızca tarihsel alıntılarda geçebilir.

**Normatif kaynaklar (erişim: 02.08.2026):** [HGVS 21.1.4 genel önerileri](https://hgvs-nomenclature.org/21.1.4/recommendations/general/) · [HGVS referans dizileri](https://hgvs-nomenclature.org/stable/background/refseq/) · [HGVS alel/faz gösterimi](https://hgvs-nomenclature.org/stable/recommendations/DNA/alleles/) · [HGVS protein çerçeve kayması](https://hgvs-nomenclature.org/stable/recommendations/protein/frameshift/) · [HGNC yazım kuralları](https://www.genenames.org/help/faq/) · [IUPHAR Na<sub>V</sub>1.2 kaydı](https://www.guidetopharmacology.org/GRAC/ObjectDisplayForward?familyId=82&objectId=579) · [NCBI *SCN2A* kaydı](https://www.ncbi.nlm.nih.gov/gene/6326).

## 3. Kopya sayısı ve sitogenetik gösterim

Kopya sayısı varyantları **ISCN** biçiminde yazılır ve genom sürümü mutlaka belirtilir:

`arr[GRCh38] 17p12(14111772_15442362)x3`

Metin içinde okunabilirlik için sadeleştirilmiş anlatım kullanılabilir ("17p12 bölgesini kapsayan yaklaşık 1,4 Mb'lık duplikasyon"), ancak sadeleştirme gösterimin yerine geçmez.

Kromozom bölgeleri `17p12`, `15q11-q13`, `11p15.5` biçiminde yazılır. Genom sürümü (GRCh37/hg19 veya GRCh38/hg38) koordinat verilen her yerde belirtilir.

## 4. Tekrar dizileri

Tekrar birimleri parantez içinde, sayı `n` ile gösterilir: `(CAG)n`, `(CGG)n`, `(GGGGCC)n`. Alel boyu tekrar sayısı olarak verilir ("55–200 tekrar"), baz çifti olarak değil. Tekrar kategorileri kitapta tek biçimde adlandırılır: **normal**, **ara (intermediate)**, **premutasyon**, **tam mutasyon**.

## 5. Epigenetik ve metilasyon

Metilasyon sonuçları, ilgili bölgeye göre ve yön belirtilerek yazılır: "ICR1 hipermetilasyonu", "11p15.5 ICR2 hipometilasyonu". Damgalama bölgeleri kısaltmalarıyla (ICR, DMR) anılır; ebeveyn kökeni belirtilirken **maternal/paternal** terimleri kullanılır.

## 6. Sınıflandırma terimleri

Varyant sınıfları beş standart terimle yazılır: **patojenik**, **olası patojenik**, **klinik önemi belirsiz varyant (VUS)**, **olası benign**, **benign**. Kriter kodları özgün biçimleriyle bırakılır (PVS1, PS3, PM2, BP4…); Türkçeleştirilmez.

Gen–hastalık ilişkisinin geçerlilik sınıfları: **Kesin**, **Güçlü**, **Orta**, **Sınırlı**, **Bildirilmiş kanıt yok**, **Çelişkili kanıt**.

## 7. Türkçe terim tercihleri

Kitap boyunca aşağıdaki tercihler tek biçimde uygulanır:

| Kullanılan | Kullanılmayan | Not |
|---|---|---|
| varyant | mutasyon | "mutasyon" yalnız yerleşik adlandırmalarda (tam mutasyon, premutasyon, mutasyonel hotspot, de novo mutasyon oranı) |
| nonsense | nonsens | |
| hotspot | sıcak nokta | ilk geçişte "hotspot (sıcak nokta)" |
| eksik penetrans | azalmış penetrans | |
| dizileme | sekanslama | |
| dominant-negatif | dominant negatif · baskın-olumsuz | tireli yazılır; "baskın-olumsuz" yalnız ilk tanımda açıklayıcı karşılık olabilir |
| alel · alelik · bialelik · monoalelik | allel · allelik · biallelik | tek "l" ile; kitap geneli sabittir |
| haploinsufficiency | haployetersizlik · yalnız "yetersiz doz" | ilk geçişte **"haploinsufficiency — tek işlevsel kopyanın yetersizliği"**; sonra HI |
| kodlamayan | nonkoding | "kodlamayan" ≠ "düzenleyici"; ayrımı §7B'de |
| kriptik splice bölgesi | — | ilk geçişte "kriptik splice bölgesi (*cryptic splice site*)" |
| ekzon atlama · intron tutulması | ekzon skipping · intron retansiyonu | kitap geneli bu iki biçimi kullanır |
| donör (5′) / akseptör (3′) splice bölgesi | donor / acceptor (düz İngilizce) · verici / alıcı | Bölüm 7'de ilk geçişte İngilizce karşılık parantezde verilir; dallanma noktası (*branchpoint*) ve polipirimidin yolu aynı biçimde |

### 7A. İngilizce terime Türkçe ek getirme

Uzun İngilizce ortak adlara kesme işaretiyle art arda Türkçe ek yapıştırmak okunabilir ama kitap dili açısından tercih edilmez. **Sıralama şudur:**

1. **Yeğlenen:** terimden sonra Türkçe bir taşıyıcı sözcük — "haploinsufficiency **durumunda**", "triplosensitivity **kavramının**", "splicing **sırasında**", "enhancer **bölgesinde**".
2. **Kabul edilen:** kısaltmalara ek — **HI'de**, **LoF'un**, **PVS1'in**, **ACMG/AMP'nin**, **VAF'ı**.
3. **Kaçınılan:** "haploinsufficiency'sinin", "triplosensitivity'ye", "enhancer'ının" gibi uzun terim + zincirleme ek.

Kısa ve yerleşmiş terimlerde (splicing'de, hotspot'ta) tek ek kabul edilebilir; asıl kaçınılması gereken **uzun terim + iyelik + hâl eki** zinciridir.

### 7B. Birbirine indirgenmemesi gereken kavram çiftleri

Aşağıdaki kavramlar birbirinin otomatik eşdeğeri değildir; bu eşitlemeler metinde **kurulamaz**:

| Eşitlenmemeli | Neden |
|---|---|
| kesici (truncating) varyant = gerçek null | NMD'den kaçan transkript ürün verir; mekanizma DN/GoF'a kayabilir |
| düşük LOEUF = kanıtlanmış haploinsufficiency | Constraint popülasyon ölçümüdür, klinik mekanizma kanıtı değildir |
| missense + multimerik protein = dominant-negatif | DN net etkidir; ürünün üretilmesi *ve* trans etkisi gösterilmelidir |
| toksik işlev kazanımı = neomorfik | Neomorfi *neyin değiştiğini*, toksisite *sonucu* anlatır |
| son ekzon = otomatik düşürülmüş PVS1 | Güç, kesilen bölgenin kritikliğine göre belirlenir |
| kanonik splice = PVS1_VeryStrong | Gen-spesifik karar ağacı ve NMD beklentisi gerekir |
| kodlamayan varyant = PVS1 asla uygulanamaz | Splicing mekanizmalı intronik varyantta PVS1_Strength(RNA) olabilir |
| iki gende nadir varyant = digenik hastalık | Kanıt basamakları tamamlanmadan yalnız *aday* modeldir |
| domain konumu = fenotip/prognoz | Kohort düzeyinde zenginleşme, bireysel öngörü değildir |
| kodlamayan = düzenleyici | Derin intronik splice, kodlamayan RNA ve tekrar varyantları da kodlamayandır |
| VAF = mutant hücre oranı | Heterozigot varyantta VAF ≈ hücre oranının yarısıdır |

**Latince ifadeler:** *de novo* düz yazılır (Türkçe klinik genetikte yerleşiktir); *in vitro*, *in silico*, *in cis*, *in trans* italik yazılır.

**İngilizce teknik terimler** ilk geçişte parantezle Türkçeleştirilir, sonra tek biçimde devam edilir. Kısaltmalar ilk geçişte açılır.

## 8. Sayı, birim ve aralık

Ondalık ayırıcı **virgül** (`0,41`), binlik ayırıcı **nokta** (`20.068`). Yüzde işareti sayıdan **önce** yazılır (`%25`), aralıklarda **en-dash** kullanılır (`%90–99`, `12–24 ay`, `405–424`). Kat artışı "≈100 kat" biçiminde yazılır.

## 9. Metin içi kutular ve işaretler

| İşaret | Anlamı |
|---|---|
| 🔬 **Deep-dive** | Mekanizmanın derinine inen, ileri düzey tartışma |
| 🟦 **Klinikte dikkat** | Doğrudan uygulamaya dönük uyarı |
| 🔴 **Sık yapılan hata** | Yaygın yanlışların listesi |
| 🧠 **Hatırlatıcı** | Mnemonik veya özet |
| 📘 **Okuma katmanları** | Bölüm başındaki üç katmanlı okuma yolu (① Temel · ② Klinik · ③ İleri düzey) |
| 🏷️ | Kitabın pedagojik sentezi — literatürde bu adla yerleşik bir çerçeve değildir |
| ⚠️ | Tartışmalı, sınırlı ya da doğrulanması gereken iddia |
| ✅ / ⬜ | Tamamlanmış / bekleyen öz-denetim maddesi |

## 10. Şekil, algoritma ve tablo numaralandırması

Numaralar **bölüm.sıra** biçimindedir ve metinde ilk anıldıkları sıraya göre verilir: `Şekil 5.2`, `Algoritma 12.3`, `Tablo 9.1`.

- **Şekil:** çizim (SVG) — mekanizma şeması, anatomi, eğri, harita.
- **Algoritma:** karar ağacı ve klinik akış şeması.
- **Tablo:** kavram, varyant tipi, test ve öz-denetim tabloları.

Kitabın başındaki üç liste (Şekiller, Algoritmalar, Tablolar) bu numaralardan otomatik üretilir. HTML'de her satır bölüm başına değil, doğrudan ilgili şekil, algoritma veya tabloya bağlanır. Sabit sayfası olmayan akışkan HTML'de bölüm bilgisi gösterilir; nihai sayfalandırılmış PDF/baskı çıktısında gerçek hedef sayfa numarası otomatik üretilir.

## 11. Atıf biçimi

Metin içinde **yazar-yıl**: "… (Richards ve ark., 2015)". Tam künyeler bölüm sonu kaynakçalarında ve kitabın sonundaki toplu kaynakçada yer alır. Her künye şu sırayı izler:

**Yazar(lar) (Yıl).** Tam başlık. *Derginin tam adı* cilt(sayı):sayfa–sayfa. **PMID:** … · DOI: bağlantı — *kullanım amacı*.

Dört veya daha az yazar tam listelenir; beş ve üzeri için ilk üç yazar ve "ve ark." kullanılır. Dergi adları kısaltılmaz. Bibliyografik veriler PubMed üzerinden doğrulanmıştır.


---

## 12. Hedef kitle katmanları

Kitap farklı deneyim düzeylerine hitap eder, ancak gruplar eşit ağırlıkta değildir. **Birincil hedef kitle:** tıbbi genetik uzmanları ve uzmanlık öğrencileri; çocuk genetiği alanında çalışan hekimler ve yandal öğrencileri; klinik genomik ve varyant yorumlama yapan hekimler; tıbbi biyoloji uzmanları ve araştırmacıları; moleküler genetik tanı laboratuvarı ekipleridir. **İkincil hedef kitle:** pediatri uzmanları ve asistanları; moleküler biyoloji ve genetik alanında eğitim alanlar; genetik danışmanlık ekipleri ve ileri düzey tıp öğrencileridir.

Bu ayrım her bölümün başındaki **📘 Okuma katmanları** bloğuyla uygulanır:

| Katman | Kim | Ne okur |
|---|---|---|
| **① Temel** | İleri düzey tıp öğrencisi ve alana yeni giren okur | Bölümün çekirdek sezgisini kuran 1–2 başlık ve anahtar şekil |
| **② Klinik** | Tıbbi genetik/pediatri hekimi ve diğer klinisyenler | Fenotipe dönüşüm, test seçimi ve karar algoritması hattı |
| **③ İleri düzey** | Tıbbi genetik, klinik genomik, tıbbi biyoloji, moleküler tanı ve varyant yorumlama ekipleri | Mekanizmanın moleküler ayrıntısı ve ACMG/ClinGen ölçüt uygulaması |

Kural: katmanlar **okuma yolu** gösterir, içerik kısıtlaması değildir; hiçbir bölüm bir katman için basitleştirilmez. Deep-dive kutuları (🔬) doğal olarak ③, 🟦 kutuları ② katmanına aittir.
