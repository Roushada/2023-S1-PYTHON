n=int(input("enter thye limit:"))
n1=0
n2=1
n3=n2
fib=0
count=0
if(n<=0):
    print("enter a valid positive number")
elif(n==1):
    print("fiboacci number upto",n)
    print(n1)
else:
    while count<=n:
        print(n1)
        fib=n1+n2
        n1=n2
        n2=n3
        count=count+1
    
      print(fib)
        
        
        
    

