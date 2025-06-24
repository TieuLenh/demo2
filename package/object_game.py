class player(object):
    def __init__(self, x = 0, y = 0, w = 0, h = 0, hp = 0, mp = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.mp = mp
    
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
    

    