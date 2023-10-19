def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

# P str
# R str where it says a different string when teh name == "Johnny"
# E Johnny -> 'Hello, my love!'  Jim -> 'Hello, Jim'
# P needed to rearrange the returns and add an else