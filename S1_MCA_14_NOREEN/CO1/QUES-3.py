#GENERATE POSITIVE LIST OF NUMBERS FROM A GIVEN LIST OF INTEGERS
list=[-2,3,4,-5,-6,10]
positive_numbers=[num for num in list if num>0]
print("Positive",positive_numbers)


#SQUARE OF N NUMBERS
N=s
squares=[i**2 for i in range(N)]
print("Square Upto N",squares)



#FORM A LIST OF VOWELS SELECTED FROM A GIVEN WORD
word='Hello World'
vowels=[char for char in word if char.lower()in 'aeiou']
print("Vowels",vowels)



#LIST ORDINAL VALUE OF EACH ELEMENT OF A WORD
word='Hello World'
ordinal_value=[ord(char)for char in word]
print("Ordinal Value",ordinal_value)
