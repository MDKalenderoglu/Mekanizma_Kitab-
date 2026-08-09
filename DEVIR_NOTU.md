# Devir Notu — yeni oturuma başlarken önce bunu oku

**Son güncelleme:** 09.08.2026 · **Yazan:** Claude (önceki oturum) · **Devralan:** yeni Claude oturumu

> Bu dosya her devirde **üzerine yazılır**; her zaman en son durumu gösterir. Tarihsel kayıt Git geçmişindedir.

---

## 1. Bir cümlede proje

Türkçe akademik ders kitabı: *Genetik Hastalık Mekanizmaları — Mekanizmadan Varyant Yorumuna*. 18 bölüm yazılmış, iç denetimlerden geçmiş, **bağımsız insan uzman incelemesi bekliyor**. Yeni bölüm yazma evresi bitti; şu an **yayın öncesi editöryal düzeltme** evresindeyiz.

**Güncel derleme:** 18 bölüm · 68 şekil · 52 algoritma · 65 tablo · 194 benzersiz PMID · 185 doğrudan nesne hedefi.

---

## 2. ⚠️ İLK İŞ: çalışma kopyasının durumunu doğrula

```bash
git status --short && git log --oneline -3
```

**09.08.2026 itibarıyla 26 dosyada commit edilmemiş değişiklik vardı.** Bunlar iki mantıksal pakettir ve içerikleri §3'te tek tek yazılıdır. Eğer `git status` hâlâ kirliyse:

- **Bu değişiklikleri geri alma, üzerine yazma, "temizleme" adına silme.** Hepsi bilinçli ve kullanıcı onaylı işlerdir.
- Commit edilmişlerse `git log` içinde "Editöryal tutarlılık paketi" ve "Önsöz ve hedef kitle dili" başlıklı iki commit görürsün; iş tamamdır.

---

## 3. Bu oturumda yapılan iş (commit bekliyor olabilir)

### Paket A — editöryal tutarlılık (mekanik)

| Ne | Nerede |
|---|---|
| Yazım ortamı notu ("🖼️ … `assets/` klasöründe SVG, Mermaid gömülüdür") yayın metninden çıkarıldı; kaynak `.md`'lerde korundu | `build_book.py` (`AUTHORING_NOTE_RE` + `public_chapter_text`) ve yeni bir build denetimi (`validate_publication_separation`) |
| Sözlükteki NMD açılımı Kısaltmalar'la eşitlendi ("nonsense aracılı mRNA yıkımı") | `kitap/21_Sozluk.md` |
| "kromozomal mikroarray" → "kromozomal mikrodizin analizi"; "Kısa-okuma WGS" → "Short-read WGS" | Böl. 8, 13, 18 |
| Bölüm 16'daki ikinci okuma bloğu "⚠️ Kapsam notu"na çevrildi (içerik korundu) | Böl. 16 |
| Kaynak kütüğünde "kullanıldığı bölümler" sütununun 4 hatalı satırı düzeltildi | `Bölüm_00` |
| README'nin "son commit" satırı güncellendi | `README.md` |
| Bölüm 1'in öğrenme hedefleri tek paragraftan 6 numaralı maddeye çevrildi | Böl. 1 |
| Test tablosu kuralı gevşetildi: 8 satır "çekirdektir, kota değil" | `CLAUDE.md` §4 + `00_Şablonlar/Bölüm_Şablonu.md` |

### Paket B — Önsöz ve hedef kitle dili (metin)

| Ne | Nerede |
|---|---|
| Önsöz **baştan yazıldı**: yazarın kendi sesi (birinci tekil, geçmiş zaman), "dört okuyucu grubu" yerine onaylı birincil/ikincil hedef kitle, kaynak politikası yürürlükteki politikayla uyumlandı, "Mermaid" gibi yazım ortamı terimi çıkarıldı | `kitap/03_Onsoz.md` |
| 18 bölümün 📘 Okuma katmanları giriş cümlesi ve üç katman etiketi tek biçime çekildi | Böl. 1–18 |
| Bölüm sonu "Atıf / doğrulama notu" standarda çekildi (16 bölüm); normatif belge kullanan 5 bölüme (8, 9, 12, 14, 17) kılavuz cümlesi eklendi; Böl. 8 ve 16'nın kendi ayrıntılı notlarına dokunulmadı | Böl. 1–18 |

