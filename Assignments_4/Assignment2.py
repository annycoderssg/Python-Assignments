from functools import reduce

Mult = lambda intNo1, intNo2 : intNo1 * intNo2

def main():
    intNo1 = int(input("Enter Number 1 : "))

    intNo2 = int(input("Enter Number 2 : "))
    
    print("Multiplication of numbers is : ", reduce(Mult, [intNo1, intNo2]) )

if __name__ == "__main__":
    main()