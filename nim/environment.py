## TODO: Document the functions. 
import random

class Environment:
    # creates a new nim environment
    def __init__(self, heap=[10, 10, 10], current_player=0, num_players=2):

        self.heap = [h for h in sorted(heap) if h > 0]
        self.current_player = current_player if current_player < num_players else 0
        self.num_players = num_players

    #  Returns the identifier for the current player.
    def turn(self):
        return self.current_player

    # Returns an iterable of all actions which can be taken from this environment.
    def valid_actions(self):
        if self.is_terminal():
            return iter([])
        
        return ((i, j) for i in range(len(self.heap)) for j in range(1, self.heap[i]+ 1))

    def random_action(self):
        '''
        Produces a random action
        '''
        if self.is_terminal():
            return None

        pile = random.choices(range(len(self.heap)), weights=self.heap)[0]
        pile_stones = self.heap[pile]
        num_stones = random.randrange(0,pile_stones) + 1

        # return random.choice([a for a in self.valid_actions()])

        return (pile,num_stones)


    # Returns the state which results from taking action. Actions are of the form (heap, stones_to_take_out)
    def what_if(self, action): 

        if action[0] < 0 or action[0] > len(self.heap) - 1:
            return Environment(self.heap, self.current_player, self.num_players)
        
        new_value = self.heap[action[0]] - action[1]
        if new_value < 0 or self.is_terminal() or action[1] <= 0:
            return Environment(self.heap, self.current_player, self.num_players)
        
        new_heap = self.heap.copy()
        new_heap[action[0]] = new_value
        
        if new_heap[action[0]]==0:
            new_heap.pop(action[0])
    
        new_current_player = (self.current_player + 1) % self.num_players # a little confused
        environment = Environment(new_heap, new_current_player, self.num_players)
        return environment

    # Returns True if this state is a terminal state.
    def is_terminal(self):
        return len(self.heap) == 1

    # Returns the value for this environment. Values can only be calculated for terminal states.
    def value(self, current_player):
        score = None
        if self.is_terminal() and (current_player < self.num_players):
            score = 1 if self.current_player == current_player else -1
        return score
    
    # Returns number of agents
    def num_agents(self):
        return self.num_players

    # Returns current state (num_players, current_player, heap)
    def state(self):
        state = (tuple(self.heap), self.current_player, self.num_players)
        return state
    
    # Making it into a string
    def __repr__(self) -> str:
        return f"Heap {self.heap}, Current Player {self.current_player}, Number of Players {self.num_players}"

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Environment):
            return self.heap == o.heap and self.current_player == o.current_player and self.num_players == o.num_players 
        return False

# Returns an environment from a state
def from_state(state):
    return Environment(list(state[0]), state[1], state[2])


def str_to_action(action_str):
    return tuple(map(int, action_str.split(",")))

