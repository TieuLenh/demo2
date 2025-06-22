import pygame
from package.color import *
from object_game import player

pygame.init()
unit = 30

#display setting
wd_w, wd_h = 12 * unit, 20*unit
screen = pygame.display.set_mode((wd_w, wd_h), flags=pygame.RESIZABLE)
#surface
sf1 = pygame.Surface((wd_w, wd_h))
#player
pl1 = player(w=unit,h=unit)
pl1r = pl1.plr()
pl_step = 1
#game loop
clock = pygame.time.Clock()
fps = 90
running = True
while running:
  if wd_w != screen.get_width() or wd_h != screen.get_height():
     wd_w, wd_h = pygame.display.get_window_size()
  
  #processing surface
  screen.blit(sf1,(wd_w//2 - sf1.get_width()//2,0))
  sf1.fill(green) 
  #processing event.
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
  pl1r = player.moving(pl1)
  pygame.draw.rect(surface=sf1, color=red, rect=pl1r)
  #setting fps and display
  pygame.display.update()
  clock.tick(fps)
pygame.quit()