def count_sheep(n):
    return ''.join((str(s) + ' sheep...') for s in range(1,n + 1))

# P str
# R str where for n, it counts up from 1 and concats with string ' sheep...'
# E 4 -> '1 sheep...2 sheep...3 sheep...4 sheep'
# P can use ''.join() and a for loop with range (1,n +1)