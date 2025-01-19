def calculteIMC():
    """
    Calculates the IMC of a person given its weight and height.

    Asks user for input, then prints the IMC to the console.
    """
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    imc = weight / (height ** 2)
    return print(f"The IMC is: {imc}")
calculteIMC()