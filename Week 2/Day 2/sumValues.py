def sumValues():
    """
    Asks the user for two numbers and prints their sum.

    Parameters:
    None

    Returns:
    A printed statement showing the sum of the two numbers.
    """
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    sum = num1 + num2
    print(f'The sum of {num1} and {num2} is {sum}')
sumValues()