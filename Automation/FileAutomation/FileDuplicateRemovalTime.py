from sys import *
import os
import hashlib
import time

def DeleteFiles( dict1 ):
    results = list( filter(lambda x: len(x) > 1, dict1.values() ) )

    icount = 0
    iFound = 0
    if len( results ) > 0:
        for result in results:
            for subresult in result:
                icount+= 1
                if icount >= 2:
                    iFound+= 1
                    os.remove( subresult )
            icount = 0

        print( "Number of duplicates file and deleted : ", iFound )
    else:
        print( "No duplicate files found" )

def hashfile( path, blocksize = 1024 ):
    afile = open( path, 'rb' )
    hasher = hashlib.md5()
    buf = afile.read( blocksize )

    while len( buf ) > 0:
        hasher.update( buf )
        buf = afile.read( blocksize )
    afile.close()

    return hasher.hexdigest()

def findDup( path ):
    flag = os.path.isabs( path )

    if False == flag:
        path = os.path.abspath( path )

    exists = os.path.isdir( path )

    dups = {}
    if exists:
        for dirName, subdirs, fileList in os.walk( path ):
            print( "Current folder is : " + dirName )
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

def printResults( dict1 ):
    results = list( filter( lambda x: len(x) > 1, dict1.values() ) )

    if len( results ) > 0:
        print( "Duplicates Found:" )
        print( "The following files are duplicate" )
        for result in results:
            for subresult in result:
                print("\t\t%s" %subresult )
    else:
        print( "No duplicate file found." )

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
        startTime = time.time()
        arr = findDup( argv[1] )
        printResults( arr )
        DeleteFiles( arr )
        endTime = time.time()

        print( "Took %s seconds to evaluate" % ( endTime - startTime ) )

    except ValueError:
        print( "Error: Invalid datatype of input" ) 

    except Exception as E:
        print( "Error: Invalid input", E )

if __name__ == "__main__":
    main()