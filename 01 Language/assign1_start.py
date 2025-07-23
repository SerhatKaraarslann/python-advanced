# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
x = 5
print(x)

#  the assignment operator is part of an expression
(x := 7)
print(x)

#  The assignment expression is useful for writing concise codeserhat
while (thestr :=input("Value? : ")) != "exit":
    print(thestr)

# Thats the same but the style above is better and easy to read
# thestr = input("Value? : ")
# while thestr != "exit":
#     print(thestr)
#     thestr = input("Value? : ")