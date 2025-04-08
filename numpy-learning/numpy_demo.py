# What is NumPy?
# NumPy is a Python library used for working with arrays.

# It also has functions for working in domain of linear algebra, fourier transform, and matrices.

# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

# NumPy stands for Numerical Python.


# Why Use NumPy?
# In Python we have lists that serve the purpose of arrays, but they are slow to process.

# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# Arrays are very frequently used in data science, where speed and resources are very important.


# Why is NumPy Faster Than Lists?
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

# This behavior is called locality of reference in computer science.

# This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.


# Which Language is NumPy written in?
# NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

import numpy as np
from numpy import pi

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)
# print(np.__version__)

# arr = np.array(42)

# print(arr)


# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

# These are the most common and basic arrays.

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# print(arr)


# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(arr)


# import numpy as np

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

import numpy as np

# arr = np.arange(15, dtype="complex").reshape(3, 5)
# print(arr)
# print(arr.ndim)
# print(arr.dtype)
# print(arr.shape)
# print(arr.size)
# print(arr.itemsize)
# print(arr.data)
# print(arr.nbytes)

# arr = np.empty((10, 10), dtype="int")
# print(arr)

# arr = np.arange(0, 2, 0.3)
# print(arr)

# arr = np.linspace(0, 2, 9)

# print(arr)

# x = np.linspace(0, 2 * pi, 100)
# print(x)
# f = np.sin(x)
# print(f)

# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# c = a - b
# print(c)

# print(b)

# c = b**2

# print(c)

# c = 10 * np.sin(a)
# print(c)

# d = a < 35

# print(d)

# A = np.array([[1, 1], [0, 1]])
# B = np.array([[2, 0], [3, 4]])
# C = A * B  # elementwise product
# D = A @ B  # matrix product

# print(C)
# print(D)

# E = A.dot(B)  # another matrix product
# print(E)


# rg = np.random.default_rng(1)
# a = np.ones((2, 3), dtype=int)
# b = rg.random((2, 3))
# a *= 3
# print(a)
# b += a
# print(b)
# a += b

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print(b.dtype.name)
c = a + b
print(c)
print(c.dtype.name)

d = np.exp(c * 1j)
print(d)
print(d.dtype.name)
