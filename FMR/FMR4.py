#Unnamed Function or ( Lambda/Anonymous Function )
#Name = lambda Parameter_Lists : Function_Logic

def Add( intNo1, intNo2 ):
    return intNo1 + intNo2

AddX = lambda intNo1, intNo2 : intNo1 + intNo2

def CheckEven( intNo ):
    return ( 0 == ( intNo % 2 ) )

CheckEvenX = lambda intNo : ( 0 == ( intNo % 2 ) )

def Increase ( intNo ):
    return intNo + 2

IncreaseX = lambda intNo : ( intNo + 2 )

def main():
    print("Demonstration of Filter Map Reduce")

    intResult = Add(10, 20)
    print("Addition is : ", intResult )

    intResult = CheckEven( 2 )
    print( intResult )

    intResult = Increase( 5 )
    print( intResult )

    intResult = AddX(10, 20)
    print("Addition is : ", intResult )

    intResult = CheckEvenX( 2 )
    print( intResult )

    intResult = IncreaseX( 5 )
    print( intResult )

    # arrData = []
    # intLoop = int(input('Enter Number of Elements : ') )

    # print("Enter elements: ")
    # for i in range( intLoop ):
    #     intNo = int(input())
    #     arrData.append( intNo )

    # intTotal = 0
    # # for i in range( len(arrData) ):
    # #     if( True == CheckEven( arrData[i] ) ):
    # #         intMap = Increase( arrData[i] )
    # #         intTotal = Add( intTotal, intMap)

    # arrEveneNumbers = list(filter(CheckEven, arrData))
    # print( arrEveneNumbers )
    
    # arrIncreasedList = list(map(Increase, arrEveneNumbers))
    # print(arrIncreasedList)
    
    # intTotal = reduce(Add, arrIncreasedList)
    # print(intTotal)

    # print("Addition of after FMR is : ", intTotal )

if __name__ == "__main__":
    main()