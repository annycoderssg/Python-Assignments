import os.path

def main():
    print("Enter the name of file that you want to open for writing purpose: ")
    strFileName = input()

    if True == os.path.exists( strFileName ):
        objFile = open( strFileName, "w" )      # write mode with overwrite
        
        if objFile:
            print( "File successfully open in writing mode:" )
            
            print( "Enter the data which you write in file: " )
            Data = input()

            objFile.write( Data )    # write the data into the file

            objFile.close()
        else:
            print("Unable to open file")
    else:
        current_working_directory = os.getcwd()
        print( "File is not available in ", current_working_directory )

if __name__ == "__main__":
    main()