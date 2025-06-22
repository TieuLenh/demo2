from random import randint
import pygame
class player(object):
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def plr(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)
    
    def moving(self, wd_w = 0, wd_h = 0, step = 0, mode = 'flat'):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.x += step
        if key[pygame.K_a]:
            self.x -= step
        if mode == 'flat':
            if key[pygame.K_s]:
                self.y += step
            if key[pygame.K_w]:
                self.y -= step
        else:
            if key[pygame.K_SPACE]:
                self.y += 4 * step
        return pygame.Rect(self.x, self.y, self.w, self.h)