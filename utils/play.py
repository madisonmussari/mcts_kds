# This functions looks at the current environment, asks the corresponding player to make a move, 
# and updates the  current environment accordingly
def play(environment, players):
    log_moves = []
    while not environment.is_terminal():
        current_player = environment.turn()
        action = players[current_player].action(environment)
        environment = environment.what_if(action)
        moves = [(environment, current_player, action)]
        log_moves = log_moves + moves
    return log_moves