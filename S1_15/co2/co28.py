li=[]
n=int(input("Enter the size:"))
print("Enter the elemnts:")
for i in range(0,n):
    ele=input()
    li.append(ele)
print(li)
s=max(li)
x=len(s)
print("longest word length is",x)
