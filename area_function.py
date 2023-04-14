import math

def area_of_circle(radius):
    area = math.pi * radius ** 2
    return area
radius = 5
area = area_of_circle(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}")