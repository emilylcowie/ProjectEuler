# " If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9.
#   The sum of these multiples is 23.
#   Find the sum of all the multiples of 3 or 5 below 1000 "


# ----------------------------------------------------------------------
# simplest way to solve for range of 1000

sum1 = 0
limit = 1000
for i in range(limit):
    if i % 3 == 0 or i % 5 == 0:
        sum1 += i
print(sum1)

# ----------------------------------------------------------------------

# more efficient method to instead calculate the sum of numbers divisible
#   by 3, add to the sum of numbers divisible by 5, then subtract sum of
#   nums divisible by 15:


def sum_divisible_by(divisor):
    max_multiple = (limit - 1) // divisor
    return divisor * (max_multiple * (max_multiple + 1)) // 2


print(sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15))

# ----------------------------------------------------------------------

# using list comprehension
print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))
