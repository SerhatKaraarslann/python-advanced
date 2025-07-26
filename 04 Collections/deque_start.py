# deque objects are like double-ended queues

import collections
import string


def main():
    
    # initialize a deque with lowercase letters
    my_dequeu = collections.deque(string.ascii_lowercase)
    print(my_dequeu)

    # deques support the len() function
    print("Anzahl der Elemente : ",len(my_dequeu)) # 26

    # deques can be iterated over
    iterable = iter(my_dequeu)
    print(next(iterable))

    while True:
        try:
             print(next(iterable))
        except StopIteration:
            break

    for element in my_dequeu:
        print(element.upper(), end= ",")

    print("\n")

    # manipulate items from either end
    my_dequeu.pop() # pop from right, standart
    my_dequeu.popleft()

    print(my_dequeu)

    my_dequeu.append(5) # append on the right, standart
    my_dequeu.appendleft(1)

    print(my_dequeu)

    # rotate the deque

    my_dequeu.rotate(5) # last 5 elements on the start
    print(my_dequeu)

    my_dequeu.rotate(15) # last 15 elements on the start, dequeue has been rotated
    print(my_dequeu)

if __name__ == "__main__":
    main()
