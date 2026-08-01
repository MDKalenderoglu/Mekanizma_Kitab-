# Terminoloji ve Yazım Kuralları

Bu bölüm, kitap boyunca kullanılan gösterim ve yazım kurallarını toplar. Amacı yalnızca tutarlılık değildir: **klinik genetikte gösterim biçimi, bilginin kendisidir.** Yanlış yazılmış bir varyant gösterimi, yanlış bir varyanttır.

---

## 1. Gen ve protein adlandırma

Gen adları **HGNC** (HUGO Gene Nomenclature Committee) onaylı sembollerle ve **italik** yazılır: *LMNA*, *FGFR3*, *SCN2A*. Protein adları **düz** yazılır: lamin A/C, fibroblast büyüme faktörü reseptörü 3, Na<sub>V</sub>1.2.

İnsan gen sembolleri **büyük harfle**, fare gen sembolleri **yalnız ilk harfi büyük** olacak biçimde yazılır: insan *FGFR3*, fare *Fgfr3*. Bu ayrım kitapta özellikle hayvan modeli tartışmalarında anlam taşır.

Eski/alternatif sembol kullanılması gerektiğinde güncel sembol parantez içinde verilir. Gen ailesi ya da lokus adı gerektiğinde italik kullanılmaz (ör. HLA sınıf II bölgesi).

## 2. Varyant gösterimi (HGVS)

Varyantlar **HGVS** standardına göre yazılır. Her gösterim üç bileşen içerir: **referans dizi**, **koordinat tipi** ve **değişim**.

| Ön ek | Neyi gösterir | Örnek |
|---|---|---|
| `c.` | kodlayan DNA dizisi | `NM_000138.5:c.7754G>A` |
| `g.` | genomik dizi | `NC_000015.10:g.48470535C>T` |
| `m.` | mitokondriyal DNA | `m.3243A>G` |
| `n.` | kodlamayan RNA geni | `n.76A>G` |
| `r.` | RNA düzeyi (gözlenen transkript) | `r.655_770del` |
| `p.` | protein düzeyi | `p.(Gly380Arg)` |

**Kurallar:**

- Klinik raporda ve bu kitapta, kodlayan varyant için **referans transkript sürümüyle birlikte** yazmak esastır: `NM_000138.5:c.7754G>A`. Metin akışında transkript tekrar tekrar yazılmaz; bölümde bir kez belirtilir.
- Protein değişimi **üç harfli** amino asit koduyla yazılır: `p.Gly380Arg` (`p.G380R` değil).
- Protein sonucu **öngörülüyorsa** parantez kullanılır: `p.(Gly380Arg)`. Deneysel olarak gösterilmişse parantezsiz yazılır.
- Delesyon `del`, duplikasyon `dup`, insersiyon `ins`, delesyon-insersiyon `delins` ile gösterilir: `c.76_78del`, `c.76_77dup`.
- Sonlanma kodonu `Ter` ile yazılır: `p.(Arg1162Ter)`; `*` kısaltması metin içinde tercih edilmez.
- Çerçeve kayması `fs` ile: `p.(Gly380ArgfsTer12)`.
- İki varyantın aynı alelde olması `[;]` yerine metinde ***in cis***, farklı alellerde olması ***in trans*** diye ifade edilir.
- **Yerleşik adlandırmalar korunur:** literatürde kökleşmiş kısa gösterimler (ör. akondroplazide p.Gly380Arg, MELAS'ta m.3243A>G, progeria'da c.1824C>T) metinde bu biçimleriyle anılır.

> **⚠️ Sık yapılan gösterim hatası:** "G380R mutasyonu" gibi transkriptsiz, ön eksiz ve tek harfli gösterim, hangi genin hangi transkriptine göre yazıldığını belirsiz bırakır. Bu kitapta böyle bir gösterim yalnızca tarihsel alıntılarda geçebilir.

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

