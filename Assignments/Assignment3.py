#Write a program which contains one function named as Add(). Which accept two numbers from user and return addition of that two numbers

def Add( intValue1, intValue2 ):
    intAddition = intValue1 + intValue2 
    return intAddition

def main():
    intNumber1 = 0
    intNumber2 = 0
    intNumber1 = int(input("Enter 1st Number : "))
    intNumber2 = int(input("Enter 2nd Number : "))
    
    intResult = Add( intNumber1, intNumber2 )
    print("Addition of two numbers :", intResult )

if __name__ == "__main__":
    main()