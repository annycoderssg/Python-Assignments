import math

class Numbers:
    def __init__(self, intValue ):
        self.intValue = intValue

    def ChkPrime(self):
        if self.intValue > 1:
            for i in range(2, int(self.intValue/2)+1):
                if 0 == (self.intValue % i):
                    return True
                break
            else:
                return False
        else:
            return False

    def ChkPerfect(self):
        intSum = 0  
        for i in range(1,self.intValue):  
            if 0 == ( self.intValue % i ):  
                intSum = intSum + i
        
        if( self.intValue == intSum ):
            return True
        else:
            return False  

    def Factors(self):
        arrList = []
        for i in range(1, self.intValue + 1):
            if 0 == ( self.intValue % i ):
                arrList.append( i )
        
        return arrList

    def SumFactors(self):
        arrList = self.Factors() 
        intTotal = sum( arrList )
        print( "Sum of Factors: ", intTotal )

def main():
    intNumber = int( input("Enter Number 1: ") )

    objNumbers = Numbers( intNumber )
    if( True == objNumbers.ChkPrime() ):
        print( "Number is Prime" )
    else:
        print( "Number is not Prime" )
    
    if( True == objNumbers.ChkPerfect() ):
        print( "Number is Perfect" )
    else:
        print( "Number is not Perfect" )

    objNumbers.SumFactors()

    intNumber = int( input("Enter Number 2: ") )

    objNumbers2 = Numbers( intNumber )
    if( True == objNumbers2.ChkPrime() ):
        print( "Number is Prime" )
    else:
        print( "Number is not Prime" )
    
    if( True == objNumbers2.ChkPerfect() ):
        print( "Number is Perfect" )
    else:
        print( "Number is not Perfect" )

    objNumbers2.SumFactors()

if __name__ == "__main__":
    main()