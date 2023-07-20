import pygame, sys
from pygame.locals import QUIT

pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Blitting images!')

#Define Colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
BLACK = (0, 0, 0)

# See all available fonts
fonts = pygame.font.get_fonts()
#Load font from asset
system_font = pygame.font.SysFont("Calibri", 64)
custom_font = pygame.font.Font("assets/AttackGraffiti.ttf", 32)

system_text = system_font.render("Dragons Rule!", True, GREEN, DARK_GREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render("Move the dragon", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

running = True
while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
  DISPLAYSURF.blit(system_text, system_text_rect)
  DISPLAYSURF.blit(custom_text, custom_text_rect)
  pygame.display.update()
pygame.quit()
sys.exit()