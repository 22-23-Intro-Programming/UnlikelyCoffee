from graphics import *
from Button import *

def main():

    win = GraphWin("PALINDROME", 800, 600)
    win.setBackground("beige")

    Q = Button(win, Point(650, 500), Point(775, 575), "tomato", "EXIT")

    P = Button(win, Point(300, 335), Point(500, 385), "lime", "PALINDROME")

    E = Entry(Point(400, 300), 30)
    E.draw(win)

    T = Text(Point(400, 250), "Type something you think is a palindrome!")
    T.draw(win)

    NY = Text(Point(400, 450), "Is this a PALINDROME?")

    while True:
        m = win.getMouse()

        if Q.isClicked(m):
            break

        if P.isClicked(m):
            pal = E.getText()
            last = len(pal) - 1
            start = pal[0]

            i = 0
            for char in pal:
                if(pal[0+i] != pal[last-i]):
                    NY.setText("No, this is not a palindrome.")
                else:
                    NY.setText("Yes, this is a palindrome!")
                i = i + 1

            NY.undraw()
            NY.draw(win)

    win.close()

if __name__ == "__main__":
    main()
