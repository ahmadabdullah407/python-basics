# # Split:
# song = "The rain in Spain..."
# wds = song.split() # get rids of spaces and splits string at space and makes a list
# print(wds)
#
# song = "The rain in Spain..."
# wds = song.split('ai') # will get rid of argument specified and cuts string at argument
# print(wds)
# Join:
wds = ["red", "blue", "green"]
glue = ';' # Glue is the variable that comes between items of list when they join
s = glue.join(wds) # Specify The lest in parenthisis you want to join
print(s)
print(wds) # join still does not change the original value of the list

print("***".join(wds)) # Another method to join list
print(wds)
print(type(wds))
wds= "".join(wds) #how to change list to string with joining
print(type(wds))
print(wds)