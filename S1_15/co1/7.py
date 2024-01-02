li1=[9,2,3,4]
li2=[6,7,9,8]
if(len(li1)==len(li2)):
    print("same length")
else:
    print("Different length")
sum1=0
for i in li1:
    sum1=sum1+i
print("sum of list1=",sum1)
sum2=0

for i in li2:
    sum2=sum2+i
print("sum of list2=",sum2)
if(sum1==sum2):
    print("same sum",sum1)
else:
    print("different sum")

set1=set(li1)
set2=set(li2)
sets=set1.intersection(set2)
if(len(sets)>0):
    print("same value exists",sets)
else:
    print("No same value")

