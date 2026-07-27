# Bölüm 2 — Loss-of-Function (İşlev Kaybı) Mekanizmaları

> **Bölümün çekirdek tezi:** Loss-of-function (LoF), genin işlevsel ürününün **niceliksel olarak azalması veya kaybolması**dır. Ancak "varyant LoF yapar" demek tek başına ne patojeniteyi, ne kalıtım modelini, ne de fenotip ağırlığını belirler. Bunları üç eksen belirler: *(1)* transkript **NMD'ye girer mi**, *(2)* gen LoF'a ne kadar **duyarlı** (doz/haploinsufficiency), *(3)* etkilenen **domain ve rezidüel fonksiyon** ne kadar. Bu üç eksen, aynı varyant tipinin neden bir gende ağır resesif, başka gende hafif veya dominant hastalık yaptığını açıklar.

Bu bölüm, Bölüm 1'deki **niceliksel vs niteliksel bozukluk** ayrımının "niceliksel" kolunu derinleştirir. Niteliksel kol (GoF, dominant-negatif, neomorfik) Bölüm 4–6'da; doz hastalıklarının özel hâli haploinsufficiency Bölüm 3'te işlenir.

---

## Öğrenme hedefleri

Bu bölümü tamamlayan okuyucu:
1. LoF'a giden tüm moleküler yolları (null, nonsense, frameshift, kanonik splice, start-loss, ekzon/tam gen delesyonu, promoter/enhancer kaybı) ayırt edebilir.
2. NMD ve NMD-escape mekaniğini, PTC konumuyla ilişkilendirerek klinik sonuca bağlayabilir.
3. Okuma çerçevesi kuralını (in-frame vs out-of-frame) Duchenne/Becker örneğiyle açıklayabilir.
4. "LoF her zaman patojen midir?" sorusunu constraint metrikleri (pLI, LOEUF) ve gen-hastalık mekanizması üzerinden yanıtlayabilir.
5. Aynı gendeki LoF'un neden bazen dominant (haploinsufficiency) bazen resesif olduğunu gerekçelendirebilir.
6. Hipomorfik allel ve rezidüel fonksiyon kavramını genotip-fenotip korelasyonuyla (PKU) bağlayabilir.
7. PVS1 kriterini ClinGen SVI karar ağacına göre, gücünü doğru ayarlayarak uygulayabilir.

---

## 1. Kavramsal tanım

**Tablo 2.1 — İşlev kaybının temel kavramları**

| Kavram | Tanım | Klinik anlamı |
|--------|-------|---------------|
| **Loss-of-function (LoF)** | Gen ürününün işlevinin kısmen/tamamen kaybı | Mekanizmanın yönü "azalma"dır; doz/eşik mantığı geçerli |
| **Null allel (amorf)** | Hiç işlevsel ürün üretmeyen allel | En şiddetli LoF ucu (tam fonksiyon kaybı) |
| **Hipomorfik allel** | Azalmış ama sıfır olmayan işlev | Rezidüel fonksiyon fenotipi hafifletir |
| **Rezidüel fonksiyon** | Varyant sonrası kalan işlev miktarı | Genotip–fenotip korelasyonunun motoru |
| **Nonsense-mediated decay (NMD)** | PTC taşıyan mRNA'yı yıkan gözetim mekanizması | "Transkript yok" → gerçek null; kaçarsa → truncated protein |
| **NMD escape** | PTC'nin NMD'den kurtulması (genelde son ekzon) | Truncated protein üretilir → DN/GoF riski (Bölüm 5) |
| **Truncated protein** | Erken sonlanmış kısa protein | İşlevsiz, yarı-işlevsel veya toksik olabilir |
| **Haploinsufficiency** | Tek işlevsel allelin (%50 doz) yetersizliği | Heterozigot LoF → dominant hastalık (Bölüm 3) |
| **Resesif LoF** | Hastalık için iki allelin de kaybı gerekir | Heterozigot taşıyıcı sağlıklı |
| **Compound heterozigot** | Aynı gende iki farklı patojen allel (trans) | Resesif hastalıkların büyük kısmı; faz şart |
| **LoF intoleransı** | Genin LoF'a popülasyon düzeyinde dayanıksızlığı | "Bu gende LoF beklenen mekanizma mı?" |

