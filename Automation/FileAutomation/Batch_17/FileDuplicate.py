from sys import *
import os
import hashlib

def hashfile( path, blocksize = 1024 ):
    fd = open( path, 'rb' )
    hasher = hashlib.md5()
    buf = fd.read( blocksize )

    while len( buf ) > 0:
        hasher.update( buf )
        buf = fd.read( blocksize )

    fd.close()

    return hasher.hexdigest()

def FindDuplicate( path ):
    flag = os.path.isabs( path )

    if False == flag:
        path = os.path.abspath( path )

    exists = os.path.isdir( path )

    dups = {}
    if exists:
        for dirName, subDirs, fileList in os.walk( path ):
            for filen in fileList:
                path = os.path.join( dirName, filen )
                file_hash = hashfile( path )

                if file_hash in dups:
                    dups[file_hash].append( path )
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print( "Invalid Path" )

def PrintDuplicate( dict1 ):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len( results ) > 0:
        print("Duplicate Found")

        print( "The following files are identical.")

        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt > 2:
                    print( "\t\t%s" % subresult )
    else:
        print( "No duplicate files found" )

def main():
    print( "+++++++++++ Marvellous Infosystems by Piyush Khairnar +++++++++++")

    print( "Application Name : " + argv[0] )

    if( len(argv) != 2 ):
        print("Error: Invalid number of arguments")
        exit()

    if( argv[1] == "-h" or argv[1] == "-H" ):       # Flag for displaying usage of help
        print("Help: This script is used to traverse specific directory and display size of files")
        exit()
    
    elif( argv[1] == "-u" or argv[1] == "-U" ):       # Flag for displaying usage of script
        print( "Usage: Application_name AbsolutePath_of_directory Extension")
        print( "Example: Demo.py Automation")
        exit()

    try:
        arr = {}
        arr = FindDuplicate( argv[1] )
        PrintDuplicate( arr )

    except ValueError:
        print( "Error: Invalid datatype of input" ) 

if __name__ == "__main__":
    main()