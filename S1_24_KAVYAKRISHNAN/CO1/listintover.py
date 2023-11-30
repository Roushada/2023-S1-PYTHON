list=[]
n=int(input("enter the number of elements:"))
print("enter",n,"values")
for i in range(n):
    i=int(input())
    list.append(i)

print("the list is:",list)
for i in range(n):
    if list[i]>100:
        list[i]="over"
print(list)
