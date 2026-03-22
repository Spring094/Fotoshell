# FOTOSHELL: Islak Laboratuvar (Wet-Lab) Sentez ve Kaplama Protokolü
*Bahar (Biyokimyager & PI), Amber (Dijital Mimar)*

Bu protokol, bilgisayar ortamında (in silico) hesaplanarak onaylanan Zn-TCPP / PEDOT:PSS biyomimetik fotovoltaik matrisinin, fiziksel bir laboratuvarda (in vitro) üretilmesi için gerekli adım adım adımları (Standard Operating Procedure - SOP) içerir.

---

## BÖLÜM 1: GEREKLİ KİMYASALLAR VE CİHAZLAR (MATERIAL LIST)

### 1.1. Kimyasallar (Reaktifler)
1.  **Işık Emici Biyo-Boya (Sensitizer):** Zn-TCPP [Zinc(II) meso-tetra(4-carboxyphenyl)porphyrin] tozu (Purity: >98%).
2.  **Yarı İletken Nano-İskele (Scaffold):** Titanyum Dioksit (TiO2) Nanopartikül Pastası (Anatase faz, 20-30 nm partikül boyutu).
3.  **İletken Koruyucu Kabuk (Shell/HTM):** PEDOT:PSS sulu dispersiyonu (1.3 wt % in H2O, iletken kalite).
4.  **Çözücüler (Solvents):** Susuz Etanol (Ethanol, Anhydrous >99%), Dimetil Sülfoksit (DMSO) veya N,N-Dimetilformamid (DMF).
5.  **Karşı Elektrot (Counter Electrode):** Karbon/Grafit pastası veya Platin (Pt) kaplı FTO camı.

### 1.2. Cihazlar (Equipment)
*   Spin Coater (Döndürerek Kaplama Cihazı) veya Doktor Bıçağı (Doctor Blade) aparatı.
*   Manyetik Karıştırıcı (Isıtıcılı - Hot Plate Magnetic Stirrer).
*   Vakum Etüvü (Vacuum Oven) veya Kül Fırını (Muffle Furnace, 450°C'ye çıkabilen).
*   Ultrasonik Banyo (Ultrasonic Bath).

---

## BÖLÜM 2: SENTEZ VE KAPLAMA AŞAMALARI (PROCEDURE)

### Aşama 1: TiO2 İskelenin Hazırlanması (Yüzey Kaplama)
1.  Temizlenmiş (Aseton ve Etanol ile ultrasonik banyoda 15 dk yıkanmış) metal/FTO cam yüzey alınır.
2.  Yüzeye **TiO2 pastası**, 'Doktor Bıçağı (Doctor Blade)' tekniği kullanılarak ~10-15 mikrometre kalınlığında ince bir film halinde sürülür.
3.  TiO2 kaplı yüzey, yavaşça fırında ısıtılarak **450°C'de 30 dakika** boyunca sinterlenir. (Bu adım, TiO2 moleküllerinin birbirine ve yüzeye kaynaşmasını, gözenekli bir sünger yapısı oluşturmasını sağlar).
4.  Yüzeyin 80°C'ye kadar soğuması beklenir.

### Aşama 2: Biyomimetik Boyanın (Zn-TCPP) Hazırlanması ve Yüklenmesi
1.  **Boya Solüsyonu:** 0.3 mM konsantrasyonunda Zn-TCPP boyası, susuz Etanol içinde çözülür. (Molekülün çözünürlüğünü artırmak için karanlıkta 15 dk ultrasonik banyoda bekletilebilir).
2.  **Yükleme (Sensitization):** Hala 80°C civarında ılık olan TiO2 kaplı test yüzeyi, doğrudan Zn-TCPP etanol solüsyonunun içine daldırılır.
3.  Yüzey bu boya çözeltisinde **oda sıcaklığında, tamamen karanlık bir ortamda 12-18 saat** bekletilir. (Bu sürede Zn-TCPP molekülündeki karboksil (-COOH) grupları, TiO2 yüzeyine kimyasal kancalarla (bidentate) tutunur).
4.  Süre sonunda yüzey çıkarılır, fazla boyayı atmak için temiz Etanol ile yıkanır ve azot gazıyla (N2) kurutulur. Kaporta artık güneşi emen yeşil/kızıl bir renge bürünmüştür.

### Aşama 3: Kapsülleme (Encapsulation) - "Shell" Matrisinin Uygulanması
Biyomimetik moleküllerin dış ortamdan (su/oksijen) korunması ve üretilen elektronların/deliklerin toplanması için koruyucu iletken polimer (PEDOT:PSS) katmanı uygulanır.
1.  Boyanmış TiO2 yüzeyinin üzerine, damlalık ile birkaç damla **PEDOT:PSS solüsyonu** damlatılır.
2.  Yüzey hemen **Spin Coater** cihazına yerleştirilir ve 3000 RPM hızında 30 saniye döndürülerek polimerin homojen, nano-incelikte bir zırh (kapsül) oluşturması sağlanır.
3.  Kaplama bittikten sonra, polimer kabuğun kuruması ve sertleşmesi için numune **100°C'de 15 dakika** sıcak plakada (Hot Plate) fırınlanır.
4.  (Opsiyonel): Endüstriyel otomotiv dayanıklılığı için en üste ince bir şeffaf poliüretan sızdırmazlık tabakası spreylenebilir.

### Aşama 4: Karşı Elektrotun Kapatılması ve Test
1.  Üzerine karbon/platin kaplanmış ikinci bir şeffaf yüzey (veya iletken kaporta filmi), bu sandviç yapının en üstüne kapatılır.
2.  Kenarlar epoksi veya Surlyn (sıcak eriyik film) ile mühürlenir.
3.  **Güneş Simülatörü Testi:** Hazırlanan bu "Fotoshell" numunesi, AM 1.5G standart güneş simülatörünün (100 mW/cm²) altına konur ve multimetre/potansiyostat ile ürettiği Volt (Voc) ve Amper (Jsc) ölçülür.

---
*Protokol Sonu. Bu belge, bilgisayarda tasarlanan Fotoshell'in fiziksel dünyadaki ilk prototip (MVP) üretim rehberidir.*
