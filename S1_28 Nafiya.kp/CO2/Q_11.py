rectangle=lambda l,w:l*w
n=int(input("enter length"))
m=int(input("enter width"))
print("area of rectangle","is",rectangle(n,m))
triangle=lambda b,h:b*h/2
n=int(input("enter the base of triangle"))
m=int(input("enter the height of triangle"))
print("area of triangle is",triangle(n,m))
square=lambda a:a*a
n=int(input("enter the sides of square"))
print("area of square",n,"is",square(n))
