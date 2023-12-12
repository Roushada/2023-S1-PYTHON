class circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius
rad1=float(input("Enter the radius of first circle:"))
rad2=float(input("Enter the radius of second circle:"))
obj_circle1=circle(rad1)
obj_circle2=circle(rad2)
a1=obj_circle1.area()
p1=obj_circle1.perimeter()
print("first circle: area=",a1,"and perimeter=",p1)
a2=obj_circle2.area()
p2=obj_circle2.perimeter()
print("second circle:area=",a2,"and perimeter=",p2)
if a1>a2:
    print("Area of first circle is bigger!")
else:
    print("Area of second circle is bigger!")
if p1>p2:
    print("Perimeter of first circle is bigger!")
else:
    print("Perimeter of second circle is bigger!")
