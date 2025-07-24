# Demonstrate the use of variable argument lists


# define a function that takes variable arguments
def addition(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def main():
    # pass different arguments
    print(addition(5,10,23,235,546))
    print(addition(5,10,23))
    print(addition(5,10,23,235,546,74567458))
    
    # pass an existing list
    numbers = [4,5643,5564,232,67,78]
    print(addition(*numbers))


if __name__ == "__main__":
    main()
