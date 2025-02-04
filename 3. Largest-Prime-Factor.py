# " The prime factors of 13195 are 5, 7, 13 and 29.
#   What is the largest prime factor of the number 600851475143? "

number = 600851475143
factors = []
prime_factors = []

for i in range(round(number/3),0,-1):
    print(i)
    if number % i == 0:
        factors.append(i)
        break
        
print(factors)

#unfinished