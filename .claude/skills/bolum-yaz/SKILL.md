---
name: bolum-yaz
description: Mekanizma Kitabı (genetik hastalık mekanizmaları textbook'u) için bir bölümü baştan yaz veya mevcut bölümü standarda yükselt. Kullanıcı "bölüm yaz", "Bölüm N'e geç", "şu bölümü genişlet/derinleştir" dediğinde veya bu projede yeni bölüm üretirken kullan. Textbook derinliği, T1–T5 iddia tiplemesiyle doğrulanmış kaynaklar, doğrulanmış SVG + Mermaid görseller ve standart 10-başlık formatını uygular.
---

# Skill: bolum-yaz

Bu skill, **Mekanizma Kitabı** projesinde bir bölümü textbook standardında üretmek için izlenecek adımları tanımlar.

**Bağlayıcı belgeler — önce bunları oku. Bu skill onların yerine geçmez, onları uygular:**

| Konu | Dosya |
|---|---|
| Proje kuralları, altın kurallar, 10-başlık formatı, test tablosu esneklik kuralı | `CLAUDE.md` |
| Ton, anlatı-önce kuralı, biçim ögeleri, atıf biçimi | `00_Şablonlar/Stil_Rehberi.md` |
| **İddia türleri T1–T5 ve her türün doğrulama otoritesi** | `00_Şablonlar/Dogrulama_Protokolu.md` |
| Kaynak türüne uygun kalıcı kimlik + doğrulama iş akışı | `00_Şablonlar/Kaynak_Protokolü.md` |
| **Görsel standardı — tek source-of-truth** | `00_Şablonlar/Görsel_Doktrini_v2.md` |
| Bölüm iskeleti | `00_Şablonlar/Bölüm_Şablonu.md` |
| Gösterim/yazım kuralları · §7B **eşitlenmemesi gereken kavram çiftleri** · işaret sözlüğü (🏷️ ⚠️ 🔬 🟦 🔴) | `kitap/07_Terminoloji_ve_Yazim_Kurallari.md` |
| İlerleme + kaynak/görsel kütüğü | `Bölüm_00_İçindekiler_ve_İlerleme.md` |
| Uygulanmış doğrulama kaydı ve bilinen hata kalıpları | `Dogrulama_Kutugu.md` |

## Ne zaman çalışır
- Yeni bölüm yazımı, mevcut bölümü derinleştirme/standarda yükseltme, görsel/algoritma ekleme.

## Adım adım iş akışı

### 1. Bağlamı yükle
`CLAUDE.md` + `Bölüm_00_İçindekiler_ve_İlerleme.md` (ilerleme + kaynak/görsel kütüğü) + yukarıdaki bağlayıcı belgeleri oku.

### 2. Bölümü planla (kısa)
- Öğrenme hedefleri (6–8, ölçülebilir).
- Bölümün "anahtar soruları" (kullanıcının orijinal brief'indeki sorular).
- Gerekli görseller (≥3 SVG) ve algoritmalar (≥2 Mermaid).
- Örnek genler/hastalıklar (tercihen pediatrik, somut).

### 3. Kaynakları ve iddiaları doğrula — **İKİ AYRI DENETİM**

> ⚠️ **Bibliyografik doğrulama ≠ iddia düzeyi doğrulama.** Bunlar iki farklı denetimdir ve biri diğerinin yerine geçmez. "X/X kaynağın künyesi doğrulandı" cümlesi, metindeki her iddianın o kaynaklarca desteklendiğini **göstermez** ve öyleymiş gibi yazılamaz (`Dogrulama_Protokolu.md` §0 · CLAUDE.md §2.5). Kütükte bulunmuş altı "atıf kapsamı hatası" — cümle doğru, kaynak var, künye kusursuz, ama o cümle o kaynakta yok — tam olarak bu ayrımın atlandığı yerde doğdu.

**3A. İddiaları önce türle** (`Dogrulama_Protokolu.md` §1 — *tür belirlenmeden doğrulama yapılmaz*):

| Tür | İçerik | Otorite / yöntem |
|---|---|---|
| **T1** | Normatif/kılavuz kuralı (kriter, eşik, güç düzeyi) | Yürürlükteki ClinGen/ACMG belgesi indirilir, **kural cümlesi** karşılaştırılır |
| **T2** | Spesifik çalışma bulgusu (sayı, oran, kohort, kat) | Kaynağın özeti; özette yoksa PMC **tam metni** — cümle düzeyinde |
| **T3** | Gen–varyant–hastalık–dozaj eşleşmesi | **Dosya indirilir, programatik eşleştirilir** (ClinGen gen **ve** bölge listesi, ClinVar, gnomAD, MITOMAP, HGNC) |
| **T4** | Mekanizma ders bilgisi | Atıf denetimi + **(a)/(b)/(c) üçe ayırma** + uzman değerlendirmesi |
| **T5** | Kitabın özgün pedagojik sentezi | **Doğrulanmaz — 🏷️ ile etiketlenir** |

**T4 üçe ayırma:** atıfsız her mekanistik önerme (a) gerçekten yerleşik ders bilgisi → kaynak gerekmez, kütükte öyle işaretlenir · (b) kaynaklanabilir → kaynak bulunur ve eklenir · (c) aslında çıkarım → **yumuşatılır veya çıkarılır.** Kaynaksız, kulağa doğru gelen cümle en riskli cümledir.

**3A-bis. Çekirdek kaynak seti:** bölüm başına **5–8 çekirdek kaynak** — landmark mekanizma + kılavuz + klinik örnek + (gerekirse) metodoloji (CLAUDE.md §6.1).

**3B. Kaynak künyesi — kaynak türüne uygun kalıcı kimlik** (`Kaynak_Protokolü.md` §1 · CLAUDE.md §2.4):

- **Hakemli makale:** PubMed MCP ile doğrulanmış **PMID + DOI** (`search_articles` → `lookup_article_by_citation` → `get_article_metadata`).
- **Kılavuz / uzman panel spesifikasyonu** (HGVS, ClinGen SVI, VCEP/CSpec, ACMG teknik standardı, ACGS, EMQN): **kurum + belge + sürüm + tarih + kalıcı bağlantı + erişim tarihi.**
- **Veri tabanı kaydı:** **veri sürümü + sorgu tarihi.**

> ⚠️ Eski "PMID/DOI veremediğin kaynağı çıkar" kuralı **terk edilmiştir** — alanın en yetkili PMID'siz kaynaklarını dışlıyordu. Esneyen şey **kimlik biçimidir, titizlik değildir.** PMID'i olmayan bir ClinGen belgesi meşru bir T1 otoritesidir; kimliği sürüm ve tarihle verilir.

**3C. Kanıt toplama kuralı (ihlal edilemez):** ⛔ **Doğrulama, veriyi bir modele okutarak yapılamaz.** `WebFetch` uydurabilir — kanıtlandı: ClinGen listesinde bulunmayan bir gen için "PAX6: HI = 3" yanıtı üretti. Veri tabanı kanıtı **`curl` ile indirilir + Python ile tam eşleştirilir**; WebFetch/WebSearch yalnız **keşif** içindir, kanıt değildir. Kitap geneli künye taraması için `00_Şablonlar/kunye_denetle.py`.

**3D. Kütük:** önce `Bölüm_00` kaynak kütüğüne bak — daha önce doğrulanmış kaynağı **yeniden doğrulama**, tekrar kullan. Aynı kaynak birden çok bölümde geçerse künye **birebir aynı** olur. Yeni doğrulananları kütüğe ekle. **Asla bellekten PMID/DOI yazma.**

**3E. Tuzaklar:** ClinGen dozaj skorları **gen** ve **bölge** olmak üzere iki ayrı listededir; tekrarlayan CNV bölgeleri ve imprintli lokuslarda **gen düzeyi skor yanıltıcıdır.** Ayrıca **bir genin listede olmaması, doza duyarlı olmadığı anlamına gelmez.**

### 4. Görselleri üret — **ve doğrula**

Görsel standardının bağlayıcı tanımı `00_Şablonlar/Görsel_Doktrini_v2.md`'dir (palet, tipografi, çakışma yasağı, yapısal iskelet, `markerUnits` tuzağı, teknik kurallar). SVG'leri `assets/sekil_NN_<ad>.svg` olarak yaz; Mermaid diyagramlarını metne göm (`Stil_Rehberi.md` §3.3).

**Her yeni/değişmiş SVG için üç adım ZORUNLU — atlanamaz:**

1. **XML geçerliliği**
   ```bash
   xmllint --noout assets/sekil_NN_*.svg
   ```
2. **En-boy oranını koruyan render — tek standart**
   ```bash
   node .claude/skills/figure-review/render_svg.mjs assets/sekil_NN_*.svg <çıktı.png> 1600
   ```
   İlk kullanımda bir kez `cd .claude/skills/figure-review && npm ci`. Çıktıyı **projeye değil**, oturum scratchpad'ine yaz. Render çıktısının en-boy oranı kaynak `viewBox` oranıyla eşleşmeli.
3. **Gözle bak** — PNG'yi Read ile aç. Çakışma / taşma / metnin şekil arkasında kaybolması varsa düzelt, yeniden render et, **tekrar bak**.

> ⛔ **`qlmanage` kullanılmaz** — gerekçe ve tek render standardı: `Görsel_Doktrini_v2.md` → "RENDER + GÖZLE DENETİM ZORUNLU". **`xmllint` görsel çakışmayı göstermez**; adımlar birbirinin yerine geçmez.

### 5. Bölümü yaz

`Bölüm_Şablonu.md` iskeletini kullanarak `Bölüm_NN_<Konu>.md` dosyasını oluştur:

- Çekirdek tez + **📘 Okuma katmanları** (① Temel · ② Klinik · ③ İleri düzey — zorunlu) + öğrenme hedefleri + render notu.
- 10 standart başlık (eksiksiz), deep-dive (🔬) / klinikte dikkat (🟦) / sık yapılan hata (🔴) kutuları.
- **Test tablosu — çekirdek, kota değil** (CLAUDE.md §4 esneklik kuralı, 04.08.2026 kullanıcı kararı): çekirdek satırlar WES · Short-read WGS · Long-read WGS · Array-CGH/SNP array · MLPA · RNA-seq · Methylation array · Karyotip. Bölüm iki yönde sapabilir ve **sapma gerekçesi metinde görünür olmalıdır:** (a) mekanizmayla gerçekten ilgisiz satır **çıkarılabilir**; (b) bölüme özgü araçlar **eklenebilir** ya da tablo o alanın araç setine göre **yeniden kurulabilir** (onaylı örnek: Bölüm 8'in sitogenetik tablosu — KA · TCA · QF-PCR · FISH · CMA/array-CGH · SNP-array · MLPA · Short-read WGS · OGM). Değişmeyen iki kural: **her satır bir soruyu ve bir sınırlılığı birlikte verir**, ve **araç adları kitap genelinde tek biçimdir.**
- Karar algoritması (Mermaid).
- Kaynaklar (kaynak türüne uygun kalıcı kimlikle — §3B), öz-denetim tablosu, kaynak doğrulama durumu **iki satır hâlinde**: (a) bibliyografik, (b) iddia düzeyi.

**Yazarken zorunlu işaretleme:**
- **🏷️ — T5:** kitabın özgün pedagojik çerçevesi yerleşik sınıflandırma gibi sunulamaz. Her birine şu anlamda not düşülür: *"Bu çerçeve kitabın pedagojik sentezidir; literatürde bu adla yerleşik bir sınıflandırma değildir. Bileşenlerin her biri kaynaklıdır, gruplama editöryaldir."*
- **⚠️ — doğrulanamayan / tartışmalı / sınırlı iddia.** Doğrulanamayan iddia ya ⚠️ ile işaretlenir ya çıkarılır. Spekülasyon açıkça etiketlenir.
- **§7B eşitleme yasakları:** `kitap/07_Terminoloji_ve_Yazim_Kurallari.md` §7B'deki kavram çiftleri birbirinin otomatik eşdeğeri **değildir**; bu eşitlemeler metinde kurulamaz (ör. kesici varyant = gerçek null · düşük LOEUF = kanıtlanmış haploinsufficiency · kanonik splice = PVS1_VeryStrong · kodlamayan = düzenleyici · VAF = mutant hücre oranı). Bölümü bitirmeden bu listeye karşı oku.
- **Kesinlik tonu kanıtın üstüne çıkmaz.** Kaynak "işaret ediyor" derken metin "göstermiştir" demez; "ikinci en yüksek" → "en yüksek" olmaz. Kütükteki üç hata kalıbından biri budur.

### 6. İndeksi güncelle
`Bölüm_00`'da bölüm durumunu ✅ yap; görsel ve kaynak kütüklerini güncelle. Doğrulama turu yapıldıysa `Dogrulama_Kutugu.md`'ye yaz.

### 7. Raporla
Kullanıcıya kısa özet + dosya linkleri + **iki ayrı doğrulama sonucu** (bibliyografik X/X · iddia düzeyi: hangi tür kaç iddia, işaretlenen/çıkarılan) + bir sonraki bölüm önerisi. Kullanıcı "devam"/"hepsini yaz" demedikçe bir sonraki bölüm için onay bekle. **Stage/commit/push için ayrı onay iste** (CLAUDE.md §1C).

## Kalite çıtası (tamamlanmadan kontrol et)

**İçerik**
- [ ] Textbook derinliği (özet değil), **anlatı-önce** (madde listesi kavramı açıklamaz), deep-dive kutuları var.
- [ ] mekanizma → varyant tipi → hücresel sonuç → klinik fenotip → tanısal test → varyant yorumu zinciri kurulmuş.
- [ ] 10 başlık eksiksiz + 📘 Okuma katmanları + öz-denetim tablosu.
- [ ] En az 2–3 somut, kaynaklı pediatrik örnek.
- [ ] Test tablosu çekirdeği karşılanmış; sapma varsa **gerekçesi metinde görünür**; araç adları tek biçimde.

**Doğrulama — iki ayrı satır**
- [ ] **Bibliyografik:** her künye kaynak türüne uygun kalıcı kimliğiyle doğrulandı (makale PMID+DOI · kılavuz belge+sürüm+tarih+erişim · veri tabanı sürüm+sorgu tarihi). Bellekten yazılmış kimlik yok.
- [ ] **İddia düzeyi:** iddialar T1–T5 türlenmiş ve her biri **kendi otoritesiyle** karşılaştırıldı. T3 iddiaları programatik olarak eşleştirildi (WebFetch ile değil). T4 önermeleri (a)/(b)/(c) ayrımına sokuldu; (c) yumuşatıldı/çıkarıldı.
- [ ] 🏷️ (T5) ve ⚠️ (doğrulanamayan/tartışmalı) işaretleri yerinde; T5 hiçbir yerde yerleşik sınıflandırma gibi sunulmuyor.
- [ ] §7B eşitleme yasaklarına karşı okundu; kesinlik tonu kanıt sınıfını aşmıyor.

**Görsel**
- [ ] ≥3 SVG + ≥2 Mermaid.
- [ ] Her yeni/değişmiş SVG: `xmllint` ✅ → oranı koruyan render ✅ → **gözle bakıldı** ✅ (çakışma/taşma yok).
- [ ] Palet, tipografi, iskelet ve teknik kurallar `Görsel_Doktrini_v2.md`'ye uygun.

**Kayıt**
- [ ] `Bölüm_00` ve (gerekiyorsa) `Dogrulama_Kutugu.md` güncellendi.
