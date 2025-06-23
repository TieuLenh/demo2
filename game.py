import pygame
from package.color import *
from package.object_game import player
from package.actions import *

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
pl1 = player(x=0, y=wd_w - unit, w=unit,h=unit)
pl_speed = 5


#game loop
clock = pygame.time.Clock()
fps = 90 
t = 0 # so giay chay chuong trinh
fos = 0 # khung hinh thu fos + 1 cua 1 giay 
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
            if event.key == pygame.K_SPACE:
                t0 = t
                jumped = True
    
    if jumped:
        pl1.jumping(10, t0, t, fos,fps)
    #key pressing 
    key = pygame.key.get_pressed()
    pl1.moving(key=key, speed=pl_speed)
    lim1(pl1, sf1.get_width(), sf1.get_height())
    pygame.draw.rect(surface=sf1, color=black, rect=(pl1.x, pl1.y, pl1.w, pl1.h))

    #setting fps and display
    pygame.display.update()
    clock.tick(fps)
    fos += 1
    if fos / fps >= 1:
        fos = 0
        t += 1
pygame.quit()