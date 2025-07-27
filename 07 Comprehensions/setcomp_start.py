# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # build a set of unique Fahrenheit temperatures
    ftemps1 = [( t * 9/5) + 32 for t in ctemps] # ein list and hier kann ein Wert beliebig viel Mals kommen
    ftemsp2 = {(t * 9/5) + 32 for t in ctemps} # bei der set kommt ein key nur ein mal 
    print(ftemps1)
    print(ftemsp2)

    # build a set from an input source
    sTemp = "teh quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in sTemp if not c.isspace()}
    print(chars)

if __name__ == "__main__":
    main()
