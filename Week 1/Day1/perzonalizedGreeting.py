from datetime import datetime


def perzonalizedGreeting():
    """
    Prompts the user to enter their name and then prints a personalized greeting
    along with the current time in hours, minutes, and seconds.
    """

    name = str(input('Enter your name: '))
    return print(f"Hi, {name}! are the { datetime.now().hour}:{datetime.now().minute}:{ datetime.now().second} o'clock")

perzonalizedGreeting()