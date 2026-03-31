def FactorialNumber(Value1):
    for No in range(1, Value1, 1):
        if( 0 == ( Value1 % No ) ):
            print("Number is Factor ", No )


def main():
    Number = int(input("Enter Number to check Factors"))
    FactorialNumber( Number )

if __name__ == "__main__":
    main()