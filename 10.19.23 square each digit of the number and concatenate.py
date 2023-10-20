def square_digits(num):
    s = str(num)
    s2 = ''
    for c in s:
        s2 += str(int(c)**2)        
    return int(s2)

# P int
# R int where each digit is squared and concatenated to form a new int
# E 1234 -> 14916
# P can't iterate a number
# turn to string, then iterate for each character
# append to string variable
# return the int() of the string variable