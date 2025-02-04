# " The prime factors of 13195 are 5, 7, 13 and 29.
#   What is the largest prime factor of the number 600851475143? "

def largest_prime_factor(number):
    factor = 2
    while factor ** 2 <= number:
        if number % factor:
            factor += 1
        else:
            number //= factor
    return number

num = 600851475143
print(largest_prime_factor(num))

# Explanation:
#   Continue dividing the number by the smallest factor until factor squared is greater than the number.
#   If the number is not divisible by the current factor, increment the factor
#   If the number is divisible by the current factor, divide the number by the factor
#   The remaining number is the largest prime factor

#-----------------------------------------------------
# Optimized for large numbers

def largest_prime_factor(n):
    if n % 2 == 0:
        last_factor = 2
        while n % 2 == 0:
            n //= 2
    else:
        last_factor = 1

    factor = 3
    max_factor = n

    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            n //= factor
            last_factor = factor
            while n % factor == 0:
                n //= factor
            max_factor = n
        factor += 2

    if n == 1:
        return last_factor
    else:
        return n

num = 600851475143
print(largest_prime_factor(num))

# This code efficiently finds the largest prime factor by:
# Handling the factor of 2 separately.
# Using a loop to check odd factors starting from 3.
# Updating the maximum factor dynamically to reduce unnecessary checks.