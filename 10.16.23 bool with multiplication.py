def hero(bullets, dragons):
    return bullets >= dragons * 2

# P bool
# R bool representing if there will be enough bullets if each dragon requires 2 bullets to defeat
# E 6,2 -> true 3,2 -> false
# P make the statement create the bool. bullets >= dragons * 2