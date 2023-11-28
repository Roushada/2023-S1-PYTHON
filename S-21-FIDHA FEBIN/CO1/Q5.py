lst=[]
n=int(input("enter the number of elements"))
print("enter",n,"values")
for i in range(n):
    i=int(input())
    lst.append(i)

print("the list is:",lst)
for i in range(n):
    if lst[i]>100:
        lst[i]="over"
print(lst)
