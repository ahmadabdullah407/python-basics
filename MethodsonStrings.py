# None of these methods mutate the strings:
ss ="  Hello World  "

# #upper and lower Capitalize and decapitalize all the letters in string:
# print(ss.upper())
# tt = ss.lower()
# print(tt)
# print(ss) # as ss does not change
# # count, strip and replace:
# els = ss.count("l") # Counts number of times a substring appears in the string
# print(els)
# print("***"+ss.strip()+"***") # strips the spaces from both ends but does not strip spaces in the middle
# new = ss.replace("o","***") # replaces the 1st item specified with the item given
# print(new)

# String format() method:
# scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
# for person in scores:
#     name = person[0]
#     score = person[1]
#     print("Hello {}. Your score is {}.".format(name, score)) # better use f strings easier parameter values are passed at {}

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
# :.2f represents float upto 2 decimals
# it also rounds the value
# if we do not put :.xf it interpretar chooses
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)

