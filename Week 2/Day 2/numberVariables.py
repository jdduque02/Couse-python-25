def numberVariables():
    """
    Ask the user for a number of variables and the values of these variables to print them out in a list.

    This function asks the user for a number of variables, then asks for the value of each variable, and finally it prints out all the values in a list.
    """
    number = int(input("Enter a number variables: "))
    listValues = []
    for i in range(number):
        listValues.append(int(input("Enter a number: ")))
    print(listValues)
numberVariables()