Varyant sınıfları beş standart terimle yazılır: **patojenik**, **olası patojenik**, **belirsiz önemde varyant (VUS)**, **olası benign**, **benign**. Kriter kodları özgün biçimleriyle bırakılır (PVS1, PS3, PM2, BP4…); Türkçeleştirilmez.

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

### 7A. İngilizce terime Türkçe ek getirme (E5 kararı)

Uzun İngilizce ortak adlara kesme işaretiyle art arda Türkçe ek yapıştırmak okunabilir ama kitap dili açısından tercih edilmez. **Sıralama şudur:**

1. **Yeğlenen:** terimden sonra Türkçe bir taşıyıcı sözcük — "haploinsufficiency **durumunda**", "triplosensitivity **kavramının**", "splicing **sırasında**", "enhancer **bölgesinde**".
2. **Kabul edilen:** kısaltmalara ek — **HI'de**, **LoF'un**, **PVS1'in**, **ACMG/AMP'nin**, **VAF'ı**.
3. **Kaçınılan:** "haploinsufficiency'sinin", "triplosensitivity'ye", "enhancer'ının" gibi uzun terim + zincirleme ek.

Kısa ve yerleşmiş terimlerde (splicing'de, hotspot'ta) tek ek kabul edilebilir; asıl kaçınılması gereken **uzun terim + iyelik + hâl eki** zinciridir.

### 7B. Birbirine indirgenmemesi gereken kavram çiftleri

Bu liste, uzman turunun (G2.2) "otomatik eşitleme" uyarısının yazım kuralına çevrilmiş hâlidir. Aşağıdaki eşitlemeler metinde **kurulamaz**:

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

Kitabın başındaki üç liste (Şekiller, Algoritmalar, Tablolar) bu numaralardan otomatik üretilir; her satır ilgili bölüme bağlantılıdır.

## 11. Atıf biçimi

Metin içinde **yazar-yıl**: "… (Richards ve ark., 2015)". Tam künyeler bölüm sonu kaynakçalarında ve kitabın sonundaki toplu kaynakçada yer alır. Her künye şu sırayı izler:

**Yazar(lar) (Yıl).** Tam başlık. *Derginin tam adı* cilt(sayı):sayfa–sayfa. **PMID:** … · DOI: bağlantı — *kullanım amacı*.

Dört veya daha az yazar tam listelenir; beş ve üzeri için ilk üç yazar ve "ve ark." kullanılır. Dergi adları kısaltılmaz. Bibliyografik veriler PubMed üzerinden doğrulanmıştır.


---

## 12. Hedef kitle katmanları (F6 kararı)

Kitap dört okuyucu grubuna hitap eder, ancak bunlar eşit ağırlıkta değildir. **Birincil hedef: çocuk genetiği yandal asistanı ve klinik genomik veri yorumlayan hekim.** Genel pediatrist ve tıp öğrencisi **ikincil** hedef kitledir; laboratuvar/genomik yorumlayanlar birincil hedefin bir alt kümesidir.

Bu ayrım her bölümün başındaki **📘 Okuma katmanları** bloğuyla uygulanır:

| Katman | Kim | Ne okur |
|---|---|---|
| **① Temel** | Tıp öğrencisi | Bölümün çekirdek sezgisini kuran 1–2 başlık ve anahtar şekil |
| **② Klinik** | Genel pediatrist, klinisyen | Fenotipe dönüşüm, test seçimi ve karar algoritması hattı |
| **③ İleri düzey** | Yandal asistanı, laboratuvar, varyant yorumlayan | Mekanizmanın moleküler ayrıntısı ve ACMG/ClinGen kriter uygulaması |

Kural: katmanlar **okuma yolu** gösterir, içerik kısıtlaması değildir; hiçbir bölüm bir katman için basitleştirilmez. Deep-dive kutuları (🔬) doğal olarak ③, 🟦 kutuları ② katmanına aittir.
