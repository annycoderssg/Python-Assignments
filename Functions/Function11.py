# Function define another function inside it ( Inner Function )
# Using Inner function we can achieve abstraction in python
def Marvellous( intVal1, intVal2 ):
    # Add = lambda A, B: A + B
    def Add( intNo1, intNo2 ):
        return intNo1 + intNo2

    Ans = Add(intVal1, intVal2)

    return Ans
    

def main():
    Ret = Marvellous(10, 11)
    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()