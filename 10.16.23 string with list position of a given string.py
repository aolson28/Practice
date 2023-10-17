def find_needle(haystack):
    return 'found the needle at position ' + str(haystack.index('needle'))

# P str
# R str with 'found the needle at position ' and the string index of needle in the list haystack
# E ['no', '2nd', 'needle', 42, false] -> 'found the needle at position 3'
# P can use haystack.index('needle') to determine the index
# also can use f'found the needle at position {haystack.index('needle')}'