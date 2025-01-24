def multiplicationTable():
    """
    Shows the multiplication table of a given number.
    
    Asks the user for a number and then prints the multiplication table of that number from 1 to 10.
    """
    
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")
multiplicationTable()