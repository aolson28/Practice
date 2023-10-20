def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'

# P str
# R str depending on if name == owner
# E 'joe', 'joe' -> 'Hello boss', 'Brad','Jim' -> 'Hello guest'
# P could use single line if else statement in the return. or could do the traditional multi line if else statement and returns for each case