# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    biggest_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if is_palindrome(i*j) == True:
                if i*j > biggest_palindrome:
                    biggest_palindrome = i*j
    return biggest_palindrome

print(largest_palindrome_product())

#----------------------------------------------------
# Halving number of calculations, a*b = b*a

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    largestPalindrome = 0
    a = 999
    while a >= 100:
        b = 999
    while b >= a:
        if a*b <= largestPalindrome:
            break #Since a*b is always going to be too small
        if isPalindrome(a*b):
            largestPalindrome = a*b
        b = b-1
    a = a-1