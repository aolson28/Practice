def xo(s):
    return sum(1 if c in 'xX' else 0 for c in s) == sum(1 if c in 'oO' else 0 for c in s)

# P bool
# R bool if there are equal amounts of 'x' and 'o' in a string, case insensitive
# E 'Rox' -> true, 'x012abcx' -> false
# P can compare the sum of characters that are in 'xX' or 'oO' in the string
# simpler way would be s.lower().count('x') == s.lower().count('o')