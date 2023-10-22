import math
def square_or_square_root(arr):
    return [math.sqrt(x) if math.sqrt(x) % 1 == 0 else x**2 for x in arr]


# P list
# R list with ints that are the square root if it has an integer square root, else return as the number squared
# E [1,2,3,4] -> [1,4,9,2]
# P can import math for math.sqrt (or import sqrt from math) or use **0.5, can also use (x**0.5).is_integer() instead of % 1 == 0
