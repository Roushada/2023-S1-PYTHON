import Graphics.rectangle
import Graphics.circle
import Graphics.D_graphics.sphere
import Graphics.D_graphics.cuboid


l1=int(input("Enter the length of rectangle:"))
b1=int(input("Enter the breadth of rectangle:"))
Graphics.rectangle.area(l1,b1)

r1=int(input("Enter the radius of circle:"))
Graphics.circle.area(r1)
Graphics.circle.perimeter(r1)

l2=int(input("Enter the length of cuboid:"))
b2=int(input("Enter the breadth of cuboid:"))
h=int(input("Enter the height of cuboid:"))
Graphics.D_graphics.cuboid.area(l2,b2,h)
Graphics.D_graphics.cuboid.perimeter(l2,b2,h)

r2=int(input("Enter the radius of sphere:"))
Graphics.D_graphics.sphere.area(r2)
Graphics.D_graphics.sphere.perimeter(r2)
