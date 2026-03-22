import Arithmetic

def main():
    intValue1 = int( input("Enter First Number For Addition : ") )
    intValue2 = int( input("Enter Second Number For Addition : ") )

    intResult = Arithmetic.Add( intValue1, intValue2 )

    print( "Addition of two number is : ", intResult )

    intResult = Arithmetic.Sub( intValue1, intValue2 )

    print( "Subtraction of two number is : ", intResult )

    intResult = Arithmetic.Mult( intValue1, intValue2 )

    print( "Multiplication of two number is : ", intResult )

    intResult = Arithmetic.Div( intValue1, intValue2 )

    print( "Division of two number is : ", intResult )

if __name__ == "__main__":
    main()