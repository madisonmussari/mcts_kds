def i_ll_play():
    print("I'll play")

## TODO: Document the functions. 
## TODO: Type annotations.

class Environment:
    # creates a new nim environment
    def __init__(self, heap=[10, 10, 10], current_player=0, num_players=2):

        self.heap = sorted(heap)
        self.current_player = current_player if current_player < num_players else 0
        self.num_players = num_players

    #  Returns the identifier for the current player.
    def turn(self):
        return self.current_player

    # Returns an iterable of all actions which can be taken from this environment.
    def valid_actions(self):
        return ((0, 0) for x in range(2))

    # Returns the state which results from taking action. Actions are of the form (heap, stones_to_take_out)
    def what_if(self, action):
        return self

    # Returns True if this state is a terminal state.
    def is_terminal(self):
        return len(self.heap) == 1

    # Returns the value for this environment. Values can only be calculated for terminal states.
    def value(self, current_player):
        score = None
        if self.is_terminal() and (current_player < self.num_players):
            score = 1 if self.current_player == current_player else -1
        return score

    # Returns current state (num_players, current_player, heap)
    def state(self):
        state = (self.num_players, self.current_player, self.heap)
        return state


# main program -  do I need this?
# while self.game_play == True:
#   self.turn()
