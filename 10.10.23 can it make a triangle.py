def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
    
# P bool
# R bool if 3 given integers could make a triangle
# E [1, 2, 4] -> False [2, 2, 3 ]-> True
# P test for triangle is any 2 sides must be greater than the 3rd side. Could sort and add the 2 smaller or write out the 3 combos as comparrisons
