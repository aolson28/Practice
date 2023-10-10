import math
def find_next_square(sq):
    if math.sqrt(sq) % 1 > 0:
        return -1
    else:
        return (math.sqrt(sq) +1)**2


# P int
# R next bigger perfect sq
# E 4 -> 9
# P calculate sqrt and see if it's perfect using % 1, then return the sqrt + 1 and square that