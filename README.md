# 🛸 Geliştirdiğim Alien Invasion Projem

Bu projede, Eric Matthes'in *Python Crash Course* kitabında yer alan temel "Alien Invasion" oyununu baz aldım. Ancak amacım sadece hazır bir kodu kopyalamak değil, üzerine kendi tasarım fikirlerimi ve yazılım çözümlerimi ekleyerek projeyi tamamen özgün ve profesyonel bir arcade oyununa dönüştürmekti.

---

## 🎯 Projemin Vizyonu
Kitaptaki orijinal oyunda var olan sınırsız hareket özgürlüğünü değiştirerek oyuna bir **hayatta kalma ve kaynak yönetimi** mekaniği eklemek istedim. Oyuncunun sadece rastgele ateş ettiği değil; enerjisini ve stratejisini yönettiği, görsel ve işitsel açıdan daha tatmin edici bir deneyim sunmayı hedefledim.

---

## 🛠️ Kullandığım Teknolojiler
* **Dil:** Python
* **Kütüphane:** Pygame (Görselleştirme, Ses ve Sprite Yönetimi için tercih ettim)
* **Veri Depolama:** Dosya tabanlı kalıcı veri yönetimi (`.txt`)

---

## ✨ Kitaptan Farklı Olarak Eklediğim Özellikler
* **Enerji ve Yakıt Yönetimi:** Geminin hareket etmesini ve ateş etmesini enerji tüketimine bağladım. Enerjinin dolması için geminin durması gerekiyor. Böylece oyuncuyu "ateş gücü kazanmak için savunmasız kalmayı göze alma" stratejisine zorladım.
* **Dinamik Düşman Hiyerarşisi:** Orijinal projedeki monotonluğu kırmak adına `alien_type` parametresi ekledim. Farklı görsellere sahip; 50, 75 ve 100 puanlık Sarı, Mor ve Normal uzaylı türleriyle oyuna bir hedef önceliği stratejisi kattım.
* **Kalıcı Skor Sistemi (`high_score.txt`):** En yüksek skorun oyundan çıkılsa bile hafızada kalmasını sağladım. Ayrıca `try-except` bloğu kullanarak dosya silinse dahi oyunun çökmesini engelleyerek programın dayanıklılığını artırdım.
* **Görsel Tasarım ve Kullanıcı Arayüzü (UI):** Enerji seviyesi %25'in altına düştüğünde yeşilden kırmızıya dönen anlık bir enerji barı tasarladım. Giriş ekranı için de estetik bir pembe/beyaz kontrastına sahip, fare tıklamalarını algılayan etkileşimli bir buton geliştirdim.

---

## ⚙️ Öne Çıkan Teknik Detaylar & Optimizasyonlarım
* **OOP ve Mimari Yapı:** Nesne Yönelimli Programlama prensiplerine sadık kalarak `Ship`, `Alien`, `Bullet` gibi varlıkları ayrı sınıflarda modüller halinde kurguladım. `Sprite` sınıfından miras alarak mermi-uzaylı çarpışmalarını çok daha verimli yönettim.
* **Bellek Yönetimi:** Oyunun uzun süreli kullanımlarda RAM'i şişirmemesi için ekran sınırlarını aşan her mermiyi anında listeden temizleyen bir optimizasyon kurdum.
* **Zorluk Eğrisi:** Matematiksel bir modelleme ile oyunun her seviyede %10 zorlaşmasını sağladım.

---

## 📁 Proje Klasör Yapım

```text
alien-invasion-project/
├── alien_invasion.py     # Ana oyun döngüm ve kontrol merkezim
├── ship.py               # Oyuncu gemisi özellikleri ve enerji yönetimi
├── alien.py              # Düşman türlerim ve hiyerarşik yapı
├── bullet.py             # Mermi fiziği ve nesne temizliği
├── settings.py           # Oyunun tüm teknik ve dinamik ayarları
├── game_stats.py         # Skor, enerji ve durum verileri
├── scoreboard.py         # Arayüz ve görsel bilgilendirme panelim
├── button.py             # Pembe temalı etkileşimli giriş butonum
├── high_score.txt        # Kalıcı olarak saklanan rekor skor verisi
├── images/               # Görsel varlıklar (Gemi ve Uzaylı resimleri)
└── sounds/               # Ses efektleri ve arka plan müzikleri
 
