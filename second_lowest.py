# Find out the second lowest number using a single for loop.

num = [0,-7,-8,5,2,7,5,-9]
# output = -8

lowest = second_lowest = float('inf')

for n in num:
  if n<lowest:
    second_lowest = lowest
    lowest = n
  elif lowest < n < second_lowest:
    second_lowest = n
print(second_lowest)
