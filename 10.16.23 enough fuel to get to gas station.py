def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

# P bool
# R bool if mpg * fuel_left >= distance_to_pump
# E 75, 20, 3 -> 60 >= 75 -> false
# P bool comparison