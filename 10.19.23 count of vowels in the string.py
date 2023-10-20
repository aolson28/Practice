def get_count(sentence):
    count = 0
    for c in sentence:
        if c in ('a','e','i','o','u'):
            count += 1
    return count

# P int
# R int count of vowels in a string
# E 'This is a test' -> 4
# P can use for loop with condition if each character is in ('a','e','i','o','u')