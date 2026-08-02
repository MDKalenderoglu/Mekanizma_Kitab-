# Genetik Hastalık Mekanizmaları — Mekanizmadan Varyant Yorumuna

Türkçe, akademik bir ders kitabı projesidir. Genetik hastalıkları bir gen veya
sendrom kataloğu olarak değil, aşağıdaki nedensellik zinciri üzerinden öğretir:

> **mekanizma → varyant tipi → hücresel sonuç → klinik fenotip → tanısal test → varyant yorumu (ACMG/ClinGen)**

Kitap; tıbbi genetik ve çocuk genetiği hekimleri, klinik genomik/varyant yorumlama
uzmanları, tıbbi biyoloji uzmanları ve moleküler tanı laboratuvarı ekipleri için
hazırlanmaktadır. Pediatri hekimleri, moleküler biyoloji ve genetik alanında eğitim
alanlar, genetik danışmanlık ekipleri ve ileri düzey tıp öğrencileri ikincil hedef
kitleyi oluşturur.

---

## Güncel durum — 2 Ağustos 2026

- Mevcut kitap gövdesindeki **17 bölümün tamamı yazılmış**, kaynaklandırılmış ve
  bütüncül editöryal/uzman değerlendirme turlarından geçmiştir.
- Güncel derleme **64 SVG şekil**, **49 Mermaid algoritması** ve **153 benzersiz
  PMID** içerir.
- Güvenli başlangıç commit'i: `599a12e` (`Editöryal tur 2: bulgu formu eklendi`).
- Yerel güvenlik etiketi: `pre-editorial-round-2`.
- Editöryal karar kaydı, düşük riskli teknik temizlik ve doğrudan nesne
  bağlantıları + terminoloji/HGVS denetimi tamamlanmıştır. Proje artık **ayrı
  bilimsel/yapısal revizyon paketleri, bağımsız değerlendirme ve yayın kapanışı**
  aşamasındadır.
- Teknik temizlik sonrası doğrulanan envanter: **17 bölüm · 64 şekil · 49 algoritma
  · 73 tablo · 153 benzersiz PMID**. Derleme, eksik SVG veya geçersiz/mükerrer tablo
  numarasında hata vererek durur.

Güncel durum ve yol haritası için önce
[`Bölüm_00_İçindekiler_ve_İlerleme.md`](Bölüm_00_İçindekiler_ve_İlerleme.md),
sonra [`Editor_Degerlendirme_Formu_Tur2.md`](Editor_Degerlendirme_Formu_Tur2.md)
okunmalıdır.

---

## Onaylanan yayın hedefi

2 Ağustos 2026 tarihli editöryal karar görüşmesinde aşağıdaki hedefler onaylandı;
bu maddelerin dosya/bölüm düzeyindeki uygulaması henüz ayrı paketler hâlinde
yapılacaktır:

1. Önce **HTML + PDF değerlendirme sürümü**, bağımsız uzman incelemelerinden sonra
   dijital ve baskıya hazır nihai sürüm üretilecek.
2. Mevcut Bölüm 15 (alelik seri), mevcut Bölüm 14'ten (digenik/oligogenik mimari)
   önce gelecek.
3. **Kalıtsal kanser yatkınlığı ve ikinci vuruş** bağımsız Bölüm 16 olarak
   hazırlanacak; mevcut yorum ve klinik sentez bölümleri 17 ve 18'e kayacak.
4. Okuyucuya yönelik öz değerlendirme soruları bölüm sonlarından ayrı olarak
   kitabın sonunda, bölüm bazında gruplanmış bir kısımda toplanacak; bölüm
   sonlarında bu kısma bağlantı verilecek.
5. Ayrıntılı üretim ve doğrulama günlükleri proje içinde korunacak, yayımlanan
   kitapta yalnız kısa ve okuyucuya yönelik yöntem açıklaması bulunacak.
6. Türkiye'ye özgü klinik uygulama eki mevcut yayın kapsamına alınmayacak; gelecekte
   hazırlanması taahhüt edilmeyecek.

---

## Araçlar arası devamlılık

