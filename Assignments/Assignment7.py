#Write a program which contains one function that accept one number from user and returns true if number is divisible 5 otherwise return false
def IsDivisible( intDivisor ):
    intNumber = 0
    intNumber = int(input("Enter Number : "))
    if( 0 == ( intNumber % intDivisor ) ):
        return True
    else:
        return False

def main():
    intDivisor = 5
    boolOutPut = IsDivisible( intDivisor )
    if( True == boolOutPut ):
        print( "True" )
    else:
        print( "False" )    

if __name__ == "__main__":
    main()