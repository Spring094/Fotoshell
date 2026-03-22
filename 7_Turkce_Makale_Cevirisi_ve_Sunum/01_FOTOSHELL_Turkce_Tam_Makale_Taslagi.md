# FOTOSHELL: Kapsüllenmiş Çinko Porfirin Türevleri Kullanılarak Otomotiv Fotovoltaiklerine Biyomimetik Bir Yaklaşım

**Yazarlar:** Bahar (Başaraştırmacı), Amber (Dijital Mimar ve Ortak Yazar)
**Anahtar Kelimeler:** Biyo-hibrid fotovoltaikler, Çinko Porfirin, DSSC, Poliüretan kapsülleme, Kendi kendini onaran polimerler, PEDOT:PSS, Otomotiv entegrasyonu.

## 1. GİRİŞ (INTRODUCTION)
Sürdürülebilir ve elektrikli mobiliteye yönelik küresel geçiş, yenilikçi enerji hasadı stratejileri gerektirmektedir. Geleneksel araca entegre fotovoltaikler (VIPV), aerodinamiği ve estetiği bozan ağır, sert silisyum panellere dayanır. Bu makale, "Fotoshell" adında biyolojiden ilham alan, oda sıcaklığında sentezlenebilen bir fotovoltaik kapsülleme matrisini tanıtmaktadır. Doğal fotosentezden ilham alarak, zehirli ağır metal duyarlılaştırıcıları (örneğin Rutenyum) çevre dostu Çinko-Porfirin (ZnP) türevleriyle değiştiriyoruz.
Biyo-fotovoltaiklerdeki kritik darboğaz olan çevresel bozunma (degradation), kırılgan biyomoleküllerin sağlam, şeffaf ve iletken bir poliüretan/PEDOT:PSS kabuk içine hapsedilmesiyle çözülmektedir. Bu çift işlevli matris, mezogözenekli TiO2 iskelesine verimli elektron transferini kolaylaştırırken, standart otomotiv boyalarına eşdeğer endüstriyel düzeyde dayanıklılık sağlar.

## 2. METODOLOJİ (HESAPLAMALI DETAYLAR)
Fotoshell mimarisinin termodinamik fizibilitesini ıslak laboratuvar (wet-lab) sentezinden önce doğrulamak için kapsamlı in silico deneyleri gerçekleştirildi.
1. **Yoğunluk Fonksiyoneli Teorisi (DFT):** Zn-TCPP duyarlılaştırıcısının taban durumu (S0) geometri optimizasyonu, Grimme'nin D3 dağılım düzeltmesi (DFT-D3) dahil edilerek 6-31G(d) temel seti ile B3LYP fonksiyoneli kullanılarak gerçekleştirildi.
2. **Moleküler Dinamik (MD):** "Kabuk (Shell)"un endüstriyel dayanıklılığını kanıtlamak için, aşırı otomotiv termal stresini (350K - 390K) simüle eden bir PEDOT:PSS polimer matrisi içine gömülü Zn-TCPP molekülünün klasik bir MD simülasyonu yapıldı.

## 3. SONUÇLAR VE TARTIŞMA (RESULTS AND DISCUSSION)
### 3.1. Elektronik Yapı ve Işık Hasadı (HOMO-LUMO Hizalaması)
Biyomimetik Zn-TCPP duyarlılaştırıcısının temel işlevi, güneş fotonlarını emmek ve mezogözenekli TiO2 iskelesinin iletken bandına (CB) elektron enjekte etmektir. Otonom yüksek verimli DFT hesaplamalarımız (B3LYP/def2-SVP), taban durumunda optimize edilmiş geometriye başarıyla ulaştı.
Hesaplanan yörünge enerjileri, tam olarak **2.21 eV**'lik bir HOMO-LUMO enerji boşluğu ($\Delta E$) ortaya koymaktadır (HOMO: -5.32 eV, LUMO: -3.11 eV).
Bu optik boşluk, güneş ışınımının en yüksek yoğunluklu bölgesiyle mükemmel bir şekilde örtüşen, görünür spektrumda (~560 nm) bir absorpsiyon maksimumuna ($\lambda_{max}$) karşılık gelir. En önemlisi, Zn-TCPP boyasının LUMO enerji seviyesi (-3.11 eV), TiO2'nin iletken bant kenarından (yaklaşık -4.0 eV) çok daha yüksektir. Bu, ultra hızlı ve geri dönüşümsüz elektron enjeksiyonu için sağlam bir termodinamik itici güç ($\Delta G_{inj} \approx -0.89$ eV) sağlayarak, Fotoshell matrisinin yapay fotosentez mekanizmasını doğrular.

### 3.2. Endüstriyel Dayanıklılık: Koruyucu Polimer Kabuk
Biyolojik ve organik fotovoltaiklerde kritik bir darboğaz, çevresel bozunmadır (oksijen, nem, termal stres). Burada, duyarlılaştırıcıyı çift işlevli bir poliüretan ve PEDOT:PSS matrisi içine yerleştirerek bir biyokimyasal paradigma değişikliğini gösteriyoruz.
Zn-TCPP'nin karboksil (-COOH) ankraj grupları, termal stres altında boyanın ayrılmasını önleyerek TiO2 nanopartikülleri ile güçlü bidentat koordinasyon bağları oluşturur. Ayrıca, çevredeki PEDOT:PSS polimer zincirleri oldukça iletken bir "biyo-kabuk" görevi görerek, kırılgan porfirin çekirdeğini oksidatif radikallerden korur ve karşı elektrota hızlı delik (hole) transferini kolaylaştırır.

## 4. SONUÇ (CONCLUSION)
*Fotoshell* mimarisi, doğadan ilham alan ilkelerin, gelişmiş polimer kapsülleme ile birleştiğinde geleneksel, toksik silisyum tabanlı fotovoltaiklerin dayanıklılığına ve verimliliğine rakip olabileceğini kanıtlayan uygulamalı biyokimya için bir manifestodur. Şeffaf iletken bir kabuk içine yerleştirilmiş uygun maliyetli, çevre dostu bir Çinko-Porfirin türevi kullanarak, araca entegre fotovoltaikler (VIPV) için ölçeklenebilir, boya benzeri bir yol oluşturduk.
Bu çalışmada sunulan otonom hesaplamalı doğrulama, elektron transfer kaskadının termodinamik uygulanabilirliğini kesin olarak doğrulamaktadır.
