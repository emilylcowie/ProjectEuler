#   Let d(n) be defined as the sum of proper divisors of n (numbers less than n that divide into n).
#   
#   If d(a) = b and d(b) = a, where a != b, 
#   then a and b are an amicable pair and each of a and b are called amicable numbers.
#
#   For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and 110; 
#   therefore d(220) = 284. The proper divisors of 284 are 1,2,4,71 and 142;
#   so d(284) = 220.
#
#   Evaluate the sum of all the amicable numbers under 10,000.

def divisors(n):
    divisorsList = []
    for i in range(1, (n//2)+1):
        if n%i == 0 and n!=i:
            divisorsList.append(i)
    return divisorsList

def d(n):
    sum = 0
    for i in divisors(n):
        sum += i
    return sum

amicables = []
for a in range(0, 10000):
    b = d(a)
    if d(b) == a and a not in amicables and b not in amicables and a!=b:
        amicables.append(a)
        amicables.append(b)

print(amicables)
sum = 0
for i in amicables:
    sum += i
print(sum)