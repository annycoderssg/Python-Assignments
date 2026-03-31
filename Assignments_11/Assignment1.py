from sys import *
import os
import hashlib

def hashfile( path, blocksize = 1024 ):

    afile = open( path, 'rb')
    hasher = hashlib.md5()

    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()

def DisplayChecksum( path ):
    flag = os.path.isabs( path )
    if False == flag:
        path = os.path.abspath(path)
    
    exits = os.path.isdir(path)

    if exits:
        for dirName, subDirs, fileList in os.walk( path ):
            for file in fileList:
                file = os.path.join( path, file )
                file_hash = hashfile( file )
                print( ' ' )
                print( file, ' => ', file_hash )

def main():
    print( "Application Name : " + argv[0] )

    if( len(argv) != 2 ):
        print("Error: Invalid number of arguments")
        exit()
    
    if( argv[1] == "-h" or argv[1] == "-H" ):       # Flag for displaying usage of help
        print("Help: This script is used to traverse specific directory and display checksum of files")
        exit()
    
    elif( argv[1] == "-u" or argv[1] == "-U" ):       # Flag for displaying usage of script
        print( "Usage: Application_name AbsolutePath_of_directory" )
        print( "Example: Assignment1.py Demo" )
        exit()

    try:
        print( "Display Checksum: ")
        DisplayChecksum( argv[1] )

    except ValueError:
        print( "Error: Invalid datatype of input" )

    except Exception as E:
        print( "Error: Invalid input", E )

if __name__ == "__main__":
    main()