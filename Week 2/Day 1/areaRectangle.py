def areaRectangle():
    """
    Calculates the area of a rectangle given its length and width.

    Asks user for input, then prints the area to the console.
    """
    
    length= float(input("Enter the length of the rectangle: "))
    width= float(input("Enter the width of the rectangle: "))
    area = length * width
    return print(f"The area of the rectangle is: {area}")
areaRectangle()