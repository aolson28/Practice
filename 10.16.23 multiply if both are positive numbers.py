def paperwork(n, m):
    if n > 0 and m > 0:
        return n * m
    else:
        return 0

# P int
# R int of n * m unless one of the numbers is negative
# E (6,3) -> 18 but (6, -3) -> 0
# if else