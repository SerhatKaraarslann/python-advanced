# Demonstrate the usage of Counter objects

from collections import Counter


def main():
    # list of students in class 1
    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah"
              "Kevin", "James", "James", "Melanie", "Penny", "Steve"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    #  Create a Counter for class1 and class2
    counter1 = Counter(class1)
    counter2 = Counter(class2)

    # How many students in class 1 named James?
    print(counter1.get("James")) 
    print(counter1["James"])

    # How many students are in class 1?
    print(counter1.total() + 1)
    print(sum(counter1.values())," Studenten in der Klasse1.")

    # Combine the two classes
    counter1.update(class2)
    print(sum(counter1.values())," Studenten in der Klasse1.")

    # What's the most common name in the two classes?
    print(counter1.most_common(3)) # most common 3 elements

    # Separate the classes again
    counter1.subtract(class2)
    print(sum(counter1.values())," Studenten in der Klasse1.")

    # What's common between the two classes?
    print(counter1 & counter2)

if __name__ == "__main__":
    main()
