def factorial(x):
    y = 1
    for i in range(1, x + 1):
        y = y * i

    print ("The factorial of " + str(x) + " is ",end="")
    print (y)

def doubleIt():
    word = input("Write the phrase you want doubled:\n")
    output = ""
    for char in word:
        output = output + char * 2
    print(output)

def camelCase():
    file = input("Please enter filename:\n")
    split = file.split(" ")
    camelcase = split[0] + "".join(word.title() for word in split[1:])
    camelcase = camelcase.replace("/", "-")
    camelcase = camelcase.replace("_", "")
    print(camelcase)
    
def main():
    factorial(1)
    factorial(12)
    factorial(6)

    doubleIt()

    camelCase()


if __name__ == "__main__":
    main()
