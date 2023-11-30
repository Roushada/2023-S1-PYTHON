list=["apple","banana","orange","avacado"]
count=0
for x in list:
    count+=x.lower().count("a")

print(count)
