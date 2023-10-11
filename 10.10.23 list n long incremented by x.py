def count_by(x, n):
    s = 0
    a = 0
    l = []
    while s < n:
        l.append(a+x)
        a = a + x
        s += 1
    return l
    
# P List
# R list with n number of items, increment by x
# E count_by(3,3) -> [3, 6, 9]
# P while loop, appending the list
