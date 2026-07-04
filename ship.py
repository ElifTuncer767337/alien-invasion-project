import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Gemiye ait tüm davranışları ve görselliği yönetecek sınıf."""

    def __init__(self, ai_game):
        """Gemiyi başlatır."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship-3.png')
        self.rect = self.image.get_rect()
        self.stats = ai_game.stats #Enerjiye ulaşmak için stats ekledik
        self.rect.midbottom = self.screen_rect.midbottom
        
        
        # self.rect tanımlandıktan sonra self.x oluşturulmalı
        self.x = float(self.rect.x)

        # Hareket bayrakları
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Gemiyi güncel konumunda ekrana çizer."""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Konumu günceller (Sınır kontrolü dahil)."""
        # Sağa git ve ekranın sağ kenarını geçme:
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.stats.energy >0:
             self.x += self.settings.ship_speed
             self.stats.energy -= 0.15 #Hareket enerji harcar
            
        # Sola git ve ekranın sol kenarını (0) geçme:
        if self.moving_left and self.rect.left > 0:
            if self.stats.energy >0:
             self.x -= self.settings.ship_speed
             self.stats.energy -= 0.15
             #Sola hareket : Enerji > 0 ise git
         #Enerji yenilenmesi: Hareket etmiyorsa dolsun.    
        if not self.moving_right and not self.moving_left:
           if self.stats.energy < self.stats.max_energy:
              self.stats.energy += 0.6

        self.rect.x = self.x
        
    def center_ship(self):
       '''Gemiyi ekranın alt merkezine yerleştirir'''
       self.rect.midbottom = self.screen_rect.midbottom
       self.x = float (self.rect.x)