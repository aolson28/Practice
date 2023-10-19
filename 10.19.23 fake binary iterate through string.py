def fake_bin(x):
    s = str()
    for i in x:
        if int(i) < 5:
            s += '0'
        else:
            s += '1'
    return s

# P str
# R str where each digit in the string is converted, if <5 then 0, else 1
# E '1928374650' -> '0101010110
# P can iterate the string and use if else to append the digit. Simpler way is like return ''.join('0' if i < '5' else '1' for i in x) since x is already a string