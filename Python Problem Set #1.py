def greeting():
    name = input("Your name is\n")
    print("Hello " + name + "! Nice to meet you!")
    print("Have a good day!")

def isMultiple(x, y):
    if x % y == 0:
        print(str(x) + " is a multiple of " + str(y))
    else:
        print(str(x) + " is not a multiple of " + str(y))

def palindrome(z):
    return z == z[::-1]

#another palindrome method
def palindrometwo():
    answer = input("Write something you think is a palindrome.\n")
    last = len(answer) - 1
    start = answer[0]

    i = 0
    for char in answer:
        if(answer[0+i] != answer[last-i]):
            return False
        i = i + 1
        
    return True
            
#while = repeat until

def main():
    greeting()
    
    isMultiple(10, 5)
    isMultiple(4, 3)

    z = input("Is this a palindrome?\n")
    ans = palindrome(z)
    if ans:
        print("Yes, this is a palindrome.")
    else:
        print("No, this isn't a palindrome.")

    palindrometwo()

if __name__ == "__main__":
    main()


    
    

