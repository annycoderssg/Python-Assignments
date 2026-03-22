def main():
    intValue = int( input("Enter Number to generate factors : ") )
    intFactor = 0
    if( intValue < 0 or intValue == 0 ):
        print("Number should greater than zero")
    else:    
        for i in range( 1, intValue ):
            if( 0 == ( intValue % i ) ):
                intFactor = intFactor + i
        print( "Addition of Factors are: ", intFactor )

if __name__ == "__main__":
    main()