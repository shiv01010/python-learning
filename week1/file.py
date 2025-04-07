"""
close()	Closes the file
detach()	Returns the separated raw stream from the buffer
fileno()	Returns a number that represents the stream, from the operating system's perspective
flush()	Flushes the internal buffer
isatty()	Returns whether the file stream is interactive or not
read()	Returns the file content
readable()	Returns whether the file stream can be read or not
readline()	Returns one line from the file
readlines()	Returns a list of lines from the file
seek()	Change the file position
seekable()	Returns whether the file allows us to change the file position
tell()	Returns the current file position
truncate()	Resizes the file to a specified size
writable()	Returns whether the file can be written to or not
write()	Writes the specified string to the file
writelines()	Writes a list of strings to the file

"""

# filename = "demofile.txt"
# bytes = bytes(filename, encoding="utf-8")
# # print(bytes)
# f = open(bytes, "r")
# print(f.read())
# f.close()


# f = open("demofile.txt", "r")
# print(f.fileno())


# f = open("myfile.txt", "a")
# f.write("Now the file has one more line!")
# f.flush()
# f.write("...and another one!")


# f = open("demofile.txt", "r")
# print(f.isatty())

# f = open("demofile.txt", "r")
# print(f.read())

# f = open("demofile.txt", "r")
# print(f.readable())

# Read the first line of the file "demofile.txt":
# f = open("demofile.txt", "r")
# print(f.readline())

# f = open("demofile.txt", "r")
# print(f.readlines())

# Change the current file position to 4, and return the rest of the line:
# f = open("demofile.txt", "r")
# f.seek(4)
# print(f.readline())


# f = open("demofile.txt", "r")
# print(f.seekable())

# f = open("demofile.txt", "r")
# print(f.tell())


# f = open("demofile.txt", "a")
# f.truncate(20)
# f.close()

# # open and read the file after the truncate:
# f = open("demofile.txt", "r")
# print(f.read())

# f = open("demofile.txt", "a")
# print(f.writable())

# f = open("demofile2.txt", "a")
# f.write("See you soon!")
# f.close()

# # open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())


# f = open("demofile3.txt", "a")
# f.writelines(["See you soon! \n", "Over and out.\n"])
# f.close()

# # open and read the file after the appending:
# f = open("demofile3.txt", "r")
# print(f.read())
