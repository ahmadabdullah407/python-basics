# for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
# #you can put any variable name that iterates we named it name
#     print("Hi", name, "Please come to my party on Saturday!")

# for achar in "Go Spot Go": #you can do same with string
#     print(achar)

# (The range function takes an integer n as input and returns a sequence of numbers,
# starting at 0 and going up to but not including n(i.e. n is len).
# Thus, instead of range(3), we could have written [0, 1, 2])
# print("This will execute first")
# for i in range(3): # range is basically a kind of list that can have length specified in bracket and puts increment in i
#     print(i)
#     print("This line will execute three times")
#     print("This line will also execute three times")
# print("Now we are outside of the for loop!")
#
# print("range(5): ")
# for i in range(5):
#     print(i)
# print("range(0,5): ")
# for i in range(1, 5):
#     print(i)
# # Notice the casting of `range` to the `list`
# print(list(range(5)))
# print(list(range(1,5)))
# # Note: `range` function is already casted as `list` in the textbook but not in python environment
# print(range(5))

# accumulator Variable:
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# accum = 0 # accum is a accumulator variable
# for w in nums:
#     accum = accum + w # it keeps updating with each iteration
# print(accum)
# sec_accum = 0 # Can do the same with range
# for w in range(1,11):
#     sec_accum = sec_accum + w
# print(sec_accum)