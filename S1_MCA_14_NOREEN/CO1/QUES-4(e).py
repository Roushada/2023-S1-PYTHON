def count_occurrences(text):
    word_dict= {}
    words = text.split()
    
    for word in words:
        word=word.strip('.,?!()[]{}"\'').lower()
        if word:
            if word in word_dict:
               word_dict[word] += 1
        else:
            word_dict[word]= 1
            return word_dict

text=input("enter a line:")
word_occurrences=count_occurrences(text)
print("word occurrences in the input text:")
for word in word_occurrences.item():
    print(f"'{word}':{count}")
