e1 = 5
e2 = 11
e3 = 12

def is_prime(num):
  int_num = int(num)
  if int_num <= 3:
    return n>1
  if int_num % 2 == 0 or int_num % 3 == 0:
    return False
  i = 5
  while i ** 2 <= int_num:
    if int_num % i == 0 or int_num % (i + 2) == 0:
      return False
    i += 6
  return True
