def validateNumberRange():
    """
    Checks if the user entered a number between 10 and 20 and prints a message to the console accordingly.
    """
    number = float(input('Enter a number between 1 and 10: '))
    if number >= 10 and number <= 20:
        print('The number is between 10 and 20')
    else:
        print('The number is not between 10 and 20')
validateNumberRange()