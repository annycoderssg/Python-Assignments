def main():
    intValue = int( input("Enter Number to display pattern : ") )
    if( intValue < 0 or intValue == 0 ):
        print("Number should greater than zero")
    else:
        intNumbers = 0
        for char in str(intValue):
            intNumbers = intNumbers + int( char )
        print( "Number of digits are: ", intNumbers )

if __name__ == "__main__":
    main()