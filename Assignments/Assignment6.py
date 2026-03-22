#Write a program which accept number from user and check whether that number is positive or negative or zero.
def main():
    intNumber1 = 0
    intNumber1 = int(input("Enter Number : "))
    if( intNumber1 == 0 ):
        print("Zero")
    elif( intNumber1 > 0 ):
        print("Positive Number")
    elif( intNumber1 < 0 ):
        print("Negative Number")

if __name__ == "__main__":
    main()