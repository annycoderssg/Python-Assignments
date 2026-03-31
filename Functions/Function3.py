# Function accepts more parameter and return nothing    
def Marvellous( strName, strDesignation, fltSalary ):
    print(type(strName))
    print("Inside Marvellous Function")
    print("Welcome", strName )
    print("You are selected for designation : ", strDesignation)
    print("Your Salary is : ", fltSalary)

def main():
    Marvellous("Anand", "Sr Engineer", 15000 )
    Marvellous("Sagar", "Full Stack Dev", 90.90)

if __name__ == "__main__":
    main()