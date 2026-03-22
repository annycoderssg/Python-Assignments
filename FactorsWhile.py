def DisplayFactors(Value1):
    No = 1
    while(No < Value1):
        if( 0 == ( Value1 % No ) ):
            print("Number is Factor ", No )
        No = No + 1


def main():
    Number = int(input("Enter Number to check Factors"))
    DisplayFactors( Number )

if __name__ == "__main__":
    main()