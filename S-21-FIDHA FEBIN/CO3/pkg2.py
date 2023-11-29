import graphics.circle 
from graphics.rectangle import*
import graphics.threeDgraphics.cuboid
from graphics.threeDgraphics.sphere import area
from graphics.threeDgraphics.sphere import perimeter
l1=int(input("enter the length of rectangle:"))
b1=int(input("enter the breadth of rectangle:"))
graphics.rectangle.area(l1,b1)
graphics.rectangle.perimeter(l1,b1)
r1=int(input("enter the radius of circlr:"))
graphics.circle.area(r1)
graphics.circle.perimeter(r1)
l2=int(input("enter the length of cuboid:"))
b2=int(input("enter the breadt of cuboid:"))
h=int(input("enter the height of cuboid:"))
graphics.threeDgraphics.cuboid.area(l2,b2,h)
graphics.threeDgraphics.cuboid.perimeter(l2,b2,h)
r2=int(input("enter the radius of sphere:"))
graphics.threeDgraphics.sphere.area(r2)
graphics.threeDgraphics.sphere.perimeter(r2)
