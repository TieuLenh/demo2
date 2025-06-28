from package.main import *

pygame.init()
unit = 50

#display setting
dts =  pygame.display.get_desktop_sizes()
dt_w, dt_h = dts[0]
wd_w, wd_h = 20*unit, 12 * unit 
screen = pygame.display.set_mode((wd_w, wd_h), flags=pygame.RESIZABLE)
pygame.display.set_caption('pygameDemo')

#surface
view_point = pygame.Surface((wd_w,wd_h))
#
turnRigh = pygame.transform.scale(pygame.image.load('character.png'),(unit, unit))
turnleft = pygame.transform.flip(turnRigh, True, False)


#player
pl1 = player(x= wd_w/2 - unit/2, y= wd_h/2 - unit/2, w=unit,h=unit, hp = 100, mp = 100)
pl1.char = turnRigh
pl_speed = 5


# gun

d = 5 * pl_speed

#key
dict_key = {
    'left': pygame.K_a,
    'right': pygame.K_d,
    'jump': pygame.K_k,
    'down': pygame.K_s,
    'reset': pygame.K_r,
    'fire': pygame.K_j,
    'heal_hp': pygame.K_u,
    'heal_mp': pygame.K_i
}

# jumping
j0 = wd_h
jable = True

# function
# display showwing





#game loop
clock = pygame.time.Clock()
fps = 90
t = 0 # so giay chay chuong trinh
fos = 0 # khung hinh thu fos + 1 cua 1 giay 
running = True
while running:

    wd_w, wd_h, view_point = get_sf_size(screen, view_point, wd_w, wd_h)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == dict_key['jump'] and jable:
                j0 = pl1.y
                jumped = True
                jable = False
            if event.key == dict_key['fire']:
                pl1.append_bullet(d)
            pl1.healing(event.key, dict_key)
    
    # 1.2 processing pressing key  
    key = pygame.key.get_pressed()

    if pl1.moving(key=key, dict_key=dict_key, speed=pl_speed):
        moved = True
        pl1.mp -= 0.05
        if key[dict_key['left']]:
            pl1.char = turnleft
            d = -5 * pl_speed
        if key[dict_key['right']]:
            pl1.char = turnRigh
            d = 5 * pl_speed

    lim_view(pl1, view_point.get_width(), view_point.get_height())
    
    moved = False


    # 2. display
    # 2.1 updating window's size 
    

    screen.blit(view_point, (0, 0))
    view_point.fill(white)

    pl1.draw(view_point)
    pl1.draw_bullet(view_point)
    pl1.del_bullet(view_point.get_width())

    if pl1.y <= j0 - 100:
        jumped = False
    if jumped == True and pl1.y > j0 - 100:
        pl1.y -= 2 * pl_speed
    pl1.y += pl_speed

    if lim3(pl1, view_point.get_height() - 50):
        jable = True

    pygame.display.update()
    clock.tick(fps)
    fos += 1
    if fos / fps >= 1:
        fos = 0
        t += 1
pygame.quit()
print(pl1.bulletLi)

