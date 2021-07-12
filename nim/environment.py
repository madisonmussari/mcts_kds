from typing import List

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
    def valid_actions(self) -> set:
        valid_actions = []
        action = []
        for i in range(len(self.heap)-1,0, -1):
            value = self.heap[i]
            while value > 0:
                action = action + [(i,value)] + [(0,1)]
                value -= 1
            valid_actions = valid_actions + action
        return valid_actions

    # Returns the state which results from taking action. Actions are of the form (heap, stones_to_take_out)
    def what_if(self, action: List[int]): # what is up with my type annotations?

        new_value = self.heap[action[0]] - action[1]
        if new_value < 0 or self.is_terminal():
            return Environment(self.heap, self.current_player, self.num_players)
        
        new_heap = self.heap.copy()
        new_heap[action[0]] = new_value
        
        if new_heap[action[0]]==0:
            new_heap.pop(action[0])
    
        new_current_player = (self.current_player + 1) % self.num_players # a little confused
        environment = Environment(new_heap, new_current_player, self.num_players)
        return environment

    # Returns True if this state is a terminal state.
    def is_terminal(self) -> bool:
        return len(self.heap) == 1

    # Returns the value for this environment. Values can only be calculated for terminal states.
    def value(self, current_player: int) -> int:
        score = None
        if self.is_terminal() and (current_player < self.num_players):
            score = 1 if self.current_player == current_player else -1
        return score

    # Returns current state (num_players, current_player, heap)
    def state(self) -> tuple:
        state = (self.num_players, self.current_player, self.heap)
        return state



