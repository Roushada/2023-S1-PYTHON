text="Hello This is my world welcome to my world"
text_list=text.split()
count=0
for i in text_list:
    for j in text_list:
        if i==j:
            count+=1
    print(i,"-",count,"times")
    count=0
