import sys

def main():
    print("Addition of Two Numbers using command Line: ")

    print("Number of elements in command line arr : ", len(sys.argv))

    intValue1 = int(sys.argv[1]);
    intValue2 = int(sys.argv[2]);

    print("Addition of two numbers : ", intValue1 + intValue2 )

if __name__ == "__main__":
    main()

#py Command1.py Marvellous 11    