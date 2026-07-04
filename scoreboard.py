#Enerji barını görselleştiren fonksiyonu ekliyoruz.
from pygame.sprite import Group
from ship import Ship
import pygame.font

class Scoreboard:
    '''Skor bilgilerini raporlayan sınıftır'''

    def __init__(self, ai_game):
        '''Skor tutma özniteliklerini başlat'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game
       

        #Skor bilgileri için yazı tipi ayarları
        self.text_color =  (202, 97,128)
        self.font = pygame.font.SysFont("consolas", 48)
        self.prep_images()
     
       
    def prep_images(self):
        '''Tüm görsel metotları burada toplayalım '''
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Skoru işlenmiş bir resme dönüştür."""
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Yüksek skoru işlenmiş bir resme dönüştür."""
        high_score_str = "{:,}".format(round(self.stats.high_score, -1))
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Seviyeyi işlenmiş bir resme dönüştür."""
        level_str = f'Lvl{self.stats.level}'
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''Kaç tane gemi kaldığını gösterir'''
        self.ships = Group()
        start_x = 240 #enerji barının bittiği yerden başlaması için (20 başlangıç + 200 genişlik + 20 boşluk)
        self.image = pygame.image.load('images/ship-3.png')
        new_width, new_height = 30, 30
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.image = pygame.transform.scale(self.image, (new_width, new_height))
            ship.rect =ship.image.get_rect()
            ship.rect.x = start_x + ship_number * (ship.rect.width + 10)
            ship.rect.y =20  
            self.ships.add(ship)

    def draw_energy_bar(self):
        '''Enerji barını ekrana çizer'''
        bar_width = 200
        bar_height = 25
        x,y = 20,20 #position = (sol üst köşe)
        
    #Barın dış çevresi
        pygame.draw.rect(self.screen, (142, 33, 76), (x, y, bar_width, bar_height),5)

    #Doluluk oranını hesapla
        fill = (self.stats.energy / self.stats.max_energy) * (bar_width - 6)

    #Enerji durumuna göre renk seçimi (kritikse kırmızı, değilse yeşil olsun)
        color = (0,255,0) if self.stats.energy > 25 else (255,0,0)

    #İçteki dolu barı çiz
        if fill > 0:
            pygame.draw.rect(self.screen, color, (x + 3, y + 3, fill, bar_height - 6))

    def show_score(self):
        '''Skorları ve enerji barını ekrana çiz.'''
   
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        #Enerji barı her zaman görünsün (veya şartına göre)
        self.draw_energy_bar()
        self.ships.draw(self.screen)
    
    
