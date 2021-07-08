def i_ll_play():
    print("I'll play")


class Environment:
    # Creates a new Nim environment with the current heap allocation and player.
    def __init__(self,
                 heap=[10, 10, 10],
                 current_player=0,
                 num_players=2):
        self.heap = heap
        self.current_player = current_player
        pass

    #  Returns the identifier for the current player.
    def turn(self):
        pass

    # Returns an iterable of all actions which can be taken from this environment.
    def valid_actions(self):
        pass

    # Returns the state which results from taking action. Actions are of the form (heap, stones_to_take_out)
    def what_if(self, action):
        pass

    # Returns True if this state is a terminal state.
    def is_terminal(self):
        pass

    # Returns the value for this environment.  Values can only be calculated for terminal states.
    def value(self, player):
        pass

    # Returns current state (num_players, current_player, heap)
    def state(self):
        pass
