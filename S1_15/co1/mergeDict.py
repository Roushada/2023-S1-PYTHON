def Merge(cict1,dict2):
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1
dict1={"a":1,"b":2,"c":3}
dict2={"x":11,"y":22,"z":33}
dict3=Merge(dict1,dict2)
print(dict3)
