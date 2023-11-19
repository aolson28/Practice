def whose_move(last_player, win):
    if win:
        return last_player
    elif last_player == 'black':
        return 'white'
    else:
        return 'black'

# P str
# R str indicating next player. the player that won the last round gets to start the next round
# E 'black','True' -> 'black'
# P if last player didn't win, it's the opposite.
# Can use a dict or can use ifelse