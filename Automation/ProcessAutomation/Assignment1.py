import sys
import os

def scanDirectory( path, extension ):
    flag = os.path.isabs( path )
    if False == flag:
        path = os.path.abspath(path)

    exits = os.path.isdir(path)

    if exits:
        for dirName, subDirs, fileList in os.walk( path ):
            for file in fileList:
                arrMixFile = file.split( extension )
                print( arrMixFile )

def main():
    print( "Application Name : " + argv[0] )

    if( len(argv) != 3 ):
        print("Error: Invalid number of arguments")
        exit()
    
    if( argv[1] == "-h" or argv[1] == "-H" ):       # Flag for displaying usage of help
        print("Help: This script is used to traverse specific directory and display checksum of files")
        exit()
    
    elif( argv[1] == "-u" or argv[1] == "-U" ):       # Flag for displaying usage of script
        print( "Usage: Application_name AbsolutePath_of_directory Extension")
        print( "Example: Demo.py Automation '.txt")
        exit()

    try:
        arr = scanDirectory( argv[1], argv[2] )
        print( arr )

    except ValueError:
        print( "Error: Invalid datatype of input" )

    except Exception as E:
        print( "Error: Invalid input", E )

if "__name__" == "__main__":
    main()