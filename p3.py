list=[]
n=int(input(" enter the total  number of elemts :"))
for i in range(0,n) :
    y=int(input(" values :"))
    list.append(y)
print(list)
for i in range(0,n):
        if  list [i] > 100:
            list [i]=" over flow"
print (list) 
