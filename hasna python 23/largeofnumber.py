x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))
print(x,y,z)
if x>y and x>z:
    print(x," is the largest one")
elif y>x and y>z:
    print(y," is the greater one")
else:
    print(z," is the greater number")
    
