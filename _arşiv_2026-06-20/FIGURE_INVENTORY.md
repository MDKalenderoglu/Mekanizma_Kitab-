# FIGURE INVENTORY — Genetik Hastalık Mekanizmaları

**Tarih:** 2026-06-20
**Amaç:** Görsel revizyon (VISUAL_REVISION_v2) öncesi tüm figürlerin envanteri, önerilen bölüm-bazlı yeni numaralandırma ve revizyon durumu.

> **Mimari not:** HTML dosyası `build_book.py` tarafından `.md` + `assets/*.svg` + CSS'den **otomatik üretilir**. Bu nedenle figürlerin "asıl" kaynağı `assets/`'taki SVG dosyaları ve `.md` içine gömülü Mermaid bloklarıdır. Revizyon kaynağa uygulanmalı, HTML yeniden üretilmelidir (bkz. mimari karar — kullanıcı onayı bekleniyor).

---

## 1. SVG figürleri (hâlen referanslı — 17 adet)

Numaralandırma önerisi: **bölüm-bazlı, belge sırasına göre** (mevcut düz 1–17 numaralandırmasında bazı şekiller belge içinde sıra dışı; ör. B1'de Şekil 3 fiziksel olarak 5'ten sonra, B4'te Şekil 15 16'dan sonra). Yeni numaralar **görünüm sırasına** göre verilmiştir → atlama/karışıklık giderilir.

| Eski figür no | Yeni figür no | Başlık | Dosya | Durum | Yapılan / planlanan değişiklik | Not |
|---|---|---|---|---|---|---|
| Şekil 1 | Şekil 1.1 | Kromozom ve kromatin hiyerarşisi | `sekil_01_kromozom_kromatin_hiyerarsisi.svg` | unchanged | redrawn (planlı): ökromatin/heterokromatin inset, akış netleştir, SVG-içi başlık kaldır | B1 §giriş |
| Şekil 2 | Şekil 1.2 | Gen anatomisi: DNA→transkript→protein | `sekil_02_gen_anatomisi.svg` | unchanged | redrawn (planlı): DNA/pre-mRNA/mature mRNA/protein ayrı panel, 5′ donor–branch–3′ acceptor, domain haritası | B1 |
| Şekil 4 | Şekil 1.3 | Temel kalıtım kalıpları (pedigri) | `sekil_04_kalitim_kaliplari_pedigri.svg` | unchanged | restyled (planlı): standart pedigri simgeleri, ferah düzen, sade legend | B1 — belge sırası 3. |
| Şekil 5 | Şekil 1.4 | Allelik vs lokus heterojenitesi | `sekil_05_allelik_vs_lokus_heterojenite.svg` | unchanged | redrawn (planlı): iki panel + alt klinik sonuç tablosu (tüm gen vs panel/WES) | B1 — belge sırası 4. |
| Şekil 3 | Şekil 1.5 | Penetrans vs ekspresivite | `sekil_03_penetrans_ekspresivite.svg` | unchanged | restyled (planlı): semantik renk, SVG-içi başlık kaldır | B1 — belge sırası 5. (eski no sıra dışıydı) |
| Şekil 6 | Şekil 1.6 | Yaşa bağlı penetrans | `sekil_06_yasa_bagli_penetrans.svg` | unchanged | restyled (planlı) | B1 |
| Şekil 7 | Şekil 2.1 | NMD kararı: PTC nerede? | `sekil_07_nmd_karar.svg` | **redrawn (v2 — UYGULANDI 2026-06-20)** | 50–55 nt kuralı, NMD var/yok → null vs truncated → PVS1 gücü; bilimsel teyit ✓ | B2 — canlıya uygulandı, HTML yeniden derlendi |
| Şekil 8 | Şekil 2.2 | Okuma çerçevesi kuralı (DMD) | `sekil_08_okuma_cercevesi_dmd.svg` | unchanged | redrawn (planlı): in/out-of-frame → BMD/DMD, distrofin domain haritası (ABD/rod/CR/C-term) | B2 |
| Şekil 9 | Şekil 2.3 | LoF allelik spektrumu (rezidüel fonksiyon) | `sekil_09_lof_spektrum.svg` | unchanged | redrawn (planlı): x=rezidüel fonksiyon, y=şiddet; null/severe/mild hypomorphic/near-normal; varyant tipleri yerleştir | B2 |
| Şekil 10 | Şekil 3.1 | Doz–yanıt ve eşik (haploinsufficiency) | `sekil_10_doz_yanit_esigi.svg` | unchanged | redrawn (planlı): %100/%50/eşik bandı, taşıyıcılık inset | B3 |
| Şekil 11 | Şekil 3.2 | TF neden doza duyarlıdır | `sekil_11_tf_doz_duyarliligi.svg` | unchanged | restyled (planlı) | B3 |
| Şekil 12 | Şekil 3.3 | Farklı varyant → "tek allel sustu" | `sekil_12_varyant_delesyon_esdegerligi.svg` | unchanged | restyled (planlı) | B3 |
| Şekil 13 | Şekil 3.4 | Dozaj duyarlılığı spektrumu + metrikler | `sekil_13_dozaj_duyarlilik_spektrumu.svg` | unchanged | restyled (planlı) | B3 |
| Şekil 14 | Şekil 4.1 | İşlev kazanımının dört yolu | `sekil_14_gof_mekanizma_turleri.svg` | restyled (kısmen, v1) | redrawn (planlı): 4 panel ortak şablon (normal/varyant/hücresel/klinik), PVS1-uygulanmaz mesajı | B4 |
| Şekil 16 | Şekil 4.2 | Konstitütif aktivasyon (reseptör) | `sekil_16_konstitutif_aktivasyon_reseptor.svg` | **redrawn (v2 — UYGULANDI 2026-06-20)** | yeni standartla yeniden çizildi; canlıya uygulandı | B4 — belge sırası 2. |
| Şekil 15 | Şekil 4.3 | LoF vs GoF zıt yönde hastalık | `sekil_15_doz_yanit_gof_vs_lof.svg` | restyled (v1) | semantik palet uyumu (planlı) | B4 — belge sırası 3. |
| Şekil 17 | Şekil 4.4 | Aynı gen, iki yön (RET, SCN2A) | `sekil_17_ayni_gen_gof_lof.svg` | **redrawn (v2 — UYGULANDI 2026-06-20)** | yeni standartla yeniden çizildi; canlıya uygulandı | B4 — belge sırası 4. |

