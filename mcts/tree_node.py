from .utils import random_rollout
from math import sqrt

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

    def selection(self, exploration_parameter=sqrt(2)):
        '''
        This method returns a list with the best child nodes based on the uct selection function
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