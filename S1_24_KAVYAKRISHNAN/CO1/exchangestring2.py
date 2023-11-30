
def exchangefirstandlastchar(string):
    if len(string) <= 1:
        return string
    else:
        return string[-1] + string[1:-1] + string[0]

string = "Kavya"
newstring = exchangefirstandlastchar(string)
print(newstring)
