import pygame
class player(object):
    def __init__(self, x = 0, y = 0, w = 0, h = 0, hp = 0, mp = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.mp = mp
    
    def moving(self, key, speed=0):
        moved = False
        if key[pygame.K_a]:
            self.x -= speed
            moved = True
        if key[pygame.K_d]:
            self.x += speed
            moved = True
        if key[pygame.K_w]:
            self.y -= speed
            moved = True
        if key[pygame.K_s]:
            self.y += speed
            moved = True 
        return moved
    
    def jumping(self, speed, t0, t, fos, fps):
        jumped = True
        if t+ fos/fps < t0 + 0.1:
            self.y -= speed
        else:
            self.y += speed
            jumped = False
        return jumped

    