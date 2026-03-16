#   You are given the following information, but you may prefer to do some research for yourself.

#   1 Jan 1900 was a Monday.

#   Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.

#   A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#   How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#   1 Jan 1901 was a Tuesday so firt Sunday was 6th Jan 1901

def isLeapYear(year):
    def isLeapYear(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def daysInYear(year):
    if isLeapYear(year):
        #print(year, '366')
        return 366
    else:
        #print(year, '365')
        return 365

monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthDaysLeapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
score = 0

def firstOfMonth(year):
    if isLeapYear(year):
        days = monthDaysLeapYear
    else:
        days = monthDays
    firsts = [1]
    for i in range(1, 13):
        firsts.append(firsts[i-1] + days[i-1])
    return firsts

def weekday_offset(year):
    total_days = 0
    for y in range(1900, year):
        total_days += daysInYear(y)
    return total_days % 7

def Sundays(year):
    offset = weekday_offset(year)
    first_sunday = (6 - offset) % 7 + 1
    if first_sunday == 0: first_sunday = 7 
    sundays = [first_sunday]
    total_days = daysInYear(year)
    while sundays[-1] + 7 <= total_days:
        sundays.append(sundays[-1] + 7)
    return sundays
        
def check(year, score):
    score = 0
    for i in firstOfMonth(year):
        for j in Sundays(year):
            if i == j:
                score += 1
    return(score)

for i in range(1901, 2001):
    score += check(i, score)
print(score)
print('hi')
