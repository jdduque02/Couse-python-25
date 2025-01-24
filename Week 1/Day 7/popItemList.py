def popFrieds():
    """
    Removes a friend from the list at a specified index and prints the updated list.

    This function prompts the user to input the index of the friend to be deleted from 
    the predefined list of friends, removes the friend at that index, and then prints 
    the updated list to the console.
    """

    friends = ['Alejo','krathmo', 'Jorge','Juan', 'Pabon']
    elementDeleted = int(input('Enter the number of the element you want to delete: '))
    friends.pop(elementDeleted)
    print(friends)
popFrieds()
