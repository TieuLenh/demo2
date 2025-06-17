from random import randint

class monster:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def set_monster(wd_w, wd_h, n):
    monster_list = [] 
    for i in range(n):
        monster_list.append(monster(randint(0, wd_w), randint(0, wd_h)))
    return monster_list


def del_monster(monster_list, index):
    del monster_list[index]
    return monster_list