import pygame
from color import * 

pygame.init()
unit = 30

#display setting
wd_w, wd_h = 12 * unit, 20*unit
screen = pygame.display.set_mode((wd_w, wd_h), flags=pygame.RESIZABLE)
#player

#game loop
clock = pygame.time.Clock()
fps = 90
running = True
while running:
    
    #processing event.
    for event in pygame.event.get():
        pass
    
    pygame.draw
    #setting fps and display
    pygame.display.update()
    clock.tick(fps)
pygame.quit()