from graphics.circle import circleArea
from graphics.circle import circlePerimeter
r=int(input("enter the radius:"))
circleArea(r)
circlePerimeter(r)
print(" ")
from graphics.rectangle import rectangleArea
from graphics.rectangle import rectanglePerimeter
l=int(input("enter the length of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
rectangleArea(l,b)
rectanglePerimeter(l,b)
print(" ")
from graphics.dgraphics.cuboid import cuboidarea
from graphics.dgraphics.cuboid import cuboidperimeter
l=int(input("enter the length of cuboid:"))
b=int(input("enter the breadth of cuboid:"))
h=int(input("enter the height of cuboid:"))
cuboidarea(l,b,h)
cuboidperimeter(l,b,h)
print(" ")
from graphics.dgraphics.sphere import spherearea
from graphics.dgraphics.sphere import sphereperimeter
r=int(input("enter the radius:"))
spherearea(r)
sphereperimeter(r)
print(" ")
