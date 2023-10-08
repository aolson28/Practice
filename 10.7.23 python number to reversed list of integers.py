def digitize(n):
    s = str(n)[::-1]
    l = list(s)
    return list(map(int,l))
    
# P list of int
# R list of integers containing the reversed digits of a given number
# E 1234 -> [4,3,2,1]
# P list will have to map as int and turned into list