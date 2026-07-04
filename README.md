1- Proje Yapısı ve Dosya Organizasyonu 

alien-invasion-project/ 
│ 
├── alien_invasion.py      # Ana oyun döngüsü ve kontrol merkezi 
├── ship.py                
# Oyuncu gemisi özellikleri 
├── alien.py               
# Düşman türleri ve hareket mantığı 
├── bullet.py              
# Mermi fiziği ve yönetimi 
├── settings.py            
# Oyunun tüm teknik ayarları 
├── game_stats.py          
# Skor ve enerji verileri 
├── scoreboard.py          
# Arayüz ve görsel bilgilendirme 
├── button.py              
# Giriş ekranı butonu 
├── high_score.txt         
│ 
├── images/                
# Kaydedilen en yüksek skor verisi 
# Görsel varlıklar klasörü 
│   ├── ship-3.png 
│   ├── alien-image.png 
│   ├── yellow-alien-image.png 
│   └── purple-alien-image.png 
│ 
└── sounds/                
# Ses efektleri ve müzik klasörü 
├── laser_sound.wav 
└── game_music.mp3 

2-Projenin Vizyonu 

Bu projede, Python Crash Course kitabındaki temel "Alien Invasion" oyununu baz 
alarak, üzerine kendi tasarım fikirlerimi ve yazılım çözümlerimi eklemeyi hedefledim. 
Amacım, sadece oyunun bir kopyasını yapmak değil; oyuncunun kaynak yönetimi yaptığı, 
farklı stratejiler geliştirdiği ve işitsel-görsel olarak daha tatmin edici bir deneyim yaşadığı 
bir arcade oyunu ortaya koymaktı. Kitaptaki orijinal yapıdan farklı olarak; yakıt sistemi, 
dinamik düşman hiyerarşisi ve gelişmiş bir kullanıcı arayüzü ekleyerek projeyi 
profesyonel bir seviyeye taşıdım. 

3-Nesne Yönelimli Programlama (OOP) ve Mimari 
Yapı 

Projeyi kurgularken Nesne Yönelimli Programlama prensiplerine sadık kalarak 
modüler bir yapı oluşturdum. 
• Modülerlik: Ship, Alien, Bullet gibi varlıkları ayrı sınıflarda tanımlayarak kodun 
sürdürülebilirliğini sağladım. 
 
• Kalıtım (Inheritance): Bullet ve Alien sınıflarında Pygame’in Sprite sınıfını 
miras alarak, grup halindeki nesneleri tek bir komutla yönetme kolaylığına eriştim. 
Bu yapı sayesinde mermi-uzaylı çarpışmalarını verimli bir şekilde kontrol 
edebiliyorum. 
 
4-Enerji ve Yakıt Yönetimi 
def update(self): 
    # Sağa git ve enerji harca 
    if self.moving_right and self.rect.right < 
self.screen_rect.right: 
        if self.stats.energy > 0: 
            self.x += self.settings.ship_speed 
         self.stats.energy -= 0.15  
             
    # Sola git ve enerji harca 
    if self.moving_left and self.rect.left > 0: 
    if self.stats.energy > 0: 
            self.x -= self.settings.ship_speed 
            self.stats.energy -= 0.15 
             
    # Hareket edilmiyorsa pasif enerji dolumu 
    if not self.moving_right and not self.moving_left: 
        if self.stats.energy < self.stats.max_energy: 
            self.stats.energy += 0.6 
 
Burada kurduğum mantıkla geminin hareketini enerjiye bağladım. 0.15 birimlik 
azalma, oyuncunun sürekli manevra yapmasını kısıtlarken; 0.6 birimlik dolma hızı, 
oyuncuyu stratejik olarak durmaya ve enerji biriktirmeye zorluyor. Bu, Eric Matthes'in 
projesindeki sınırsız hareket özgürlüğünden tamamen ayrılan, benim eklediğim bir 
hayatta kalma mekanizmasıdır. 
• Enerji Tüketimi: Gemim hareket ederken (self.stats.energy -= 0.15) ve 
mermi fırlatırken (self.stats.energy -= 3) enerji tüketiyor. Bu sayede 
oyuncunun rastgele ateş etmesini değil, hedef odaklı oynamasını sağladım. 
• Stratejik Dinlenme: Enerji dolumu için geminin durması gerekiyor. Bu mekanikle 
oyuncuya şunu hissettirmek istedim: "Ateş gücünü kazanmak için savunmasız 
kalmayı göze almalısın." 

5-Enerji Barının Görselleştirilmesi (UI Tasarımı) 

#Enerji durumuna göre renk seçimi(kritikse kırmızı, değilse 
yeşil) 
color = (0,255,0) if self.stats.energy > 25 else (255,0,0) 
#İçteki dolu barı enerjinin oranına göre çiz 
if fill > 0: pygame.draw.rect(self.screen, color, (x + 3, y + 
3, fill, bar_height - 6)) 
Kullanıcıya enerjiyi sadece sayı olarak göstermek yerine, görsel bir bar tasarımı 
yaptım. Özellikle enerjinin %25 altına indiğinde rengin yeşilden kırmızıya dönmesi, 
oyuncuya o anki tehlikeyi hissettiren dinamik bir geri bildirim  mekanizmasıdır. 

