class TreeNode:
    def __init__(self, environment):
        '''
        Initializes a node for montecarlo tree search.
        '''
        pass

    def selection(self):
        '''
        Given a current_environment, this method returns an action based on the
        current state of the montecarlo tree. 
        '''
        pass

    def simulation(self, selection_function):
        '''
        Runs a current environment until a terminal state and returns its value. 
        It selects new environments based on a selection_function. The selection_function 
        takes an environment and returns an action. A simple selection_function will return a 
        random action from all possible actions.
        '''
        pass

    def expansion(self):
        '''
        Expands a current_environment until all its nodes have been visited at least once.
        '''
        pass

    def backpropagation(self, current_environment, value):
        '''
        Propagates the value from a node to all of its ancesters. 
        '''
        pass
