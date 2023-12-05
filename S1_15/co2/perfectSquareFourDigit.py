def generate(start,end):
    li=[]
    for i in range(start,end+1):
        if all(int(x)%2==0 for x in str(i)):
            if(int(i**0.5)**2==i):
               li.append(i)
            return li
st=1000
en=9999
result=generate(st,en)
print(result)
