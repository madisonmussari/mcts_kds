import random

class Environment:
    """
    Creates a new nim environment.
    """
    def __init__(self, heap=[10, 10, 10], current_player=0, num_players=2):
        """
        Args:
            heap: [int]
                describes the number of heaps and stones in each heap. Defaults to [10, 10, 10].
            current_player: int
                keeps track of which player's turn it is. Defaults to 0.
            num_players: int
                takes note of the number of players in the game. Defaults to 2.
        """

        self.heap = [h for h in sorted(heap) if h > 0]
        self.current_player = current_player if current_player < num_players else 0
        self.num_players = num_players

    
    def turn(self): 
        """
        Determines which player's turn it is. 

        Returns:
            current_player: int 
                the identifier for the current player
        """
        return self.current_player


    def valid_actions(self):
        """
        Finds the possible actions that could be taken by the player in the current environment. 

        Returns:
            valid_action_iterable: [(pile,num_stones)]
                a valid heap and number of stones that a player could take from that heap. 
        """
        if self.is_terminal():
            return iter([])
        
        return ((i, j) for i in range(len(self.heap)) for j in range(1, self.heap[i]+ 1))

    def random_action(self):
        """
        Produces a valid random action.

        Returns:
           (pile,num_stones): (int,int)
                the location and number of stones removed from a heap
        """
        if self.is_terminal():
            return None

        pile = random.choices(range(len(self.heap)), weights=self.heap)[0]
        pile_stones = self.heap[pile]
        num_stones = random.randrange(0,pile_stones) + 1

        # return random.choice([a for a in self.valid_actions()])

        return (pile,num_stones)


    def what_if(self, action): 
        """
        Produces game state/environment assuming that player moves "action". 

        Args:
            action (int,int): Describes the location and number of stones removed from a heap by the player

        Returns:
            environment: nim.Environment
                the state which results from taking action
        """

        if action[0] < 0 or action[0] > len(self.heap) - 1:
            return Environment(self.heap, self.current_player, self.num_players)
        
        new_value = self.heap[action[0]] - action[1]
        if new_value < 0 or self.is_terminal() or action[1] <= 0:
            return Environment(self.heap, self.current_player, self.num_players)
        
        new_heap = self.heap.copy()
        new_heap[action[0]] = new_value
        
        if new_heap[action[0]]==0:
            new_heap.pop(action[0])
    
        new_current_player = (self.current_player + 1) % self.num_players 
        environment = Environment(new_heap, new_current_player, self.num_players)
        return environment


    def is_terminal(self):
        """
        Checks if the current heap represents a terminal position. 

        Returns:
            Boolean: True or False
                True if the state is terminal, False if it is not
        """
        return len(self.heap) == 1

    
    def value(self, current_player):
        """
        Determines the value of a terminal environment (last node in a branch). If the environment is not terminal, it returns None

        Args:
            current_player (int): the identifier for the current player

        Returns:
            score: int
                the value for this environment (1 for a win and -1 for a loss)
                when the environment is not terminal, it returns None.
        """
        score = None
        if self.is_terminal() and (current_player < self.num_players):
            score = 1 if self.current_player == current_player else -1
        return score
    
    def num_agents(self):
        """
        Returns:
            num_players: int
                number of agents in the game
        """
        return self.num_players

    
    def state(self):
        """
        Describes the current envrionment of the game.

        Returns:
            state: list
               (heap, current_player, num_players)  
        """
        state = (tuple(self.heap), self.current_player, self.num_players)
        return state
    

    def __repr__(self) -> str:
        """
        Makes the current environment information into a string.

        Returns:
            environment_str: str
                describes heap, current_player, and num_player information
        """
        return f"Heap {self.heap}, Current Player {self.current_player}, Number of Players {self.num_players}"

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Environment):
            return self.heap == o.heap and self.current_player == o.current_player and self.num_players == o.num_players 
        return False
    
    def __hash__(self) -> int:
        return hash(repr(self))


def from_state(state):
    """
    Creates a nim environment from the current state.

    Args:
        state (list): (heap, current_player, num_players) 

    Returns:
        Environment: list
            returns a list of states
    """
    return Environment(list(state[0]), state[1], state[2])


def str_to_action(action_str):
    """
    Converts a string into an action for Nim.

    Args:
        action_str (str):
            A string of the form "(pile,num_stones)"

    Returns:
        (int, int):
            ((pile,num_stones)), actions intended by action_str
    """
    return tuple(map(int, action_str.split(",")))

