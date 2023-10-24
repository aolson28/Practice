def get_planet_name(id):
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name


# P string
# R string of the planet name given the id (position away from sun)
# E 4 = 'Mars'
# P case statements use match as a keyword in python