# Function accepts parameter and call another function from it & return multiple values    
Add = lambda A, B: A + B

Sub = lambda A, B : A - B

def Marvellous( intValue1, intValue2 ):
    Adition = Add(intValue1, intValue2)
    Subtraction = Sub(intValue1, intValue2)

    return Adition,Subtraction

def main():
    Ret = Marvellous(20, 5)
    print("Addition is : ", Ret[0])
    print("Subtraction is : ", Ret[1])

    Ret = Marvellous(35, 10)
    print("Addition is : ", Ret[0])
    print("Subtraction is : ", Ret[1])

if __name__ == "__main__":
    main()