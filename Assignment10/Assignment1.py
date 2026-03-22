import os
from sys import argv

def scanDirectory( path, extension ):
    flag = os.path.isabs( path )
    if False == flag:
        path = os.path.abspath(path)

    exits = os.path.isdir(path)

    if exits:
        for dirName, subDirs, fileList in os.walk( path ):
            for file in fileList:
                if extension in file:
                    print( "Match File Name: ", file )

                # arrMixFile = file.split( '.' )
                
                # if len(arrMixFile) > 2:
                #     print("Invalid file name : ", file )

                # if extension == arrMixFile[1]:
                #     print( "Match File Name: ", file )

def main():
    print( "Application Name : " + argv[0] )
    
    if(len(argv) == 1 ):
        print("Invalid number of arguments")
        exit()

    if( argv[1] == "-h" or argv[1] == "-H" ):       # Flag for displaying usage of help
        print("Help: This script is used to traverse specific directory and display checksum of files")
        exit()
    
    elif( argv[1] == "-u" or argv[1] == "-U" ):       # Flag for displaying usage of script
        print( "Usage: Application_name AbsolutePath_of_directory Extension")
        print( "Example: Assignment1.py 'Demo' '.txt'")
        exit()

    elif( len(argv) != 3 ):
        print("Error: File extension argument is missing")
        exit()

    try:
        print( "Match files in directory : " )
        scanDirectory( argv[1], argv[2] )

    except ValueError:
        print( "Error: Invalid datatype of input" )

    except Exception as E:
        print( "Error: Invalid input", E )

if __name__ == "__main__":
    main()