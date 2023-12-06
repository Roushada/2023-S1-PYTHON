string=input("enter the string:")
a={}
for i in string:
    if i in a:
       a[i]+=1
    else:
        a[i]=1
        
print(a)  