---

## 2. Mermaid diyagramları (12 adet — `.md` içine gömülü)

| Bölüm | Konu (yaklaşık) | Durum | Plan |
|---|---|---|---|
| B1 | (3 diyagram — kalıtım/kavram akışları) | unchanged | converted to SVG (planlı) veya CSS profesyonelleştirme |
| B2 | NMD / PVS1 / LoF karar ağaçları | unchanged | **converted to SVG (öncelikli)** |
| B3 | Dominant/resesif ayrım · CNV puanlama · karar algoritması | unchanged | converted to SVG (planlı) |
| B4 | GoF/LoF ayrımı · ACMG GoF yorum · karar algoritması | unchanged | converted to SVG (planlı) |

> Mermaid blokları her bölümde 3 adet (toplam 12). Tam başlık eşlemesi revizyon sırasında bu tabloya işlenecek.

---

## 3. Yeni eklenecek "wow" figürleri (planlı — newly added)

| Geçici no | Başlık | İçerik | Yerleşim |
|---|---|---|---|
| Yeni F1 | Varyanttan fenotipe nedensellik zinciri | DNA→RNA→protein→yolak→doku→fenotip→yorum→tedavi | Kitabın başı (manifesto) |
| Yeni F2 | Genetik hastalık mekanizmaları atlası | LoF / GoF / Dozaj-regülatör / Repeat-epigenetik-mito tek sayfa harita | Kitabın başı veya B1 sonu |
| Yeni F3 | ACMG mekanizma entegrasyonu | Varyant tipi→mekanizma→gen-hastalık geçerliliği→ACMG kriteri→güç→sınıf | İlgili bölüm (B16 ileride) |
| Yeni F4 | Varyant yorumlamada mekanizma tuzakları | 6 yaygın tuzak (nonsense, missense, sinonim, aile öyküsü, pLI/LOEUF, NMD yok) | Kapanış/özet |

---

## 4. Yetim (orphan) SVG dosyaları — referanssız, yedekte korunacak

Aşağıdaki dosyalar `assets/`'te var ama hiçbir `.md` tarafından referanslanmıyor (B4'ün erken taslakları, sonradan farklı isimle yeniden çizilmiş). **Silinmeyecek**, yedekte duruyor; v2 derlemesine dahil edilmeyecek.

| Dosya | Olası amaç | Durum |
|---|---|---|
| `sekil_14_gof_mekanizma_tipleri.svg` | B4 Şekil 14 erken taslak | orphan (referanssız) |
| `sekil_15_fgfr3_konstitutif.svg` | B4 erken konstitütif aktivasyon taslağı | orphan |
| `sekil_16_aktivite_ekseni_allelik_seri.svg` | B4 erken aktivite ekseni taslağı | orphan |
| `sekil_17_gof_varyant_imzasi.svg` | B4 erken GoF varyant imzası taslağı | orphan |

---

## Durum kodları
`unchanged` · `restyled` · `redrawn` · `converted from Mermaid` · `newly added` · `needs scientific review`
