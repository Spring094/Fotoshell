# FOTOSHELL PROJESİ: HESAPLAMALI KİMYA İLE İKNA VE İCAT TAKVİMİ

Bu takvim, fiziksel laboratuvara (ıslak laboratuvar) girmeden, sadece bilgisayar destekli hesaplamalı kimya (in silico) yöntemleriyle projeyi akademik bir icada ve yatırıma dönüştürme stratejisini içerir.

## FAZ 1: TEORİK TASARIM VE LİTERATÜR (HAFTA 1-2)
**Hedef:** Projenin bilimsel iskeletini kurmak ve literatürdeki boşluğu (gap) ispatlamak.
*   **Adım 1:** Işık emici biyomimetik moleküllerin (örneğin Zn-Porfirin türevleri) tespiti ve kimyasal yapılarının (SMILES kodlarının) çıkarılması.
*   **Adım 2:** İletken polimer (PEDOT:PSS) ve koruyucu kapsül (Silika/Poliüretan) matrisinin teorik etkileşim mekanizmasının belirlenmesi.
*   **Adım 3:** Makalenin 'Giriş (Introduction)' bölümünün literatür atıflarıyla birlikte yazılması (Amber tarafından).

## FAZ 2: HESAPLAMALI KİMYA (IN SILICO) SİMÜLASYONLAR (HAFTA 3-5)
**Hedef:** Laboratuvara girmeden, bilgisayar ortamında moleküllerin elektrik üreteceğini ve parçalanmayacağını kuantum mekaniği ile ispatlamak.
*   **Adım 1:** Moleküllerin Yoğunluk Fonksiyoneli Teorisi (DFT) ile 3 boyutlu optimizasyonu.
*   **Adım 2:** HOMO ve LUMO (elektron verme ve alma kapasitesi) enerji seviyelerinin hesaplanması. Bu sayede güneş ışığının hangi dalga boylarını emeceği kanıtlanacak (TD-DFT analizi).
*   **Adım 3:** Molekülün TiO2 (Yarı iletken) yüzeyine tutunma (adsorpsiyon) enerjilerinin simüle edilmesi. (Bağlantı ne kadar güçlüyse, dayanıklılık o kadar yüksektir).
*   **Adım 4:** Fiziksel dayanıklılık (Degradation) kanıtı: Polimer matris içindeki molekülün termal ve UV stabilitesinin bilgisayar ortamında stres testlerine (Molecular Dynamics - MD) sokulması.

## FAZ 3: VERİ ANALİZİ VE AKADEMİK YAZIM (HAFTA 6-7)
**Hedef:** Simülasyon çıktılarından makale sonuçlarını üretmek.
*   **Adım 1:** DFT ve MD log dosyalarından elde edilen enerji, optik absorbsiyon spektrumları ve bağ enerjisi verilerinin toplanması.
*   **Adım 2:** Verilerin Origin/Python gibi araçlarla profesyonel grafiklere (Şekiller ve Tablolar) dönüştürülmesi.
*   **Adım 3:** Makalenin 'Yöntem (Methodology)', 'Bulgular (Results)' ve 'Tartışma (Discussion)' bölümlerinin yazılması.

## FAZ 4: İKNA VE FON BULMA (PITCH & PUBLISH) (HAFTA 8+)
**Hedef:** Sanal verilerle fiziksel laboratuvar için bütçe/destek sağlamak.
*   **Adım 1:** Yazılan hesaplamalı makalenin hakemli bir dergiye (Q1/Q2 seviyesi) veya saygın bir ön baskı (preprint) sunucusuna gönderilmesi.
*   **Adım 2:** Makaledeki %100 kanıtlanmış "teorik verimlilik" grafiklerinin bir yatırımcı sunumuna (Pitch Deck) eklenmesi.
*   **Adım 3 (Nihai Hedef):** "Bilgisayar ortamında termodinamik ve kuantum düzeyinde bu molekülün %X verimle elektrik üreteceği ve polimer içinde dağılmayacağı kanıtlanmıştır. Şimdi bunu fiziksel olarak sentezlemek için laboratuvar/fon talep ediyoruz" argümanıyla üniversite fonlarına (TÜBİTAK vb.) veya yatırımcılara başvurulması.
