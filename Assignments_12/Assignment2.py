# Inheritance and super()
#
# Concepts demonstrated:
#   Single inheritance   : child class inherits from one parent
#   super().__init__()   : calling parent constructor from child
#   super().method()     : calling parent method from child
#   Extending behaviour  : child adds its own attributes and methods

class Person:
    def __init__(self, strName, intAge):
        self.strName = strName
        self.intAge  = intAge

    def Display(self):
        print("Name :", self.strName)
        print("Age  :", self.intAge)


class Student(Person):
    def __init__(self, strName, intAge, strCourse, fltPercentage):
        super().__init__(strName, intAge)   # call Person.__init__
        self.strCourse      = strCourse
        self.fltPercentage  = fltPercentage

    def Display(self):
        super().Display()                   # call Person.Display
        print("Course     :", self.strCourse)
        print("Percentage : %.2f%%" % self.fltPercentage)


class Teacher(Person):
    def __init__(self, strName, intAge, strSubject, fltSalary):
        super().__init__(strName, intAge)
        self.strSubject = strSubject
        self.fltSalary  = fltSalary

    def Display(self):
        super().Display()
        print("Subject :", self.strSubject)
        print("Salary  :", self.fltSalary)


def main():
    print("=== Person ===")
    objPerson = Person("Ramesh Kumar", 45)
    objPerson.Display()

    print()
    print("=== Student (inherits Person) ===")
    objStudent = Student("Anvit Shinde", 20, "Computer Science", 88.5)
    objStudent.Display()

    print()
    print("=== Teacher (inherits Person) ===")
    objTeacher = Teacher("Anand Shinde", 38, "Python Programming", 75000.0)
    objTeacher.Display()

    print()
    print("Is objStudent an instance of Person?", isinstance(objStudent, Person))
    print("Is objTeacher an instance of Student?", isinstance(objTeacher, Student))
    print("Is Student a subclass of Person?", issubclass(Student, Person))

if __name__ == "__main__":
    main()
