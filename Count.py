import random 
a = random.randint(1,30)

MySelf = input("Tell us about Yourself")
CharacterCount = 0 
WordCount = 0 
for i in MySelf:
    CharacterCount = CharacterCount + 1
    if i == " ":
        WordCount = WordCount + 1

print(CharacterCount)
print(WordCount)

print("Your no. is " , a)


