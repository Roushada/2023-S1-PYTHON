list=[]
x=input("enter color seperated by commas:")
list=a.split(",")
if len(list)>=1:
    first=list[0]
    last=list[-1]
    print("first color:",first)
    print("last color:",last)
else:
    print("no color")
    
