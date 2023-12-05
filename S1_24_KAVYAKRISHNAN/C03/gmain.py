import graphics.circle
from graphics.rectangle import*
import graphics.threedgraphics.cuboid
from graphics.threedgraphics.sphere import area
from graphics.threedgraphics.sphere import perimeter
print("Rectangle")
l1=int(input("enter the length of rectangle:"))
b1=int(input("enter the breadth of rectangle:"))
graphics.rectangle.area(l1,b1)
graphics.rectangle.perimeter(l1,b1)
print("Circle")
r1=int(input("enter the radius of circle:"))
graphics.circle.area(r1)
graphics.circle.perimeter(r1)
print("Cuboid")
l2=int(input("enter the length of cuboid:"))
b2=int(input("enter the breadth of cuboid:"))
h=int(input("enter the height of cuboid:"))
graphics.threedgraphics.cuboid.area(l2,b2,h)
graphics.threedgraphics.cuboid.perimeter(l2,b2,h)
print("Sphere")
r2=int(input("enter the radius of sphere:"))
graphics.threedgraphics.sphere.area(r2)
graphics.threedgraphics.sphere.perimeter(r2)
