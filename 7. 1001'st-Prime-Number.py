# " By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#       we can see that the 6th prime is 13.

#       What is the 1001'st prime number? "

def is_prime(n):
    for i in range(2,n):
        print("I",i)
        print("N",n)
        if n % i == 0:
            print("True")
        else:
            print("False")
            return False
    return True
        
for n in range(1,100):
    if is_prime(n) == True:
        print("")