def q1():
    myList = [1, 3, 7, 7, 9]
    for i in range(len(myList)):
        if myList[i] == 7:
            if myList[i+1] == 7:
                return "True"
    return "False"

def q2():
    output = 0
    sumList = [2, 3, 5, 8, 0, 2, 4, 1]
    for x in range(len(sumList)):
        if sumList[x] == 0:
            break
        else:
            output = output + sumList[x]
    print(output)

def q3():
    theTotal = 0
    soup = [1, 7, 9, 21, 14, 2, 5, 95, 6, 3, 48]
    b = 0 
    while b < len(soup):
        if soup[b] == 2:
            b = b + 1
            break
        else:
            theTotal = theTotal + soup[b]
            b = b + 1

    while b < len(soup):
        if soup[b] == 3:
            b = b + 1
            break
        else:
            b = b + 1

    while b < len(soup):
        theTotal = theTotal + soup[b]
        b = b + 1

    print(theTotal)

def main():
    print(q1())

    q2()

    q3()
    
if __name__ == "__main__":
    main()
