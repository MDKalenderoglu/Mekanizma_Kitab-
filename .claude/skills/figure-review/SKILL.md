---
name: figure-review
description: Mekanizma Kitabı'ndaki SVG şekilleri (mekanizma şemaları, pathway diyagramları, domain haritaları, karşılaştırmalı görseller) bağımsız bilimsel doğruluk açısından inceletir. Codex (resmi openai/codex-plugin-cc eklentisi + yerel Codex CLI görsel girdisi) salt-okunur editördür; ok yönü, moleküler ilişki, lokalizasyon, zaman sırası, etiket ve legend hatalarını arar; estetiği bilimsel doğruluktan ayrı raporlar. Kullanıcı "görselleri kontrol ettir", "şekilleri incelet", "figure-review" dediğinde kullan.
---

# Skill: figure-review

`academic-review`'un görsel-odaklı kardeşi; aynı **Claude = Principal Author / Codex = Senior Scientific Editor** modeli. Codex **hiçbir dosyayı değiştirmez**, yalnız rapor üretir.

## Neden yerel Codex CLI görsel girdisi? (smoke test edildi 2026-09-27)

- Plugin'in rescue/app-server yolu **görsel taşımaz** (kaynak taramasıyla doğrulandı: companion `task` komutunda `--image` yok, app-server lib'lerinde image alanı yok). O yol SVG'yi yalnız XML metni olarak okur — gerçek "vision" değil.
- Bu yüzden görsel inceleme, **resmi yerel Codex CLI'nin çok-kipli (multimodal) görsel girdisiyle** yapılır: `codex exec --image <PNG> --sandbox read-only`. Bu resmi CLI'dir, özel bir bridge DEĞİL. Test edildi: Codex render'daki başlıkları, panel adlarını, ok/işaret durumlarını ve alt-notu doğru okudu.
- `--sandbox read-only` OS düzeyinde yazma-engelidir; smoke test'te inceleme sonrası `git diff` birebir boş kaldı.

## Render kuralı — geniş şekiller kareye kırpılmamalı (KRİTİK)

Kitabın şekilleri **geniştir** (viewBox ~1200×780, ~1.5:1). `qlmanage` bunları **kareye kırpar ve en sağdaki paneli keser** (smoke test'te 4/4 panelden yalnız 3'ü göründü). Bu yüzden **`qlmanage` KULLANMA.** Bunun yerine en-boy oranını koruyan render helper:

```bash
# bir kez: cd .claude/skills/figure-review && npm i sharp   (prebuilt, sistem bağımlılığı yok)
node "$CLAUDE_PLUGIN_ROOT_OR_SKILL_DIR/render_svg.mjs" <girdi.svg> <çıktı.png> 1600
```
`render_svg.mjs` (bu klasörde) sharp ile SVG'yi ~1600px genişlikte, oranını koruyarak (ör. 1600×1040) beyaz zeminli PNG'ye çevirir ve çıktı boyutlarını yazdırır. `rsvg-convert`/`cairosvg` kuruluysa onlar da kullanılabilir (aspect korudukları sürece). Çıktıyı **scratchpad'e** yaz, projeye değil.

**Zorunlu ön kontrol:** Render'dan sonra çıktı PNG boyut oranı SVG viewBox oranıyla eşleşmeli (kırpılma olmadığını kanıtlar). Emin olmak için Claude PNG'yi kendi de bir kez görüntüler (Read), sonra Codex'e gönderir.

## Adım adım iş akışı

### 1. Kapsamı belirle
Hangi şekil(ler)? Her hedef için: `assets/sekil_NN_*.svg` yolu, bölümdeki figcaption ve şekli çevreleyen 1-2 paragraf (metin-görsel tutarlılığı için birlikte verilir). SVG içi metin etiketlerini `grep -o '<text[^>]*>[^<]*</text>'` ile çıkarıp ground-truth olarak elinde tut.

### 2. Claude ön-incelemesi
Stil_Rehberi §3 (Görsel standardı v2: palet semantiği, panel iskeleti, okunurluk) kendi gözünle. Codex'in odağı **bilimsel** doğruluk; estetik/biçim Claude'un işi.

