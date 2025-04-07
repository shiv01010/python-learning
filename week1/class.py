# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.


class Person:
    def __init__(self, firstname, lastname, gender, uid):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.uid = uid

    def print_full_name(self):
        print(f"{self.firstname} {self.lastname}")


# print(tapan.firstname)
# The string representation of an object WITHOUT the __str__() function:
# print(tapan)

# tapan = Person("tapan", "agerwal", "m", "12345")

# tapan.print_full_name()


# class Employee(Person):
#     pass


# deepak = Employee("DEEPAK", "KUSHWAHA", "M", "123456")

# deepak.print_full_name()


class Student(Person):
    def __init__(self, firstname, lastname, gender, uid, roleno, std):
        self.roleno = roleno
        self.std = std
        super().__init__(firstname, lastname, gender, uid)


akash = Student("akash", "madhwal", "M", "1234", "3", "10TH")

print(akash.std)
akash.print_full_name()
