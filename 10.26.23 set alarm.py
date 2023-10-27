def set_alarm(employed, vacation):
    return employed and not vacation

# P bool
# R bool whether alarm should be set, only when employed and not on vacation
# E employed = True and vacation = False -> True, employed = False and vacation = True -> False
# P since it's a bool, can just use return employed and not vacation