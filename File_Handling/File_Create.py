def main():
    print("Enter the name of file that you want to create: ")
    strFileName = input()

    objFile = open( strFileName, "x" )

if __name__ == "__main__":
    main()