---

## 2. Moleküler mekanizma

### 2.1. LoF'a giden yollar — fonksiyon nerede kaybedilir?

İşlevsel ürün, santral dogmanın herhangi bir basamağında kaybedilebilir. Bunları "yukarıdan aşağıya" izlemek tanısal düşünmeyi kolaylaştırır:

1. **Transkript hiç/yetersiz üretilir** → *promoter/enhancer kaybı, tam gen delesyonu.* (Bu varyantlar WES'te çoğu kez görünmez; Bölüm 8, 13.)
2. **Transkript yanlış işlenir** → *kanonik splice-site varyantı* → ekzon atlama veya intron retansiyonu (Bölüm 7).
3. **Transkript yıkılır** → *nonsense/frameshift* → PTC → NMD → fonksiyonel null.
4. **Protein başlatılamaz** → *start-loss* (AUG kaybı) → translasyon başlamaz veya aşağı akıştaki alternatif AUG kullanılır (belirsizlik).
5. **Protein kısalır/bozulur** → *NMD'den kaçan PTC* → truncated protein; *in-frame indel* → domain bozulması; *destabilize edici missense* → katlanamayan/yıkılan protein (fonksiyonel null'a eşdeğer olabilir).

> **🔬 Deep-dive — Missense de "LoF" olabilir.** LoF yalnızca truncating varyantların işi değildir. Protein katlanmasını/stabilitesini bozan bir missense, hücrede hızla yıkılan bir ürün oluşturarak **fonksiyonel null** gibi davranabilir (ör. birçok metabolik enzim varyantı). Bu nedenle "LoF mekanizması" gen düzeyinde bir özelliktir; varyant tipi tek başına mekanizmayı garanti etmez.

### 2.2. NMD: LoF mekanizmasının kalbi

![Şekil 2.1 — NMD kararı: PTC nerede?](assets/sekil_07_nmd_karar.svg)

