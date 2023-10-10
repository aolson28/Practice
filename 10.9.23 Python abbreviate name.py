def abbrev_name(name):
    u = name.upper()
    s = u.split()
    return str(s[0])[0] + '.' + str(s[1])[0]

# P string
# R First initial of first and last name, joined by '.', capitalized
# E John Doe -> J.D
# P needs upper and join by '.', doesn't need str() though could need if statement to make sure it's not a number or other character
# Better Way below:
# use txt.join with for loop of the split(), connect to upper