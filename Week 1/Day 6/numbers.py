def numbersValues ():
    """
    Prints numbers from 1 to 100 and calculates their sum.

    This function iterates through numbers 1 to 100, prints each number, 
    and calculates the cumulative sum of these numbers. Finally, it prints 
    the total sum.
    """

    sum = 0
    for i in range(1, 101):
        print(i)
        sum += i
    print(f"Sum: {sum}")

numbersValues()