def favoriteNumber():
    """
    Gets user data and prints a greeting message.

    Gets user data like username and favorite number, and prints a greeting message.

    """
    username = input("Enter your name: ")
    favoriteNumber = input("Enter your favorite number: ")
    return print(f"Hi {username}! Your favorite number is {favoriteNumber}")
favoriteNumber()