def disemvowel(string_):
    repa = string_.replace('a','')
    repe = repa.replace('e','')
    repi = repe.replace('i','')
    repo = repi.replace('o','')
    repu = repo.replace('u','')
    repA = repu.replace('A','')
    repE = repA.replace('E','')
    repI = repE.replace('I','')
    repO = repI.replace('O','')
    repU = repO.replace('U','')
    return repU

# P string
# R string without vowels
# E 'TEST ABCDEF' -> 'TST BCDF'
# P could use stacked replaces like above. Should use below. could use the string of vowels as below or in list. string uses less characters.
#
# def disemvowel(string_):
#    for i in 'aeiouAEIOU':
#       string_ = string_.replace(i,'')
#    return string_
