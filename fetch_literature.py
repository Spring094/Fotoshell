import urllib.request
import json
import time

print("\n[*] FOTOSHELL AR-GE: Literatur Taramasi Baslatildi (Biyomimetik Zn-Porfirin)")
print("[*] PubMed ve EuropePMC Veritabanlarina API Istegi Gonderiliyor...\n")
time.sleep(1)

# EuropePMC API kullanarak "Zinc Porphyrin DSSC" aramasi
url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Zinc%20Porphyrin%22%20AND%20%22DSSC%22&format=json&resultType=core"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        
        results = data.get('resultList', {}).get('result', [])
        print(f"[+] Toplam {data.get('hitCount')} bilimsel makale bulundu. Ilk 5 tanesi analiz ediliyor:\n")
        
        for idx, paper in enumerate(results[:5]):
            title = paper.get('title', 'Bilinmeyen Baslik')
            journal = paper.get('journalTitle', 'Bilinmeyen Dergi')
            year = paper.get('pubYear', 'Tarih Yok')
            doi = paper.get('doi', 'DOI Yok')
            print(f"[{idx+1}] BASLIK: {title}")
            print(f"    DERGI: {journal} ({year})")
            print(f"    DOI/LINK: https://doi.org/{doi}")
            print("-" * 60)
            time.sleep(0.5)
            
        print("\n[*] Bu veriler (Z_Indirilen_Kaynaklar_ve_PDFler) klasorune referans olarak kaydediliyor.")
        
        # Referanslari dosyaya yazdiralim (Sadece log olmasin, gercekten kaydetsin)
        with open("/data/data/com.termux/files/home/.openclaw/workspace/Fotoshell_Makale_Projesi/Z_Indirilen_Kaynaklar_ve_PDFler/References.txt", "w") as f:
            f.write("FOTOSHELL PROJESI - ILK LITERATUR REFERANSLARI\n")
            f.write("="*50 + "\n")
            for paper in results[:10]:
                f.write(f"- {paper.get('title')} ({paper.get('pubYear')}), DOI: {paper.get('doi')}\n")

except Exception as e:
    print(f"[-] Hata olustu: {e}")
