from graphics import *
from Button import *

def main():

    win = GraphWin("Image Example", 600, 600)
    wins = GraphWin("Image Examplëe", 600, 600)
    vins = GraphWin("Image Exámplëe", 600, 600)

    win.setBackground('#550010')
    wins.setBackground('#A77FFF')
    vins.setBackground('#FFB833')
    

    bruh = Image(Point(400, 600), "Bruh.png")
    #bruh.draw(win)

    sun = Image(Point(300, 300), "_;).png")
    #sun.draw(win)

    

if __name__ == "__main__":
    main()
