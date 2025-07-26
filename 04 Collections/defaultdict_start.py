# Demonstrate the usage of defaultdict objects
from collections import defaultdict

def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = defaultdict(int)
    fruitCounter2 = defaultdict(lambda: 10)

    # Count the elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1
        fruitCounter2[fruit] += 1

    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))

    # print the result from fruitCounter2
    for (k, v) in fruitCounter2.items():
        print(k + ": " + str(v))

if __name__ == "__main__":
    main()
