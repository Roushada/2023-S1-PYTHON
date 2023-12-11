from graphics.circle import circleArea
from graphics.circle import circlePerimeter
r=int(input("Enter the radius : "))
circleArea(r)
circlePerimeter(r)
print("")

from graphics.rectangle import rectArea
from graphics.rectangle import rectPerimeter
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
rectArea(l,b)
rectPerimeter(l,b)
print("")

from graphics.dGraphics.cuboid import cuboidArea
from graphics.dGraphics.cuboid import cuboidPerimeter
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
h=int(input("Enter the height : "))
cuboidArea(l,b,h)
cuboidPerimeter(l,b,h)
print("")

from graphics.dGraphics.sphere import sphereArea
from graphics.dGraphics.sphere import spherePerimeter
r=int(input("Enter the radius : "))
sphereArea(r)
spherePerimeter(r)
print("")
 
