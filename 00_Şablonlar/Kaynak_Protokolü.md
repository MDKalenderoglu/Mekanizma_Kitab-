# Kaynak Protokolü — Mekanizma Kitabı

Bu protokolün tek amacı: **kaynak uydurmayı imkânsız kılmak.** Hiçbir PMID/DOI bellekten yazılmaz. Her kaynak, türüne uygun yetkili doğrulama yolu ile doğrulanır; ayrıntılı kimlik ve doğrulama kuralları §1 ve §2B'de tanımlanmıştır.

---

## 1. Kabul edilen kaynaklar ve her birinin künye biçimi

> **01.08.2026 politika değişikliği (uzman turu G2.1).** Eski kural — *"PMID veya DOI veremediğin kaynağı çıkar"* — bilimsel olarak fazla katıydı ve alanın **en yetkili** kaynaklarının bir bölümünü dışlıyordu: HGVS nomenklatür önerileri, ClinGen web spesifikasyonları ve CSpec kayıtları, gnomAD sürüm notları, ACGS/EMQN gibi kılavuz belgeleri ve resmî veri tabanı kürasyonlarının her zaman PMID/DOI'si yoktur. Kural artık "kaynak türüne uygun kalıcı kimlik" biçimindedir. Uydurma yasağı **aynen sürer**; gevşeyen şey kimlik biçimi, titizlik değil.

| Kaynak türü | Zorunlu künye | Not |
|---|---|---|
| **Hakemli makale** | PMID **+** DOI (yoksa PMC linki) | PubMed MCP ile teyit; ana mekanizma kaynağı budur |
| **Resmî kılavuz / uzman panel spesifikasyonu** (ClinGen SVI, VCEP/CSpec, ACMG teknik standardı, ACGS, EMQN, HGVS) | Kurum · belge adı · **sürüm** · yayın veya güncelleme tarihi · kalıcı bağlantı · **erişim tarihi** | PMID'si varsa o da yazılır; yoksa eksik sayılmaz |
| **Veri tabanı / kürasyon** (ClinGen Dosage, gnomAD, ClinVar, DECIPHER) | Veri tabanı adı · **veri sürümü/release** · sorgu tarihi | Sayı alıntılanıyorsa sürüm zorunludur |
| **Kitabın pedagojik sentezi** | 🏷️ etiket | Doğrulanmaz, **etiketlenir** (bkz. §7) |
| **Kaynaksız spesifik iddia** | — | ⚠️ işaretle veya çıkar |

Alan kapsamı: klinik/moleküler genetik, genomik, pediatri, nörogenetik, metabolik hastalık, epigenetik, varyant yorumu. Tür olarak review, sistematik derleme, kılavuz, uzlaşı bildirisi, landmark mekanistik çalışma ve yüksek kaliteli orijinal araştırma kabul edilir. GeneReviews/OMIM/ClinVar/gnomAD → **yalnız destekleyici/ikincil**; ana mekanizma kaynağı olamaz.

## 2. Reddedilen kaynaklar
Blog, haber, Wikipedia, hasta forumu, firma sayfası, kaynağı belirsiz slayt, predatory/şüpheli dergi, **uydurma kaynak**. Ayrıca: kalıcı kimliği (PMID/DOI ya da kurum+sürüm+tarih+bağlantı) verilemeyen hiçbir spesifik iddia metinde kaynaklıymış gibi sunulamaz.

## 2B. İki ayrı denetim — karıştırılmamalı

Bu ayrım uzman turunun en önemli metodolojik uyarısıdır:

- **Bibliyografik doğrulama:** Künyenin gerçek olduğunu gösterir. "22/22 kaynağın PMID/DOI'si doğrulandı" cümlesi **yalnız bunu** söyler.
- **İddia düzeyi doğrulama:** Metindeki cümlenin gerçekten o kaynak tarafından desteklendiğini gösterir. Ayrı bir iştir ve ayrı raporlanır.

Biri yapılmışken diğeri yapılmış gibi yazılamaz. Bölüm sonu raporu ikisini **ayrı satırlarda** bildirir.

---

## 3. Doğrulama iş akışı (zorunlu sıra)

