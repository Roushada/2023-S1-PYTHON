from graphics.circle import circleArea
from graphics.circle import circlePerimeter
r=int(input("Enter the radius:"))
circleArea(r)
circlePerimeter(r)
print("")

from graphics.rectangle import rectangleArea
from graphics.rectangle import rectanglePerimeter
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
rectangleArea(l,b)
rectanglePerimeter(l,b)
print("")

from graphics.Dgraphics.cuboid import cuboidArea
from graphics.Dgraphics.cuboid import cuboidPerimeter
l=int(input("Enter the length of cuboid:"))
b=int(input("Enter the breadth of cuboid:"))
h=int(input("Enter the height of cuboid:"))
cuboidArea(l,b,h)
cuboidPerimeter(l,b,h)
print("")

from graphics.Dgraphics.sphere import sphereArea
from graphics.Dgraphics.sphere import spherePerimeter
r=int(input("Enter the radius of sphere:"))
sphereArea(r)
spherePerimeter(r)
