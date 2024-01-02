li=[]
n=int(input("Enter the limit:"))
print("Enter the elements:")
for i in range(0,n):
    ele=int(input())
    li.append(ele)
print(li)
sum=0
for i in li:
    sum=sum+i
print("sum=",sum)
    
