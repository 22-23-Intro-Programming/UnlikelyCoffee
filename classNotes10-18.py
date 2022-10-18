def add3(z):
    #this is part of add3
    result = z + 3
    return result

def main():
    #print("Hello World!")
    '''print(1234)

    hello = "Hello Class!"
    numStudents = 13
    print(hello + " There are " + str(numStudents) + " of you today")'''

#these are comments wow so cool much fun

    #asking weather and number and stuff
    '''x = input("What is the weather today? ")
    if x == "Sunny":
        print("Wow, what a lovely day.")
    else:
        print(x + "? That's crazy")

    y = input("What is your favorite number? ")
    y = int(y)
    if y > 10:
        print(int(y) / 2)
    else:
        print(int(y) + 1)'''

res = add3(15)
print(res)
print(add3(13))

myString = "Bird Zhang Bao"
firstChar = myString[0]
seventh = myString[6]
#print (firstChar)
#print (seventh)

for char in myString:
    print(char)

print(8 % 3)

#mod is %

if __name__ == "__main__":
    main()
