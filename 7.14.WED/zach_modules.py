from math import pi

def houseArea(length, width):
    """
    Given arguments for length & width, calculates the area of a house into sq ft.
    """
    area = length * width
    print(f"The area of this house is: {area} sq ft.")

def circumference(radius):
    """
    Given argument for radius, cauculates the curcumference of a circle.
    """
    circ = pi*2*radius
    print(f"The circumference of this circle is: {circ}.")