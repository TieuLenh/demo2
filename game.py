import pygame
from package.color import *
from package.object_game import player

pygame.init()
unit = 30

#display setting
dts =  pygame.display.get_desktop_sizes()
dt_w, dt_h = dts[0]
wd_w, wd_h = 12 * unit, 20*unit
screen = pygame.display.set_mode((wd_w, wd_h), flags=pygame.RESIZABLE)
#surface
sf1 = pygame.Surface((wd_w, wd_h))
#player
pl1 = player(w=unit,h=unit)
pl1r = pl1.plr()
print(pl1r)
pl_step = 2

#limited moving
def lim1(plr,w,h):
  if plr.x <= 0:
    plr.x = 0
  if plr.y <= 0:
    plr.y = 0

#game loop
clock = pygame.time.Clock()
fps = 90
running = True
while running:
  if wd_w != screen.get_width() or wd_h != screen.get_height():
     wd_w, wd_h = pygame.display.get_window_size()
  
  #processing surface
  screen.blit(sf1,(wd_w//2 - sf1.get_width()//2,0))
  #screen.blit(sf1,(0,0))
  sf1.fill(white) 
  #processing event.
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
  key = pygame.key.get_pressed()
  if key[pygame.K_w]:
    pl1r.y -= pl_step
  if key[pygame.K_s]:
    pl1r.y += pl_step
  if key[pygame.K_a]:
    pl1r.x -= pl_step
  if key[pygame.K_d]:
    pl1r.x += pl_step
  lim1(pl1r, wd_w, wd_h)
  pygame.draw.rect(surface=sf1, color=red, rect=pl1r)
  #setting fps and display
  pygame.display.update()
  clock.tick(fps)
pygame.quit()