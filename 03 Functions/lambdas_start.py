# Use lambdas as in-place functions


def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # Use regular functions to convert temps
    print("Fahrenheit to Celcius : ",ftemps,list(map(FahrenheitToCelsisus,ftemps)))
    print("Celsius to Fahrenheit : ", ctemps, list(map(CelsisusToFahrenheit,ctemps)))

    # Use lambdas to accomplish the same thing
    print("Fahrenheit to Celcius : ",ftemps,list(map(lambda x : (x-32) *5/9,ftemps)))
    print("Celsius to Fahrenheit : ", ctemps, list(map(lambda x : (x * 9/5) + 32,ctemps)))


if __name__ == "__main__":
    main()
