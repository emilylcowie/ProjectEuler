# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_multiple(numbers):
    lcm_value = numbers[0]
    for number in numbers[1:]:
        lcm_value = lcm(lcm_value, number)
    return lcm_value

numbers = range(1, 21)
result = lcm_multiple(numbers)
print(result)

#----------------------------------------------------
# without math imports

import math

def smallest_multiple(k):
    N = 1
    i = 0
    check = True
    limit = math.sqrt(k)
    primes = [2, 3, 5, 7, 11, 13, 17, 19]  # List of prime numbers up to 20
    a = [0] * len(primes)

    while primes[i] <= k:
        a[i] = 1
        if check:
            if primes[i] <= limit:
                a[i] = math.floor(math.log(k) / math.log(primes[i]))
            else:
                check = False
        N *= primes[i] ** a[i]
        i += 1

    return N

k = 20
result = smallest_multiple(k)
print(result)