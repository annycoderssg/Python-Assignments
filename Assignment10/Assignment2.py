import os
from sys import argv

def scanDirectory( path, oldExtension, newExtension ):
    flag = os.path.isabs( path )
    if False == flag:
        path = os.path.abspath(path)

    exits = os.path.isdir(path)

    if exits:
        for dirName, subDirs, fileList in os.walk( path ):
            for file in fileList:
                if oldExtension in file:
                    file = os.path.join( path, file )
                    print("FIle name is : ", file ) 
                    pre, ext = os.path.splitext(file)
                    # print( pre, ext, newExtension)
                    os.rename(file, pre+newExtension)
                    print("Changed file extension : ", file )                


def main():
    print( "Application Name : " + argv[0] )

    if(len(argv) == 1 ):
        print("Invalid number of arguments")
        exit()
    
    if( argv[1] == "-h" or argv[1] == "-H" ):       # Flag for displaying usage of help
        print("Help: This script is used to traverse specific directory and display checksum of files")
        exit()
    
    elif( argv[1] == "-u" or argv[1] == "-U" ):       # Flag for displaying usage of script
        print( "Usage: Application_name AbsolutePath_of_directory OldExtension NewExtension")
        print( "Example: Assignment2.py Demo '.txt' '.doc'")
        exit()
    
    elif( len(argv) != 4 ):
        print("Error: Arguments are missing")
        exit()

    try:
        print( "Change file extensions in directory : " )
        scanDirectory( argv[1], argv[2], argv[3] )

    except ValueError:
        print( "Error: Invalid datatype of input" )

    except Exception as E:
        print( "Error: Invalid input", E )

if __name__ == "__main__":
    main()