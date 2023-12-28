str=input("Enter a string:")
a={}
for i in str:
    if i in a:
        a[i]+=1
    else:
        a[i]=1      
print(a)
