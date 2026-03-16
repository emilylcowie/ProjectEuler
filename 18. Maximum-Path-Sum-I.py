# By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
# the maximum total from top to bottom is 23
#           3
#          7 4
#         2 4 6
#        8 5 9 3        3 + 7 + 4 + 9 = 23

# Find the maximum total from top to bottom of the triangle below:

#                         75
#                       95  64
#                      17 47 82
#                    18 35  87 10
#                   20 04 82 47 65
#                 19 01 23  75 03 34
#                88 02 77 73 07 63 67
#              99 65 04 28  06 16 70 92
#             41 41 26 56 83 40 80 70 33
#           41 48 72 33 47  32 37 16 94 29
#          53 71 44 65 25 43 91 52 97 51 14
#        70 11 33 28 77 73  17 78 39 68 17 57
#       91 71 52 38 17 14 91 43 58 50 27 29 48
#     63 66 04 68 89 53 67  30 73 16 69 87 40 31
#    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
# it cannot be solved by brute force, and requires a clever method! ;o)

# maybe think of it as a binary tree?
# with small example, consider 2  if you add 8+2 and 2+5, 8+2>2+5 so go down that route if the pointer goes to 2?
#                             8 5
# so the three lowest values to compare are 10, 13, 15
# then with the 7-4 row you get, 17or20, 17or19, so 20, 19
# then the top row (3), you compare 23 and 21, therefore 23 is the biggest sum.

pyramid = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

lines = pyramid.strip().split('\n')
array = []
for line in lines:
    numbers = list(map(int, line.split()))
    array.append(numbers)

def biggestSum(array):
    lastLine = array[-1]
    penultimate = array[-2]
    for i in range(0, len(penultimate)):
        sum1 = lastLine[i] + penultimate[i]
        sum2 = lastLine[i+1] + penultimate[i]
        penultimate[i] = compare(sum1, sum2)
    array[-2] = penultimate
    array.pop()
    if len(array) == 1:
        print(array)
        return array
    else:
        biggestSum(array)

def compare(a, b):
    if a>b:
        return a
    else:
        return b

biggestSum(array)
print('hi')