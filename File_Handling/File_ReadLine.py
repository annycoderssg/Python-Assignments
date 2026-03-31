import os.path
# Demonstration of file handling
def main():
    print("Enter the name of file that you want to open for reading purpose: ")
    strFileName = input()

    if True == os.path.exists( strFileName ):
        objFile = open( strFileName, "r" )      # read mode
        
        if objFile:
            print( "File successfully open in read mode:" )
            
            Line1 = objFile.readline()    # read the line from file
            Line2 = objFile.readline()    # read the line from file
            Line3 = objFile.readline()    # read the line from file

            print("Line 1 : ", Line1 )
            print("Line 2 : ", Line2 )
            print("Line 3: ", Line3 )

            objFile.close()
        else:
            print("Unable to open file")
    else:
        current_working_directory = os.getcwd()
        print( "File is not available in ", current_working_directory )

if __name__ == "__main__":
    main()