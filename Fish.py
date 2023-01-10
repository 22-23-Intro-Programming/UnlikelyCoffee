import random
from graphics import*

class Fish:
    def __init__(self, win, x, y):
        self.x = x
        self.y = y

        j = random.randint(0, 19)
        i = random.randint(0, 19)
        
        self.img = Image(Point(x+i*20, y+j*20), "fish.png")
        self.img.draw(win)

    def move(self):
        possibleMoves = []
        above = self.y - 1
        below = self.y + 1
        right = self.x + 1
        left = self.x - 1
        
        addMoves = [[right, self.y], [left, self.y],
                             [self.x, above], [self.x, below]]
        for move in addMoves:
            if (-1 < move[0] < 8) and (-1 < move[1] < 8):
                possibleMoves.append(move)
        return possibleMoves
        
