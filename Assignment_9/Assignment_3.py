import os.path
import sys

def main():
    strOldFileName = sys.argv[1]
    strNewFileName = input( "Enter File name which you want reading mode: " )

    print( "Old File name is : ", strOldFileName )
    print( "New File name is : ", strNewFileName )

    current_working_directory = os.getcwd()
    if True == os.path.exists( strOldFileName ):
        objFile1 = open( strOldFileName, 'r' )

        if objFile1:
            print( "File successfully open in read mode:" )
            
            Data = objFile1.read()

            if True == os.path.exists( strNewFileName ):
                print("Unable to open new file on path : ", current_working_directory )
            else:
                objFile2 = open( strNewFileName, 'a' )

                if objFile2:
                    print( "New file successfully open in write mode :")

                    objFile2.write( Data )

                    objFile2.close()

                    print( "Content is successfully copied from " + strOldFileName + " to new file " + strNewFileName )
                else:
                    print( "New file has not access to open: " )

            objFile1.close()
        else:
            print( "You don't have permission to open new file in reading mode" )
    else:
        print("Old File is not available on current path : ", current_working_directory )

if __name__ == "__main__":
    main()