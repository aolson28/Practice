def solution(text, ending):
    l = (len(text)-len(ending))
    l2= len(text)
    return ending in text[l:l2]

# P bool
# R check if ending is actually the end of the given string
# E ending = 'st' text = 'test' -> True  ending = 'st' text = 'not' -> False
# P use in and determine index of the ending