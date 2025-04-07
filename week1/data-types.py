"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

# str = "str"
# print(str)


# x = 9
# print(type(x))
# x = 9.0
# print(type(x))
# x = 45j
# print(x, type(x))  # complex

# x = ["csk", "mi", "rcb"]
# x[1] = "dc"
# print(x, type(x))

# y = ("csk", "mi", "rcb", "dc")
# print(type(y))

# z = range(0, 33)

# print(z, type(z))

# z = {"tapan": 1, "ai": 2, "openai": "3"}
# z.__setitem__("56", 56)
# print(z, type(z), z.get("tapan"))

# x = {7, 7, 8, 9, "orange"}
# x.add(5)
# print(x, type(x))

# z = frozenset({"apple", "banana", "orange"})
# z.add("5")
# print(z, type(z))

# a = True
# print(a, type(a))

# x = bytes([65, 66, 67, 68])
# print(x, type(x))

# print(x[0])


# y = "tapan"
# # convert string to bytes
# b = y.encode("utf-8")
# print(y, b, b[0])

# ba = bytearray([65, 66, 67, 68])  # "ABCD"
# print(ba)  # Output: bytearray(b'ABCD')

# # Modifying a byte
# ba[0] = 97  # Changing 'A' (65) to 'a' (97)
# print(ba)  # Output: bytearray(b'aBCD')

# # Appending a byte
# ba.append(69)  # Appends 'E' (ASCII 69)
# print(ba)  # Output: bytearray(b'aBCDE')

# # Convert bytearray back to bytes
# b = bytes(ba)
# print(b)  # Output: b'aBCDE'


# Creating a memoryview of a bytearray
# ba = bytearray([97, 98, 99, 100, 101, 102])
# mv = memoryview(ba)

# Accessing bytes using memoryview
# print(mv[0])  # Output: 97

# Slicing a memoryview
# sub_mv = mv[1:4]  # Creates a view, does not copy
# print(sub_mv.tolist())  # Output: [98, 99, 100]

# Modifying the original bytearray via memoryview
# mv[1] = 65
# print(ba)  # Output: bytearray(b'aAcdef') (modified original data)
