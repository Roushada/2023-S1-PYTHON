string=input("enter a string:")
print(string[-3:])
if (string[-3:]=="ing"):
    str1=(string[0:]+"ly")
    print(str1)
else:
    print(string+"ing")
