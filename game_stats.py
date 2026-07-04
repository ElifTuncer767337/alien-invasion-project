class GameStats:
  '''Alien invasion için istatistikleri takip et'''

  def __init__(self,ai_game):
    '''İstatistikleri başlat'''
    self.settings  = ai_game.settings
    self.reset_stats()
    self.game_active = False
    #Oyunun yüksek skorunu sıfırlar
    #self.high_score = 0

    # en yüksek skoru dosyadan oku 
    try:
       with open('high_score.txt', 'r') as f:
         self.high_score = int(f.read())
    except FileNotFoundError:
      self.high_score = 0 # Dosya yoksa rekor 0' dır.
    

  def reset_stats(self):
    '''Oyun sırasında değişebilecek istatistikleri sıfırla'''
    self.ships_left = self.settings.ship_limit
    self.score = 0
    self.level = 1
    

    # Enerji sistemi
    self.max_energy = 100
    self.energy = self.max_energy

