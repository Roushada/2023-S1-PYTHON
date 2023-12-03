l1=[]
n=int(input("enter the nmber of elements:"))
for i in range(n):
    value=int(input("enter the elements:"))
    l1.append(value)
new_list=[x for x in l1 if x%2!=0]
print("list removing even numbers:",new_list)
