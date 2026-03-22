def main():
    intValue = int( input("Enter Number to generate factorial : ") )
    intFactorial = 1
    if( intValue < 0 or intValue == 0 ):
        print("Number should greater than zero")
    else:    
        for i in range( 1, (intValue +1) ):
            intFactorial = intFactorial * i
        print( "Factorial Number is: ", intFactorial )

if __name__ == "__main__":
    main()