from graphics import*
from Button import*
from random import*
from Shark import*
from Fish import*

def run():
    pass

def move():
    
    pass

def start():
    pass

def main():

    win = GraphWin("Shark Simulator", 600, 600)

    shark = Shark(win, 110, 110)

    fish = Fish(win, 110, 110)
    fish2 = Fish(win, 110, 110)
    fish3 = Fish(win, 110, 110)
    
    for i in range(21):
        
        L = Line(Point(100,100+i*20), Point(500,100+i*20))
        L.draw(win)

    for j in range(21):

        L2 = Line(Point(100+j*20,100), Point(100+j*20,500))
        L2.draw(win)

    Q = Button(win, Point(240, 525), Point(360, 575), "red", "EXIT")
    run = Button(win, Point(15, 15), Point(120, 50), "tomato", "Run!")
    move = Button(win, Point(250, 25), Point(350, 75), "Green", "Move!")
    reset = Button(win, Point(295, 15), Point(400, 50), "Blue", "Reset!")
    
    while True:
        m = win.getMouse()

        #if run.isClicked(m):
            #run()
        
        #if move.isClicked(m):
            #move()

        #if reset.isClicked(m):
            #start()

        if win.getMouse():
            print(m)
        
        if Q.isClicked(m):
            break
        
        
    win.close()
        
if __name__ == "__main__":
    main()
