from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
        
        
        
    """BFS algoritması kullanarak en az aktarmalı rotayı bulma"""
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
       
        #Başlangıç ve hedef istasyonların varlığını kontrol etmek için. 
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        # Başlangıç ve hedef listeleri oluşturuyoruz
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        # BFS algoritması için kuyruk oluşturma:
        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edildi = {baslangic} # Bir ziyaret edildi sözlüğü oluşturuyoruz.
        
        while kuyruk:
            mevcut_istasyon, istasyon_listesi = kuyruk.popleft()   
            
            # Eğer hedeflenen istasyona ulaşıldıysa istasyon listesini döndür.    
            if mevcut_istasyon == hedef:
                return istasyon_listesi
            
            # Ziyaret edilen istasyonları takip et.
            ziyaret_edildi.add(mevcut_istasyon)    

            # Komşu istasyonları bulma döngüsü.
            for komsu,_ in mevcut_istasyon.komsular: 
                if komsu not in ziyaret_edildi:
                    kuyruk.append((komsu, istasyon_listesi + [komsu]))
                
        return None
    
            
    """A* algoritması kullanarak en hızlı rotayı bulma"""
    
    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
       
        # Başlangıç ve hedef istasyonların varlığını kontrol ediyoruz.
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        #başlangıç ve hedef istasyonlar.
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        #Sezgisel fonksiyon
        #Heuristik değer için aktarma sürelerine göre ortalama bir değer aldık. Gerçek değerden küçük veya eşit olacak şekilde
        def heuristic(istasyon: Istasyon)-> int:
            if istasyon.hat==hedef.hat:
                return 0  #Eğer aynı hattaysa heuristik değer 0
            else:
                return 2  #Aktarma yapılırsa heuristik değer +2.
            
            
        # Öncelik kuyruğu oluşturuyoruz.
        # #(f, g, baslangic id, mevcut_istasyon (node), istasyon_listesi )
        pq=[(0,0, id(baslangic), baslangic, [baslangic])] 
        
        # Ziyaret edilen istasyonlar
        ziyaret_edildi = set()
        
        while pq:
            
            # Kuyruktaki en düşük f(n) değeri olan istasyonu çıkarıyoruz, yani en hızlı rota 
            _, toplam_sure, _, mevcut_istasyon, istasyon_listesi= heapq.heappop(pq)
            
            # Hedefe ulaşıldığında istasyon_listesi ve toplam_süreyi döndür
            if mevcut_istasyon == hedef:
                return (istasyon_listesi, toplam_sure)
            
            # Eğer istasyon daha önce ziyaret edildiyse geç 
            if mevcut_istasyon in ziyaret_edildi:
                continue   
           
            ziyaret_edildi.add(mevcut_istasyon)  #Ziyaret edildi listesini güncelle
            
            # Komşu istasyonları dolaşma döngüsü, yeni rota ve süreyi hesaplamak için.
            for komsu, sure in mevcut_istasyon.komsular:
                if komsu not in ziyaret_edildi:
                    
                    yeni_toplam_sure= toplam_sure + sure  # Yeni toplam süre, g(n)
                   
                    yeni_f =  yeni_toplam_sure + heuristic(komsu)   # Yeni maliyet (f(n))
                    
                    # Yeni süre ve rotayı öncelik kuyruğuna ekliyoruz.
                    heapq.heappush(pq, (yeni_f, yeni_toplam_sure, id(komsu), komsu, istasyon_listesi + [komsu] ))
        
        # Eğer rota bulunamazsa;            
        return None
                    

    
            
            

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 
        
    # Benim eklediğim farklı senaryolar:    
    # Senaryo 4: Ulus'tan Keçiören'e 
    print("\n4. Ulus'tan Keçiören'e:")
    rota = metro.en_az_aktarma_bul("K2", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("K2", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))   
        
        
    # Senaryo 5: Sıhhiye'den OSB'ye    
    print("\n5. Sıhhiye'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M3", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M3", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        
    
    
