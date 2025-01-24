def leapYear():
    """
    Determines if a given year is a leap year.

    Prompts the user to input a year, then checks if it is a leap year 
    based on the rules:
    - A year is a leap year if it is divisible by 4, except for end-of-century 
      years which must be divisible by 400.
    - Prints a message indicating whether the input year is a leap year or not.
    """

    year = int(input("Enter a year: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
leapYear()
