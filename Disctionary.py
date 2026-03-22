def main():

    Books = {"C" : "Dennis Ritchie", "C++" : "Bjarne Stroustrup", "Java" : "James Gosling", "Python" : "Guido Van Rossum"}

    print(type(Books))

    print(len(Books))

    print(Books)

    Language = Books.keys()

    print(type(Language))

    print(Language)

    Authors = Books.values()

    print(type(Authors))

    print(Authors)

    for i in Books:
        print("Book Name is : ", i , " & Writer : ", Books[i])
    
if __name__ == "__main__":
    main()