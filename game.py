import pygame
from package.color import *
from package.object_game import player
from package.actions import *

pygame.init()
unit = 50

#display setting
dts =  pygame.display.get_desktop_sizes()
dt_w, dt_h = dts[0]
wd_w, wd_h = 20*unit, 12 * unit 
screen = pygame.display.set_mode((wd_w, wd_h), flags=pygame.RESIZABLE)
pygame.display.set_caption('pygameDemo')

#surface
sf1 = pygame.Surface((wd_w, wd_h))
#
turnRigh = pygame.transform.scale(pygame.image.load('character.png'),(unit, unit))
turnleft = pygame.transform.flip(turnRigh, True, False)
char = turnRigh
#player
pl1 = player(x= wd_w/2 - unit/2, y= wd_h/2 - unit/2, w=unit,h=unit, hp = 100, mp = 100)
pl_speed = 5
max_hp = 100
max_mp = 100

# gun
gun = []
gun_x = pl1.w
d = 5 * pl_speed

#key
dict_key = {
    'left': pygame.K_a,
    'right': pygame.K_d,
    'up': pygame.K_w,
    'down': pygame.K_s,
    'jump': pygame.K_SPACE,
    'reset': pygame.K_r,
    'fire': pygame.K_j
}
# jumping
j0 = pl1.y
jable = True

#game loop
clock = pygame.time.Clock()
fps = 90
t = 0 # so giay chay chuong trinh
fos = 0 # khung hinh thu fos + 1 cua 1 giay 
running = True
while running:
    # 1. processing all alrithemtic
    # 1.1 processing event.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == dict_key['jump'] and jable:
                j0 = pl1.y
                jumped = True
                jable = False
            if event.key == dict_key['reset']:
                pl1 = player(x= wd_w/2 - unit/2, y= wd_h/2 - unit/2, w=unit,h=unit, hp = 100, mp = 100)
            if event.key == dict_key['fire']:
                gun.append([pl1.x + gun_x, pl1.y + unit/2, d])
                if d > 0:
                    pl1.x -= 5
                else:
                    pl1.x += 5 
    # 1.2 processing pressing key  
    key = pygame.key.get_pressed()

    if pl1.mp <= 0:
        pl1.mp = 0
    if pl1.hp <= 0:
        pl1 = player()
    if pl1.moving(key=key, dict_key=dict_key, speed=pl_speed):
        moved = True
        pl1.mp -= 0.05
        if key[dict_key['left']]:
            char = turnleft
            gun_x = 0
            d = -5 * pl_speed
        if key[dict_key['right']]:
            char = turnRigh
            gun_x = pl1.w
            d = 5 * pl_speed

    lim1(pl1, sf1.get_width(), sf1.get_height())
    # 1.3 del bullet
    for bullet in range(len(gun)-1,-1,-1):
        if lim2(gun[bullet],wd_w):
            del(gun[bullet])
    # 1.4 
    perc_hp, perc_mp = pl1.w * (pl1.hp/max_hp), pl1.w * (pl1.mp/max_mp)
    if moved == False and pl1.mp/max_mp < 1 :
        pl1.mp += 0.1
    if hurted == False and pl1.hp/max_hp < 1:
        pl1.hp += 1
    moved = False
    hurted = False

    # 2. display
    # 2.1 updating window's size 
    if wd_w != screen.get_width() or wd_h != screen.get_height():
        wd_w, wd_h = pygame.display.get_window_size() 
    screen.blit(sf1,(wd_w//2 - sf1.get_width()//2, wd_h//2 - sf1.get_height()//2,))
    sf1.fill(white)

    
    # 2.2 drawing object
    #pygame.draw.rect(sf1, black, (pl1.x, pl1.y, pl1.w, pl1.h))
    pygame.draw.circle(sf1, green, (sf1.get_width()/2, sf1.get_height()/2), 100, 5)
    pygame.draw.line(sf1, blue, (pl1.x, pl1.y - 6),(pl1.x + perc_mp, pl1.y - 6), 4)
    pygame.draw.line(sf1, red, (pl1.x, pl1.y - 12),(pl1.x + perc_hp, pl1.y - 12), 4)
    pygame.draw.line(sf1, black, (0,sf1.get_height() - 50), (sf1.get_width(),sf1.get_height() - 50), 2)
    sf1.blit(char, (pl1.x, pl1.y))
    for dg in gun:
        pygame.draw.circle(sf1, red, (dg[0], dg[1]), 5)
        dg[0] += dg[2]
    # 3. setting fps
    if pl1.y <= j0 - 100:
        jumped = False
    if jumped == True and pl1.y > j0 - 100:
        pl1.y -= 2 * pl_speed
    pl1.y += pl_speed 
    if lim3(pl1,wd_h - 50):
        jable = True
    pygame.display.update()
    clock.tick(fps)
    fos += 1
    if fos / fps >= 1:
        fos = 0
        t += 1
pygame.quit()
print(gun)