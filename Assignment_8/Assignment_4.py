intSum = 0
def SumOfDigits( intNumber ):
    global intSum

    if intNumber == 0:
        print( "Summation is : ", intSum )
    else:    
        intReminder = intNumber % 10
        intSum = int( intSum ) + intReminder
        intNumber = int( intNumber / 10 )
        SumOfDigits( intNumber )

def main():
    intNumber = int( input( "Enter Number : ") )
    SumOfDigits( intNumber )
    
if __name__ =="__main__":
    main()