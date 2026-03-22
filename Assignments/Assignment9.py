#Write a program which display 1st 10 even numbers on screen.
# import array as arr

def main():
    intNumber = 0
    intNumber = int( input("Enter Count of Even Numbers You Want : ") )
    intEvenNumbers = (intNumber+1) * 2
    strOutput = ""
    # arrResult = []

    for i in range(1, intEvenNumbers, 1):
        if( 0 == (i % 2) ):
            print(i, end =" ")
            # arrResult.append(i)

    print(strOutput)
    # print(arrResult)

if __name__ == "__main__":
    main()