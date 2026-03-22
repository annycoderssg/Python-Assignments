import threading

def Small( strString ):
    intSmallChars = 0
    for i in range(len(strString)):
        if strString[i].islower():
            intSmallChars = intSmallChars + 1

    print( "Number of small characters : ", intSmallChars )

def Capital( strString ):
    intCaptialChars = 0
    for i in range(len(strString)):
        if strString[i].isupper():
            intCaptialChars = intCaptialChars + 1

    print( "Number of Capital characters : ", intCaptialChars )

def Digits( strString ):
    intDigits = sum(1 for c in strString if c.isdigit())
    print( "Number of Digits from String: ", intDigits )

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