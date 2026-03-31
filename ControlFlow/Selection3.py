import Infosystems

def main():
    Number = 0
    Number = int(input("Enter Number"))
    if( 0 == Infosystems.CheckEvenOrOdd(Number) ):
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()