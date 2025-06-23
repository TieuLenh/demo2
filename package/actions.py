import pygame

jumped = False
moved = False
hurted = False

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
    if pl.y >= h - pl.h:
        pl.y = h - pl.h
        touched = True
    return touched

def lim2(dan,w):
    touched = False
    if dan[0] <= 0:
        touched = True
    if dan[0] >= w :
        touched = True
    return touched



