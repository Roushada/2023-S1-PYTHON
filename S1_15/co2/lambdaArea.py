square=lambda a:a*a
x=int(input("Enter the side of square:"))
print("The area of square is",square(x))

triangle=lambda b,h:0.5*b*h
p=int(input("Enter the base of triangle:"))
q=int(input("Enter the height of triangle:"))
print("The area of triangle  is",triangle(p,q))

rectangle=lambda l,b:l*b
u=int(input("Enter the length of rectangle:"))
v=int(input("Enter the breadth of rectangle:"))
print("The area of rectangle is",rectangle(u,v))
