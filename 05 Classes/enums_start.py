# define enumerations using the Enum base class
from enum import Enum, unique, auto
@unique #With this we can't have a value more than 1 time
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    KIWI = 5
#   TEST = 1
    PEAR = auto() # automatisch next Value, auto increment
    BERRY = auto()

def main():
    pass

    # enums have name and value properties
    print(Fruit.BANANA)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))


    print(Fruit.APPLE.name, Fruit.APPLE.value)
    print(Fruit.KIWI.name, Fruit.KIWI.value)

    # print the auto-generated value
    print(Fruit.PEAR.name, Fruit.PEAR.value) 
    print(Fruit.BERRY.name, Fruit.BERRY.value)

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])
    print(myFruits)

if __name__ == "__main__":
    main()
