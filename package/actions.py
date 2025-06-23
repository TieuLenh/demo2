import pygame

jumped = False
moved = False

def lim1(pl,w,h):
    if pl.x <= 0:
        pl.x = 0
    if pl.y <= 0:
        pl.y = 0
    if pl.x >= w - pl.w:
        pl.x = w - pl.w
    if pl.y >= h - pl.h:
        pl.y = h - pl.h
    return None



