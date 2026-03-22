import os.path
import sys

def main():
    strFile1 = input( "Enter 1st File name which you want to open in reading mode: " )
    strFile2 = input( "Enter 2nd File name which you want to open in reading mode: " )

    print( "1st File name is : ", strFile1 )
    print( "2nd File name is : ", strFile2 )

    current_working_directory = os.getcwd()
    if True == os.path.exists( strFile1 ):
        objFile1 = open( strFile1, 'r' )

        if objFile1:
            print( "File 1 successfully open in read mode:" )
            
            DataFile1 = objFile1.read()

            if True == os.path.exists( strFile2 ):
                objFile2 = open( strFile2, 'r' )

                if objFile2:
                    print( "New file successfully open in write mode :" )

                    DataFile2 = objFile2.read()

                    objFile2.close()

                    if DataFile1 == DataFile2:
                        print( "Files are identical" )
                    else:
                        print( "Files are not same" )
                else:
                    print( "File 2 has not access to open: " )

            objFile1.close()
        else:
            print( "File 1 has not access to open: " )
    else:
        print("File 1 is not available in path : ", current_working_directory )

if __name__ == "__main__":
    main()