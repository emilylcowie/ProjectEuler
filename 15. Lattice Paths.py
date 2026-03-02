# Starting in the top left corner of a 2x2 grid, 
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

# Starting by taking paths that start with a horizontal route first?

# 00, 10, 20, 21, 22
# 00, 10, 11, 21, 22

from math import comb

n = 20
print(comb(2*n, n))