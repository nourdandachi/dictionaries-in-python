message= input("Please enter a sentence: ")
sentence= message.split()
dict1 = {}
for word in sentence:
    if word in dict1:
        dict1[word] +=1
    else:
        dict1[word] = 1

print(dict1)
