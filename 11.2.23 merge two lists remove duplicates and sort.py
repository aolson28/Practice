def merge_arrays(first, second): 
    arr = set(first + second)
    return sorted(arr)

# P list
# R list of two lists combined, no duplicates, sorted ascending
# E [5,1,3] [2,3,4] = [1,2,3,4,5]
# P add the arrays and convert to set to remove duplicates, then use sorted() to sort and convert back to list