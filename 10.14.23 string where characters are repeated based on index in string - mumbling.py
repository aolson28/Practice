def accum(s):
    low = s.lower()
    l = [str(low[c]) * (c + 1) for c in range(len(low))]
    return  '-'.join(l).title()

# P str
# R str where the position of each character is the number of times the
#   character is repeated, separated by '-' with only the first of each character being uppercase
# 'abc' -> 'A-Bb-Ccc'
# P lower case the string. Then loop through each character, using the index -
#   where the index is represented by the incrementing number in range(len(s)).
#   Then join with '-' and title() for capitalization
