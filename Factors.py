def DisplayFactors(Value1):
    for No in range(Value1):
        if( No == 0 ):
            continue;

        if( 0 == ( Value1 % No ) ):
            print("Number is Factor ", No )


def main():
    Number = int(input("Enter Number to check Factors"))
    DisplayFactors( Number )

if __name__ == "__main__":
    main()