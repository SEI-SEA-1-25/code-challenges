def is_prime(num):
    #edge cases
    if num <= 1:
        return False
    if num == 2:
        return True

    for i in range(3, num):
        if (num % i) == 0:
            return False
