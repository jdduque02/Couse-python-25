def comparingTwoValues():
    """
    Asks the user for two numbers and compares them, then prints the greater one
    """
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 > num2:
        return print(f"{num1} is greater than {num2}")
    else:
        return print(f"{num2} is greater than {num1}")

comparingTwoValues()