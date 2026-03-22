#Write a program which accept name from user and display length of its name.

def main():
    strName = ''
    strName = str( input("Enter Name : ") )

    print(len(strName))    

if __name__ == "__main__":
    main()