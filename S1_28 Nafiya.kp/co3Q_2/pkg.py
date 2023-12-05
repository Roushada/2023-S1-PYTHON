import graphics.circle
import graphics.rectangle 
import graphics.threedgraphics.cuboid
import graphics.threedgraphics.sphere 
import graphics.threedgraphics.sphere 
l1=int(input("enter the length of rectangle:"))
b1=int(input("enter the breadth of rectangle:"))
graphics.rectangle.area(l1,b1)
graphics.rectangle.perimeter(l1,b1)
r1=int(input("enter the radius of circle:"))
graphics.circle.area(r1)
graphics.circle.perimeter(r1)
l2=int(input("enter the lenngth of cuboid:"))
b2=int(input("enter the breadth of cuboid:"))
h=int(input("enter the height of cuboid:"))
graphics.threedgraphics.cuboid.area(l2,b2,h)
graphics.threedgraphics.cuboid.perimeter(l2,b2,h)
r2=int(input("enter the radius of sphere:"))
graphics.threedgraphics.sphere.area(r2)
graphics.threedgraphics.sphere.perimeter(r2)
