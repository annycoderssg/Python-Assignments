import os.path

def main():
    print("Enter the name of file that you want to open for read: ")
    strFileName = input()

    if True == os.path.exists( strFileName ):
        objFile = open( strFileName, "r" )
        if objFile:
            print( "File successfully open:" )
            objFile.close()
        else:
            print("Unable to open file")
    else:
        current_working_directory = os.getcwd()
        print( "File is not available in ", current_working_directory )

if __name__ == "__main__":
    main()