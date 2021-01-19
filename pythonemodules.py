# import random
# prob = random.random()       # returns float from 0 to 1
# print(prob)
# diceThrow = random.randrange(1,7)       # return an int, one of 1,2,3,4,5,6
# print(diceThrow)
# Alternate:
from random import randrange, random
prob = random()
print(prob)
dicethrow = randrange(1,7)
print(dicethrow)

prob5 = random()
result5 =prob5*5     # increases the range in floats
print(result5)