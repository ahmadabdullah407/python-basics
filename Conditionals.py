# Binary selection:
# This selection contains if and else. if boolean returns True if is executed otherwise else is executed
# Unary Selection:
# In this selection else is omitted entirely if condition is True if is executed otherwise regular pattern is followed

# Nested conditionals:
x = 10
y = 10
if x < y:
    print("x is less than y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("x and y must be equal")

# Chained Conditionals:
# Python provides an alternative way to write nested selection such as the one shown in the previous section.
# This is sometimes referred to as a chained conditional.
# elif statements check 2 things in order to execute.
# 1) it checks that all of if and elif conditions above it were false
# 2) it checks the condition it is presented with is True
# Remember final else condition will only run if all above if and elif conditions are False
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")


