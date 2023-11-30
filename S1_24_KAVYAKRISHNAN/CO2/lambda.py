print("//Square//")
square=lambda x:x**2
a=int(input("enter length:"))
print("area of square",a,"is:",square(a))

print("//Rectangle//")
rectangle=lambda x,y:x*y
l=int(input("enter length:"))
b=int(input("enter breadth:"))
print("area of rectangle length:",l,"breadth:",b,"is:",rectangle(l,b))

print("//Triangle//")
triangle=lambda x,y:(1/2)*x*y
h=int(input("enter height:"))
w=int(input("enter width:"))
print("area of rectangle height:",h,"width:",w,"is:",triangle(h,w))
