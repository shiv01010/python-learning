"""
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
        <	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
        >	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others

"""

# fruits = {"apple", "banana", "cherry"}

# fruits.add("orange")

# print(fruits)

# fruits = {"apple", "banana", "cherry"}

# fruits.clear()

# print(fruits)

# fruits = {"apple", "banana", "cherry"}

# x = fruits.copy()

# print(x)


# Return a set that contains the items that only exist in set x, and not in set y:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.difference(y)

# print(z)  # {"cherry","banana"}

# Remove the items that exist in both sets:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.difference_update(y)

# print(x)  # {"cherry","banana"}


# fruits = {"apple", "banana", "cherry"}

# fruits.discard("banana")

# print(fruits)

# Return a set that contains the items that exist in both set x, and set y:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)

# print(z)

# Remove the items that is not present in both x and y:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)

# print(x)

# Return True if no items in set x is present in set y:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}

# z = x.isdisjoint(y)

# print(z)


# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}

# z = x.issubset(y)

# print(z)


# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}

# z = x.issuperset(y)

# print(z)

# fruits = {"apple", "banana", "cherry"}

# fruits.pop() #removes random element from set

# print(fruits)


# fruits = {"apple", "banana", "cherry"}

# fruits.remove("banana")

# print(fruits)


# Return a set that contains all items from both sets, except items that are present in both sets:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)

# print(z)


# Remove the items that are present in both sets, AND insert the items that is not present in both sets:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)

# print(x)


# Return a set that contains all items from both sets, duplicates are excluded:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.union(y)

# print(z)

# Insert the items from set y into set x:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.update(y)

# print(x)
