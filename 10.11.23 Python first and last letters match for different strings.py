def feast(beast, dish):
    return (beast.upper()[0] == dish.upper()[0]) and (beast.upper()[-1] == dish.upper()[-1])

# P bool
# R bool if beast and dish start and end with the same letters
# E Blue Yew, Beef Stew -> True, Blue Cat, Cream Tart -> False
# P bool statement