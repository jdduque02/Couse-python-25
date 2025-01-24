def convertCelsiusFahrenheit():
    """
    Asks the user for a temperature in Celsius and returns the temperature in Fahrenheit
    """
    celsiys = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsiys * 1.8) + 32
    return print(f"The temperature in Fahrenheit is: {fahrenheit}")
convertCelsiusFahrenheit()