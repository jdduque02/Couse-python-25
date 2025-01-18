def dataType():
    """
    Function to get user data and print a greeting message.

    Gets user data like first name, last name, age and height in cm, and prints a greeting message.

    """
    name = input('Enter your first name: ')
    lastName = input('Enter your last name: ')
    age = input('Enter your age: ')
    height = input('Enter your height in cm: ')
    return print(f'Hi! {name} {lastName}, your age is {age}, your height is {height} cm')

dataType()