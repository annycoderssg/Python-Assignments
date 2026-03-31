import sys

def main():
    print("Demonstration of Command line Arguments: ")

    print("Number of elements in command line arr : ", len(sys.argv))

    print("1st Argument : ", sys.argv[0])

    print("2nd Argument : ", sys.argv[1])

    print("3rd Argument : ", sys.argv[2])

if __name__ == "__main__":
    main()

#py Command1.py Marvellous 11    