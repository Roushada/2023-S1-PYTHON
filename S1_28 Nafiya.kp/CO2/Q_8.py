list=[]
n=int(input("enter the number of words:"))
for i in range(0,n):
    words=input("enter a word:")
    list.append(words)
print(list)
x=max(list)
print(x)
print("the length of longest word is:",len(x))

    
