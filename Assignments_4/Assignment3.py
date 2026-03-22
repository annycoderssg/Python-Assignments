from functools import reduce

Add = lambda intNo1, intNo2 : intNo1 + intNo2

NumberRange = lambda intNo : ( 70 <= intNo and 90 >= intNo )

Increase = lambda intNo : ( intNo + 10 )

def main():
    arrintData = []

    intLoop = int(input("Enter Number of Elements : "))

    print( "Enter Your Numbers : " )
    for i in range( intLoop ):
        intValue = int(input())
        arrintData.append( intValue )

    print("Intput Data List : ", arrintData )

    intResult = list(filter(NumberRange, arrintData))
    print("List After Filter : ", intResult )

    intResult = list(map(Increase, intResult) )
    print("List After Map : ", intResult )

    intResult = reduce(Add, intResult)
    print("Output of reduce : ", intResult )

if __name__ == "__main__":
    main()