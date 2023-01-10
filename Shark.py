import random
from graphics import*

class Shark:
    def __init__(self, win, x, y):
        self.x = x
        self.y = y

        j = random.randint(0, 19)
        i = random.randint(0, 19)
        
        self.img = Image(Point(x+i*20, y+j*20), "shark.png")
        self.img.draw(win)
        
        
