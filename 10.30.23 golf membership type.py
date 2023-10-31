def open_or_senior(data):
    l = []
    for x in data:
        if x[0] >= 55 and x[1] > 7:
            l.append('Senior')
        else: 
            l.append('Open')
    return l

# P list
# R list with strings saying which category the applicant would be in
# P Senior requires being 55 or older and handicap greater than 7
# could also do something like return ['Senior' if age >= 55 and handicap > 7 else 'Open' for (age, handicap) in data] for one liner