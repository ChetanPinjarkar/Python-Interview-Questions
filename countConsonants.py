vowel = ['a','e','i','o','u']
word = "Programming"
count=0

for char in word:
    if char in vowel:
        count+=1
print(count,f"Consonants present in {word}")

