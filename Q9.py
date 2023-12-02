def swap(string):
    first = str[0]
    last = str[-1]
    middle = str[1:-1]
    new_str = last + middle + first
    return new_str

str=input("Enter the word:")
new_str = swap(str)
print(new_str)
