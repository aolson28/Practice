def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'

# P string
# R the next color in the sequence
# E 'Yellow' -> 'Red'
# P use if and elif, might be an easier way of doing this like: return {"green": "yellow", "yellow": "red", "red": "green"}[current]