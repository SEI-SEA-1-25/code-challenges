def is_prime(num):
  # Edge cases:
  if num<= 1:
    return False
  if num == 2:
    return True
  for i in range(2, num):
    if (num % 1 ) == 0:
      return False 
  # If the num is negative 
  # If the num is 2 - 2 is still prime 
  pass #TODO
