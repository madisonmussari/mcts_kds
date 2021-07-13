
def play(environment, players):
    moves = []
    log_moves = ()
    while not environment.is_terminal():
        current_player = environment.turn()
        action = players(current_player).action(environment)
        environment = environment.what_if(action)
        moves = [environment, current_player, action]
        log_moves = log_moves + (moves)
    return log_moves

play(([2,3,1],0,3), [0,1,2])
    



