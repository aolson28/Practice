def expression_matter(a, b, c):
    l = [a + b + c, a * b * c, a + (b * c), (a + b )* c, a * (b + c), (a * b) + c, a * b + c, a + b * c]
    return max(l)

# P int
# R int of the max of every way to add or multiply 3 digits between 1 and 9
# E 1, 2, 3 -> 9 ((1+2) * 3)
# P list out the variations. can be in a list, or as options with in the max, or in a tuple ()