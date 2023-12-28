square=lambda a:a**2
rectangle=lambda l,w:l*w
triangle=lambda b,h:0.5*b*h

a=int(input("Enter the sides of square:"))
print("Area of a square:",square(a))
print('')

l=int(input("Enter the length of rectangle:"))
w=int(input("Enter the width of rectangle:"))
print("Area of a rectangle:",rectangle(l,w))
print('')

b=int(input("Enter the base of triangle:"))
h=int(input("Enter the height of tiangle:"))
print("Area of a triangle:",triangle(b,h))


