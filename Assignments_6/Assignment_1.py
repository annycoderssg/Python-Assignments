class BookStore:
    intNoofBooks = 0

    def __init__(self, strName, strAuthor ):
        self.strName = strName
        self.strAuthor = strAuthor

    def Display(self):
        print("Book Name: ", self.strName )
        print("Book Author Name: ", self.strAuthor )
        print("Number of Books: ", BookStore.intNoofBooks )

def main():
    objBookStore1 = BookStore( "Linux System Programing", "Robert Love")
    BookStore.intNoofBooks = BookStore.intNoofBooks + 1
    objBookStore1.Display()

    objBookStore2 = BookStore( "C Programing", "Dennis Ritchie" )
    BookStore.intNoofBooks = BookStore.intNoofBooks + 1
    objBookStore2.Display()

if __name__ == "__main__":
    main()