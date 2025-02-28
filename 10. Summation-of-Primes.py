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
num = 5
sum = 5
while num < limit:
    num += 2
    if is_prime(num):
        sum += num

print(sum)

# Using The sieve of Eratosthenes
# - create a boolean array, marking every value from 0-n True initally.
# - Set index 0 and 1 to False as 0 and 1 are not primes
# - For each prime number, mark the multiples of that number as False
# - At the end, sum all the indices as these are the primes

limit = 2000000
sum = 0

sieve = [True] * limit
sieve[0] = sieve[1] = False  # 0 and 1 are not primes

for i in range(2, int(limit ** 0.5) + 1):
    if sieve[i]:
        for j in range(i, limit, i):
            sieve[j] = False

for i in sieve:
    if sieve[i] == True:
        print(i)
        sum += sieve.index(i)

print(sum)