def is_prime(num):
num = 11
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            return num, True,  "isprime"
        else:
            return num, False, "is not prime"
          
is_prime(num) 
