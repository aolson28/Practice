def lovefunc( flower1, flower2 ):
    return flower1 %2 != flower2 %2

# P bool
# R bool true if flower1 and flower2 are both not odd or both not even
# E (1,3) -> false but (6, 3) -> true
# can just return the bool statement