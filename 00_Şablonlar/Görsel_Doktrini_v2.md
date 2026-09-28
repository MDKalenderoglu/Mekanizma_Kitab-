# Görsel Doktrini v2 — SVG Çizim Standardı (kalıcı)

> **Bu dosya neden var?** Bu doktrin başlangıçta Claude Code'un proje-dışı hafızasında (`~/.claude/.../memory/gorsel-doktrini-v2.md`) tutuluyordu. O hafıza **git ile taşınmaz** ve farklı bir PC'de kaybolur. Bu yüzden doktrin buraya, **repo içinde izlenen bir dosyaya** taşınmıştır. Kullanıcı bu doktrini 2026-06-20'de onayladı.

> **⚠️ TEK SOURCE-OF-TRUTH.** Görsel standardının bağlayıcı tanımı **yalnız bu dosyadır.** `Stil_Rehberi.md` §3 ayrıntıyı tekrarlamaz, buraya referans verir; proje-dışı hafızadaki özet yalnız bir işaretçidir. Palet, tipografi, iskelet, okunurluk ve doğrulama kuralları arasında bir uyuşmazlık görürsen **bu dosya geçerlidir** ve diğer kopya hatalıdır — düzeltilmesi gerekir.

Mekanizma Kitabı'ndaki (Genetik Hastalık Mekanizmaları textbook) tüm görseller **v2 editöryal textbook standardıyla** çizilir.

