from .utils import random_rollout

class TreeNode:
    def __init__(self, environment, parent=None):
        '''
        Initializes a node for montecarlo tree search.
        '''
        self.environment = environment
        self.num_visits = 0
        self.agent_to_value = []    # Keeps a list with the current value for each agent.
        self.children = []
        self.is_expanded = False
        self.parent = parent
        pass

    def selection(self, exploration_parameter):
        '''
        Given a current_environment, this method returns an action based on the
        current state of the montecarlo tree. 
        '''
        pass

    def simulation(self, rollout_strategy=random_rollout):
        '''
        Runs a current environment until a terminal state and returns its value. 
        It selects new environments based on a selection_function. The rollout_strategy 
        takes an environment and returns an action. A simple rollout_strategy will return a 
        random action from all possible actions.
        '''
        pass

    def expansion(self):
        '''
        Populates children
        '''
        pass

    def backpropagation(self, value):
        '''
        Propagates the value from a node to all of its ancesters. 
        '''
        pass
