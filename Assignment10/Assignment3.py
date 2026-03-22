import os
import shutil
from sys import argv

def scanDirectory( sourcePath, destinationPath ):
    
    if False == os.path.isabs( sourcePath ):
        sourcePath = os.path.abspath(sourcePath)

    if False == os.path.isabs( destinationPath ):
        destinationPath = os.path.abspath(destinationPath)

    if os.path.isdir(sourcePath):
        for dirName, subDirs, fileList in os.walk( sourcePath ):
            for file in fileList:
                src_file = os.path.join( sourcePath, file )
                dst_file = os.path.join( destinationPath, file )
                print( "File move from : " + src_file + " => " + dst_file  )
                shutil.move( src_file, dst_file )

        print("Process complete")

def createNewDirectory( dirName ):
    if False == os.path.isabs( dirName ):
        dirName = os.path.abspath(dirName)

    if False == os.path.isdir(dirName):
        try:
            os.mkdir( dirName )
            print( "Directory created successfully: " )
            return True
        except Exception as E:
            print( "Error: Fail to create directory", E )
            return False
    else:
        print("Directory is already exists: ", dirName )
        return False

def main():
    print( "Application Name : " + argv[0] )

    if(len(argv) == 1 ):
        print("Invalid number of arguments")
        exit()
    
    if( argv[1] == "-h" or argv[1] == "-H" ):       # Flag for displaying usage of help
        print("Help: This script is used to traverse specific directory and display checksum of files")
        exit()
    
    elif( argv[1] == "-u" or argv[1] == "-U" ):       # Flag for displaying usage of script
        print( "Usage: Application_name Folder_1 Folder_2")
        print( "Example: Assignment3.py 'Demo' 'Copy'")
        exit()

    if( len(argv) != 3 ):
        print("Error: Arguments are missing")
        exit()

    try:
        print( "Change file extensions in directory : " )
        createNewDirectory( argv[2] )
        scanDirectory( argv[1], argv[2] )

    except ValueError:
        print( "Error: Invalid datatype of input" )

    except Exception as E:
        print( "Error: Invalid input", E )

if __name__ == "__main__":
    main()