# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# Function Polymorphism
# An example of a Python function that can be used on different objects is the len() function.

# mytuple = ("apple", "banana", "cherry")

# print(len(mytuple))

# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# print(len(thisdict))


# method overriding aka runtime polymorphism
# class Animal:
#     def make_sound(self):
#         return "Some generic sound"


# class Dog(Animal):
#     def make_sound(self):  # Overriding parent class method
#         return "Bark"


# class Cat(Animal):
#     def make_sound(self):  # Overriding parent class method
#         return "Meow"


# # Creating objects of different classes
# animals = [Dog(), Cat(), Animal()]

# # Demonstrating polymorphism
# for animal in animals:
#     print(animal.make_sound())  # Output: Bark, Meow, Some generic sound


# class AI:
#     def what_it_is(self):
#         return "It is generic term used for any artificial intelligence"


# class genAI(AI):
#     def what_it_is(self):
#         return "A type of AI"


# class ML(AI):
#     def what_it_is(self):
#         return "Subset of AI"


# ai = AI()
# genai = genAI()
# ml = ML()

# print(ai.what_it_is())
# print(genai.what_it_is())
# print(ml.what_it_is())


# method overloading (compiletime polymorphism)


# class MathOperations:
#     def add(self, a, b, c=0):  # Default argument
#         return a + b + c


# math_op = MathOperations()
# print(math_op.add(2, 3))  # Output: 5
# print(math_op.add(2, 3, 4))  # Output: 9
# print(math_op.add(2, 3, 4, 5))


class MathOps:
    def add(this, *args):
        return sum(args)


mathops = MathOps()
print(mathops.add(1, 10, 15, 100))
