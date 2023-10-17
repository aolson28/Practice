def grow(arr):
    x = 1
    for i in arr:
        x = i * x
    return x

# P int
# R int with each number in the list multiplied with the next one
# E [2,3,4] -> 2 * 3 * 4 = 24
# P iterate the list and multiply with the previous number, stored in x