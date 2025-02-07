# " The sum of the squares of the first ten natural numbers is,
#           1^2 + 2^2 + ... + 10^2 = 385
#   The square of the sum of the first ten natural numbers is,
#           (1 + 2 + ... + 10)^2 = 552 = 3025
#   Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
#           3025 − 385 = 2640.
#   Find the difference between the sum of the squares of the first n natural numbers and the square of the sum."

#------First Attempt------------------------------------
def sumOfSquares():
    sum = 0
    for i in range(1,101):
        sum += i**2
    return sum

def squareOfSum():
    sum = 0
    for i in range(1,101):
        sum += i
    return sum**2

print(squareOfSum() - sumOfSquares())

#--------Making it shorter-------------------------------
limit = 100
sum = 0
sumsq = 0

for i in range(1, limit+1):
    sum += i
    sumsq += i**2
print(sum**2 - sumsq)

#----------Simplest--------------------------------------
limit = 100
sum = limit*(limit + 1)/2
sumsq = (2*limit + 1)*(limit + 1)*limit/6
print(sum**2 - sumsq)