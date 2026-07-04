import sys
import pygame
import time #ekranı durdurmak için zaman lazım


from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien 
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

class AlienInvasion:
    """Oyun varlıklarını ve davranışlarını yöneten genel sınıf."""

    def __init__(self):
        """Oyunu başlatır ve oyun kaynaklarını oluşturur."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        
        pygame.display.set_caption("Alien Invasion")
        
 
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
       
        
        self.clock = pygame.time.Clock()
        
       
        
        self.stats = GameStats(self)
        self.stats.game_active = False
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "Play")
        
        #Mermi lazer sesi
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound('sounds/laser_sound.wav')
        pygame.mixer.music.load('sounds/game_music.mp3')
        pygame.mixer.music.set_volume(0.2)
        
    def run_game(self):
        """Oyun için ana döngüyü başlatır."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets() 
                self._update_aliens() 

            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """Klavye ve fare olaylarına yanıt verir."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: #fareye basıldığında
             mouse_pos = pygame.mouse.get_pos()
             self._check_play_button(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button (self, mouse_pos):
        '''Oyuncu play butonuna tıkladığında yeni oyunu başlatır'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            
        
        

            #İstatistikleri sıfırla
            self.stats.reset_stats()
            self.sb.prep_level()
            self.stats.game_active = True
            self.sb.prep_ships()

            #fare imlecini gizle
            pygame.mouse.set_visible(False)

            #Müzik kontrolü
            pygame.mixer.music.play(-1) #-1 parametresi müziğin sürekli dönmesini sağlar

            #Ekranı temizle
            self.aliens.empty()
            self.bullets.empty()

            #yeni filo oluştur ve gemiyi ortala
            self._create_fleet()
            self.ship.center_ship()
    
    def _check_high_score(self):
        '''yeni bir rekor olup olmadığını kontrol et.'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.sb.prep_high_score()

            #Rekoru anlık olarak dosyaya yazdır
            with open ('high_score.txt', 'w') as f:
                f.write(str(self.stats.high_score))
                 
    def _create_fleet(self):
        '''Uzaylı filosunu oluşturur'''
        #İlk uzaylıyı oluştur ve gruba ekle
        # Bir uzaylı oluştur ve bir sıraya kaç uzaylı sığacağını hesapla.
        #Boşluk, bir uzaylı genişliğine eşit olacak.

        alien = Alien (self)
        alien_width , alien_height = alien.rect.size 

        #Ekranın sağında ve solunda birer uzaylı genişliği kadar boşluk bırakıyoruz.
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Dikey boşluk hesabı 
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -  (3 * alien_height)- ship_height)

        number_rows = available_space_y // (2 * alien_height)

        # Uzaylı filosunu oluştur
        for row_number in range(number_rows): 
           for alien_number in range(number_aliens_x):
            self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        '''Bir uzaylı oluşturur ve onu sıraya yerleştirir'''
        alien = Alien(self)
        if row_number == 0:
            current_type = 'yellow'
        elif row_number == 1:
            current_type = 'purple'
        else:
           current_type = 'normal'
        
        alien = Alien(self, alien_type= current_type)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2  *alien_width * alien_number
        alien.rect.x = alien.x
        # alien.x = float(alien.rect.x)
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_keydown_events(self, event):
        """Tuşa basma olaylarına yanıt verir."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q: # Oyundan hızlı çıkış için 'q' tuşu
            sys.exit()

    def _check_keyup_events(self, event):
        """Tuş bırakma olaylarına yanıt verir."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''Yeni bir mermi oluştur ve enerji varsa fırlat'''
        #Ateş etmek için en az 5 enerji gereksin 
        if self.stats.energy >= 5:
           if len(self.bullets) < self.settings.bullets_allowed:
              new_bullet = Bullet(self)
              self.bullets.add(new_bullet)
              self.stats.energy -= 3 #Her atış 3 enerji harcar

         #Mermi oluşturulduğu an sesi çal
           self.laser_sound.play()

    def _update_bullets(self):
        """Mermilerin konumunu günceller ve eski mermileri siler."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
    #Mermi uzaylı çarpışmalarına tepki verir.
     collisions = pygame.sprite.groupcollide  (self.bullets, self.aliens, True, True)
        
     if not self.aliens:
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed() # filo bitti hızı arttır.
        self.stats.level +=1
        self.sb.prep_level()

     if collisions:
        #Her çarpışma için puan ekle
        for aliens_list in collisions.values():
            for alien in aliens_list:
                self.stats.score += alien.points  
           
        self.sb.prep_score() #skor tablosunu güncelle 
        
        self._check_high_score()

    def _update_aliens(self):
        '''Filodakai tüm
         uzaylıların konumunu günceller'''
        self._check_fleet_edges() # önce kenarları kontrol et
        self.aliens.update() # sonra hareket ettir.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print('EYVAH! Gemi vuruldu')
            self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):
        '''Gemiye bir uzaylı çarptığında yapılacaklar'''
         #canı azalt ve oyunu sıfırla
        self.stats.ships_left -= 1 #kalan gemi sayısını 1 azalt
        self.sb.prep_ships()

        if self.stats.ships_left > 0:
         self.aliens.empty()
         self.bullets.empty() #ekrandaki tüm uzaylıları ve mermileri temizle

        # yeni bir filo oluştur ve gemiyi merkeze al
         self._create_fleet()
         self.ship.center_ship()

        #oyuncunun ne olduğunu anlaması için kısa bir ara ver
         time.sleep(0.5)
        else:
            self.stats.game_active = False #canlar bitti
            pygame.mouse.set_visible(True)
            #Müziği durdur
            pygame.mixer.music.stop()
            

    def _check_aliens_bottom(self):
        '''Herhangi bir uzaylınun ekranın altına ulaşıp ulaşmadığını kontrol eder'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #gemi vurulmuş gibi aynı işlemleri yap
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        '''Herhangi bir uzaylı kenara ulaştıysa uygun tepkiyi verir.'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break 
    def _change_fleet_direction(self):
        '''Tüm filoyu aşağı indirir ve yönünü değiştirir.'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1    

    def _update_screen(self):
        """Ekrandaki görüntüleri günceller ve yeni ekrana geçer."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
          bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()

        if not self.stats.game_active:
         self.play_button.draw_button()
         

        pygame.display.flip()

if __name__ == '__main__':
    # Oyun örneğini oluştur ve çalıştır.
    ai = AlienInvasion()
    ai.run_game()