NMD, erken sonlanma kodonu (PTC) taşıyan transkriptleri yıkan bir mRNA gözetim sistemidir; bu transkriptlerin yıkılmaması, dominant-negatif veya gain-of-function etkilerle hücreye toksik olabilen anormal proteinlerin sentezine yol açabilir ve NMD bilgisi çeşitli genetik hastalıklarda genotip–fenotip korelasyonunu anlamak için gereklidir (Khajavi, Inoue, Lupski, 2006, *Eur J Hum Genet*; [DOI](https://doi.org/10.1038/sj.ejhg.5201649)).

**Pozisyon kuralı (basitleştirilmiş):** Bir PTC, **son ekzon-ekzon bağlantısının yaklaşık 50 nükleotid yukarısından daha önce** yer alıyorsa transkript genellikle NMD'ye uğrar (→ fonksiyonel null). PTC **son ekzonda** veya son bağlantıya çok yakınsa **NMD'den kaçar** (→ truncated protein üretilir; DN/GoF riski; Şekil 2.1).

Bu ayrım klinik olarak belirleyicidir, çünkü:
- **NMD (+):** Transkript yok → "temiz" LoF → fenotip haploinsufficiency (dominant gende) veya resesif LoF mantığıyla; toksik protein riski düşük.
- **NMD (−) / escape:** Truncated protein üretilir → işlevsiz, yarı-işlevsel **veya dominant-negatif/toksik** olabilir → mekanizma sınıfı kayabilir (Bölüm 5) ve PVS1 gücü düşer (§6).

> **🔬 Deep-dive — NMD verimliliği mutlak değildir.** NMD'nin etkinliği transkripte, hücre tipine ve fizyolojik duruma göre değişir; bazı transkriptler kısmen kaçar. Bu nedenle *in silico* "NMD bekleniyor" tahmini, mümkünse **RNA çalışmasıyla** (allel-spesifik ekspresyon) doğrulanmalıdır.

### 2.3. Okuma çerçevesi (reading-frame) kuralı

![Şekil 2.2 — Okuma çerçevesi kuralı (DMD)](assets/sekil_08_okuma_cercevesi_dmd.svg)

DMD lokusundaki kısmi delesyonlarda okuma çerçevesini **bozan** (out-of-frame) delesyonlar truncated/anormal protein ile ağır **Duchenne** fenotipine; çerçeveyi **koruyan** (in-frame) delesyonlar ise daha kısa ama yarı-işlevsel protein ile daha hafif **Becker** fenotipine yol açar; aynı mekanizma splice mutasyonlarına da uygulanır (Monaco ve ark., 1988, *Genomics*; [DOI](https://doi.org/10.1016/0888-7543(88)90113-9)).

Bu "okuma çerçevesi hipotezi" LoF biyolojisinin klasik örneğidir ve iki dersi birden verir: *(1)* aynı tip varyant (delesyon) bile **çerçeve etkisine** göre farklı şiddet yapar; *(2)* mekanizma bilgisi tedaviye dönüşür — **ekzon-atlama (exon-skipping)** tedavileri, out-of-frame bir transkripti yeniden in-frame'e çevirerek Duchenne'i Becker-benzeri daha hafif bir tabloya kaydırmayı amaçlar.

---

## 3. Varyant tipleri ve beklenen LoF sonucu

**Tablo 2.2 — Varyant tipleri ve beklenen işlev kaybı sonuçları**

| Varyant tipi | Tipik moleküler sonuç | NMD beklentisi | Notlar |
|--------------|------------------------|----------------|--------|
| **Nonsense (stop-gain)** | PTC | Erken → NMD; son ekzon → kaçış | Kaçışta truncated protein |
| **Frameshift (indel)** | Çerçeve kayması → downstream PTC | Çoğunlukla NMD | Son ekzonda kaçabilir |
| **Kanonik ±1,2 splice** | Ekzon atlama / intron retansiyonu | Sonuç çerçeveye bağlı | RNA ile doğrulama ideal (Bölüm 7) |
| **Start-loss** | Translasyon başlamaz / alternatif AUG | NMD dışı | Belirsizlik; fonksiyonel kanıt yardımcı |
| **Büyük/tam gen delesyonu** | Allel tümüyle yok | — | Saf doz kaybı (array/MLPA) |
| **Tek/çok ekzon delesyonu** | Çerçeveye bağlı LoF | — | DMD'de çerçeve kuralı belirleyici |
| **Promoter/enhancer kaybı** | Transkripsiyon azalır/durur | — | WES kaçırır (Bölüm 13) |
| **İn-frame indel** | Domain bütünlüğü bozulur | NMD dışı | LoF veya DN olabilir |
| **Destabilize missense** | Katlanma/stabilite kaybı | NMD dışı | Fonksiyonel null'a eşdeğer olabilir |

---

## 4. Klinik fenotipe dönüşüm — bölümün anahtar soruları

### 4.1. Bir LoF varyantı her zaman patojen midir? → **Hayır.**

LoF tahmini (pLoF), patojenite ile eşanlamlı **değildir**. Patojenite için en az şu koşullar gerekir:
- **Gen, LoF'a duyarlı olmalı** (LoF gerçekten o gen için hastalık mekanizması olmalı).
- **Varyant gerçekten null etki yapmalı** (NMD, son ekzon, doku-özgü ekspresyon, alternatif transkriptler dikkate alınmalı).
- **Kalıtım modeli uymalı** (dominant haploinsufficiency mi yoksa resesif mi? Tek allel mi, iki allel mi?).

> **🔬 Deep-dive — Sağlıklı insanlarda da LoF vardır.** Tipik bir insan genomu çok sayıda predicted-LoF varyantı taşır ve genler inaktivasyona tolerans açısından geniş bir spektrumda yer alır; LoF'a **kısıtlı (constrained)** genler hastalıkla ilişki için zenginleşmiştir (Karczewski ve ark., 2020, *Nature*; [DOI](https://doi.org/10.1038/s41586-020-2308-7)). Yani "bir LoF varyantı bulundu" demek, ilgili genin LoF-intoleran olduğu gösterilmeden patojenite anlamına gelmez.

### 4.2. LoF intoleransı ve constraint metrikleri (pLI, LOEUF, HI)

**Tablo 2.3 — İşlev kaybı intoleransı metrikleri ve yorum yönü**

| Metrik | Ne ölçer? | Yorum yönü |
|--------|-----------|-----------|
| **pLI** | Genin LoF'a intolerans olasılığı (0–1) | pLI ≥ 0,9 → haploinsufficiency/dominant LoF için güçlü ipucu |
| **LOEUF** | Gözlenen/beklenen pLoF üst güven sınırı | Düşük LOEUF → LoF intoleran gen |
| **HI skoru / ClinGen dozaj** | Tek kopya kaybının patojenitesi | CNV yorumuna bağlanır (Bölüm 3, 8) |

> ⚠️ Bu metrikler **gen düzeyinde** önceliklendirme aracıdır; tek bir varyantın patojenitesini tek başına kanıtlamaz. Ayrıca **resesif LoF genleri** (her iki allel gerekir) genellikle "intoleran" görünmez — metriklerin doğru yorumlanması için kritik bir nokta.

### 4.3. Aynı gendeki LoF neden bazen dominant, bazen resesif?

**Algoritma 2.1 — Aynı gendeki işlev kaybı neden farklı ağırlıkta hastalık yapar?**

```mermaid
flowchart TD
  A["Heterozigot LoF varyantı (tek allel)"] --> B{"Tek işlevsel allel (%50 doz) yeterli mi?"}
  B -->|"Hayır → doz duyarlı gen"| C["Haploinsufficiency<br/>DOMİNANT hastalık (Bölüm 3)"]
  B -->|"Evet → yeterli rezerv var"| D["Heterozigot SAĞLIKLI (taşıyıcı)"]
  D --> E{"İkinci allel de kaybedilirse?"}
  E -->|"Evet (homozigot/compound het)"| F["RESESİF hastalık"]
```

Karar, genin **doz duyarlılığı** ve **fonksiyonel rezervi** ile belirlenir. Doz duyarlı genler (transkripsiyon faktörleri, kromatin düzenleyiciler, gelişim genleri) tipik olarak haploinsufficiency → dominant; yüksek rezervli genler (birçok metabolik enzim) resesif davranır. Constraint metrikleri bu ayrımda yön gösterir.

### 4.4. NMD olur / olmazsa klinik sonuç (özet)

**Tablo 2.4 — NMD olması ve olmaması durumunda klinik sonuçlar**

| | **NMD (+)** | **NMD (−) / escape** |
|---|------------|----------------------|
| Ürün | Transkript yıkılır → ürün yok | Truncated protein üretilir |
| Mekanizma | Temiz LoF (haploinsuff/resesif) | LoF **veya** dominant-negatif/toksik |
| Şiddet eğilimi | Genin doz mantığına uyar | Bazen beklenenden ağır |
| PVS1 gücü | Tam (gen uygunsa) | Düşürülür |

### 4.5. C-terminal truncation neden bazen hafif, bazen ağır?

- **Hafif olabilir:** Kesilen C-terminal bölge işlevsel olarak az önemliyse, protein büyük ölçüde işlevini korur (yarı-işlevsel) → hafif fenotip.
- **Ağır olabilir:** C-terminal kritik bir domain (dimerizasyon, lokalizasyon sinyali, düzenleyici bölge) içeriyorsa **veya** truncated protein dominant-negatif etki gösteriyorsa (NMD'den kaçtığı için üretilir), fenotip beklenenden ağır olur.

> "Son ekzon = her zaman hafif/benign" varsayımı bu nedenle **yanlıştır** (Şekil 2.1B).

### 4.6. Rezidüel fonksiyon ve allelik spektrum

![Şekil 2.3 — LoF allelik spektrumu: rezidüel fonksiyon → fenotip](assets/sekil_09_lof_spektrum.svg)

Resesif LoF hastalıklarında fenotip ağırlığı, kalan işlevle ters orantılı bir **spektrum** oluşturur (Şekil 2.3). Compound heterozigotlarda pratik kural: **fenotipi genellikle daha hafif (rezidüel işlevi daha yüksek) allel belirler** — "daha iyi allel kazanır". Bu, PKU'da klasik PKU → hafif PKU → hafif hiperfenilalaninemi spektrumunun temelidir (§7.4).

---

## 5. Tanısal testlerle ilişkisi

**Tablo 2.5 — İşlev kaybı mekanizmasını hangi test yakalar?**

| Test | Bu mekanizmayı yakalar mı? | Sınırlılığı |
|------|----------------------------|-------------|
| **WES** | ✅ Nonsense, frameshift, kanonik splice, start-loss, missense | Promoter/enhancer kaybı, derin intronik LoF, bazı ekzon delesyonlarını (kapsama bağlı) kaçırır |
| **Short-read WGS** | ✅ Yukarıdakiler + birçok CNV/ekzon delesyonu + regülatör | Karmaşık SV ve tekrar bölgelerinde sınırlı |
| **Long-read WGS** | ✅ Büyük del/kompleks SV, faz (trans/cis) | Maliyet/erişim; standartizasyon gelişmekte |
| **Array-CGH / SNP array** | ✅ Tam/büyük gen delesyonu; SNP array UPD | Tek ekzon altı çözünürlük ve SNV göremez |
| **MLPA** | ✅ Ekzon düzeyi del/dup (DMD, NF1) | Yalnız hedef lokus; dizi bilgisi yok |
| **RNA-seq** | ✅ NMD'yi (allel dengesizliği), splice etkisini gösterir | İlgili dokuda ekspresyon ve uygun örnek gerekir |
| **Methylation array** | ⚠️ Doğrudan değil | LoF'u göstermez (Bölüm 10) |
| **Karyotip** | ⚠️ Yalnız çok büyük delesyonlar | Çözünürlük düşük |

> **Bu mekanizmayı hangi test yakalar? (özet):** Nokta LoF varyantları → **WES/WGS**; ekzon düzeyi delesyon/duplikasyon → **MLPA veya array/WGS**; NMD ve splice sonucu → **RNA-seq** doğrular. DMD/NF1 gibi delesyon-duplikasyon ağırlıklı genlerde dizileme + doz testi **birlikte** gereklidir; yalnız dizileme yapmak büyük delesyonu kaçırır.

---

## 6. Varyant yorumlama açısından önemi (ACMG/ClinGen — PVS1)

ACMG/AMP çerçevesi predicted LoF için güçlü patojenik kriter PVS1'i tanımlar (Richards ve ark., 2015, *Genet Med*; [DOI](https://doi.org/10.1038/gim.2015.30)); ancak orijinal kılavuz LoF tiplerinin ayrımını ve güç derecelendirmesini ayrıntılandırmamıştı. ClinGen SVI çalışma grubu, PVS1'i **varyant tipi, konumu, NMD beklentisi ve genin LoF mekanizması** üzerinden karar ağacına bağlayan ve gücü (PVS1 → Strong → Moderate → Supporting) ayarlayan ayrıntılı öneriler yayımlamıştır (Abou Tayoun ve ark., 2018, *Hum Mutat*; [DOI](https://doi.org/10.1002/humu.23626)).

**PVS1 karar ağacı (ClinGen SVI mantığının basitleştirilmiş özeti):**

**Algoritma 2.2 — Öngörülen işlev kaybı varyantında PVS1 akışı**

```mermaid
flowchart TD
  A["Predicted LoF varyant"] --> G{"Gen için LoF, BİLİNEN hastalık mekanizması mı?"}
  G -->|"Hayır / belirsiz"| GX["PVS1 UYGULAMA<br/>(GoF/DN mekanizmalı gende uygunsuz)"]
  G -->|"Evet"| T{"Varyant tipi?"}
  T -->|"Nonsense / frameshift"| N{"NMD bekleniyor mu?"}
  N -->|"Evet (erken PTC)"| P1["PVS1 (güçlü)"]
  N -->|"Hayır (son ekzon/yakın)"| P2["Kesilen bölge kritik mi?<br/>Evet→PVS1_Moderate/Strong · Hayır→düşür/Supporting"]
  T -->|"Kanonik ±1,2 splice"| S["RNA/çerçeve sonucunu değerlendir (Bölüm 7)<br/>→ güç buna göre"]
  T -->|"Start-loss"| SL["Alternatif AUG ve bölge önemi → genelde daha zayıf"]
  T -->|"Tek/çok ekzon delesyonu"| D["Çerçeve etkisi + NMD → güç buna göre"]
```

Mekanizmadan doğan kontroller (özet):
- **Gen LoF-mekanizmalı mı?** PVS1 yalnız bu genlerde tam güçle.
- **NMD beklentisi var mı?** Son ekzon kaçışı → güç düşer.
- **Kesilen bölgenin önemi:** Truncation klinik açıdan önemli/biofonksiyonel bir domaini çıkarıyor mu?
- **Allelik heterojenite uyarısı:** CFTR gibi genlerde binlerce varyantın yalnız bir kısmı hastalık nedenidir; tahmini LoF dahi klinik+fonksiyonel kanıtla desteklenmelidir (Sosnay ve ark., 2013, *Nat Genet*; [DOI](https://doi.org/10.1038/ng.2745)).

> **🟦 Klinikte dikkat — PVS1 otomatik değildir:** "Çok güçlü" bir kriter olan PVS1'in mekanizma kontrolü yapılmadan uygulanması, yanlış-patojen sınıflamanın en sık kaynaklarından biridir. Önce gen-hastalık geçerliliği ve LoF mekanizması; sonra varyant tipi/konum.

---

## 7. Pediatrik genetikten klinik örnekler

### 7.1. NF1 — haploinsufficiency ile dominant LoF
NF1 (nörofibromin) bir tümör baskılayıcıdır; heterozigot LoF varyantları (nonsense, frameshift, splice, tam gen/ekzon delesyonu) tek allel kaybıyla **dominant** nörofibromatozis tip 1'e yol açar. *Öğreti:* hem nokta LoF hem büyük delesyonlar aynı gende hastalık yapar → tanıda **dizileme + doz analizi (MLPA/array)** birlikte. (Haploinsufficiency → Bölüm 3; tümör baskılayıcı "ikinci vuruş" → Bölüm 15.)

### 7.2. DMD — çerçeve kuralı ile Duchenne vs Becker
Distrofin geninde out-of-frame delesyonlar truncated protein ile ağır **Duchenne**'e; in-frame delesyonlar yarı-işlevsel protein ile daha hafif **Becker**'e yol açar (Monaco ve ark., 1988; [DOI](https://doi.org/10.1016/0888-7543(88)90113-9)). *Öğreti:* aynı gen, aynı "delesyon" tipi — fakat **çerçeve etkisi** fenotip ağırlığını belirler (Şekil 2.2); ekzon-atlama tedavilerinin mantıksal temeli budur.

### 7.3. CFTR — resesif LoF ve allelik heterojenite
Kistik fibroz, CFTR'de **iki** patojen allel gerektiren resesif bir hastalıktır; çok sayıda varyant tanımlıdır ama yalnız bir kısmı hastalık nedenidir ve patojenite klinik + fonksiyonel veriyle tanımlanmalıdır (Sosnay ve ark., 2013; [DOI](https://doi.org/10.1038/ng.2745)). *Öğreti:* heterozigot taşıyıcı sağlıklıdır; tanı için **trans faz** ve allel patojenitesi gösterilmelidir.

### 7.4. PKU/PAH — hipomorfik aleller ve rezidüel fonksiyon
Fenilketonüri, PAH genindeki varyantlarla oluşan resesif bir aminoasit metabolizması hastalığıdır; genotipler rezidüel enzim aktivitesini yansıtan bir spektrumda (klasik PKU → hafif PKU → hafif hiperfenilalaninemi) dağılır ve büyük genotip veritabanları fenotip ile BH4 yanıtını öngörmeyi mümkün kılar (Hillert ve ark., 2020, *Am J Hum Genet*; [DOI](https://doi.org/10.1016/j.ajhg.2020.06.006)). *Öğreti:* **rezidüel fonksiyon = fenotip ağırlığının motoru**; compound heterozigotlarda fenotipi genellikle daha hafif allel belirler (Şekil 2.3).

---

## 8. Sık yapılan hatalar

> **🔴 Sık yapılan hata kutusu**
>
> 1. **"pLoF = patojen" varsaymak.** Gen LoF-duyarlı mı, NMD oluyor mu, kalıtım uyuyor mu kontrol edilmeli.
> 2. **Son-ekzon nonsense'i otomatik "hafif/benign" saymak.** NMD kaçışı → truncated protein → DN/GoF riski.
> 3. **PVS1'i mekanizma kontrolü yapmadan uygulamak.** GoF/DN gende PVS1 uygunsuz (Abou Tayoun 2018).
> 4. **pLI/LOEUF'u resesif genlerde yanlış yorumlamak.** Resesif LoF genleri "tolerant" görünebilir.
> 5. **Sadece dizileme yapıp ekzon delesyonunu kaçırmak.** NF1/DMD'de MLPA/array eklenmeli.
> 6. **Resesif tanıda fazı doğrulamamak.** İki varyantın trans olduğu (ebeveyn testi) gösterilmeli.
> 7. **Çerçeve etkisini ihmal etmek.** İn-frame vs out-of-frame fenotipi kökten değiştirir.
> 8. **Missense'i "LoF olamaz" sanmak.** Destabilize missense fonksiyonel null olabilir.

---

## 9. Klinik pratikte karar algoritması

**Algoritma 2.3 — İşlev kaybı varyantı saptandığında klinik karar akışı**

```mermaid
flowchart TD
  A["LoF (predicted) varyant saptandı"] --> B{"Gen LoF-mekanizmalı mı?<br/>(constraint pLI/LOEUF + ClinGen gen-hastalık geçerliliği)"}
  B -->|"Hayır/şüpheli"| BX["PVS1 uygulama; mekanizmayı yeniden değerlendir"]
  B -->|"Evet"| C{"Varyant tipi + konum"}
  C -->|"Nonsense/frameshift"| N{"NMD bekleniyor mu?"}
  N -->|"Evet"| N1["Temiz LoF → PVS1 (güç tip/gene göre)"]
  N -->|"Hayır/son ekzon"| N2["Truncated protein → DN/GoF değerlendir (Bölüm 5); PVS1 ↓"]
  C -->|"Kanonik splice"| S["RNA ile doğrula (Bölüm 7); çerçeve sonucu?"]
  C -->|"Start-loss / tek-ekzon del"| SL["Ayrı karar dalı (Abou Tayoun 2018)"]
  N1 --> K{"Kalıtım modeli"}
  N2 --> K
  S --> K
  SL --> K
  K -->|"Dominant (haploinsuff)"| K1["Tek allel yeterli mi? (Bölüm 3)"]
  K -->|"Resesif"| K2["İkinci allel? trans fazı doğrula (ebeveyn testi)"]
  K1 --> Z["Doz analizi gerekli mi? (NF1/DMD → MLPA/array/WGS-CNV)"]
  K2 --> Z
  Z --> R["Rezidüel fonksiyon / genotip-fenotip → prognoz ve tedavi (ör. PKU)"]
```

---

## 10. Kaynaklar

> **Atıf / doğrulama notu:** Bu bölümün bibliyografik verileri PubMed üzerinden alınmış ve doğrulanmıştır; her kaynağın PMID **ve** DOI'si bu oturumda tek tek teyit edilmiştir. Metin içinde yazar-yıl, kaynakçada DOI-link kullanılmıştır.

1. **Richards S, Aziz N, Bale S, ve ark. (2015).** Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. *Genetics in Medicine* 17(5):405–424. **PMID: 25741868** · DOI: [10.1038/gim.2015.30](https://doi.org/10.1038/gim.2015.30) — *Guideline / PVS1 dahil kanıt çerçevesi.*
2. **Abou Tayoun AN, Pesaran T, DiStefano MT, ve ark. (2018).** Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. *Human Mutation* 39(11):1517–1524. **PMID: 30192042** · DOI: [10.1002/humu.23626](https://doi.org/10.1002/humu.23626) — *Guideline / PVS1 karar ağacı ve güç derecelendirmesi.*
3. **Khajavi M, Inoue K, Lupski JR (2006).** Nonsense-mediated mRNA decay modulates clinical outcome of genetic disease. *European Journal of Human Genetics* 14(10):1074–1081. **PMID: 16757948** · DOI: [10.1038/sj.ejhg.5201649](https://doi.org/10.1038/sj.ejhg.5201649) — *Mekanizma/review; NMD ve genotip-fenotip, NMD-escape toksisitesi.*
4. **Monaco AP, Bertelson CJ, Liechti-Gallati S, Moser H, Kunkel LM (1988).** An explanation for the phenotypic differences between patients bearing partial deletions of the DMD locus. *Genomics* 2(1):90–95. **PMID: 3384440** · DOI: [10.1016/0888-7543(88)90113-9](https://doi.org/10.1016/0888-7543(88)90113-9) — *Landmark mekanistik; okuma çerçevesi hipotezi (Duchenne vs Becker).*
5. **Sosnay PR, Siklosi KR, Van Goor F, ve ark. (2013).** Defining the disease liability of variants in the cystic fibrosis transmembrane conductance regulator gene. *Nature Genetics* 45(10):1160–1167. **PMID: 23974870** · DOI: [10.1038/ng.2745](https://doi.org/10.1038/ng.2745) — *Klinik örnek / allelik heterojenite, LoF varyantlarının kanıtla doğrulanması (CFTR).*
6. **Hillert A, Anikster Y, Belanger-Quintana A, ve ark. (2020).** The Genetic Landscape and Epidemiology of Phenylketonuria. *American Journal of Human Genetics* 107(2):234–250. **PMID: 32668217** · DOI: [10.1016/j.ajhg.2020.06.006](https://doi.org/10.1016/j.ajhg.2020.06.006) — *Klinik örnek / hipomorfik allel, rezidüel fonksiyon, genotip-fenotip (PAH).*
7. **Karczewski KJ, Francioli LC, Tiao G, ve ark. (2020).** The mutational constraint spectrum quantified from variation in 141,456 humans. *Nature* 581(7809):434–443. **PMID: 32461654** · DOI: [10.1038/s41586-020-2308-7](https://doi.org/10.1038/s41586-020-2308-7) — *Mekanizma/metodoloji; LoF intoleransı, LOEUF/pLI.*

> **İkincil/destekleyici kaynak notu:** GeneReviews/OMIM/ClinVar/gnomAD yalnız destekleyici bilgi olarak anılmıştır.

---

## ✅ Bölüm öz-denetim tablosu

**Tablo 2.6 — Bölüm 2 öz-denetim tablosu**

| Kriter | Durum | Not |
|--------|-------|-----|
| Mekanizma doğru anlatıldı mı? | ✅ | LoF yolları, NMD, çerçeve kuralı, rezidüel fonksiyon, missense-LoF |
| Klinik bağlantı kuruldu mu? | ✅ | NF1, DMD, CFTR, PKU ile dominant/resesif/hipomorf eksenleri |
| Varyant tipi ile mekanizma ilişkilendirildi mi? | ✅ | Tablo 3 + NMD/çerçeve/PVS1 karar ağaçları |
| Pediatrik örnek verildi mi? | ✅ | 4 pediatrik gen, kaynaklı |
| Test seçimi açıklandı mı? | ✅ | WES/WGS + MLPA/array + RNA-seq, doz analizi vurgusu |
| ACMG/ClinGen bağlantısı doğru mu? | ✅ | PVS1 + SVI güç derecelendirmesi (Abou Tayoun 2018) |
| Kaynaklar PMID/DOI ile verildi mi? | ✅ | 7 kaynak; PMID+DOI doğrulandı |
| Spekülatif iddialar işaretlendi mi? | ✅ | NMD "~50 nt" kuralı basitleştirme olarak işaretlendi |
| Kaynak uydurma riski var mı? | ✅ Yok | Tüm kaynaklar PubMed metadata ile karşılaştırıldı |
| Görsel/şema/algoritma desteği yeterli mi? | ✅ | 3 SVG (NMD, çerçeve, spektrum) + 3 Mermaid (dominant/resesif, PVS1, karar algoritması) |

---

### 🔎 Bölüm sonu kaynak doğrulama komutu (zorunlu)
> "Bu bölümdeki tüm kaynakların PMID/DOI bilgisini kontrol et. PMID veya DOI veremediğin kaynağı çıkar. Kaynağı olmayan iddiayı 'kaynak doğrulaması gerekli' olarak işaretle."
>
> **Bu bölüm için durum:** 7/7 kaynak PMID+DOI doğrulandı. NMD eşik kuralı (son ekzon-ekzon bağlantısı ~50 nt) öğretici basitleştirmedir; gen/transkripte göre istisnalar olabilir ve RNA ile doğrulama önerilir.
