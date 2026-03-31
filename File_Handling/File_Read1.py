import os.path

def main():
    print("Enter the name of file that you want to open for reading purpose: ")
    strFileName = input()

    if True == os.path.exists( strFileName ):
        objFile = open( strFileName, "r" )      # read mode
        
        if objFile:
            print( "File successfully open in read mode:" )
            
            Data = objFile.read(10)    # write the data into the file

            print("File contents are: ", Data )

            objFile.close()
        else:
            print("Unable to open file")
    else:
        current_working_directory = os.getcwd()
        print( "File is not available in ", current_working_directory )

if __name__ == "__main__":
    main()