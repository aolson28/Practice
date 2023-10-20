def filter_list(l):
    return [i for i in l if isinstance(i,int)]

# P list
# R list of only int from list of mixed types
# E [1, 2.7, 'test', false, 3] -> [1,3]
# P can use for loop in [], use isistance() to create condition for when the list item is an integer