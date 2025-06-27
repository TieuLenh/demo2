import pygame
from package.object_game import *
from package.color import *

jumped = False
moved = False
hurted = False

def draw_pl(sf, pl):
    pygame.draw.line(sf, blue, (pl.x, pl.y - 6),(pl.x + pl.get_pcMp(), pl.y - 6), 4)
    pygame.draw.line(sf, red, (pl.x, pl.y - 12),(pl.x + pl.get_pcHp(), pl.y - 12), 4)
    sf.blit(pl.char, (pl.x, pl.y))
    return None

def lim1(pl,w,h):
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
    if pl.y >= h - 100:
        pl.y = h - 100
        touched = True
    return touched

def lim2(dan,w):
    touched = False
    if dan.x <= 0:
        touched = True
    if dan.x >= w :
        touched = True
    return touched

def lim3(pl,h):
    touched = False
    if pl.y + pl.w >= h:
        touched = True
    return touched

def del_bullet(pl,w):
    for i in range(len(pl.bulletLi)-1, -1, -1):
        if lim2(pl.bulletLi[i],w):
            del pl.bulletLi[i]
    return None

def draw_bullet(sf,pl):
    for dg in pl.bulletLi:
        pygame.draw.circle(sf, red, (dg.x, dg.y), 5)
        dg.x += dg.d
    return None

def get_sf_size(sf,w,h):
    if w != sf.get_width() or h != sf.get_height():
        w, h = sf.get_width(), sf.get_height()
        changed = True
    return w, h