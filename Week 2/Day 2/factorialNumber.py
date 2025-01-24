def factorialNumber ():
    """
    Calculates the factorial of a number.

    Asks the user for a number, then prints its factorial to the console.

    """
    factorial = int(input("Enter a number: "))
    result = 1
    for i in range(1, factorial + 1):
        result *= i
    return print(f"The factorial of {factorial} is: {result}")

factorialNumber()