6-Dinamik Düşman Hiyerarşisi 

Orijinal projede tüm uzaylılar aynı tipte ve aynı puandadır. Ben bu monotonluğu 
kırmak için Alien sınıfına alien_type parametresini ekledim. 
if self.type == 'yellow': 
     self.image = pygame.image.load('images/yellow-alien
image.png') 
     self.points = 100 
elif self.type == 'purple': 
     self.image = pygame.image.load('images/purple-alien
image.png') 
     self.points = 75 
else: 
     self.image = pygame.image.load('images/alien-image.png') 
     self.points = 50 
 
 
• Sarı Uzaylılar: Filosunun en üstünde yer alır ve 100 puan verir. Ulaşılması en zor 
oldukları için ödüllerini en yüksek tuttum. 
 
• Mor ve Normal Uzaylılar: 75 ve 50 puanlık değerlerle oyunun puan dengesini 
oluşturdum. Bu özellik sayesinde oyuncuya, yüksek puanlı hedeflere öncelik 
verme stratejisini aşılamayı amaçladım. 
 
7-Zorluk ve Ses Yönetimi 
self.speedup_scale = 1.1 
self.laser_sound 
=pygame.mixer.Sound('sounds/laser_sound.wav') 
pygame.mixer.music.play(-1) 
 
Oyunun her seviyede %10 zorlaşmasını sağlayan bir matematiksel modelleme 
kurdum. Ses efektleri ve sürekli dönen arka plan müziği ile oyuncunun oyun dünyasına 
tam olarak girmesini sağladım. 

8- Kalıcı Veri 

Yönergedeki "Kalıcı Veri" maddesini karşılamak için high_score.txt sistemini 
kurdum. 

#Skorun dosyaya yazılması 

with open('high_score.txt', 'w') as f: 
f.write(str(self.stats.high_score)) 
• Dosya İşlemleri: En yüksek skoru bir dosyadan okuyup, rekor kırıldığında bu 
dosyayı güncelleyen bir yapı kurdum. 
• Hata Yönetimi: try-except bloğu kullanarak, dosya silinse bile oyunun 
çökmeden 0 skoruyla devam etmesini sağladım; bu da programın dayanıklılığını 
(robustness) artırdı. 

9- Giriş Ekranı ve Buton Tasarımı 

Oyunun doğrudan başlaması yerine oyuncuyu karşılayan bir arayüz sunmak 
amacıyla Button sınıfını geliştirdim. Bu bölüm, oyunun "pasif" bir döngüden oyuncu 
kontrolüne geçtiği ilk etkileşim noktasıdır. 
self.rect.center = self.screen_rect.center 
#Merkezi Konumlandırma: Bu kod satırı ile butonun her   
çözünürlükte ekranın tam ortasında durmasını sağladım. 
def init(self, ai_game, msg):  

# Buton boyutları ve estetik renk tercihleri (Pembe/Beyaz 
kontrastı) 

self.width, self.height = 200, 50 
self.button_color = (213, 82, 163) 
self.text_color = (255, 255, 255) 

# Butonu ekranın merkezine sabitleme 
self.rect = pygame.Rect(0, 0, self.width, self.height) 
self.rect.center = self.screen_rect.center 
• Metin İşleme: Pygame'in metinleri doğrudan çizememesi nedeniyle _prep_msg 
metodunu kullanarak "Play" yazısını bir görsele dönüştürdüm ve butonun üzerine 
yerleştirdim. 
Aslında bu butonu sadece 'Play' yazan bir kutu olsun diye değil, oyunun daha 
profesyonel bir başlangıcı olsun diye ekledim. Kitaptaki orijinal yapının üzerine bu özelliği 
katarken beni en çok heyecanlandıran şey, sadece ekrana bir resim çizmek değil, farenin 
o kutuya tıkladığını koda anlatabilmek oldu. Kullanıcının yaptığı bir hareketin yazılım 
tarafından algılanıp oyunu başlatması, bir programın dış dünyaya nasıl tepki verdiğini 
kavramam açısından gerçekten çok öğretici bir deneyimdi. 

10- Bellek Yönetimi ve Performans Optimizasyonu 

Oyunun uzun süreli kullanımlarda yavaşlamaması için bellek yönetimine 
odaklandım. 
• Nesne Temizliği: Ekran sınırlarını aşan her bir mermiyi 
self.bullets.remove(bullet) komutuyla listeden sildim. 
• Neden? Bu sayede Python'ın listesinde binlerce gereksiz mermi nesnesinin 
birikmesini önleyerek, RAM kullanımını minimumda tuttum. 

11- Sonuç ve Kişisel Kazanımlarım 

‘Alien Invasion’ projesi benim için sadece bir ödev değil, bir yazılımın mutfağını 
görme fırsatıydı. Kod yazmanın ötesinde; kaynakları doğru yönetmek ve sistem 
optimizasyonu gibi konularda kafa yormak ufkumu çok açtı. Temel aldığım kaynak 
projenin üzerine kendi hayal gücümü ekleyerek özgün bir mekanik oluşturmak, bir 
yazılımcı adayı olarak kendime güvenimi tazeledi. Bu süreçte öğrendiğim her detay, 
gelecekteki projelerim için harika bir temel oluşturdu.
