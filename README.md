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

## Güncel durum — 4 Ağustos 2026

- Mevcut kitap gövdesindeki **18 bölümün tamamı yazılmış**, kaynaklandırılmış ve
  iç/programatik editöryal denetimden geçmiştir. Bağımsız insan uzman incelemesi
  yayım ön koşulu olarak beklemektedir.
- Güncel derleme **68 SVG şekil**, **52 Mermaid algoritması** ve **194 benzersiz
  PMID** içerir.
- Son commit: `221a509`. Bölüm 16 paketi, öz değerlendirme ayrımı ve editöryal tutarlılık
  paketi commitlenmiştir; çalışma kopyasında bekleyen değişiklik varsa `git status`
  ile doğrulanır.
- Yerel güvenlik etiketi: `pre-editorial-round-2`.
- Editöryal karar kaydı, düşük riskli teknik temizlik ve doğrudan nesne
  bağlantıları + terminoloji/HGVS denetimi tamamlanmıştır. Proje artık **ayrı
  bilimsel/yapısal revizyon paketleri, bağımsız değerlendirme ve yayın kapanışı**
  aşamasındadır.
- Güncel doğrulanan yayın envanteri: **18 bölüm · 68 şekil · 52 algoritma
  · 65 tablo · 194 benzersiz PMID · 185 doğrudan nesne hedefi**. Kaynak
  dosyalardaki 18 iç öz-denetim tablosu yayın envanterine girmez. Derleme;
  eksik SVG/nesne hedefinde, numaralandırma hatasında, iç kalite günlüğü yayına
  sızarsa veya kapalı öz değerlendirme içeriği ana sürüme girerse hata vererek durur.
- **Bölüm 14–15 sıra değişimi tamamlandı:** Aynı gen → farklı hastalık (alelik seri)
  artık Bölüm 14; digenik/oligogenik/değiştirici mimari artık Bölüm 15'tir. Dosya,
  nesne, çapraz gönderme, kaynak kütüğü ve dizin numaraları yeni sırayla eşitlendi.
- **Bölüm 16 tamamlandı:** Kalıtsal kanser yatkınlığı ve ikinci vuruş bağımsız
  bölüm olarak eklendi; ACMG/ClinGen sentezi Bölüm 17'ye, klinik senaryolar Bölüm
  18'e kaydırıldı.
- **Öz değerlendirme materyali ayrı tutuluyor:** 18 bölüm için 54 soru ve 54
  yanıt yaklaşımı proje içinde hazırdır; ana kitapta ve bölüm sonlarında
  gösterilmez. Gerektiğinde farklı bir eğitim/sınav sürümüne eklenebilir. İç
  kalite/doğrulama günlükleri de kaynak Markdown'da korunup ana yayından ayrılır.

Güncel durum ve yol haritası için önce
[`Bölüm_00_İçindekiler_ve_İlerleme.md`](Bölüm_00_İçindekiler_ve_İlerleme.md),
sonra [`Editor_Degerlendirme_Formu_Tur2.md`](Editor_Degerlendirme_Formu_Tur2.md)
okunmalıdır.

---

## Onaylanan yayın hedefi

2 Ağustos 2026 tarihli editöryal karar görüşmesinde aşağıdaki hedefler onaylandı;
her madde ayrı paket hâlinde uygulanır ve durumu ayrıca kaydedilir:

1. Önce **HTML + PDF değerlendirme sürümü**, bağımsız uzman incelemelerinden sonra
   dijital ve baskıya hazır nihai sürüm üretilecek.
2. Alelik seri Bölüm 14'e, digenik/oligogenik/değiştirici mimari Bölüm 15'e
   alınacak. **✅ 3 Ağustos 2026'da uygulandı.**
3. **Kalıtsal kanser yatkınlığı ve ikinci vuruş** bağımsız Bölüm 16 olarak
   hazırlanacak; mevcut yorum ve klinik sentez bölümleri 17 ve 18'e kayacak.
   **✅ 4 Ağustos 2026'da uygulandı.**
4. Okuyucuya yönelik öz değerlendirme materyali proje içinde ayrı tutulacak;
   ana kitap sürümüne girmeyecek. Gerektiğinde farklı bir eğitim/sınav
   sürümünde kullanılabilecek.
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
| `DEVIR_NOTU.md` | **Araç/oturum devri: ilk okunacak dosya.** Son oturumun yaptığı iş, bilinen tuzaklar, oturum başı denetim komutu |
| `README.md` | Projenin kısa güncel durumu ve başlangıç noktası |
| `CLAUDE.md` | Bağlayıcı çalışma, bilimsel doğrulama ve devamlılık kuralları |
| `Bölüm_00_İçindekiler_ve_İlerleme.md` | Canlı bölüm/görsel/kaynak envanteri ve yol haritası |
| `Editor_Degerlendirme_Formu_Tur2.md` | Editöryal kararlar ve uygulanma durumu |
| `Dogrulama_Kutugu.md` | İddia ve kaynak doğrulama geçmişi |
| `Terminoloji_Kaynak_Denetimi.md` | Türkçe terim kararları, önce/sonra tablosu ve kaynakları |
| Git geçmişi | Her değişikliğin ne, neden ve nasıl yapıldığı |

Her yeni oturumda **önce `DEVIR_NOTU.md`**, sonra bu belgeler ve `git status` okunmalıdır. Yapılmamış bir karar,
belgelerde **“onaylandı — uygulanmadı”** olarak belirtilir; tamamlanmış gibi
sunulmaz.

---

## Dosya haritası

| Yol | İşlev |
|---|---|
| `Bölüm_01_*.md` – `Bölüm_18_*.md` | Mevcut bilimsel bölüm kaynakları |
| `kitap/` | Künye, ön/arka madde, ekler, sözlük ve dizinler |
| `kitap/19_Oz_Degerlendirme.md` | Ana kitap dışında tutulan, isteğe bağlı soru bankası ve yanıt yaklaşımları |
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
bağlantıları ve terminoloji/HGVS denetimi → Bölüm 14–15 sıra değişimi → Bölüm 8
sayısal/yapısal kromozom anomalileri revizyonu → digenik kanıt kontrol listesi →
klinik örnek çeşitliliği → bağımsız kanser yatkınlığı/ikinci vuruş Bölüm 16**.
Öz değerlendirme materyali ayrı dosyada hazırdır ve ana yayında kapalıdır.
Sıradaki evre bağımsız uzman incelemesi ve yayın kapanışıdır.
