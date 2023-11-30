list_1=['Red','Blue','Pink','Yellow','White','Green']
print("Colors Of List One:",list_1)
list_2=['Brown','Gray','Pink','Red','Orange','White']
print("Colors Of List Two:",list_2)
print("Colors From Color List1 Not Contained In Color List2:")
for color in list_1:
    if color in list_2:
        continue
    else:
     print(color)
