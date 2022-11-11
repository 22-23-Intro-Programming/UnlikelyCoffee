from graphics import*
from Button import*

def main():
    win = GraphWin("Character Creator", 800, 800)
    Face = Oval(Point(75, 100), Point(475, 700))
    Face.draw(win)
#eyes button
    eyes1 = Button(win, Point(550, 100), Point(650, 175), "tomato", "Big Eyes")
    eyes2 = Button(win, Point(675, 100), Point(775, 175), "tomato", "Small Eyes")
#nose button
    nose1 = Button(win, Point(550, 200), Point(650, 275), "orange", "Big Nose")
    nose2 = Button(win, Point(675, 200), Point(775, 275), "orange", "Small Nose")
#ears button
    ears1 = Button(win, Point(550, 300), Point(650, 375), "gold", "Round Ears")
    ears2 = Button(win, Point(675, 300), Point(775, 375), "gold", "Block Ears")
#mouth button
    mouth1 = Button(win, Point(550, 400), Point(650, 475), "lightgreen", "Big Mouth")
    mouth2 = Button(win, Point(675, 400), Point(775, 475), "lightgreen", "Small Mouth")
#hair button
    mole = Button(win, Point(550, 500), Point(650, 575), "cyan", "Mole")
    buttChin = Button(win, Point(675, 500), Point(775, 575), "cyan", "Butt Chin")
#eyes
    bigEye1 = Oval(Point(125, 200), Point(250, 300))
    bigEye2 = Oval(Point(300, 200), Point(425, 300))
    smallEye1 = Oval(Point(175, 200), Point(225, 275))
    smallEye2 = Oval(Point(325, 200), Point(375, 275))
#nose
    bigNose = Polygon(Point(275, 275), Point(225, 400), Point(325, 400))
    smallNose = Polygon(Point(275, 320), Point(250, 375), Point(300, 375))
#ears
    roundEar1 = Oval(Point(470, 300), Point(535, 450))
    roundEar2 = Oval(Point(80, 300), Point(15, 450))
    squareEar1 = Rectangle(Point(475, 325), Point(535, 475))
    squareEar2 = Rectangle(Point(75, 325), Point(15, 475))
#mouth
    bigMouth = Polygon(Point(115, 380), Point(280, 450), Point(435, 380), Point(280, 575))
    smallMouth = Line(Point(200, 525), Point(360, 515))
#mole
    Mole = Point(150, 500)
#buttchin
    chin1 = Circle(Point(225, 675), 50)
    chin2 = Circle(Point(325, 675), 50)
#reset
    RButton = Button(win, Point(550, 600), Point(775, 650), "magenta", "Reset!")
#quit
    QButton = Button(win, Point(550, 675), Point(775, 725), "red", "Quit!")
#lists
    eyes = [bigEye1, bigEye2, smallEye1, smallEye2]
    nose = [bigNose, smallNose]
    ears = [roundEar1, roundEar2, squareEar1, squareEar2]
    mouth = [bigMouth, smallMouth]
    moles = [Mole]
    butt = [chin1, chin2]
    
#while loop
    while True:
        m = win.getMouse()
        
        if eyes1.isClicked(m):
            for e in eyes:
                e.undraw()
            bigEye1.draw(win)
            bigEye2.draw(win)

        elif eyes2.isClicked(m):
            for e in eyes:
                e.undraw()
            smallEye1.draw(win)
            smallEye2.draw(win)

        elif nose1.isClicked(m):
            for n in nose:
                n.undraw()
            bigNose.draw(win)

        elif nose2.isClicked(m):
            for n in nose:
                n.undraw()
            smallNose.draw(win)

        elif ears1.isClicked(m):
            for a in ears:
                a.undraw()
            roundEar1.draw(win)
            roundEar2.draw(win)

        elif ears2.isClicked(m):
            for a in ears:
                a.undraw()
            squareEar1.draw(win)
            squareEar2.draw(win)

        elif mouth1.isClicked(m):
            for o in mouth:
                o.undraw()
            bigMouth.draw(win)

        elif mouth2.isClicked(m):
            for o in mouth:
                o.undraw()
            smallMouth.draw(win)

        elif mole.isClicked(m):
            for p in moles:
                p.undraw()
            Mole.draw(win)

        elif buttChin.isClicked(m):
            for b in butt:
                b.undraw()
            chin1.draw(win)
            chin2.draw(win)

        elif RButton.isClicked(m):
            for e in eyes:
                e.undraw()
            for n in nose:
                n.undraw()
            for a in ears:
                a.undraw()
            for o in mouth:
                o.undraw()
            for p in moles:
                p.undraw()
            for b in butt:
                b.undraw()

        elif QButton.isClicked(m):
            break

        elif win.getMouse():
            print(m)
        
    win.close()

if __name__ == "__main__":
    main()
