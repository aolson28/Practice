def square_sum(numbers):
    return sum([i**2 for i in numbers])

# P int
# R sum of the square of each number in a list
# [1, 2, 3] -> [1, 4, 9] -> 1 + 4 + 9 -> 14
# P can loop through the list, squaring the numbers, and then sum the list