from functools import reduce

Power = lambda intNo1, intNo2 : intNo1 * intNo2

def main():
    intNumber = int(input("Enter Element : "))

    intPower = reduce(Power, [intNumber, intNumber])
    print("Power of number is : ", intPower )

if __name__ == "__main__":
    main()