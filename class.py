class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*self.radius*self.radius
        print("Area is:",area)
    def perimeter(self): 
        perimeter=2*3.14*self.radius
        print("Perimeter is:",perimeter)
ci=Circle(7)
ci.area()
ci.perimeter()
    