# Function accepts parameter and call another function from it    
Add = lambda A, B: A + B

def Sub(A, B):
    return A-B

def Marvellous( intValue1, intValue2 ):
    Ans = Add(intValue1, intValue2)
    print("Addition is : ", Ans)

    Ans = Sub(intValue1, intValue2)
    print("Subtraction is : ", Ans)

def main():
    Marvellous(20, 5)

    Marvellous(35, 10)

if __name__ == "__main__":
    main()