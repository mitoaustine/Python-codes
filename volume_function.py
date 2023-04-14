import math

def vol_of_cylinder(radius,height):
    base_area = math.pi * radius ** 2
    vol = base_area * height
    return vol
radius = 2
height = 5
vol = vol_of_cylinder(radius,height)
print(f"The volume of a cylinder with radius {radius} and height {height} is {vol:.2f}")