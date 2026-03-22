from functools import reduce

def CheckEven( intNo ):
    if( 0 == intNo % 2 ):
        return True
    else:
        return False

def Increase( intNo ):
    intNo = intNo + 2
    return intNo

def Add( intSum, intNo ):
    intSum = intSum + intNo
    return intSum


def main():
    print("Demonstration of Filter Map Reduce")

    arrData = [5, 4, 9, 8, 13, 17, 12, 18]
    intTotal = 0
    # for i in range( len(arrData) ):
    #     if( True == CheckEven( arrData[i] ) ):
    #         intMap = Increase( arrData[i] )
    #         intTotal = Add( intTotal, intMap)

    arrEveneNumbers = list(filter(CheckEven, arrData))
    print( arrEveneNumbers )
    
    arrIncreasedList = list(map(Increase, arrEveneNumbers))
    print(arrIncreasedList)
    
    intTotal = reduce(Add, arrIncreasedList)
    print(intTotal)

    print("Addition of after FMR is : ", intTotal )

if __name__ == "__main__":
    main()