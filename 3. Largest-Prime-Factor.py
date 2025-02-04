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