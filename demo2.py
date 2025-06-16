import pygame
import demo21 as dm21
pygame.init()

wd_w, wd_h = 600, 350
screen = pygame.display.set_mode((wd_w,wd_h), pygame.RESIZABLE)

running = True
while running:
  sceen.fill(dm21.randCl())
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.display.update()
pygame.quit()
