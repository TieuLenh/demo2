class player(object):
    def __init__(self, x = 0, y = 0, w = 0, mhp = 100, mmp= 100, h = 0, hp = 0, mp = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.max_hp = mhp
        self.max_mp = mmp
        self.hp = hp
        self.mp = mp
    
    def get_pcHp(self):
        return self.w * (self.hp/self.max_hp)
    
    def get_pcMp(self):
        return self.w * (self.mp/self.max_mp)
    
    def moving(self, key, dict_key, speed=0):
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
    

    