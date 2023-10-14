def summation(num):
    return sum(i for i in range(num+1))

# P int
# R sum of the each digit from 1 to num
# 3 -> 1 + 2 + 3 = 6
# P can loop using for. Quicker way is sum(range(num+1)), no need to loop. also (1+num) * num / 2
