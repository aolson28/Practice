def distance_between_points(a, b):
    return ((a.x-b.x)**2 + (a.y-b.y)**2)**0.5

# P number
# R number showing the distance between two points
# E (1,1), (4,5) -> 5
# P subtract the positions x/y to get the absolute value of the distance, and find the hypotenuse a**2 + b**2 = c**2