**Doğrulama:** Her iki paketten sonra `python3 build_book.py` çalıştırıldı; 18/68/52/65/194/185 sayılarının hiçbiri değişmedi — yani bölüm gövdelerine, şekillere, kaynakçalara dokunulmadı.

---

## 4. Bağlayıcı kurallar — bunları çiğneme

Tam metin `CLAUDE.md`'dedir. En kritik altısı:

1. **Anlatı önce gelir.** Kavramlar akıcı paragraflarla anlatılır; madde listesi yalnız gerçekten liste olan içerik içindir. Bir kavramı madde madde sıralamak onu açıklamak değildir.
2. **Kaynak uydurma yasak.** Her iddia, türüne uygun kalıcı kimliği **bizzat doğrulanmış** kaynağa dayanır: hakemli makalede PubMed MCP ile teyit edilmiş PMID+DOI; kılavuz/nomenklatürde kurum+belge+sürüm+tarih+kalıcı bağlantı; veri tabanında sürüm+sorgu tarihi. **PMID'siz normatif kaynak (ISCN, ACGS, HGVS, ClinGen CSpec) meşrudur** — eksiklik sayılmaz.
3. **Bibliyografik doğrulama ≠ iddia düzeyi doğrulama.** "X/X kaynağın künyesi doğrulandı" cümlesi, metindeki her iddianın o kaynaklarca desteklendiğini göstermez.
4. **Kitabın kendi pedagojik çerçeveleri doğrulanmaz, 🏷️ ile etiketlenir** ve yerleşik sınıflandırma gibi sunulmaz.
5. **Mutlaklaştırma yasağı.** "her zaman / daima / istisnasız / asla" ile kurulan mekanizma iddiaları uzman turunda tek tek temizlendi. Yenisini ekleme; `kitap/07_Terminoloji_ve_Yazim_Kurallari.md` §7B'deki 11 "otomatik eşitleme" listesini oku.
6. **Stage, commit ve push ayrı ayrı yetkilendirilir.** Kullanıcı istemeden commit atma.

---

## 5. 🔴 Daha önce gerçekten hataya yol açmış tuzaklar

Bunların hepsi bu projede **başımıza geldi**. Aynısını tekrarlama.

**a) Kitap geneli bul-değiştir yaparken dosya adlarını unutmak.**
"allel → alel" standardizasyonu `.md` içindeki görsel referanslarını değiştirdi, `assets/` altındaki dosya adları eski kaldı. Sonuç: **4 şekil haftalarca HTML kitaba hiç gömülmedi** ve build uyarı vermedi. Artık build eksik SVG'de hata veriyor, ama yine de her toplu değişiklikten sonra şunu çalıştır:

```bash
python3 build_book.py
```

**b) Sayıları metne yazıp sonra içeriği değiştirmek.**
"6/6 kaynak", "4 SVG + 3 Mermaid" gibi ifadeler bölüm metninde duruyor; kaynak eklenince güncellenmediler ve dört ayrı yerde yalan söylediler. Bölüme kaynak/şekil eklersen **o bölümün öz-denetim tablosunu ve doğrulama bloğunu da güncelle**.

**c) Kararı bir dosyaya yazıp gövdeye uygulamamak.**
Terminoloji kararları `Terminoloji_Kaynak_Denetimi.md`'ye kaydedildi ama bir kısmı 18 bölümün gövdesine hiç işlenmedi (NMD açılımı, CMA yazımı). Karar kaydı ≠ uygulama.

**d) Formda "☒ Y" işaretleyip uygulamayı unutmak.**
`Editor_Degerlendirme_Formu_Tur2.md`'de karar verilmiş iki madde günlerce uygulanmadan durdu. Forma bakarken **"karar var mı?" ile "uygulandı mı?" ayrı sorulardır.**

