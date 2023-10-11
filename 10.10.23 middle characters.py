def get_middle(s):
    l = len(s)
    if l % 2 == 0:
        a = int((l)//2 - 1)
        return s[a:a+2]
    else:
        return s[(l - 1)//2]
    
# P str
# R middle character(s) of a string. if even number, return middle 2, if odd, return middle 1
# E 'Test' -> 'es', 'Yes' -> 'e'
# P len() and use this to index the string
