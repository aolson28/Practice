def series_sum(n):
    s = 1
    d = 0
    for i in range(0,n):
        d = d + 1/s
        s += 3
    return "%0.2f" % d
    
# P string of number with 2 decimal places
# R sum of the series to nth increment where series is 1/1 -> 1/4 (bottom increases by 3)
# E 2 -> 1.25
# P "%0.2f" % d to format the sum as d
