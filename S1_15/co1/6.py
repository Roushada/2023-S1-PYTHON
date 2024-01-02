li=[]
n=int(input("Enter the limit:"))
print("Enter the elements:")
for i in range(n):
    ele=input()
    li.append(ele)
print(li)
counts=0
for i in li:
    counts=counts+i.lower().count("a")
print(counts)
