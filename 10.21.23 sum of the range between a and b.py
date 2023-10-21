def get_sum(a,b):
    return sum(range(min(a,b),max(a,b)+1)) if a!=b else a

# P int
# R sum of interegers in the range between a & b
# E -1,4 -> 9
# P can sum the range but needs to use min() and max() + 1 to properly make the range