def main():
    intValue = int( input("Enter Number to display pattern : ") )

    intLoop = 0
    while( intLoop < intValue ):
        for i in range( intValue ):
            print( "*", end=" " )
        intLoop = intLoop + 1
        print("")

if __name__ == "__main__":
    main()