import pygame.font #metinleri ekrana çizmek için lazım

class Button:
    def __init__(self, ai_game, msg):
        '''Buton özelliklerini başlatır'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        #Butonun boyutlarını ve özelliklerini ayarla
        self.width, self.height = 200, 50
        self.button_color = (213, 82, 163)
        self.text_color = (255, 255,255) #beyaz yazı
        self.font = pygame.font.SysFont(None, 48) #varsayılan font 48 punto
        #Butonun rect nesnesini oluştur ve ekranın merkezine yerleştir
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #Buton mesajını bir kez hatırla
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # Mesajı işlenmiş bir görsele dönüştür ve butonda merkezler.
        
        self.msg_image = self.font.render (msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''Boş bir buton çiz ve üzerine mesajı yaz'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        