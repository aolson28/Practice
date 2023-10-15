def past(h, m, s):
    return (s + (((h*60) + m) * 60))*1000

# P int
# R int number of milliseconds past midnight
# 1, 1, 1 -> 3661000
# P  h * 60 * 60 * 1000, m * 60 * 1000 , s * 1000, added together
