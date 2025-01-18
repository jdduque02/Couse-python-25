def div(num1, num2):
    """
    This function divides two numbers and returns the result.
    If the second number is 0, it asks the user to input the two numbers again.
    """
    if(num2 == 0):
        print("You can't divide by 0, try again")
        numNew1 = float(input("Enter the first number: "))
        numNew1 = float(input("Enter the second number: "))
        return div(numNew1, numNew1)
    else:
        result = num1 / num2
        return print(f"The result is: {result}")
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

div(num1, num2)