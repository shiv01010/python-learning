# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')


# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


"""
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

"""

# a = "Hello, World!"
# print(a[1])

# for x in "banana":
#     print(x)

# a = "Hello, World!"
# print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword in.

# txt = "The best things in life are free!"
# print("free" in txt)  # True


# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.
# b = "Hello, World!"
# print(b[2:5])  # llo #index 5 is excluding
# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[2:])

# Use negative indexes to start the slice from the end of the string:

# b = "Hello, World!"
# print(b[-5:-2])  # orl


# UpperCase

# a = "Hello, World!"
# print(a.upper())

# LowerCase

# a = "Hello, World!"
# print(a.lower())

# Remove white spaces

# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# a = "  tapanai open ai  "
# print(a.strip())


# REPLACE
# returns a new string replaced with substring with provided number of occurences

# a = "HHello, World!"
# print(a.replace("H", "J", 1))

# split
# splits the string with given seperator and returns a list
# a = "Hello, World!"
# print(a.split(","))  # returns ['Hello', ' World!']

# by default splits using whitespace
# a = "Hello World"
# print(a.split())

# a = "max split demo to test what it does"
# print(a.split(sep=" ", maxsplit=2))


# string concat
# a = "Hello"
# b = "World"
# c = a + b
# print(c)


# age = 36
# txt = "My name is John, I am " + age
# print(txt) #error


# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

# age = 27
# txt = f"My name is John, I am {age}"
# print(txt)


# String methods
# Python has a set of built-in methods that you can use on strings.
# All string methods return new values. They do not change the original string.
"""

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

"""
# x = "abcdefgAAAAA"

# print(x.capitalize())
# print(x.casefold())
# print(x.lower())

# difference between casefold and lower
# s1 = "Straße"
# s2 = "STRASSE"

# print(s1.lower() == s2.lower())  # False
# print(s1.casefold() == s2.casefold())  # True

# x = "tapan ai tapan ai open ai"
# print(x.count("pan"))
# print(x.encode())

# txt = "My name is Ståle"

# print(txt.encode(encoding="ascii", errors="ignore"))

# x = "bcvnf"
# print(x.endswith("nf"))

# x = "tapan is react king"
# print(x.find("is")) #6

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price=50))


# txt = "For only {price:.2f} dollars! offer valid until {day}"
# map = {"price": 45, "day": "friday"}
# print(txt.format_map(map))

# txt = "Hello Sam!"
# mytable = str.maketrans("S", "P")
# print(mytable)
# print(txt.translate(mytable))

# txt = "I am learning python"
# x = txt.partition("learning")
# print(x)


txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)