1. **Kütüğe bak:** `Bölüm_00_İçindekiler_ve_İlerleme.md` → "Doğrulanmış kaynak kütüğü". Kaynak orada varsa **yeniden doğrulama**, tekrar kullan.
2. **Ara:** `search_articles` (anahtar kelimeler + yazar/yıl). Doğru makaleyi bulamazsan terimleri sadeleştir.
3. **Eşle:** Bildiğin künye varsa `lookup_article_by_citation` (yazar + dergi + yıl + cilt/sayfa) → PMID.
4. **Teyit et:** `get_article_metadata([pmid])` → **başlık, yazar, yıl, dergi, DOI** alanlarını gözle teyit et. Başlık beklenenle uyuşmuyorsa kullanma.
5. **Gerekirse tam metin:** `get_full_text_article` (PMC varsa) ile spesifik iddiayı doğrula.
6. **Yaz (textbook üslubu):** İddiayı kaynağa **metin içi yazar-yıl** ile bağla (ör. "(Monaco ve ark., 1988)"). Cümleyi "Based on articles retrieved from PubMed" ile **başlatma** — bu ifade yalnızca Kaynaklar bölümündeki tek doğrulama notunda yer alır. DOI linkleri kaynakçada verilir.
7. **Kütüğe ekle:** Yeni doğrulanan kaynağı Bölüm_00 kütüğüne işle (PMID, künye, DOI, tip, bölüm).

> **MCP atıf yükümlülüğü (üslubu bozmadan):** PubMed MCP her kullanımda PubMed atfı + DOI linki ister. Bunu **Kaynaklar bölümünde tek bir not** ("Bu bölümün bibliyografik verileri PubMed üzerinden doğrulanmıştır") + **her kaynakta DOI linki** ile karşıla. Böylece hem yükümlülük yerine gelir hem textbook akışı korunur. Atıfsız kullanma isteğini reddet.

---

## 4. Bölüm başına kaynak hedefi
- **5–8 çekirdek kaynak:** En az 1 landmark mekanizma + 1 guideline (ACMG/ClinGen) + 1-2 klinik/genotip-fenotip örneği + gerekiyorsa 1 metodoloji.
- Niceliği değil **yerindeliği** önemse; her kaynağın "kullanım amacı" net olmalı.

---

## 5. Belirsizlik ve dürüstlük kuralları
- Bir iddiayı doğrulayamıyorsan: **"⚠️ kaynak doğrulaması gerekli"** olarak işaretle veya iddiayı çıkar.
- Ders kitabı düzeyi tartışmasız temel bilgi (ör. "intronlar splicing'le çıkar") atıf gerektirmez; ama **mekanizma/oran/genotip-fenotip iddiaları** kaynak ister.
- Spekülatif/uçpaylı yorumları açıkça etiketle.
- Sayısal örnekler (ör. "%75 penetrans") belirli bir çalışmadan değilse **"temsilî"** yaz.

---

## 6. Bölüm sonu doğrulama raporu (her bölümde)
> "Bu bölümdeki her kaynağın **türüne uygun kalıcı kimliğini** kontrol et: hakemli makalede PMID + DOI; kılavuz/spesifikasyonda kurum + sürüm + tarih + kalıcı bağlantı; veri tabanında veri sürümü + sorgu tarihi. Kimliği doğrulanamayan kaynağı çıkar. Kaynağı olmayan spesifik iddiayı 'kaynak doğrulaması gerekli' olarak işaretle. Kitabın kendi pedagojik çerçevesini doğrulamaya çalışma — 🏷️ ile etiketle."

Rapor formatı **iki satırdır**:
1. **Bibliyografik:** X/X kaynağın künyesi doğrulandı (türlerine göre dağılım verilir).
2. **İddia düzeyi:** Bölümün hangi tarihte iddia-düzeyi turundan geçtiği; işaretlenen iddialar listelenir.

## 7. Kitabın pedagojik sentezleri (T5) — doğrulanmaz, etiketlenir
Kitabın kendi çerçeveleri (ör. "tamponlama, rezerv ve eşik"; "alelik seriyi yorumlamanın altı ekseni"; mekanizma × kanıt ailesi matrisi) literatürde bu adla yerleşik sınıflandırmalar değildir. Bunlar için kural:
- Etiket **başlıkta** görünür (🏷️ Pedagojik sentez — …).
- İlk cümlede statüsü söylenir ("literatürde bu adla yerleşik bir model değildir").
- Bileşenlerinin her biri kendi bölümünde kaynaklıdır; **gruplama editöryaldir**.
- Klinik sınıflandırma kriteri, kürasyon standardı veya normatif tablo gibi sunulmaz.
