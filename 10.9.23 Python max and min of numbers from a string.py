def high_and_low(numbers):
    l = numbers.split(' ')
    s = [int(i) for i in l]
    return str(max(s)) + ' ' + str(min(s))

# P string
# R string containing max and min of a group of numbers in a string, joined by ' '
# E '1 -2 2 10' -> '10 -2'
# P split and turn to int, find max and min, join by ' '
# simpler -> [in(i) for i in numbers.split()] and return f"{max(numbers)} {min(numbers)}""