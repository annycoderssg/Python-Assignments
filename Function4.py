# Function accepts parameter and return parameter    
def Marvellous( intValue1, intValue2 ):
    if( intValue1 > intValue2 ):
        return intValue1
    else:
        return intValue2

def main():
    intGreaterValue = Marvellous(20, 30)
    print("Greater value is : ", intGreaterValue )

    intGreaterValue = Marvellous(60, 20)
    print("Greater value is : ", intGreaterValue )

if __name__ == "__main__":
    main()