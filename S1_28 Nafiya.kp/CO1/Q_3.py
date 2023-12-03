list=[1,2,3,4,-2.-4,-5]
new=[x for x in list if x>0]
print(new)
n=8
list1=[x**2 for x in range(n+1)]
print("the square of number is:",list1)
#3)b
n=8
list1=[x**2 for x in range(n+1)]
print("the square of number is:",list1)
#3)c
word="awhengclg"
vowel="aeiouAEIOU"
list=[x for x in word if x in vowel]
print("vowels in the word is:",list)
#3)d
word="how are you"
print("the enterd word is ",word)
list1=[ord(value)for value in word]
print("the ordinal values",list1)
