# " The sum of the primes below 10 is 2+3+5+7 = 17.
#   Find the sum of all the primes below two million. "

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = 2000000
num = 1
sum = 0
while num < limit:
    num += 1
    if is_prime(num):
        sum += num

print(sum)