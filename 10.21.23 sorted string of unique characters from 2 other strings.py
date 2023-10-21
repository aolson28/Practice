def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))

# P str
# R str containing one of each character from both strings, sorted
# E 'this is a test' -> 'aehist'
# P can use a sorted() set() to remove duplicates and sort in alphabetical order