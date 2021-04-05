def is_prime(num):
  if num <= 1: return False
  
  for i in range(num):  
    if (i % 2 == 0):  
      return False  
    else: return True  

print(is_prime(1))  # false */
print(is_prime(2)) # true  */
print(is_prime(-1)) # false */