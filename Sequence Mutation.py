# # Some DataTypes are mutable and some are not
# # Lists are Mutable:
# fruit = ["banana", "apple", "cherry"]
# print(fruit)
# fruit[0] = "pear"
# fruit[-1] = "orange"
# print(fruit)

# # Using slicing operator we can  update several items at once:
# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# alist[1:3] = ['x', 'y']
# print(alist)
# # We do not require the things to be add in be the same length as things to be removed
# # We can also use the reassignment to delete values:
# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# alist[1:3] = []
# print(alist)
# # # We can also use reassignment to add new values without removing any:
# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# alist[1:1] =['g']
# print(alist)

# # Strings are immutable:
# greeting = "Hello, world!"
# greeting[0] = 'J'            # ERROR!
# print(greeting)
# Strings are immutable, which means you cannot change an existing string.
# The best you can do is create a new string that is a variation on the original.
# greeting = "Hello, world!"
# greeting = 'J' + greeting[1:] # The right way nothing can beat assignment operator
# print(greeting)

# Tuples are also immutable:
# they have to be treated same as strings

# # del operator:
# a = ['one', 'two', 'three']
# del a[1]
# print(a)
# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# del alist[1:5] # We can delete whole sequence of items via del
# print(alist)

# # Object and References:
# # In case of immutable objects if you assign two variables same object value,
# # They refer to same object instead of refering to two identical objects
# a = "banana"
# b = "banana"
# print(id(a))
# print(id(b))
# print(a is b)
# # That is not the case with mutable objects
# a = [81,82,83]
# b = [81,82,83]
# print(a is b) # is operator compares two variables and checks if the have been assigned to same object
# print(a == b) # == operator compares two objects and checks if both have same value
# print(id(a))
# print(id(b))

# # Aliasing:
# # Making two variables alias of each other means assigning them both same object by assignment operator
# # if Two variables are alias of each other mutating ones value will automatically mutate others
# a = [81,82,83]
# b = [81,82,83]
# print(a is b)
# b = a
# print(a is b)
# b[0] = 5
# print(a)
# # it is safer to avoid aliasing when you are working with mutable objects.
# # Of course, for immutable objects, there’s no problem.
# # That’s why Python is free to alias strings and integers when it sees an opportunity to economize.

# Cloning Lists:
# As assignment operator will not make a clone of object instead it will assign two variables same object
# a = [81,82,83]
# b = a[:]       # make a clone using slice
# print(a == b)
# print(a is b)
# b[0] = 5
# print(a)
# print(b) # only b is affected

# alist = [4,2,8,6,5]
# blist = alist * 2 # In this case as the object value has changed so python will not assign same object to blist
# blist[3] = 999
# print(alist)

# # why not use += in mutable objects
# sent = ["great", 2]
# phrase = sent
# phrase2 = sent
# phrase = phrase + [3] # This style makes a new oject so sent is safe
# print(phrase)
# print(sent)
# phrase2 += [3] # += causes same object to mutate
# print(sent)

# That is why mutation is destructive

