
def play(environment, players):
    """
    This function looks at the current environment, asks the corresponding player to make a move, 
    and updates the  current environment accordingly. The function returns a log with
    (environment, current_player, action) for each move.

    Args:
        environment: nim.Environment
        players: [description] #CHECK

    Returns:
        log_moves (list):  #CHECK
    """
    log_moves = []
    while not environment.is_terminal():
        current_player = environment.turn()
        action = players[current_player].action(environment)
        environment = environment.what_if(action)
        moves = [(environment, current_player, action)]
        log_moves = log_moves + moves
    return log_moves