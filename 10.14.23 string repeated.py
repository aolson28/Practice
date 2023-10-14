def repeat_str(n, s):
    st = str()
    for i in range(n):
        st = st + s
    return st

# P str
# R str s repeated n number of times
# 'Test', 3 -> 'TestTestTest'
# P for i in range(n)