li=[]
n=int(input("Enter the no of elements:"))
print("Enter",n,"elemments")
for i in range(n):
    ele=int(input())
    li.append(ele)
print("the list is:",li)
for i in range(n):
    if li[i]>100:
        li[i]="over"
print("Edited lis is:",li)
