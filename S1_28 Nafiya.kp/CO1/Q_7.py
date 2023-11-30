list1=[9,5,3,3]
list2=[4,59,6,7,8]
print("list1",list1,"list2",list2)
if(len(list1)==len(list2)):
    print("same length")
sum=0
for i in list1:
    sum=sum+i
print("sum of list1",sum)
sums=0
for i in list2:
    sums=sums+i
print("sum of list2",sums)
if(sum==sums):
    print("the sum of two list are same:",sum)
else:
    print("sum is different")
set1=set(list1)
set2=set(list2)
sets=set1.intersection(set2)
if(len(sets)>0):
    print("common value",sets)
else:
    print("no coomon value")
