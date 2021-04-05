# Define a function that takes one integer argument
# and returns logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is
# a natural number greater than 1 that has no
# positive divisors other than 1 and itself.

def is_prime(num):
  # print(range(num))
  if num < 2: return False
  div_list = []
  for i in range(num):
    if i > 1 and num % i == 0:
      div_list.append(i)
  if len(div_list) > 0:
    return False
  else:
    return True
  # if:
  #   # determine if integer is prime
  #   return True
  # else:
  #   return False

print(is_prime(6))

