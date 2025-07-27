# Demonstrate how to use list comprehensions
import math

def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # Perform a mapping and filter function on a list
    evenSquared =list(map(lambda e : e**2, evens))
    print(evenSquared)

    oddsSquareRoot = list(map(lambda t: math.sqrt(t),odds))
    print(oddsSquareRoot)

    oddsSquareRoot = list(map(lambda t: math.sqrt(t),filter(lambda x : x > 4 and x < 16,odds)))
    print(oddsSquareRoot)

    # Derive a new list of numbers frm a given list
    evenSquared = [e ** 2 for e in evens] # gleich wie lambda ausdruck aber besser lesbar und einfacher zu implementeiren
    print(evenSquared)

    oddsSquareRoot = [math.sqrt(t) for t in odds ]
    print(oddsSquareRoot)

    # Limit the items operated on with a predicate condition

    evenSquared = [ e**2 for e in evens if e > 4 and e < 10]
    print(evenSquared)

    oddsSquareRoot = [math.sqrt(t) for t in odds if t > 4 and t < 16]
    print(oddsSquareRoot)

if __name__ == "__main__":
    main()
