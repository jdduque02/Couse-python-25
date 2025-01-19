def increaseOrDecrease():
    """
    Prints out numbers from 1 to a given number, or from a given number down to 1.

    Asks the user for a number and then asks if they want to count up from 1 to that number, or down from that number to 1.

    """
    number = int(input("Enter value: "))
    options = int(input('Select one option: \n 1. increase by 1 \n 2. decrease by 1 \n Enter Option: '))
    if options == 1:
        for i in range(1, number + 1):
            print(i)
    elif options == 2:
        for i in range(number, 0, -1):
            print(i)
    return

increaseOrDecrease()