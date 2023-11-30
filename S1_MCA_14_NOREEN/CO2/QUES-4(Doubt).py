l=int(input("Enter A Lower Range:"))
u=int(input("Enter A Upper Range:"))
a=[]
a=[x for x in range(l,u+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
print(a)
