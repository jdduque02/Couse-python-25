

def calculateArea():
    """
    Calculates the area of a triangle given its base and height.

    Asks user for input, then prints the area to the console.
    """
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: ")) 
    area = (base * height) / 2
    return print(f"The area of the triangle is: {area}")

calculateArea()
