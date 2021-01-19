# # Boolean Expressions have only two values True,False(remember Capital T and F)
# # Boolean Expressians are used as output of comparison operators(<,>,==,!=,<=,>=)
# print(5 == 5) # ("5==5" itself is a way to represent a boolian expression True so it is a boolian expression as a whole)
# print(5 == 6)
# print(5 != 5) # Not equal to also there are <=,>=,<,> These are comparison operators and the give a boolian value
# print(5 != 6)
# # Comparisan operators and assignment operators are two completely different types of operators ( = is not same as ==)

# # Logical Operators(and,or,not):
# #  Boolean Expressions are also used with logical operators
# #  Logical operators require boolean Expressions on their left and right
# # 'and' gets True bool on both sides then and operator also gives a True bool as a whole otherwise will give False bool
# # 'or' gets atleast one True on both sides to give True otherwise it will give False
# # 'not' gets True on right side then it will give False and viceversa
# x = 5
# print(x>0 and x<10) # True on both sides so True
# n = 25
# print(n%2 == 0 or n%3 == 0) # False on both sides so False

# Order python Evaluates:
# [()]_[**]_[*,/,//,%]_[+,-]_[==,!=,<=,>=,<,>]_[not]_[and]_[or] -In same precedence which ever is left most evaluates 1st

# The in and not in operators(in,not in):
# The in operator tests if one string is a substring of another
print('p' in 'apple')
print('i' in 'apple')
print('ap' in 'apple')
print('pa' in 'apple')
print('' in 'apple') # Empty string is also a substring of string
print('apple' in 'apple') #'apple is a substring of itself
# The not in operator returns the logical opposite result of in
print('x' not in 'apple')
# We can also use the in and not in operators on lists!
print("a" in ["a", "b", "c", "d"])
print(9 in [3, 2, 9, 10, 9.0])
print('wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing'])
print("a" in ["apple", "absolutely", "application", "nope"]) # in list in operators searches for an item not a substring