dict={}
n1=int(input("total number of elements in dict1:"))
for i in range(n1):
    dict[i]=input("enter elements:")
    print(dict)
print(sorted(dict.items()))
print(sorted(dict.items(),key=lambda item:item[1]))
