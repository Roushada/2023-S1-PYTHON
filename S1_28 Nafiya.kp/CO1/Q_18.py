dict1={1:"aple",2:"orange",3:"grapes"}
dict2={4:100,5:800,6:700}
def merge(dict1,dict2):
    result=dict1|dict2
    return result
dict3=merge(dict1,dict2)
print(dict3)
