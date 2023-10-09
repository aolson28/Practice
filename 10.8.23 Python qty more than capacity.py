def enough(cap, on, wait):
    if on + wait > cap:
        return (on + wait)-cap
    else:
        return 0

# P int 
# R if on + wait > cap how many can't get on else 0 if there's enough space
# E cap = 100, on =90, wait = 20 -> 10     cap = 100, on =80, wait = 20 -> 0
# P  on + wait > cap return difference, else 0