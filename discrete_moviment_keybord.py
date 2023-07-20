import pygame

pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Discrete keybord movement")

VELOCITY = 10
BLACK = (0, 0, 0)

dragon_image = pygame.image.load("assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH//2
dragon_rect.bottom = WINDOW_HEIGHT

running = True
while running:
  for event in pygame.event.get():
    if event == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_LEFT:
        dragon_rect.x -= VELOCITY
      elif event.key == pygame.K_RIGHT:
        dragon_rect.x += VELOCITY
      elif event.key == pygame.K_UP:
        dragon_rect.y -= VELOCITY
      elif event.key == pygame.K_DOWN:
        dragon_rect.y += VELOCITY
  display_surface.fill(BLACK)
  display_surface.blit(dragon_image, dragon_rect)
  pygame.display.update()
  
pygame.quit()
