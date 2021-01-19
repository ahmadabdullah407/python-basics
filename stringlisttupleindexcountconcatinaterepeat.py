# # Concatination(Addition of lists)(+):
# fruit = ["apple","orange","banana","cherry"]
# print([1,2] + [3,4]) #Concatination
# print(fruit+[6,7,8,9]) #Concatination
# # Repitition(Multiplication of lists)(*):
# print((fruit + [0,1])*4) #Repitition (Use parenthisis)
#  # a = ['first'] + ("second","green") # Error List and string/tuple cannot be concatinated together
#  # Count method:
# a = "I have had an apple on my desk before!"
# print(a.count("e")) #Counts characters
# print(a.count("ha")) #Counts substrings too

# z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
# print(z.count("4")) # count also works on list but counts items not characters
# print(z.count(4))
# print(z.count("a"))
# print(z.count("electron"))
# Index:
music = "Pull out your music and dancing can begin" #Index works on strings as well as lists
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]

print(music.index("m")) # tells the index where m is present starts from 0
print(music.index("your")) # tells index at 1st character of substring

print(bio.index("Metatarsal")) # index always gives 1st/left most item it does not tell location of same item coming after
print(bio.index([])) # also searches for empty list
print(bio.index(43)) # also searches integer items
# print(bio.index('great')) # gives error if item not present
# print(music.index("z")) # also gives error for character