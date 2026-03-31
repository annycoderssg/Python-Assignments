import threading

def Small( strString ):
    intSmallChars = 0
    for i in range(len(strString)):
        if True ==  strString[i].islower():
            intSmallChars = intSmallChars + 1
    
    print( "Number of small characters : ", intSmallChars )

def Capital( strString ):
    intCaptialChars = 0
    for i in range(len(strString)):
        if True ==  strString[i].isupper():
            intCaptialChars = intCaptialChars + 1
    
    print( "Number of Capital characters : ", intCaptialChars )

def Digits( strString ):
    print( "Number of Digits from String: ", len( strString ) )

def main():
    strString = input( "Enter String: " )
    t1 = threading.Thread( target = Small, args = (strString,) )
    t2 = threading.Thread( target = Capital, args = (strString,) )
    t3 = threading.Thread( target = Digits, args = (strString,) )

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()