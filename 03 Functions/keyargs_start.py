# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2, *, suppressExp = False):
        pass


def main():
    # try to call the function without the keyword
    myFunction(1, 2, suppressExp = False) # we dont have to enter this 3. parameter however, if we give this, we have to give it with keyword  
    myFunction(1, 2) # or like that

if __name__ == "__main__":
    main()
