def check_for_factor(base, factor):
    return base % factor == 0

# P bool
# R bool representing if base is divisible by factor, meaning the result of dividing would be a non-negative integer
# E 12, 5 -> false
# P can use the comparison statement to make the bool, could make the if else statements as well, use modulo % to determine if divisible
# Alternative would be return not (base % factor) where the statement is looking for base % factor 0, the not means 'true if  base % factor is false' (python bool false == 0)