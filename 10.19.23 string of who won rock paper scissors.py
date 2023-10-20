def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif p1 == 'scissors' and p2 == 'paper':
        return 'Player 1 won!'
    elif p1 == 'paper' and p2 == 'rock':
        return 'Player 1 won!'
    elif p1 == 'rock' and p2 == 'scissors':
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'

# P str
# R str indicating if Player 1 or Player 2 won in rock paper scissors
# E 'paper', 'scissors' -> 'Player 2 won!'
# P could use if else case statements, could also use dictionary or some funny index math and dictionary to determine who won