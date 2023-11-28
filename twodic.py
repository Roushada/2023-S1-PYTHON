print("merge two dictionaries")
def merge(dict1 ,dict2):
      res = dict1 | dict2
      return res
dict1  = {'akash': 10}
dict2 = {'kuppattil':100}
dict3=  merge(dict1,dict2)
print(dict3)
