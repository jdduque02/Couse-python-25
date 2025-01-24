def totalSum():
    """
    This function is used to calculate the sum of a set of numbers entered by the user,
    when the user enters 0, the sum is printed and the function is finished.
    """
    validate = False
    sum = 0
    while validate == False:
        num = float(input("enter the numbers you wish to add to end the accumulation enter 0: "))
        if num == 0:
            validate = True
            return print(f"Sum: {sum}")
        else:
            sum += num
totalSum()