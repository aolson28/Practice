def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names)-2} others like this'

# P str
# R str telling number of 'likes' with some formatting rules based on number of likes
# E Aaron, Lucy, Mickey, Gaston, Elsa -> 'Aaron, Lucy and 3 others like this'
# P use elif statements and f'' to build the strings