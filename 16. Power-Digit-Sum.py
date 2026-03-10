# Power Digit Sum 
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the number 2^1000 ?

# 1, 2, 3,  4,  5,  6,   7,   8,   9,   10,   11,   12,   13,    14,    15,    16
# 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536
# 2, 4, 8,  7,  5, 10,  11,  13,   8,    7,   13,   19,   20,    22,    26,    25

# last digits always go 2,4,8,6,2,4,8,6......

power = 1000
num = 1
sum = 0

for i in range(0,power):
    num *= 2

for i in str(num):
    sum += int(i)

print(sum)