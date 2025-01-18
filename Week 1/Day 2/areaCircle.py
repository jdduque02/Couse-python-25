import math

def areaCircle():
    """
    Calculates the area of a circle given its radius.

    Asks user for input, then prints the area to the console.
    """
    radio = float(input('Enter the radius of the circle: '))
    area = math.pi * (radio ** 2)
    return print(f"The area of the circle is: {area}")
areaCircle()