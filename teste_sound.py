import pygame

pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
WINDOWS_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(WINDOWS_SIZE)
pygame.display.set_caption("Teste de som e musica")

#Define sounds
sound_1 = pygame.mixer.Sound("assets/sound_1.wav")
sound_2 = pygame.mixer.Sound("assets/sound_2.wav")

sound_2.set_volume(.1)

#Play sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()

# Play music
game_music = pygame.mixer.music;
game_music.load("assets/music.wav")
game_music.set_volume(.6)
game_music.play(-1, 0)
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(5000)
game_music.stop()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()
      