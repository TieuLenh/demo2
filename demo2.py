import pygame
import demo21 as dm21
pygame.init()

wd_w, wd_h = 600, 350
unit = 30
screen = pygame.display.set_mode((wd_w,wd_h), pygame.RESIZABLE)

pl_rect = pygame.Rect(1,1,unit,unit)
pl_move = 1
mx = 1
my = 1
clock = pygame.time.Clock()
fps = 90
running = True
while running:
  screen.fill(dm21.black)
  if wd_w != screen.get_width() or wd_h != screen.get_height():
    wd_w, wd_h = pygame.display.get_window_size()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and pl_move < 5:
        pl_move += 1
      if event.key == pygame.K_DOWN and pl_move > 1:
        pl_move -= 1
      if event.key == pygame.K_s:
        fps = int(input('Nhap fps: '))
      if event.key == pygame.K_r:
        fps = 90
      
  key = pygame.key.get_pressed()
  if key[pygame.K_w]:
    pl_rect.y -= pl_move
  if key[pygame.K_s]:
    pl_rect.y += pl_move
  if key[pygame.K_a]:
    pl_rect.x -= pl_move
  if key[pygame.K_d]:
    pl_rect.x += pl_move
  if pl_rect.x <= 0: 
    mx = 1
  if pl_rect.x + pl_rect.w >= wd_w:
    mx = -1
  if pl_rect.y <= 0: 
    my = 1
  if pl_rect.y + pl_rect.h >= wd_h:
    my = -1
  pl_rect.x += mx * pl_move
  pl_rect.y += my * pl_move
  pygame.draw.rect(screen, dm21.randCl(), pl_rect, 2)
  pygame.display.update()
  clock.tick(fps)
pygame.quit()