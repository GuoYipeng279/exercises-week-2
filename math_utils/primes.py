import math


def isprime(num):
    if num <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
