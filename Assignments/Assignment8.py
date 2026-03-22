#Write a program which accept number from user and print that number of "*" on screen.

def main():
    intNumber = 0
    intNumber = int(input("Enter a Number : "))
    strOutPut = ""
    for i in range(0, intNumber, 1):
        print("*", end=" ")
    
    print(strOutPut)

if __name__ == "__main__":
    main()