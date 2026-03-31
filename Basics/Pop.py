def Addition( intNo1, intNo2 ):
    Ans = 0
    Ans = intNo1 + intNo2
    return Ans


def Subtraction( intNo1, intNo2 ):
    Ans = 0
    Ans = intNo1 - intNo2
    return Ans

def main():
    intNo1 = int(input("Enter 1st Number: "))
    intNo2 = int(input("Enter 2nd Number: "))

    intResult = Addition( intNo1, intNo2)
    print("Addition is : ", intResult )

    intResult = Subtraction( intNo1, intNo2)
    print("Subtraction is : ", intResult )

if __name__ == "__main__":
    main()