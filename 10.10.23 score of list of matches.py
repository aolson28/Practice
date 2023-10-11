def points(games):
    s = 0
    for i in range(0,10):
        if games[i][0] > games[i][-1]:
            s += 3
        elif games[i][0] == games[i][-1]:
            s += 1
    return s 
    
# P int
# R total score for 10 games where win (x>y) is 3 points, loss (x<y) is 0 points, and ties (x=y) are 1 points
# E ['1:0','1:0','1:0','1:0','1:0','1:0','1:0','1:0','1:0','1:0'] = 30
# P use for loop to increment variable if win, loss, or tie
