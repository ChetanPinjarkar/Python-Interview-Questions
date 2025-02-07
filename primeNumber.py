def check_prime(num):
  if num<2:
    return False
  for i in range(2,num):
    if num%i == 0:
      return False
  return True

print(check_prime(10))
print(check_prime(7))