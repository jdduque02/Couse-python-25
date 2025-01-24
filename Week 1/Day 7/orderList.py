def order():
    """
    Orders a list of friends alphabetically.

    Prints the original list of friends, sorts it alphabetically, and prints the sorted list.

    """
    
    friends = ['Alejo','krathmo', 'Jorge','Juan', 'Pabon']
    print('Original list: ',friends)
    friends.sort()
    print('Sorted list: ',friends)
order()