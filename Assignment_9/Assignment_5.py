import os.path
import sys

def main():
    strFile = input( "Enter 1st File name which you want to open in reading mode: " )
    strInput = input( "Enter text which you want to search: " )

    print( "File name is : ", strFile )

    current_working_directory = os.getcwd()
    if True == os.path.exists( strFile ):
        objFile = open( strFile, 'r' )

        if objFile:
            print( "File is successfully open in read mode:" )
            
            strFileData = objFile.read()
            arrWords = strFileData.split()

            print( "File contents are: ")
            print( strFileData, arrWords )

            intNumbers = 0
            for strWord in arrWords:
                if strInput == strWord:
                    intNumbers = intNumbers + 1

            print( strInput, " Occurs in file: ", intNumbers, " times.")

        else:
            print( "File 1 has not access to open: " )
    else:
        print("File 1 is not available in path : ", current_working_directory )

if __name__ == "__main__":
    main()