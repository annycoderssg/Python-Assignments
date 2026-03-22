from functools import reduce

def Add( intSum, intNo ):
    intSum = intSum + intNo
    return intSum

def CheckPrimeNumber( intNo ):
    i = 2
    while( i <= intNo ):
        if i == intNo:
            return True
        elif( 0 == ( intNo % i ) ):
            return False
        else:
            i = i + 1

def main():
    arrintNumbers = []
    
    intNumber = int(input("Number of Elements : "))
    
    print("Input Numbers: ")
    for i in range(intNumber):
        intValue = int(input())
        arrintNumbers.append(intValue)

    arrPrimeNumbers = list(filter(CheckPrimeNumber, arrintNumbers))
    print( "Prime Number List : ", arrPrimeNumbers )

    intTotal = reduce(Add, arrPrimeNumbers)
    print("Addition of all Prime Numbers is : ", intTotal )

if __name__ == "__main__":
    main()