#Write a program which contains one function named as ChkNum(). Which accept one parameter as Number. If number is even then it should display "Even Number" 
# otherwise display "Odd Number" on console  
def ChkNum( intValue ):
    intRemainder = intValue % 2 
    if( 0 == intRemainder ):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    intNumber = 0
    intNumber = int(input("Enter a Number : "))
    ChkNum( intNumber )

if __name__ == "__main__":
    main()