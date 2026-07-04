import pygame
from  pygame.sprite import  Sprite

class Alien(Sprite):
    '''Filodaki tek bir uzaylıyı temsil eden sınıf'''

    def __init__(self, ai_game, alien_type = 'normal'): #tür parametresi ekledik
        '''Uzaylıyı başlatır ve başlangıç konumunu belirler'''
        super().__init__()  #inheritance
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.type = alien_type
       
        # Uzaylı görselini yükle ve rect özelliğini al 
       
        self.image = pygame.image.load('images/alien-image.png')
        

        # Her yeni uzaylıyı ekranın sol üst köşesine yakın bir yerde başlat 
        # Sol ve üstten birer genişik / yükseklik kadar boşluk bırakıyoruz.

        #alien türlerine göre resim ve puan belirle
        if self.type == 'yellow':
             self.image = pygame.image.load('images/yellow-alien-image.png')
             self.points = 100
        elif self.type == 'purple':
             self.image =pygame.image.load('images/purple-alien-image.png')
             self.points = 75
        else:
          self.image = pygame.image.load('images/alien-image.png')
          self.points = 50

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Uzaylının tam yatay konumunu sakla
        self.x = float(self.rect.x)

    def update(self):
            '''Uzaylıyı sağa ve sola hareket ettirir'''
            speed = self.settings.alien_speed
            self.x +=(speed * self.settings.fleet_direction)
            self.rect.x =self.x

          
    def check_edges(self):
         '''Uzaylı ekran kenarına ulaştıysa True döndürür'''
         screen_rect = self.screen.get_rect()
         return self.rect.right >= screen_rect.right or self.rect.left <= 0
      