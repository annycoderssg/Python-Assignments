intSum = 1

def Factorial( i, intNumber ):
    global intSum
    if( i < intNumber ):
        intSum = intSum + intSum * i
        i+=1
        Factorial(i, intNumber )
    else:
        print( "Factorial of number is : ", intSum )

def main():
    i = 0
    intNumber = int( input( "Enter Number : ") )
    Factorial( i, intNumber )
    
if __name__ =="__main__":
    main()