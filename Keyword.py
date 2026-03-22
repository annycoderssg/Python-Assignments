def Display( Name, Age, Marks ):
    print("Name is :", Name)
    print("Age is: ", Age)
    print("Marks is: ", Marks)

def main():
    print("Demonstration of Keyword Arguments: ")
    Display(Name = "Anand", Age = 33, Marks = 58)
    Display(Age = 5.5, Marks = 70, Name = "Anvit")

if __name__ == "__main__":
    main()

# When programer knows function argument name then only we can use keyword argument 