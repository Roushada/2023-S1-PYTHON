list1=[]
n=int(input("enter the number of elements"))
print("enter the elements")
for i in range(0,n):
          ele=int(input())
          list1.append(ele)
list2=[]
m=int(input("enter the no of elements"))
print("enter the elements")
for i in range(0,m):
      ele=int(input())
      list1.append(ele)
print("the list are of")
if (len(list1)==len(list2)):
    print("samesize")
else:
    print("different size")
sum=0
for i in list1:
    sum=sum+1
print("sum of list1",sum)
sums=0
for i in list2:
    sums=sums+1
print("sum of list2=",sums)    
    
          

