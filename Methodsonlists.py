mylist = [5,7,3,9,2]
# Appending (adds new item to the list at the end)(appending mutates the list does not make copy):
# mylist.append(5)
# mylist.append(27) #appended toward the end of the list
# mylist.append(3)
# mylist.append(12)
# print(mylist)

# # Inserting (adds new item right before item present at specified position)
# # does not delete item present at the position but moves item 1 step ahead it is mutation method too
# mylist.insert(1, 2) # takes specified position and item
# print(mylist)
# # count takes an item inside parenthesis and counts in list how many times it appeared
# print(mylist.count(2)) # non mutating
# # index takes an item inside parethesis and tells the index/position it is present at
# print(mylist.index(3)) # non mutating
# # reverse takes the order of item of the list and reverses them
# # it is mutation method too
# mylist.reverse()
# print(mylist)
# # sort takes the items in the list and reorders them from smallest to biggest
# # mutates too
# mylist.sort()
# print(mylist)
# # remove is same as del but it does not take index but item itself
# mylist.remove(5)
# print(mylist)
# # pop removes the last item from the list
# lastitem = mylist.pop() #saves last item in lastitem and also removes last item from amin list
# print(lastitem)
# print(mylist)

# # It is important to remember that methods like append, sort, and reverse all return None.
# # They change the list; they don’t produce a new list. So,
# # while we did reassignment to increment a number, as in x = x + 1,
# # doing the analogous thing with these operations will lose the entire list contents.
# mylist = mylist.sort()   #return none
# print(mylist)

# Append vs Concatinate:
# Concatinate does not mutate a list it only makes another object and reassigns variable to that onject
# As there is no variable pointing to previous object there is no way to approach it anymore
# mylist = mylist+["a"] #Concatination
# origlist = [45,32,88]
# print("origlist:", origlist)
# print("the identifier:", id(origlist))             #id of the list before changes
# newlist = origlist + ['cat']
# print("newlist:", newlist)
# print("the identifier:", id(newlist))              #id of the list after concatentation
# origlist.append('cat')
# print("origlist:", origlist)
# print("the identifier:", id(origlist))
# x+=1 and x+1 =1 are not same things in case of mutable lists += acts as append