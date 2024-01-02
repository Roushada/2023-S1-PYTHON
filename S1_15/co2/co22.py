n=int(input("Enter the limit:"))
n1=0
n2=1
sum=0
print("fibonacci series:")

for i in range(0,n):

    print(sum)
    n1=n2
    n2=sum
    sum=n1+n2
