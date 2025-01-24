def addItem():
    """
    Prompts the user to enter an item, adds it to a list, and prints the list.

    This function creates an empty list, then appends a user-provided item to it 
    before printing the list to the console.
    """

    item = input('Enter an item: ')
    items = []
    items.append(item)
    print(items)
addItem()