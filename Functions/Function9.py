# Function accepts parameter as another function  
Add = lambda A, B: A + B            # 0x00000149B48004A0 

Sub = lambda A, B : A - B           # 0x00000149B49B8CC0

def Marvellous( fptr1, fptr2 ):
    print("Function Type: ", type(fptr1))
    print(fptr1, fptr2)
    Adition = fptr1(30, 10)         # Adition = 0x00000149B48004A0(30, 10)
    Subtraction = fptr2(30, 10)     # Subtraction = 0x00000149B49B8CC0(30, 10)

    return Adition,Subtraction

def main():
    Ret = Marvellous(Add, Sub)      # Marvellous( 0x00000149B48004A0, 0x00000149B49B8CC0 )
    print("Addition is : ", Ret[0])
    print("Subtraction is : ", Ret[1])

if __name__ == "__main__":
    main()