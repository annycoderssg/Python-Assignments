def main():

    Books = {"C" : "Dennis Riche", "C++" : "Stroustrp", "Java" : "Gosling", "Python" : "Guido Van Rusum", "C++" : "Bajarne Stroustrp",}

    print(type(Books))

    print(len(Books))

    print(Books)

    Language = Books.keys();

    print(type(Language))

    print(Language)

    Aouthers = Books.values()

    print(type(Aouthers))

    print(Aouthers)

    for i in Books:
        print("Book Name is : ", i , " & Writer : ", Books[i])
    
if __name__ == "__main__":
    main()