# # string(Immutable):
# a = "green"
# a.upper()
# print(a)
# b = "Strings can be defined as sequential collections of characters. This means that the individual characters that make up a string are in a particular order from left to right."
# sentence = b.split(" ")
# print(sentence) #sentence is a list using " " to slit string
# # List(Mutable)[]:
# mylist1 =[]
# mylist1.append("great") # adds item to the list
# print(mylist1)
# mylist2 = ["kaka","Jack","jill","kaka"]
# finallist1 = mylist1 + mylist2 #Adding lists
# print(finallist1)
# abc = finallist1[0] #abc is a string
# print(type(abc))
# print(finallist1[0]) # prints item at index 0 same applicable to strings and tuples
# print(finallist1[-2]) # prints 2nd item from the right side of list(2nd last item) same applicable to strings and tuples
# print(finallist1[2:4]) # Range does not include item at index 4 same applicable to strings and tuples
# gre = finallist1[2:4]
# print(type(gre)) #gre is a list
# finallist1[3] = "jalal" # item can be reassigned value like this
# print(finallist1)
# print(len(finallist1)) #Gives number of items in list
# print(finallist1.count("kaka")) # Counts number of occurences of item in list
# # Tuples(Immutable)():
# mytuple = () # There can be an empty tuple
# print(type(mytuple))
# mytupletry = ("green") # It is a string not a tuple
# print(type(mytupletry))
# mytuple1 = ("green",) #add a comma at the end of a tuple with single item to make it a tuple
# print(type(mytuple1))

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])
print(len(julia))
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:] #Not even tuple can beat assignment operator
print(julia)
