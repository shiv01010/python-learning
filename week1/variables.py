# python has no command to declare variables
# A variable is created the moment you first assign a value to it.
# x = 5
# y = "python"
# print(x)
# print(y)


# CASTING
# If you want to specify the data type of a variable, this can be done with casting.

# x = str(3)  # x will be '3'
# y = int(3)  # y will be 3
# z = float(3)  # z will be 3.0
# n = "openai"
# print(x, type(x))
# print(y, type(y))
# print(z, type(z))
# print(n, type(n))


# you can create multiple variables in a single line in python
# x, y, z = "Orange", "Banana", "Cherry"


# you can assign same value to multiple variables in single line
# x = y = z = "tapanai"
# print(x)
# print(y)
# print(z)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.(destructuring)
# fruits = ["apple", "banana", "orange"]
# x, y, z = fruits

# print(x)
# print(y)
# print(z)


# GLOBAL VARIABLES
# Variables that are created outside of a function (as in all of the examples) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.


# x = "awesome"


# def myfunc():
#     print("Python is " + x)


# myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

# x = "awesome"


# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)


# myfunc()

# print("Python is " + x)


# the global keyword
# def myfunc():
#     global x
#     x = "fantastic"


# myfunc()

# print("Python is " + x)
