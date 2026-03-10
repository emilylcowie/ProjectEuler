# If the numbers 1 to 5 are written out in words: 
# one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. 
# For example, 342 contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

# 3, 3, 5, 4, 4, 3, 5, 5, 4, 3          1 to 10
# 6, 6, 8, 8, 7, 7, 9, 8, 8, 6          11 to 20
# 3, 6, 6, 6, 5, 5, 7, 6, 6, x+7        10 to 100

sum = 0

def need_and(hd, td, od, s):
    if hd > 0 and (td > 0 or od > 0):
        s += 3
    return s
    
def ones(num, sum):
    oneToNine = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    sum += oneToNine[num]
    return sum

def belowTwenty(num, sum):
    OneToNineteen = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    sum += OneToNineteen[num]
    return sum

def tens(num, sum):
    Tens = [0, 3, 6, 6, 6, 5, 5, 7, 6, 6]
    sum += Tens[num]
    return sum

def hundreds(num, sum):
    Hundreds = [0, 10, 10, 12, 11, 11, 10, 12, 12, 11]
    sum += Hundreds[num]
    return sum

for i in range(1, 1001):
    num = str(i)
    try:
        onesDigit = int(num[-1])   
    except:
        onesDigit = 0
    try:
        tensDigit = int(num[-2])  
    except:
        tensDigit = 0
    try:
        hundredsDigit = int(num[-3])
    except:
        hundredsDigit = 0

    if i == 1000:
        sum += 11
        continue

    sum = hundreds(hundredsDigit, sum)
    sum = need_and(hundredsDigit, tensDigit, onesDigit, sum)

    if tensDigit * 10 + onesDigit < 20:
        sum = belowTwenty(tensDigit * 10 + onesDigit, sum)
    else:
        sum = tens(tensDigit, sum)
        sum = ones(onesDigit, sum)

print(sum)
