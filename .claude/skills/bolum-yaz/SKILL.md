---
name: bolum-yaz
description: Mekanizma Kitabı (genetik hastalık mekanizmaları textbook'u) için bir bölümü baştan yaz veya mevcut bölümü standarda yükselt. Kullanıcı "bölüm yaz", "Bölüm N'e geç", "şu bölümü genişlet/derinleştir" dediğinde veya bu projede yeni bölüm üretirken kullan. Textbook derinliği, PubMed ile doğrulanmış kaynaklar, SVG + Mermaid görseller ve standart 10-başlık formatını uygular.
---

# Skill: bolum-yaz

Bu skill, **Mekanizma Kitabı** projesinde bir bölümü textbook standardında üretmek için izlenecek adımları tanımlar. Proje kuralları `CLAUDE.md`, biçim `00_Şablonlar/Stil_Rehberi.md`, kaynak `00_Şablonlar/Kaynak_Protokolü.md`, iskelet `00_Şablonlar/Bölüm_Şablonu.md` dosyalarındadır. **Önce bunları dikkate al.**

## Ne zaman çalışır
- Yeni bölüm yazımı, mevcut bölümü derinleştirme/standarda yükseltme, görsel/algoritma ekleme.

## Adım adım iş akışı

1. **Bağlamı yükle.** `CLAUDE.md` + `Bölüm_00_İçindekiler_ve_İlerleme.md` (ilerleme + kaynak/görsel kütüğü) + üç şablon dosyasını oku.

2. **Bölümü planla (kısa).** Belirle:
   - Öğrenme hedefleri (6–8, ölçülebilir).
   - Bölümün "anahtar soruları" (kullanıcının orijinal brief'indeki sorular).
   - Gerekli görseller (≥3 SVG) ve algoritmalar (≥2 Mermaid).
   - Örnek genler/hastalıklar (tercihen pediatrik, somut).

3. **Kaynakları doğrula** (`Kaynak_Protokolü.md`):
   - Önce Bölüm_00 kaynak kütüğüne bak (varsa yeniden doğrulama).
   - Eksikleri PubMed MCP ile doğrula: `search_articles` → `lookup_article_by_citation` → `get_article_metadata` (PMID + DOI + başlık teyidi).
   - 5–8 çekirdek kaynak: landmark mekanizma + guideline + klinik örnek + (gerekirse) metodoloji.
   - Asla bellekten PMID/DOI yazma.

4. **Görselleri üret.** Gerekli SVG'leri `assets/sekil_NN_<ad>.svg` olarak yaz (Stil_Rehberi renk dili + beyaz zemin + Türkçe etiket + başlık/alt-not; CSS değişkeni yok). Mermaid diyagramlarını metne göm.

5. **Bölümü yaz.** `Bölüm_Şablonu.md` iskeletini kullanarak `Bölüm_NN_<Konu>.md` dosyasını oluştur:
   - Çekirdek tez + öğrenme hedefleri + render notu.
   - 10 standart başlık (eksiksiz), deep-dive/klinikte-dikkat/sık-hata kutuları.
   - Standart test tablosu (8 satır), karar algoritması (Mermaid).
   - Kaynaklar (PMID + DOI-link + kullanım amacı), öz-denetim tablosu, kaynak doğrulama durumu.

6. **İndeksi güncelle.** `Bölüm_00`'da bölüm durumunu ✅ yap; görsel ve kaynak kütüklerini güncelle.

7. **Raporla.** Kullanıcıya kısa özet + dosya linkleri + kaynak doğrulama sonucu (X/X) + bir sonraki bölüm önerisi. Kullanıcı "devam"/"hepsini yaz" demedikçe bir sonraki bölüm için onay bekle.

## Kalite çıtası (tamamlanmadan kontrol et)
- [ ] Textbook derinliği (özet değil), deep-dive kutuları var.
- [ ] ≥3 SVG + ≥2 Mermaid.
- [ ] 10 başlık eksiksiz + öz-denetim tablosu.
- [ ] Tüm kaynaklar PubMed ile doğrulanmış (PMID+DOI); spekülasyon işaretli.
- [ ] mekanizma→varyant→hücre→fenotip→test→yorum zinciri kurulmuş.
- [ ] Bölüm_00 güncellendi.
