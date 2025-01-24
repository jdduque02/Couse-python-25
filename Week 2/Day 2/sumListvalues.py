def sumListvalues():
    """
    This function asks the user to input a list of numbers, separated by spaces, 
    and then it prints the sum of the elements in the list.
    """
    arr = list(map(int, input("enter the list of data example: 2 3 6 6 5: ").split()))
    sum = 0
    for num in arr:
        sum += num
    print(sum)
sumListvalues()