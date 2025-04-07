# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().


# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))


# We can also use a for loop to iterate through an iterable object:

# mytuple = ("apple", "banana", "cherry")

# for x in mytuple:
#     print(x)


# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):


# class MyNums:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 5:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration


# myclass = MyNums()
# myiterator = iter(myclass)

# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
