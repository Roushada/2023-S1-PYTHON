for i in range(1000,10000,1):
    for j in range(32,100):
        if i==j*j:
            print(i)
            print(type(i))
            new=int(i)
            print(type(new))
            if new[0]%2==0 and new[1]%2==0 and new[2]%2==0 and new[3]%2==0 :
                x=new
            prit(x)
            
       # st=str(i)
        #if int((st[0]%2==0) and int(st[1]%2==0) and int(st[2]%2==0) and int(st[3]%2==0)):
          #  print(i)
    