### 3. Render (yukarıdaki kural) → Codex'i çağır (`codex exec --image`, salt-okunur)

**Zorunlu:** prompt `READ-ONLY FIGURE REVIEW. DO NOT MODIFY ANY FILE.` ile başlar; write-fiili yok (`fix/apply/edit/rewrite/düzelt/uygula` yasak); yalnız stdout raporu.

```bash
codex exec --image <çıktı.png> --sandbox read-only --skip-git-repo-check --color never \
"READ-ONLY FIGURE REVIEW. DO NOT MODIFY, CREATE OR PATCH ANY FILE. Report only to stdout.
Sana bir bilimsel şekil görseli ekledim (Türkçe tıbbi genetik ders kitabı). İlgili bölüm metni ve figcaption: <figcaption + çevre paragraf metni>.
SADECE görsele + verilen metne bakarak değerlendir. HER bulguyu şu şablonla raporla:
SEVERITY (BLOCKER/MAJOR/MINOR/SUGGESTION) | LOCATION (panel/öge) | ISSUE | WHY IT MATTERS | PROPOSED ACTION | CONFIDENCE

BİLİMSEL DOĞRULUK (asıl odak):
1. Ok yönleri gerçek moleküler/nedensel ilişkiyi doğru gösteriyor mu (ters/eksik döngü)
2. Moleküler ilişki türü doğru mu (bağlanma/inhibisyon/aktivasyon karışmış mı)
3. Lokalizasyon doğru mu (organel/hücre tipi/doku)
4. Zaman/sıra doğru mu (gelişimsel/biyokimyasal adım sırası)
5. Pathway bağlantıları eksiksiz/doğru mu (atlanan ara adım, yanlış dallanma)
6. Etiketler doğru mu (gen/protein/birim/sayı; metindeki terimle birebir)
7. Figure legend/alt-not şekildekiyle uyumlu mu
8. Şekil ile çevre metin ÇELİŞİYOR mu (çelişki = BLOCKER)
9. Şekil tek başına yanlış kesinlik/basitleştirme veriyor mu

AYRI olarak, isteğe bağlı 'AESTHETIC NOTES' bölümünde estetik/biçim gözlemlerini (çakışma, kontrast, punto) SEVERITY'siz düz liste olarak ver — bunlar bilimsel bulgu değildir.

Bulgu yoksa 'bulgu yok' de; uydurma. Report only; change nothing."
```
Birden çok görsel için `--image` tekrarlanabilir veya her şekil ayrı çağrılır (ayrı çağrı daha izole).

### 4. Claude adjudication
- Her bilimsel bulguyu kaynağa/metne bakarak doğrula; yanlış pozitifleri reddet + gerekçelendir.
- Kabul edilen düzeltmeleri **Claude** SVG'de uygular (Stil_Rehberi §3.6: beyaz zemin, `&amp;`, CSS değişkeni yok).
- SVG değiştiyse: `xmllint --noout` + render helper ile PNG'ye bak (§Render); ayrıca şeklin metin/tablo ikizi varsa (ör. `kitap/20_Ekler.md`) onu da güncelle (DEVIR_NOTU §5e).
- AESTHETIC NOTES için Codex turu tekrarı gerekmez; doğrudan kendi kararınla uygula/reddet.
- T5 pedagojik sentez şekilleri (🏷️, ör. Şekil 17.3) normatif sınıflandırma gibi eleştirilmemeli; gerekirse görev tanımına ekle.

### 5. Kullanıcıya rapor
Bilimsel bulgular ile estetik notları **ayrı** özetle; uygulanan/reddedilen + gerekçe; stage/commit/push için ayrı onay.

## Model seçimi
`codex exec` çağrısına model bayrağı (`--model`, `-m`, `-c model=…`) ekleme; Codex'in **mevcut varsayılan modelini** kullan. Model ancak **kullanıcı açıkça istediğinde** override edilir.

## Sınır
Codex figürün **bilimsel doğruluğunu** denetler, estetiğini değil — ayrım raporda korunur. Bu skill bağımsız insan uzman incelemesinin yerine geçmez.
