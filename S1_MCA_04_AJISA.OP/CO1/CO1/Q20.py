integers=(input("Enter the numbers seperated by  space:"))
list=[int(x) for x in integers.split()]
new_list=[x for x in list if x%2!=0]
print("New list:",new_list)
