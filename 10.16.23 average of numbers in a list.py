def find_average(numbers):
    return sum(numbers)/len(numbers) if len(numbers) > 0 else 0

# P float or int number
# R float or int, the average of a list of numbers, 0 if list is empty
# E [1, 3, 5] -> 3
# P needs if len(numbers) > 0 else 0 statement to handle divide by 0 cases; could change if statement to if numbers else 0