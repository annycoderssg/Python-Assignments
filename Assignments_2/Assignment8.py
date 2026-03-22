def main():
    intValue = int( input("Enter Number to display pattern : ") )
    if( intValue < 0 or intValue == 0 ):
        print("Number should greater than zero")
    else:
        for i in range( 1, intValue+1 ):
            for j in range( 0, i ):
                print( j+1, end=" " )  
            print("")

if __name__ == "__main__":
    main()