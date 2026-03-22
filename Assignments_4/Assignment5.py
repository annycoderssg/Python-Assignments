from functools import reduce

Add = lambda intNo1, intNo2 : intNo1 + intNo2

def CheckPrime( intNo ):
    i = 2
    while( i <= intNo ):
        if i == intNo:
            return True
        elif( 0 == ( intNo % i ) ):
            return False
        else:
            i = i + 1

Square = lambda intNo : ( intNo * 2 )

def main():
    arrintData = []

    intLoop = int(input("Enter Number of Elements : "))

    print( "Enter Your Numbers : " )
    for i in range( intLoop ):
        intValue = int(input())
        arrintData.append( intValue )

    print("Intput Data List : ", arrintData )

    intResult = list(filter(CheckPrime, arrintData))
    print("List After Filter : ", intResult )

    intResult = list(map(Square, intResult) )
    print("List After Map : ", intResult )

    intResult = reduce(Add, intResult)
    print("Output of reduce : ", intResult )

if __name__ == "__main__":
    main()