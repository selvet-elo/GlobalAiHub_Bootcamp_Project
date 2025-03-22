# :bullettrain_front: Sürücüsüz Metro Simülasyonu 
### *Rota Optimizasyonu* 

Bu proje, bir metro ağında iki istasyon arasında en hızlı ve en az aktarmalı rotaları bulmak için geliştirilmiş bir simülasyondur. Proje, iki temel algoritma kullanır: Breadth-First Search (BFS) ve *A (A-Star)**.

-BFS Algoritması: En az aktarmalı rotayı bulmak için kullanılır. Bu algoritma, başlangıç istasyonundan başlayarak tüm komşu istasyonları tek tek inceler ve hedef istasyona ulaşana kadar geniş bir arama yapar. Aktarma sayısını en aza indirmeyi hedefler.

-A Algoritması*: En hızlı rotayı bulmak için kullanılır. Bu algoritma, hem gerçek maliyeti (duraklar arasındaki süreler) hem de tahmini maliyeti (heuristik fonksiyonu) dikkate alarak en optimize rotayı belirler. Heuristik fonksiyonu, duraklar arasındaki süreler ve aktarma maliyetlerini göz önünde bulundurur.

Proje Amacı

Projenin temel amacı, bir metro ağında:

   - En az aktarmalı rotayı bulmak (BFS algoritması ile),
   - En hızlı rotayı bulmak (A* algoritması ile),
   - Gerçek dünya problemlerini algoritmik düşünce ile çözmek

## Kullanılan Teknolojiler ve Kütüphaneler

Projede aşağıdaki Python kütüphaneleri kullanılmıştır:

   - `collections.deque` : Çift uçlu kuyruk yapısı sağlayarak BFS algoritmasında istasyonları işleme almak için kullanıldı. FIFO (First In, First Out) mantığında çalışır.
   - `heapq` : Öncelik kuyruğu yapısını kullanarak A\* algoritmasında en kısa süreli rotayı belirlemek için kullanıldı. En küçük maliyetli düğümü hızlı bir şekilde seçmeyi sağlar.
   - `defaultdict` : Varsayılan değerler içeren bir sözlük yapısı sağlayarak metro hattı verilerini organize etmek için kullanıldı. Hatlara istasyonları kolayca ekleyebilmek için tercih edildi.
   - `typing` : Kodun okunabilirliğini ve sürdürülebilirliğini artırmak amacıyla tip ipuçları (type hints) eklendi. Böylece parametrelerin ve dönüş değerlerinin türleri daha net hale getirildi.


## Algoritmaların Çalışma Mantığı

### BFS Algoritması (En Az Aktarmalı Rota)

BFS algoritması, **katman katman** ilerleyerek başlangıç istasyonundan hedef istasyona **en az durak değeri** ile ulaşan rotayı bulur.

   1. **Kuyruk** (queue) yapısı oluşturulur.
   2. Başlangıç istasyonu kuyruğa eklenir.
   3. Her istasyon için **komşular kontrol edilir** ve ziyaret edilmemiş olanlar kuyruğa eklenir.
   4. Hedef istasyona ulaşıldığında en kısa rota döndürülür.

### A\* Algoritması (En Hızlı Rota)

A\* algoritması, en hızlı rotayı bulmak için **heuristic (sezgisel) fonksiyon** kullanır.

   1. **Öncelik kuyruğu** oluşturulur (heapq kullanılır).
   2. Başlangıç istasyonu kuyruğa eklenir.
   3. İstasyonlar **süre değerine göre** kuyruktan çekilir.
   4. Her istasyonun komşuları ziyaret edilerek toplam yol süreleri hesaplanır.
   5. ***Heuristic fonksiyon***, istasyonlar arasındaki geçiş sürelerini ve hat değişikliklerini göz önünde bulundurarak en hızlı rotayı belirlemeye yardımcı olur.
        - Eğer iki istasyon aynı hatta bulunuyorsa, ek bir aktarma süresi gerektirmediğinden heuristic değeri 0 olarak atanır. Ancak, farklı bir hat üzerinden gitmek gerekiyorsa, ortalama bir aktarma süresi eklenerek yolculuk süresinin daha gerçekçi hesaplanması sağlanır.
   7. Hedefe ulaşıldığında **en hızlı rota ve toplam süre** döndürülür.

## Kurulum ve Kullanım

1. **Proje dosyasını klonlayın:**
   ```sh
   git clone https://github.com/Selvet/MetroSimulation.git
   cd MetroSimulation
   ```
2. **Python kodunu çalıştırın:**
   ```sh
   python SelvetElifDemirel_MetroSimulation.py
   ```

## Test Senaryoları

Kod aşağıdaki senaryolar ile test edilmiştir ve sonuçları proje_cıktısı.jpg dosyası olarak da bulunmaktadır:

=== Test Senaryoları ===

1. AŞTİ'den OSB'ye:
   - En az aktarmalı rota: AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
   - En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB

2. Batıkent'ten Keçiören'e:
   - En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
   - En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören

3. Keçiören'den AŞTİ'ye:
   - En az aktarmalı rota: Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
   - En hızlı rota (19 dakika): Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ

4. Ulus'tan Keçiören'e:
   - En az aktarmalı rota: Ulus -> Demetevler -> Demetevler -> Gar -> Keçiören
   - En hızlı rota (20 dakika): Ulus -> Kızılay -> Sıhhiye -> Gar -> Gar -> Keçiören

5. Sıhhiye'den OSB'ye:
   - En az aktarmalı rota: Sıhhiye -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
   - En hızlı rota (23 dakika): Sıhhiye -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB

Kod çalıştırıldığında da test senaryolarının doğru çıktıları gösterilecektir.

## Projeyi Geliştirme Fikirleri

- **Görselleştirme:** Metro ağını grafiksel olarak göstermek için `networkx` ve `matplotlib` kullanılabilir.
- **Gerçek Harita Entegrasyonu:** Google Maps veya OpenStreetMap verileri ile metro hattını gerçek zamanlı entegrasyon yaparak çalışmak.
- **Dinamik Veri Kullanımı:** Metro yoğunluğuna ve sefer saatlerine göre **dinamik** rota planlaması yapma.




