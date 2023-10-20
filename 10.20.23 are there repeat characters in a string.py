def is_isogram(string):
    s = string.lower()
    l = [s.count(c) for c in s]
    return len(string) == sum(l)

# P bool
# R bool if there are any repeat characters in a string, Isogram
# E 'Rox' -> true, 'x012abcx' -> false
# P can count the characters and store in list, sum() the list and compare to the length of the string, can also turn the string into a set to remove duplicates and compare the lengths