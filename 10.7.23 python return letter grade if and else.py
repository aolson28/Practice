def get_grade(s1, s2, s3):
    if 90 <= (s1 + s2 + s3)/3 <=100:
        return "A"
    elif 80 <= (s1 + s2 + s3)/3 <90:
        return "B"
    elif 70 <= (s1 + s2 + s3)/3 <80:
        return "C"
    elif 60 <= (s1 + s2 + s3)/3 <70:
        return "D"
    else:
        return "F"
    
# P string
# R string showing grade based on average of 3 arguments
# E (99, 86, 91) -> 92 -> 'A'
# P can use else if statements. 