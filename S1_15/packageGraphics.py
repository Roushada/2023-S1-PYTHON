from Graphics.circle import circleArea
from Graphics.circle import circlePerimeter
r=int(input("Enter the radius : "))
circleArea(r)
circlePerimeter(r)
print("")

from Graphics.rectangle import rectangleArea
from Graphics.rectangle import rectPeri
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
rectArea(l,b)
rectPeri(l,b)
print("")

from Graphics.dGraphics.cuboid import cuboidArea
from Graphics.dGraphics.cuboid import cuboidPerimeter
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
h=int(input("Enter the height : "))
cuboidArea(l,b,h)
cuboidPerimeter(l,b,h)
print("")

from Graphics.dGraphics.sphere import sphereArea
from Graphics.dGraphics.sphere import spherePerimeter
r=int(input("Enter the radius : "))
sphereArea(r)
spherePerimeter(r)
print("")
