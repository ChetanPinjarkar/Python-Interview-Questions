vowel = ['a','e','i','o','u']
word = "Programming"
count=0

for char in word:
    if char not in vowel:
        count+=1
print(count,f"Consonants present in {word}")

