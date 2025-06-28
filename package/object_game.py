from math import fabs
class bullet:
    def __init__(self, x = 0, y = 0, d = 0, damage = 0):
        self.x = x
        self.y = y
        self.d = d
        self.damage = damage


class player:
    def __init__(self, x = 0, y = 0, w = 0, m_hp = 100, m_mp= 100, h = 0, hp = 0, mp = 0, char = None, bulletLi = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.max_hp = m_hp
        self.max_mp = m_mp
        self.hp = hp if hp <= m_hp else m_hp
        self.mp = mp if hp <= m_mp else m_mp
        self.char = char
        self.bulletLi = bulletLi if bulletLi is not None else []
    
    def get_pcHp(self):
        return self.w * (self.hp/self.max_hp)
    
    def get_pcMp(self):
        return self.w * (self.mp/self.max_mp)
    
    def moving(self, key = None, dict_key = None, speed=0):
        moved = False
        if key[dict_key['left']]:
            self.x -= speed
            moved = True
        if key[dict_key['right']]:
            self.x += speed
            moved = True
        # if key[dict_key['up']]:
        #     self.y -= speed
        #     moved = True
        # if key[dict_key['down']]:
        #     self.y += speed
        #     moved = True 
        return moved
    
    def jumping(self, key = None, dict_key = None, limH = 0, current_h = 0, speed = 0):
        jumed = True
        current_h += speed
        if current_h >= limH:
            jumed = False
        return jumed, limH, current_h

    def append_bullet(self,d = 1):
        self.bulletLi.append(bullet(self.x + self.w//2, self.y + self.h//2 - 4, d))
        self.x -= 5 * d//fabs(d)
        return None
    
    def standard(self):
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        if self.mp > self.max_mp:
            self.mp = self.max_mp
        if self.mp <= 0:
            self.mp = 0
        if self.hp <= 0:
            self = 0
        return None

    def healing(self, key = None, dict_key = None, hhp = 25, hmp = 25):
        if key == dict_key['heal_hp']:
            self.hp += hhp    
        if key == dict_key['heal_mp']:
            self.mp += hmp
        self.standard()
        return None
            
    
    