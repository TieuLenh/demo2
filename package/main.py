import pygame
from package.object_game import *
from package.color import *
from package.game_map import *



jumped = False
mva = True
moved = False
hurted = False

list_map = list(map(pygame.Rect, (gm for gm in Map1)))

def get_sf_size(sf = None, view_point = None, w = 0, h = 0):
    if w != sf.get_width() or h != sf.get_height():
        w, h =  sf.get_width(), sf.get_height()
        view_point = pygame.Surface((w, h))
    return w, h, view_point

def draw(self, sf = None):
    if self.mp > 0:
        pygame.draw.line(sf, blue, (self.x, self.y - 6),(self.x + self.get_pcMp(), self.y - 6), 4)
    if self.hp > 0:
        pygame.draw.line(sf, red, (self.x, self.y - 12),(self.x + self.get_pcHp(), self.y - 12), 4)
    sf.blit(self.char, (self.x, self.y))
    return None
player.draw = draw

def rect(self):
    return pygame.Rect(self.x, self.y, self.w, self.h)
player.rect = rect

def lim_view(pl, w = 0, h = 0):
    touched = False
    if pl.x <= 0:
        pl.x = 0
        touched = True
    if pl.y <= 0:
        pl.y = 0
        touched = True
    if pl.x >= w - pl.w:
        pl.x = w - pl.w
        touched = True
    if pl.y >= h - pl.h:
        pl.y = h - pl.h 
        touched = True
    return touched

def lim2(dan, w = 0):
    touched = False
    if dan.x <= -w:
        touched = True
    if dan.x >= w :
        touched = True
    return touched

def lim3(pl, h = 0):
    touched = False
    if pl.y + pl.w >= h:
        touched = True
    return touched

def del_bullet(self, w = 0):
    for i in range(len(self.bulletLi)-1, -1, -1):
        if lim2(self.bulletLi[i], self.x + w):
            del self.bulletLi[i]
    return None
player.del_bullet = del_bullet

def draw_bullet(self, sf = None):
    for bul in self.bulletLi:
        pygame.draw.circle(sf, red, (bul.x, bul.y), 4)
        bul.x += bul.d
    return None
player.draw_bullet = draw_bullet

def pl_jump(pl, key, key_dict):
    jumped, limH, current_h = pl.jumping(key, key_dict, )
    pass

def draw_map(sf, map0):
    for gm in map0:
        pygame.draw.rect(sf, randCl(), gm, 5)

def movable(self, map0):
    if self.rect().colliderect(gm for gm in map0):
        return False
    return True
player.movable = movable

def save_data(file = 'data.txt', data = None):
    f = open(file, mode='w')
    for k in data.keys():
        f.write(k + ': ' + str(data[k]) + '\n')
    f.close()
    return None

def get_data(file = 'data.txt'):
    f = open(file, mode='r')
    dataIn = f.readlines()
    dataOut = dict()
    for i in range(len(dataIn)):
        dataIn[i] = dataIn[i].split(': ')
        dataIn[i][1] = int(dataIn[i][1].replace('\n', ''))
    f.close()
    for i in range(len(dataIn)):
        dataOut[dataIn[i][0]] = dataIn[i][1]
    return dataOut
data = get_data()

