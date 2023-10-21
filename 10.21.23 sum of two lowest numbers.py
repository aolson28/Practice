def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]

# P int
# R sum of 2 lowest numbers in the list
# E [3, 1, 2, 7] -> 3
# P can sort the list and then use the [0] and [1] of the list. simpler way is sum(numbers[:2])