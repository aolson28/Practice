def bmi(weight, height):
    if weight/(height**2) <= 18.5:
        return 'Underweight'
    elif weight/(height**2) <= 25.0:
        return 'Normal'
    elif weight/(height**2) <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'

# P str
# R str returning category of bmi
# E 90, 1.95 -> 23.7 -> 'Normal'
# P requires weight in kg and height in meters, if, elif, elif, and else