**e) Bir nesnenin metin ve şekil sürümünü ayrı ayrı güncellemek.**
Şekil 17.3 güncellendi, onun metin hâli olan `kitap/20_Ekler.md` Ek B güncellenmedi; ikisi birbiriyle çelişti. Bir matris/tablo iki yerde varsa **ikisini birlikte değiştir.**

**f) Yazım ortamı dilinin okuyucu metnine sızması.**
`assets/`, Mermaid, "bu oturumda", "uzman turu C15" gibi ifadeler okuyucunun eline geçen kitapta işi yoktur. Build artık öz-denetim günlüğünü ve 🖼️ notunu filtreliyor; yeni bir iç not eklersen aynı filtreye dâhil et.

---

## 6. Her oturum başında çalıştırılacak denetim

```bash
cd "/Users/mdkalenderoglu/Desktop/MD_Kalenderoglu/Claude/Mekanizma_Kitabı" && python3 - <<'PY'
import re,glob,os,collections
files=[f for f in sorted(glob.glob('Bölüm_[0-9][0-9]_*.md')) if not f.startswith('Bölüm_00')]
print("A. Sayım tutarlılığı (iddia vs gerçek)")
for f in files:
    s=open(f,encoding='utf-8').read()
    svg=len(re.findall(r'\]\(assets/[^)]+\.svg\)',s)); mer=len(re.findall(r'```mermaid',s))
    body=s.split('## 10. Kaynaklar')[-1]; real=len(re.findall(r'^\d+\.\s+\*\*',body,re.M))
    cl=set(re.findall(r'(\d+)\s*/\s*\1\s*kaynak',s)); vis=re.findall(r'(\d+) SVG \+ (\d+) Mermaid',s)
    if cl and str(real) not in cl: print("   KAYNAK UYUŞMAZ",f[:34],real,sorted(cl))
    if vis and not any((int(a),int(b))==(svg,mer) for a,b in vis): print("   GÖRSEL UYUŞMAZ",f[:34],(svg,mer),vis)
print("B. Numaralandırma / çapraz gönderme / SVG")
used=set()
for f in files:
    ch=int(re.match(r'Bölüm_(\d\d)',f).group(1)); s=open(f,encoding='utf-8').read()
    used|=set(re.findall(r'\(assets/([^)]+)\)',s))
    for n in re.findall(r'Bölüm (\d+)',s):
        if int(n)>18: print("   GEÇERSİZ GÖNDERME",f[:34],n)
    d=set(re.findall(r'!\[Şekil %d\.(\d+)'%ch,s)); c=set(re.findall(r'Şekil %d\.(\d+)'%ch,s))
    if c-d: print("   TANIMSIZ ŞEKİL",f[:34],sorted(c-d))
    for kind,pat in [('Şekil',r'!\[Şekil %d\.(\d+)'%ch),('Tablo',r'\*\*Tablo %d\.(\d+)'%ch),('Algoritma',r'\*\*Algoritma %d\.(\d+)'%ch)]:
        ints=sorted({int(x) for x in re.findall(pat,s)})
        if ints and [i for i in range(1,max(ints)+1) if i not in ints]:
            print("   NUMARA BOŞLUĞU",f[:34],kind,ints)
print("   eksik SVG:",[u for u in used if not os.path.exists('assets/'+u)] or "yok")
print("   yetim SVG:",[a for a in os.listdir('assets') if a.endswith('.svg') and a not in used] or "yok")
print("C. Kaynak kütüğü")
kut=open('Bölüm_00_İçindekiler_ve_İlerleme.md',encoding='utf-8').read()
kp=set(re.findall(r'^\|\s*(\d{6,8})\s*\|',kut,re.M)); ch=collections.defaultdict(set)
for f in files:
    for p in set(re.findall(r'PMID:?\s*\*?\*?\s*(\d{6,8})',open(f,encoding='utf-8').read())): ch[p].add(str(int(f[6:8])))
