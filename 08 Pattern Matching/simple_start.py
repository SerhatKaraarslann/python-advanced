x = 0
#x = 8

# Literal patterns are explicit values: integers, strings, Booleans, etc
match x:
    case 0 :
        print("Zero")
    case 1 :   
        print("One")
    case "Zero":
        print(0)
    case None:
        print("Nothing")
    case _ : #case Default geht auch
        print("No match")