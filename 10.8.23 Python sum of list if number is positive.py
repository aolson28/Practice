def positive_sum(arr):
     return sum([num for num in arr if num > 0])
# P integer
# R retrun sum of positive numbers only in a list
# E [1, -1, 2, -2, 3] -> Sum of [1,2,3] = 6
# P use for to loop through and only add them to new list if they are > 0, then sum the new list