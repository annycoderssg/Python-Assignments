def PrimeNumber( intValue ):
    i = 2
    while( i <= intValue ):
        if i == intValue:
            return True
        elif( 0 == ( intValue % i ) ):
            return False
        else:
            i = i + 1

def main():
    intValue = int( input("Enter Number to check prime number : ") )
    if( intValue < 0 or intValue == 0 ):
        print("Number should greater than zero")
    else:    
        if( True == PrimeNumber( intValue ) ):
            print("It is Prime Number")
        else:
            print("Number is not Prime")

if __name__ == "__main__":
    main()