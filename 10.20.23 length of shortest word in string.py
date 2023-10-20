def find_short(s):
    list = s.split(' ')
    l = min([len(w) for w in list])
    return l 

# P int
# R int minimum length of words in a string
# E 'This is a test' = 1
# P split words into list and return the min() of the length of each item in the list.