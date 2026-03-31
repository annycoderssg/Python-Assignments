from sys import *
import os
import hashlib

def DisplayDuplicates( dict1 ):
    results = list( filter(lambda x: len(x) > 1, dict1.values() ) )

    icount = 0
    iFound = 0
    if len( results ) > 0:
        for result in results:
            for subresult in result:
                icount+= 1
                if icount >= 2:
                    print( "Diplicate File: ", subresult )
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

def searchDuplicates( path ):

    if False == os.path.isabs( path ):
        path = os.path.abspath( path )

    arrDiplicates = {}
    if os.path.isdir( path ):
        for dirName, subdirs, fileList in os.walk( path ):
            print( "Current folder is : " + dirName )
            for filen in fileList:
                path = os.path.join( dirName, filen )
                file_hash = hashfile( path )

                if file_hash in arrDiplicates:
                    arrDiplicates[file_hash].append( path )
                else:
                    arrDiplicates[file_hash] = [path]

        return arrDiplicates
    else:
        print( "Invalid Path" )

def LogDiplicateFiles( dict1 ):
    results = list( filter( lambda x: len(x) > 1, dict1.values() ) )
    objFile = open( "Log.txt", "w" )

    if len( results ) > 0:
        print( "Duplicates Found:" )
        print( "The following files are duplicate we write it into Log.txt" )
        for result in results:
            for subresult in result:
                objFile.write( subresult )
                objFile.write( "\n" )
                print("\t%s" %subresult )
    else:
        print( "No duplicate file found." )

    objFile.close()

def main():

    print( "Application Name : " + argv[0] )

    if( len(argv) != 2 ):
        print("Error: Invalid number of arguments")
        exit()

    if( argv[1] == "-h" or argv[1] == "-H" ):       # Flag for displaying usage of help
        print("Help: This script is used to traverse specific directory and display size of files")
        exit()
    
    elif( argv[1] == "-u" or argv[1] == "-U" ):       # Flag for displaying usage of script
        print( "Usage: Application_name AbsolutePath_of_directory")
        print( "Example: Assignment2.py Demo")
        exit()

    try:
        arr = {}
        arr = searchDuplicates( argv[1] )
        LogDiplicateFiles( arr )

    except ValueError:
        print( "Error: Invalid datatype of input" ) 

    except Exception as E:
        print( "Error: Invalid input", E )

if __name__ == "__main__":
    main()