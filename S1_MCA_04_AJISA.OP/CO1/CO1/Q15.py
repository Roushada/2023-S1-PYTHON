list1=["red","yellow","green"]
list2=["white","red","blue"]
print("color_list1=",list1)
print("color_list2=",list2)
print("colors from color_list1 not contained in color_list2:")
for color in list1:
    if color in list2:
        continue
    else:
        print(color)
