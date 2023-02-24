def vol_of_cylinder(radius):
    pie=3.14
    vol=radius**2*pie*height
    return vol
radius=float(input("enter the radius :"))
height=float(input("enter the height :"))
print("The vol of the cylinder is",vol_of_cylinder(radius))