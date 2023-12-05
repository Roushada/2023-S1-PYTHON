li=[]
n=int(input("Enter the limit of  comma seperated list:"))
print("Enter the colors:")
for i in range(n):
    color=str(input())
    
    li.append(color)
    x=li.split(",")
print(x)
print("first color is",li[0])
print("last color is",li[n-1])
   
    
