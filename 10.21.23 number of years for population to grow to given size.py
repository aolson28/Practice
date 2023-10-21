def nb_year(p0, percent, aug, p):
    percent = percent/100
    y = 0
    while p0 < p:
        p0 = p0 + int(p0 * (percent)) + aug
        y += 1
    return y

# P int
# R int number of years (cycles) it would take if the population grew by percent % and by aug number of people moving in
# E 100, 10, 10, 125 -> 2
# P needed to int() or round() the people calculations since you can't add 0.4 people