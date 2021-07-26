from .utils import random_rollout
from math import sqrt
from nim import environment

class TreeNode:
    def __init__(self, environment, parent=None, action=None):
        '''
        Initializes a node for montecarlo tree search.
        '''
        self.environment = environment
        self.num_visits = 0
        self.agent_to_value = [0] * self.environment.num_agents()     # Keeps a list with the current value for each agent.
        self.children = []        
        self.is_expanded = False
        self.parent = parent
        self.action = action
        pass
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, TreeNode):
            return self.environment == o.environment and \
                 self.is_expanded == o.is_expanded and \
                     self.parent == o.parent and \
                         self.action == o.action and \
                             self.num_visits == o.num_visits and \
                                 self.agent_to_value == o.agent_to_value
        return False

    def __repr__(self) -> str:
        return f"Environment {self.environment}, Parent {self.parent}, Action {self.action} "
        
    def __hash__(self) -> int:
        return hash(repr(self))

    def selection(self, exploration_parameter=sqrt(2)):
        '''
        This method returns a list with the subset of children with higher ucb score.
        '''
        pass

    def simulation(self, rollout_strategy=random_rollout):
        '''
        Runs a current environment until a terminal state and returns its value. 
        It selects new environments based on a selection_function. The rollout_strategy 
        takes an environment and returns an action. A simple rollout_strategy will return a 
        random action from all possible actions.
        '''
        current_environment = self.environment
        while not (current_environment.is_terminal()):
            current_environment = rollout_strategy(current_environment)
        return [current_environment.value(k) for k in range(current_environment.num_agents())]

    def expansion(self):
        '''
        Populates children. To initalize a child we must give it the current environment, parent, and action.
        '''
        self.children = [TreeNode(self.environment.what_if(action), self, action) for action in self.environment.valid_actions()]
        
        for child in self.children:
            child.simulation()
        
        self.is_expanded = True
    

    def backpropagation(self, value):
        '''
        Propagates the value from a node to all of its ancesters. 
        '''
        for i in range(len(self.agent_to_value)):   
            self.agent_to_value[i] += value[i]
        
        self.num_visits +=1

        if self.parent != None:
            self.parent.backpropagation(value)

        



