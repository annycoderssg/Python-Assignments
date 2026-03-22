# Function accepts parameter as another function  
Add = lambda A, B: A + B

Sub = lambda A, B : A - B

def Marvellous( fptr1, fptr2 ):
    print("Function Type: ", type(fptr1))
    Addition = fptr1(30, 10)
    Subtraction = fptr2(30, 10)

    return Addition, Subtraction

def main():
    Ret = Marvellous(Add, Sub)
    print("Addition is : ", Ret[0])
    print("Subtraction is : ", Ret[1])

if __name__ == "__main__":
    main()