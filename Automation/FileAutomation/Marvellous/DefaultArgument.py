def Display( Name, Age, Marks = 90 ):
    print("Name is :", Name)
    print("Age is: ", Age)
    print("Marks is: ", Marks)

def main():
    print("Demonstration of Default Arguments: ")
    Display(Name = "Anand", Age = 33, Marks = 58)
    Display(Age = 5.5, Name = "Anvit")

if __name__ == "__main__":
    main()