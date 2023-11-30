n = int(input("Enter the number of terms for Fibonacci series: "))
a= 0
b= 1
print("Fibonacci Series:")
print(a)
print(b)
for i in range(1,n-1):
    a,b=b,a+b
    print(b)
