import pygame
from color import *
from monster import *

pygame.init()

unit = 30
wd_w, wd_h = 600, 350
center_x = wd_w // 2
center_y = wd_h // 2
screen = pygame.display.set_mode((wd_w,wd_h), pygame.RESIZABLE)
pygame.display.set_caption('game demo2')

pl_rect = pygame.Rect(1,1,unit,unit)
pl_move = 1
mx = 1
my = 1
cl = red
mouse_hiden = True

monster_list = set_monster(wd_w, wd_h, 10)

clock = pygame.time.Clock()
fps = 90
running = True
while running:
  screen.fill(black)
  if wd_w != screen.get_width() or wd_h != screen.get_height():
    wd_w, wd_h = pygame.display.get_window_size()
  mouse_x, mouse_y = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_h:
        mouse_hiden = not mouse_hiden
        pygame.mouse.set_pos((pl_rect.x + pl_rect.w // 2, pl_rect.y + pl_rect.h // 2  ))
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        pass


  if 0 < mouse_x <= wd_w and 0 < mouse_y <= wd_h:
    if mouse_hiden:
      pygame.mouse.set_visible(False) # hide mouse cursor
      pl_rect.x = mouse_x - unit/2
      pl_rect.y = mouse_y - unit/2
    else:
      pygame.mouse.set_visible(True) # show mouse cursor
  pygame.draw.rect(screen, cl, pl_rect)
  pygame.draw.circle(screen, black, (pl_rect.x + pl_rect.w/2, pl_rect.y + pl_rect.h/2),unit/2)
  for m in reversed(range(len(monster_list))):
    pygame.draw.circle(screen, green, (monster_list[m].x, monster_list[m].y), unit/2)
    if pl_rect.collidepoint(monster_list[m].x, monster_list[m].y):
      del_monster(monster_list,m)
  if len(monster_list) == 0:
    monster_list = set_monster(wd_w, wd_h, 10)

  pygame.display.update()
  clock.tick(fps)
pygame.quit()