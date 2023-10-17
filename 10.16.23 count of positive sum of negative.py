def count_positives_sum_negatives(arr):
    pos_count = 0
    neg_sum = 0
    for i in arr:
        if i > 0:
            pos_count += 1
        elif i < 0:
            neg_sum += i
    return [pos_count, neg_sum] if len(arr) else []

# P list
# R list with count of positive numbers and sum of negative numbers in a list, return empty list if list was empty
# E [1, 3, -5, -2, -1] -> [2, -8]
# P iterate the list and if else to see if positive or negative, save to variable, return list with variables if len(arr) (meaning is not empty) else []