Proje Codex veya Claude ile sürdürülebilir. Kararlar yalnız sohbet bağlamında
bırakılmaz; kalıcı kayıt sırası şöyledir:

| Kayıt | İşlev |
|---|---|
| `README.md` | Projenin kısa güncel durumu ve başlangıç noktası |
| `CLAUDE.md` | Bağlayıcı çalışma, bilimsel doğrulama ve devamlılık kuralları |
| `Bölüm_00_İçindekiler_ve_İlerleme.md` | Canlı bölüm/görsel/kaynak envanteri ve yol haritası |
| `Editor_Degerlendirme_Formu_Tur2.md` | Editöryal kararlar ve uygulanma durumu |
| `Dogrulama_Kutugu.md` | İddia ve kaynak doğrulama geçmişi |
| `Terminoloji_Kaynak_Denetimi.md` | Türkçe terim kararları, önce/sonra tablosu ve kaynakları |
| Git geçmişi | Her değişikliğin ne, neden ve nasıl yapıldığı |

Her yeni oturumda bu belgeler ve `git status` okunmalıdır. Yapılmamış bir karar,
belgelerde **“onaylandı — uygulanmadı”** olarak belirtilir; tamamlanmış gibi
sunulmaz.

---

## Dosya haritası

| Yol | İşlev |
|---|---|
| `Bölüm_01_*.md` – `Bölüm_17_*.md` | Mevcut bilimsel bölüm kaynakları |
| `kitap/` | Künye, ön/arka madde, ekler, sözlük ve dizinler |
| `assets/` | Aktif SVG görseller |
| `00_Şablonlar/` | Bölüm, stil, görsel, kaynak ve doğrulama protokolleri |
| `.claude/skills/bolum-yaz/SKILL.md` | Bölüm yazım iş akışı |
| `build_book.py` | Markdown, SVG ve Mermaid içeriklerinden tek HTML üretir |
| `build_assets/mermaid.min.js` | Çevrimdışı Mermaid çalışma zamanı |
| `Genetik_Hastalık_Mekanizmaları.html` | Güncel üretilmiş kitap |
| `_metin/` | Yerel doğrulama için kaynak kitap metin çıkarımları; yayıma girmez |
| `_arşiv_2026-06-20/` | Canlı derlemeye girmeyen tarihsel yedek |

---

## Derleme

Kaynak Markdown dosyaları asıldır. Güncel HTML kitap:

```bash
python3 build_book.py
```

komutuyla üretilir. HTML'deki şekil, algoritma ve tablo listeleri doğrudan ilgili
nesneye gider. Tarayıcıdan yazdırma değerlendirme PDF'i üretir; nesne listelerindeki
sabit sayfa numaraları ancak CSS hedef sayacı destekleyen bir sayfalama motoruyla
nihai PDF üretilirken hesaplanır ve görsel olarak doğrulanır. Nihai PDF/baskı kalite
kontrolü, bilimsel ve editöryal revizyonlardan sonra yapılacaktır.

---

## Çalışma ve Git protokolü

1. Çalışmaya başlamadan önce `git status`, aktif dal ve son commit doğrulanır.
2. Değişiklikler küçük, tek amaçlı paketlere ayrılır.
3. Kullanıcı onayı olmadan kapsam genişletilmez.
4. Stage, commit ve push birbirinden ayrı yetkilendirilir.
5. Commit açıklaması **ne değişti, neden değişti ve nasıl doğrulandı** sorularını
   yanıtlar.
6. İlgili durum belgesi aynı paket içinde güncellenir; kararlar yalnız sohbet
   geçmişine bırakılmaz.
7. Aynı çalışma kopyasında Codex ve Claude eş zamanlı değişiklik yapmaz; devralan
   araç önce Git durumunu ve yukarıdaki kalıcı kayıtları okur.

Tamamlanan sıra: **karar kaydı → düşük riskli teknik temizlik → doğrudan nesne
bağlantıları ve terminoloji/HGVS denetimi**. Sonraki uygulama sırası: **ayrı onaylı
bilimsel/yapısal paketler → bağımsız uzman incelemesi → yayın kapanışı**.
