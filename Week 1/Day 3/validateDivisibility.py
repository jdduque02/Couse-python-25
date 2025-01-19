def validateDivisibility():
    """
    Checks if the first number is divisible by the second number.
    Asks user for two numbers, then prints a message to the console whether the first number is divisible by the second number.
    """
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 != 0:
        if num1 % num2 == 0:
            return print(f"{num1} is divisible by {num2}")
        else:
            return print(f"{num1} is not divisible by {num2}")
    else:
        return print("You can't divide by 0, try again")
validateDivisibility()