#Counting Digits, Letters, and Spaces in a String

import re

name = "Python 3.0"

digitCount = re.sub("[^0-9]", "", name)
letterCount = re.sub("[^a-zA-z]", "", name)
spaceCount = re.findall("[ \n]",name)
print(name)
print("Digit", len(digitCount))
print("Letter", len(letterCount))
print("Spacees", len(spaceCount))
