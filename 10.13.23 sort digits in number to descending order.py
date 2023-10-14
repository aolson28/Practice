def descending_order(num):
    st = str(num)
    l = [int(c) for c in st]
    s = l.sort(reverse=True)
    i = 0
    s2 = str()
    while i < len(l):
        s2 = str(s2) + str(l[i])
        i += 1
    return int(s2)

# P int
# R int where the numbers in a string are sorted in desc order
# E 15328 -> 85321
# P turn int to list, sort desc, then while loop to append each digit to the new string, then return as int()