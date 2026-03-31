# Function accepts multiple parameter and return multiple parameter    
def Marvellous( intValue1, intValue2 ):
    intAddition = intValue1 + intValue2
    intSubtraction = intValue1 - intValue2
    intMultiplication = intValue1 * intValue2
    fltDivision = intValue1 / intValue2

    return intAddition,intSubtraction,intMultiplication,fltDivision

def main():
    Ret1, Ret2, Ret3, Ret4 = Marvellous(30, 10)
    print("Addition is: ", Ret1)
    print("Subtraction is: ", Ret2)
    print("Multiplication is: ", Ret3)
    print("Division is: ", Ret4)

    Ret1, Ret2, Ret3, Ret4 = Marvellous(15, 5)
    print("Addition is: ", Ret1)
    print("Subtraction is: ", Ret2)
    print("Multiplication is: ", Ret3)
    print("Division is: ", Ret4)

if __name__ == "__main__":
    main()