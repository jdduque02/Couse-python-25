
def basicOperations():
    """
    This function will take two numbers as input from the user and then perform basic operations of addition, subtraction, multiplication and division on those numbers.

    Parameters:
    None

    Returns:
    A printed statement showing the results of the basic operations of addition, subtraction, multiplication and division of the two numbers.

    """
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    if num2 == 0 or num1 == 0:
        return print('cannot be operated by zero')
    sum = num1 + num2
    subtract = num1 - num2
    multiply = num1*num2
    divide = num1/num2
    return print(f'Number 1: {num1} \nNumber 2: {num2} \nSum: {sum} \nSubtract: {subtract} \nMultiply: {multiply} \nDivide: {divide}')

basicOperations()
