def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

# P bool
# R bool of n being divisble by both x and y
# E 24, 6, 3 -> true
# P use % to determine if divisble, use and statement and comparison to make the bool, divisble means when divided the result is a positive integer (no decimal)