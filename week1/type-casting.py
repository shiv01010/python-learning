"""
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""

# x = int()
# print(x)  # 0

# y = int(1.99909)
# print(y)  # 1

# z = int("12e10")

# print(z)  # error

# x = int("1234")
# print(x) #1234

# y = int(123e10)
# print(y) #1230000000000

# z = int("123.5")
# print(z)  # error


# x = float(10)
# print(x)  # 10.0

# y = float("123.56")
# print(y)

# x = str("s1")  # 's1'
# y = str(2)  # '2'
# z = str(3.0)  # '3.0'

# print(x)
# print(y)
# print(z)
