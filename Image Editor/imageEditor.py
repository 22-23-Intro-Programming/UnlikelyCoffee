from graphics import*
from Button import*

def darken(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            newColor = color_rgb(abs(r - 25), abs(g - 25), abs(b - 25))
            img.setPixel(i, j, newColor)

def lighten(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            newColor = color_rgb(int(r + float(255 - r) * 0.2), int(g + float(255 - g) * 0.2), int(b + float(255 - b) * 0.2))
            img.setPixel(i, j, newColor)

def grayscale(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            avg = r + g + b
            avg = avg // 3
            newColor = color_rgb(avg, avg, avg)
            img.setPixel(i, j, newColor)

def contrast(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            avg = r + b + g
            avg = avg //3

            if avg <= 127:
                if r > 25:
                    r = r - 25
                else:
                    r == 0
                if g > 25:
                    g = g - 25
                else:
                    g == 0
                if b > 25:
                    b = b - 25
                else: b == 0
            else:
                if r < 230:
                    r = r + 25
                else:
                    r == 255
                if g < 230:
                    g = g + 25
                else:
                    g == 255
                if b < 230:
                    b = b + 25
                else:
                    b == 255
                
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)

def main():

    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("#E5E5ED")

    I = Image(Point(300, 300), "dog.png")
    I.draw(win)

    dark = Button(win, Point(600, 75), Point(725, 150), "tomato", "Darken!")
    light = Button(win, Point(600, 175), Point(725, 250), "gold", "Lighten!")
    gray = Button(win, Point(600, 275), Point(725, 350), "lime", "Grayscale!")
    cont = Button(win, Point(600, 375), Point(725, 450), "cyan", "Contrast!")

    Q = Button(win, Point(575, 525), Point(750, 575), "red", "EXIT")

    while True:
        m = win.getMouse()
        
        if dark.isClicked(m):
            darken(I)
            
        if light.isClicked(m):
            lighten(I)

        if gray.isClicked(m):
            grayscale(I)

        if cont.isClicked(m):
            contrast(I)
        
        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
