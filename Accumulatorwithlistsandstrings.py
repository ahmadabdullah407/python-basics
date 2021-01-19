# Accumulator Pattern with Lists:
# numbs = [5, 10, 15, 20, 25]
# for i in range(len(numbs)):
#     a = numbs[i] + 5
#     numbs.remove(numbs[i])
#     numbs.insert(i, a)
# print(numbs)

# Accumulator Pattern with Strings:
s = input("Enter some text")
ac = ""
for c in s:
    ac = ac + c + "-" + c + "-"
print(ac)