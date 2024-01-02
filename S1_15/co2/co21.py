n=int(input("Enter the limit:"))
fact=1
if n>=1:
  for i in range(1,n+1):
      fact*=i
print("factorial of",n,"is",fact)