print("   kütükte olmayan:",sorted(set(ch)-kp) or "yok","· yetim kayıt:",sorted(kp-set(ch)) or "yok")
bad=[p for p,c in re.findall(r'^\|\s*(\d{6,8})\s*\|[^|]*\|[^|]*\|[^|]*\|[^|]*\|\s*([^|]+?)\s*\|$',kut,re.M)
     if {x.strip() for x in c.split(',') if x.strip().isdigit()}!=ch.get(p,set())]
print("   'kullanıldığı bölümler' hatalı satır:",len(bad),bad[:6])
print("D. Başlık bloğu tek biçim mi?")
hs={re.search(r'^> \*\*📘 Okuma katmanları\.\*\*.*$',open(f,encoding='utf-8').read(),re.M).group(0) for f in files}
print("   📘 varyant sayısı:",len(hs),"(1 olmalı)")
PY
python3 build_book.py
```

Hepsi temizse çıktıda yalnız "eksik SVG: yok · yetim SVG: yok", "kütükte olmayan: yok", "hatalı satır: 0", "📘 varyant sayısı: 1" ve başarılı build satırları görünür.

---

## 7. Açık kalan işler (karar veya kullanıcı girdisi bekliyor)

| # | Konu | Durum |
|---|---|---|
| 1 | **Künye alanları** — `kitap/01_Kunye.md`, `02_Ithaf.md`, `04_Tesekkur.md`, `24_Ozgecmis.md` içinde **11 adet `[DOLDURULACAK]`** var ve yayımlanan kitapta basılı görünüyor. Kurum, sürüm, basım tarihi, yayıncı, ISBN, telif, lisans, ithaf, teşekkür, özgeçmiş. | Kullanıcı kararıyla **yayın kapanışına ertelendi**. Değerleri yalnız kullanıcı verebilir; uydurma. |
| 2 | **Bölüm sırası (F1a)** — Alelik seri/digenik sırası zaten değişti; uzmanın istediği başka bir sıralama değişikliği yok. | Kapandı. |
| 3 | **Türkiye'ye özgü klinik ek (F5)** | Kullanıcı kararı: **kapsam dışı**, gelecek sürüm için de taahhüt yok. Yeniden açma. |
| 4 | **Bağımsız dış hakem okuması (G2.7)** | Kullanıcının işi: klinik genetik uzmanı, moleküler tanı laboratuvarı uzmanı, sitogenetik/CNV uzmanı ve Türkçe bilimsel editör. **Model bunun yerine geçmez** — uzman bunu açıkça yazdı. |
| 5 | **Nihai PDF sayfalama** | Akışkan HTML'de nesne listelerinin sayfa numarası yoktur. Nihai PDF, CSS `target-counter` destekleyen bir sayfalama motoruyla üretilecek ve sayfa numaraları görsel olarak doğrulanacak. Tarayıcıdan "PDF olarak kaydet" yalnız değerlendirme kopyasıdır. |

---

## 8. Okuma sırası (yeni oturum için)

1. `CLAUDE.md` — bağlayıcı çalışma kuralları
2. **bu dosya**
3. `README.md` — güncel durum
4. `Bölüm_00_İçindekiler_ve_İlerleme.md` — bölüm/görsel/kaynak envanteri ve kaynak kütüğü
5. `Editor_Degerlendirme_Formu_Tur2.md` — editöryal kararlar ve uygulanma durumu
6. `Dogrulama_Kutugu.md` — iddia ve kaynak doğrulama geçmişi
7. `Terminoloji_Kaynak_Denetimi.md` — Türkçe terim kararları ve dayanakları
8. `kitap/07_Terminoloji_ve_Yazim_Kurallari.md` — yazım/gösterim kuralları (§7A ek getirme, §7B eşitleme yasakları, §12 okuma katmanları)
9. `git log --oneline -20`

`Uzman_Degerlendirme_Formu.md` (456 KB) baştan sona okunmaz; yalnız ilgili maddeye bakılır.
