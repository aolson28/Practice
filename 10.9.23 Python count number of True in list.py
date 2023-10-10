def count_sheeps(sheep):
    num = 0
    for s in sheep:
        if s:
            num = num +1
    return num

# P integer
# R sum of 'True' in a list
# E [ True, False, False, True] -> 2
# P use loop and increment the variable