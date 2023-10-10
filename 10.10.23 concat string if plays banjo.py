def are_you_playing_banjo(name):
    if name.upper()[0] == 'R':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
    
# P string
# R name + ' plays banjo' if first letter is 'R', name + ' does not play banjo' otherwise, use upper to allow for 'r' or 'R'
# E Jane does not play banjo, Rudy plays banjo
# P if name.upper()[0] =='R' 