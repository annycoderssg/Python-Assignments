def main():
    intValue = int( input("Enter Number to display pattern : ") )
    if( intValue < 0 or intValue == 0 ):
        print("Number should greater than zero")
    else:    
        intLoop = 0
        while( intLoop < intValue ):
            for i in range( intValue ):
                print( i+1, end=" " )
            intLoop = intLoop + 1
            print("")

if __name__ == "__main__":
    main()