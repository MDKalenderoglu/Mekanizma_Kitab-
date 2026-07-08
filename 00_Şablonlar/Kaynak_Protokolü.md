# Kaynak Protokolü — Mekanizma Kitabı

Bu protokolün tek amacı: **kaynak uydurmayı imkânsız kılmak.** Hiçbir PMID/DOI bellekten yazılmaz; her biri PubMed MCP ile doğrulanır.

---

## 1. Kabul edilen kaynaklar
1. PubMed indeksli, hakemli dergi makaleleri.
2. Klinik/moleküler genetik, genomik, pediatri, nörogenetik, metabolik hastalık, epigenetik, varyant yorumu alanları.
3. Review, systematic review, guideline, consensus statement, landmark mekanistik veya yüksek kaliteli orijinal araştırma.
4. Varyant yorumu için ACMG/AMP, ClinGen SVI, ClinGen Dosage, VCEP/CSpec — **amacı açıkça etiketlenerek**.
5. GeneReviews/OMIM/ClinVar/gnomAD → **yalnız destekleyici/ikincil**; ana mekanizma kaynağı olamaz.

## 2. Reddedilen kaynaklar
Blog, haber, Wikipedia, hasta forumu, firma sayfası, kaynağı belirsiz slayt, DOI/PMID verilemeyen iddia, predatory/şüpheli dergi, **uydurma kaynak**.

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
> "Bu bölümdeki tüm kaynakların PMID/DOI bilgisini kontrol et. PMID veya DOI veremediğin kaynağı çıkar. Kaynağı olmayan iddiayı 'kaynak doğrulaması gerekli' olarak işaretle."

Rapor formatı: **X/X kaynak PMID+DOI doğrulandı.** İşaretlenen iddia varsa listele.
