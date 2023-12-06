lst=[]
x=int(input("enter the length"))
for i in range(x):
    y=input("enter name")
    lst.append(y)
count=0
for x in lst:
    count+=x.lower().count("a")

print(count)
