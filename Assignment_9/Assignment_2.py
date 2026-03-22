import os.path

def main():
    strFileName = input( "Enter File name which you want reading mode: " )
    current_working_directory = os.getcwd()
    if True == os.path.exists( strFileName ):
        objFile = open( strFileName, 'r' )

        if objFile:
            print( "File successfully open in read mode:" )
            
            Data = objFile.read()

            print("File contents are: " )
            print( Data )

            objFile.close()
        else:
            print( "You don't have permission to open file in reading mode" )
    else:
        print("File is not available on current path : ", current_working_directory )

if __name__ == "__main__":
    main()