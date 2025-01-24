from random import *
def listRandomNumbers():
    """
    Generates and prints a list of random integers.

    Prompts the user to enter the desired length of the list, then generates a list of random integers
    between 1 and 10 with the specified length. Finally, prints the generated list to the console.
    """

    length = int(input("Enter the length of the list: "))
    list = []
    for i in range(length):
        list.append(randint(1, 10))
    print(list)
listRandomNumbers()