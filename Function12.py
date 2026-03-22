# Function define another function inside it and return as its return value ( Inner Function )
def Marvellous():
    print(Marvellous)               # 0x000001FA92F204A0()
    # Add = lambda A, B: A + B
    def Add( intNo1, intNo2 ):      # 0x000001FA93128B80( intNo1, intNo2 )
        print(Add)
        return intNo1 + intNo2      # return 0x000001FA93128B80

    return Add

def main():
    Ret = Marvellous()              # 0x000001FA92F204A0()
    Addition = Ret(11, 7)           # 0x000001FA93128B80( intNo1, intNo2 )
    print("Addition is : ", Addition)

if __name__ == "__main__":
    main()