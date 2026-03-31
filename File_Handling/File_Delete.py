import os.path

def main():
    print("Enter the name of file that you want to delete: ")
    strFileName = input()

    if True == os.path.exists( strFileName ):
        os.remove( strFileName )
        print( "Your File is successfully delete" )
    else:
        current_working_directory = os.getcwd()
        print( "File is not available in ", current_working_directory )

if __name__ == "__main__":
    main()