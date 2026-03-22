# Function define another function inside it and return as its return value ( Inner Function )
def Marvellous(intValue1, intValue2):
    print(Marvellous)               # 0x00000246D23504A0()
    # Add = lambda A, B: A + B
    def Add( intNo1, intNo2 ):      # 0x00000246D2538B80( intNo1, intNo2 )
        print(Add)
        return intNo1 + intNo2      # return 0x00000246D2538B80 

    return Add( intValue1, intValue2 )

def main():
    Ret = Marvellous(20, 15)              # 0x000001FA92F204A0()
    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()