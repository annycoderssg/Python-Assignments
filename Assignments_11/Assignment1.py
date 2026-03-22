import sys
import os
import hashlib

def hashfile(path, blocksize=1024):
    with open(path, 'rb') as afile:
        hasher = hashlib.sha256()
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
    return hasher.hexdigest()

def DisplayChecksum(path):
    if not os.path.isabs(path):
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName, subDirs, fileList in os.walk(path):
            for file in fileList:
                filepath = os.path.join(dirName, file)
                file_hash = hashfile(filepath)
                print(' ')
                print(filepath, ' => ', file_hash)

def main():
    print("Application Name : " + sys.argv[0])

    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments")
        sys.exit()

    if sys.argv[1] == "-h" or sys.argv[1] == "-H":
        print("Help: This script is used to traverse specific directory and display checksum of files")
        sys.exit()

    elif sys.argv[1] == "-u" or sys.argv[1] == "-U":
        print("Usage: Application_name AbsolutePath_of_directory")
        print("Example: Assignment1.py Demo")
        sys.exit()

    try:
        print("Display Checksum: ")
        DisplayChecksum(sys.argv[1])

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as E:
        print("Error: Invalid input", E)

if __name__ == "__main__":
    main()
