def maskify(cc):
    return '#'*(len(cc)-4) + cc[-4:]

# P str
# R str with all but the last 4 characters masked by '#'
# E '12345678 -> '####5678'
# P Can repeat # * len(cc)-4 and then concat with the last 4 characters of the string, [-4:] means last 4 characters of the string