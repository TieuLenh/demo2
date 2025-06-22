import pygame
from package.color import *
from package.object_game import player

pygame.init()
unit = 30

#display setting
dts =  pygame.display.get_desktop_sizes()
dt_w, dt_h = dts[0]
wd_w, wd_h = 20*unit, 12 * unit 
screen = pygame.display.set_mode((wd_w, wd_h), flags=pygame.RESIZABLE)
#surface
sf1 = pygame.Surface((wd_w, wd_h))
#player
pl1 = player(w=unit,h=unit)
pl1r = pl1.plr()
print(pl1r)
pl_speed = 5

#player's moving
def lim1(plr,w,h):
  if plr.x <= 0:
    plr.x = 0
  if plr.y <= 0:
    plr.y = 0
  if plr.x >= w - plr.w:
    plr.x = w - plr.w
  if plr.y >= h - plr.h:
    plr.y = h - plr.h

#game loop
clock = pygame.time.Clock()
fps = 90
t = 0
fos = t/fps
jump = 0
k = 0
running = True
while running:
  if wd_w != screen.get_width() or wd_h != screen.get_height():
     wd_w, wd_h = pygame.display.get_window_size()
  
  #processing surface
  screen.blit(sf1,(wd_w//2 - sf1.get_width()//2, wd_h//2 - sf1.get_height()//2,))
  sf1.fill(white) 
  #processing event.
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and jump == 0 and k == 0:
          jump = 1
          k = fps/2
  if fos % 2 == 0:
    key = pygame.key.get_pressed()
    if jump == 1:
      pl1r.y -= pl_speed
      k -= 1
    else:
      pl1r.y += pl_speed
    if k == 0:
      jump = 0
    if key[pygame.K_a]:
      pl1r.x -= pl_speed
    if key[pygame.K_d]:
      pl1r.x += pl_speed
  lim1(pl1r, sf1.get_width(), sf1.get_height())
  pygame.draw.rect(surface=sf1, color=red, rect=pl1r)
  #setting fps and display
  pygame.display.update()
  clock.tick(fps)
  
  t += 1000000000
  if fos / fps >= 1:
    fos = 0
    fos += 1
pygame.quit()