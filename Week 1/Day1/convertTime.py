

def convertTime():
    """
        Converts a given time in seconds to hours, minutes and seconds.
        Asks the user to input a time in seconds and prints out the equivalent time in hours, minutes and seconds.
    """
    timeMesurement = int(input('seconds to convert time: '))
    hours = int(timeMesurement) / 3600
    minutes = int(timeMesurement) / 60
    return print(f'{hours} hours and {minutes} minutes and {timeMesurement} seconds')