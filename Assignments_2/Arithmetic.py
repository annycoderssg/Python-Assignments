def Add( intNumber1, intNumber2 ):
    intAnswer = 0
    intAnswer = intNumber1 + intNumber2
    return intAnswer

def Sub( intNumber1, intNumber2 ):
    intAnswer = 0
    intAnswer = intNumber1 - intNumber2
    return intAnswer

def Mult( intNumber1, intNumber2 ):
    intAnswer = 0
    intAnswer = intNumber1 * intNumber2
    return intAnswer

def Div( intNumber1, intNumber2 ):
    intAnswer = 0
    if(intNumber2 == 0 or intNumber1 < intNumber2):
        print("Divisible Number should be greater than zero or Number1 ", intNumber1 )
    else:
        intAnswer = intNumber1 / intNumber2
    
    return intAnswer