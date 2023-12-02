list1=[5,6,2,8,3]
list2=[2,4,6,9,3,5]
print("list1=",list1)
print("list2=",list2)

print("Length of list1&2:")
print(len(list1))
print(len(list2))
if len(list1)==len(list2):
    print("Both have same length ")
else :
    print("Both have different length.")

print("Sum of list1&2:")
print(sum(list1))
print(sum(list2)) 
if sum(list1)==sum(list2):
    print("Both have same sum")
else :
    print("Both have different sum.")

print("Commen numbers in the list1&2:")
for i in list1:
    if i in list2:
        print(i)




