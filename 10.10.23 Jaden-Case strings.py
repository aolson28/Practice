def to_jaden_case(string):
    l = string.lower().split(' ')
    if string:
        return ' '.join([l[x].replace(l[x][0],l[x][0].upper(),1) for x in range (0,len(l))])
    
# P String
# R String in "Jaden-Case" where the first character of the word is capitalized
# E 'This is a test' = 'This Is A Test'
# P must not be null, can't use title() because of other punctuation
