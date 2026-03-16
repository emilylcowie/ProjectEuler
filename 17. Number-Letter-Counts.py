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

oneToNine = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tensWord = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundred = ['', 'onehundred', 'twohundred', 'threehundred', 'fourhundred',
            'fivehundred', 'sixhundred', 'sevenhundred', 'eighthundred', 'ninehundred']

def lengthNum(number):
    return len(number)

def needAnd(number):
    if number // 100 != 0:
        return True
    else:
        return False

for i in range(1, 1000):
    units = i % 10
    tens = int(i / 10) % 10
    hundreds = int(i / 100)

    if needAnd(i):
        sum += 3

    if tens == 1 and units > 0:
        num = hundred[hundreds], teens[units]
        print(num)
        for j in num:
            sum += lengthNum(j)
        continue

    num = hundred[hundreds], tensWord[tens], oneToNine[units]
    for j in num:
        sum += lengthNum(j)
    print(num)

sum += lengthNum('onethousand')
sum -= 27
print(sum)