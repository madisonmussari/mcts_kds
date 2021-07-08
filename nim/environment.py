def i_ll_play():
    print("I'll play")


class Environment:
    # Creates a new Nim environment with the current heap allocation and player.
    def __init__(self,
                 heap=[10, 10, 10],
                 current_player=0,
                 players=["A", "B"]):
        self.heap = heap
        self.current_player = current_player
        pass

    #  Returns the identifier for the current player.
    def turn():
        pass

    # Returns an iterable of all actions which can be taken from this environment.
    def valid_actions():
        pass

    # Returns the state which results from taking action.
    def what_if(action):
        pass

    # Returns True if this state is a terminal state.
    def is_terminal():
        pass

    # Returns the value for this environment.  Values can only be calculated for terminal states.
    def value():
        pass