**Neden:** Eski doygun "web rengi" paleti (#e74c3c, #27ae60, #2980b9…) amatör görünüyordu. Kullanıcı v2 figürlerinde somutlaşan editöryal, semantik, sakin standardı onayladı. Ayrıca okunurluğun net ve **öğelerin üst üste binmemesinin** kesin kural olmasını istedi.

## Nasıl uygulanır

- **Palet (semantik, sabit):** nötr/yapı = slate (`#1A2B4A` mürekkep, `#2E3440` gövde, `#475569`/`#64748B` ikincil, `#CBD5E1`/`#94A3B8` çizgi, `#E2E8F0`/`#F1F5F9`/`#F8FAFC` dolgu). Mavi `#2563EB`/`#DBEAFE`/`#1D4ED8` = LoF/normal-kontrollü/Senaryo 1/yapı. Kırmızı `#B91C1C`/`#FEE2E2`/`#FEF6F5` = GoF/patojen/Senaryo 2/aşırı aktivite. Amber `#D97706`/`#FEF3C7`/`#B45309` = vurgu/klinik dikkat/fosforilasyon. Sarı yıldız `#FCD34D`+kenar `#92400E` = "varyant burada" (★). **Eski palet KULLANILMAZ.**
- **Tipografi:** `font-family="Inter, 'Source Sans 3', 'Helvetica Neue', Arial, sans-serif"`; başlık ~14px/700, etiket ~11–12px, alt-not ~9.5–10.5px.
- **OKUNURLUK + ÇAKIŞMA YASAĞI (kritik):** hiçbir metin başka metin/çizgi/kutu üstüne binmez; min yazı ≥9px (tercihen ≥10); uzun metni `<tspan>` ile böl, kutuya sığdır (taşma yok); ferah boşluk; `text-anchor` ile hizala; yerleşimi koordinat hesabıyla doğrula.
- **Yapısal iskelet:** panel rozeti (`#1A2B4A` kare + beyaz harf A/B/C), semantik renkli panel başlığı, karşılaştırmada sol=mavi/sağ=kırmızı + kesik dikey ayraç, "Mekanizma → test → yorum" alt şeridi, tek cümlelik öğreti footer'ı, kaynaklı figürde alt köşe "Kaynaklar: Yazar (yıl)".
- **İnce işçilik:** `<defs>`'te yumuşak gölge (`feDropShadow dy=1.5 stdDeviation=2 opacity=0.10`) ve semantik renkli ok markerları; yuvarlatılmış kutular (rx≈8–14); nicel gösterim (az P vs çok P, ★).

## ⚠️ OK-UCU (marker) TUZAĞI — sistematik hata, mutlaka uygula
Marker'larda `markerUnits` belirtmezsen varsayılan `strokeWidth`'tir → ok-ucu boyutu çizgi kalınlığıyla **ÇARPILIR**. 11px tanımladığın ok-ucu, stroke-width 2.5 olunca ~28px DEV üçgen olur ve yanındaki etiketin üstüne çıkar. Bu, ok'lu figürlerde tekrar tekrar çakışmaya yol açtı.
**ÇÖZÜM:** her `<marker>` tanımına `markerUnits="userSpaceOnUse"` ekle → ok-ucu markerWidth/Height değeri kadar (gerçek px) çizilir, kalınlıktan bağımsız. Etiketi ok'un üstüne koyarken ok-ucunun gerçek boyutunu hesaba kat.

## ⚠️ RENDER + GÖZLE DENETİM ZORUNLU (en kritik kural)

SVG'yi yazdıktan sonra **körlemesine bırakma.** Her figür sırayla üç adımdan geçer:

**1. XML geçerliliği**
```
xmllint --noout assets/sekil_NN_*.svg
```

**2. En-boy oranını koruyan render — tek standart**
```
node .claude/skills/figure-review/render_svg.mjs assets/sekil_NN_*.svg <çıktı.png> 1600
```
İlk kullanımda bir kez: `cd .claude/skills/figure-review && npm ci` (sharp; prebuilt, sistem bağımlılığı yok). Çıktıyı **projeye değil**, oturum scratchpad'ine yaz.

**3. Gözle bak** — üretilen PNG'yi Read ile aç ve incele. Çakışma / taşma / metnin şekil arkasında kaybolması varsa düzelt, yeniden render et, **tekrar bak**.

### ⛔ `qlmanage` KULLANILMAZ
`qlmanage`, geniş veya standart dışı en-boy oranlı SVG'lerde kaynak `viewBox` oranını güvenilir biçimde korumadığı ve kırpma oluşturabildiği için **figür QA renderer'ı olarak kullanılmaz.** En-boy oranını koruyan proje renderer'ı (yukarıda, adım 2) **tek standarttır.** Diğer belgeler bu gerekçeyi tekrarlamaz, buraya referans verir.

### Zorunlu render ön kontrolü
- Çıktı PNG'nin en-boy oranı, kaynak SVG'nin **`viewBox` oranıyla** eşleşmeli. Eşleşmiyorsa sorun figürde değil **render'dadır**; önce onu düzelt.
- Çıktı yüksekliği `viewBox` yüksekliğinin **altına düşmemeli.** Kitabın minimum puntosu 9px olduğundan küçültme doğrudan okunmazlık üretir ve incelemede yapay "etiket yanlış/eksik" bulgusuna yol açar.

**`xmllint` yalnız XML geçerliliğini test eder; görsel çakışmayı GÖSTERMEZ.** İki adım birbirinin yerine geçmez.

Geçmiş hatalar (hepsi render edilip bakılsaydı baştan yakalanırdı): metin etiketinin reseptör/şekil gövdesine binmesi; nokta/işaretin yazının ortasına gelmesi; dar alana sıkıştırılmış etiket+ikon.

## Teknik kurallar (kırılmaz)
- `viewBox` + ilk eleman beyaz `<rect fill="#ffffff"/>`; **CSS değişkeni YOK** (img olarak izole render edilir).
- **`&` asla doğrudan → `&amp;`** (kaçırılmamış `&` SVG'yi bozar).
- Türkçe etiketler; her şekilde başlık + öğreti satırı.
- Bitince `xmllint --noout assets/*.svg` ile XML geçerliliğini doğrula — sonra yukarıdaki **render + gözle denetim** adımlarını uygula; biri diğerinin yerine geçmez.

## Referans örnekler (bu standardın canlı uygulaması)
`assets/sekil_07_nmd_karar.svg`, `sekil_16_konstitutif_aktivasyon_reseptor.svg`, `sekil_17_ayni_gen_gof_lof.svg`, ve Bölüm 10 figürleri `sekil_30`–`sekil_33`.
