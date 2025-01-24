def primeNumber():
    """
    Checks if the user entered a prime number and prints a message to the console accordingly.
    
    Asks the user for a number, then prints a message to the console whether the number is prime or not.
    """
    number = int(input("Enter a number: "))
    if number > 1 and number % 2 != 0:
        return print("The number is prime")
    else:
        return print("The number is not prime")
primeNumber()