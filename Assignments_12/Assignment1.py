# Encapsulation: Private & Protected attributes, @property getters/setters
#
# Concepts demonstrated:
#   _protected  : accessible within class and subclasses (convention)
#   __private   : name-mangled, only accessible within the class
#   @property   : Pythonic getter
#   @<name>.setter : Pythonic setter with validation

class Employee:
    intEmployeeCount = 0  # class variable

    def __init__(self, strName, fltSalary, intAge):
        self._strName   = strName       # protected
        self.__fltSalary = fltSalary    # private
        self.__intAge    = intAge       # private
        Employee.intEmployeeCount += 1

    # --- @property: getter ---
    @property
    def strName(self):
        return self._strName

    @property
    def fltSalary(self):
        return self.__fltSalary

    @property
    def intAge(self):
        return self.__intAge

    # --- setter with validation ---
    @fltSalary.setter
    def fltSalary(self, fltValue):
        if fltValue < 0:
            print("Error: Salary cannot be negative.")
        else:
            self.__fltSalary = fltValue

    @intAge.setter
    def intAge(self, intValue):
        if intValue < 18 or intValue > 65:
            print("Error: Age must be between 18 and 65.")
        else:
            self.__intAge = intValue

    def Display(self):
        print("Name   :", self._strName)
        print("Salary :", self.__fltSalary)
        print("Age    :", self.__intAge)

def main():
    objEmp1 = Employee("Anand Shinde", 55000.0, 30)
    objEmp1.Display()

    print()
    print("Updating salary and age via setter:")
    objEmp1.fltSalary = 62000.0
    objEmp1.intAge    = 31
    objEmp1.Display()

    print()
    print("Trying invalid values:")
    objEmp1.fltSalary = -1000   # should print error
    objEmp1.intAge    = 16      # should print error

    print()
    objEmp2 = Employee("Anvit Shinde", 30000.0, 22)
    objEmp2.Display()

    print()
    print("Total Employees:", Employee.intEmployeeCount)

if __name__ == "__main__":
    main()
