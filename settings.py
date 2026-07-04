class Settings:
    """Oyunun tüm ayarlarını depolayacak sınıf."""

    def __init__(self):
        """Oyunun statik ayarlarını başlatır."""
        # Ekran ayarları
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 35) 
        # self.ship_speed = 6
        # self.bullet_speed = 8
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (142, 33, 76)
        self.bullets_allowed  = 10
        self.fleet_drop_speed = 10
        self.ship_limit = 3 # Oyuncunun kaç canı olacağını belirler
        self.speedup_scale = 1.1 # oyun her seviyede 10% hızlanır.
        self.score_scale = 1.5 
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings (self):
        '''Oyun boyunca değişen ayarları sıfırlar'''
        self.ship_speed = 5.0
        self.bullet_speed = 7.0 
        self.alien_speed = 3.5 
        self.alien_points = 50 #her uzaylı başlangıçta 50 puan
        self.current_score_multiplier = 1.0

        #fleet_direction 1 sağa, -1 sola hareket ettirir.
        self.fleet_direction = 1
        

    def increase_speed (self):
        '''Hız ayarlarını arttırır'''
        self.ship_speed  *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.current_score_multiplier *= self.score_scale
        