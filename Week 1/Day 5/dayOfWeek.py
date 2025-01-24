def dayWeek():
    """
    This function takes a number from 1 to 7 as input and prints the corresponding
    day of the week in English.

    Parameters
    ----------
    day : int
        Number between 1 and 7
    """
    
    day = int(input("Enter a number between 1 and 7: "))
    if day == 1:
        return print("Monday")
    elif day == 2:
        return print("Tuesday")
    elif day == 3:
        return print("Wednesday")
    elif day == 4:
        return print("Thursday")
    elif day == 5:
        return print("Friday")
    elif day == 6:
        return print("Saturday")
    elif day == 7:
        return print("Sunday")
    else:
        return print("Error")

dayWeek()