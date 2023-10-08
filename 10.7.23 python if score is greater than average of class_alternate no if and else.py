def better_than_average(class_points, your_points):
    return your_points > (sum(class_points) + your_points)/(len(class_points)+1)
    
# P bool
# R bool True if your_points > average of class_points
# E 95 > average of (95, 91, 87) - > True
# P add my score to class_points, this time just use comparrison and not if and else to save lines