class Mcts:
    '''
    Initializes a tree with a root environment. The tree will be filled
    runing a given number of rounds. The selection process will rely on
    an exploration_parameter.
    '''
    def __init__(self, environment, rounds, exploration_parameter):
        pass

    '''
    Given a current_environment, this method returns an action based on the
    current state of the montecarlo tree. 
    '''

    def selection(self, current_environemnt):
        pass

    '''
    Runs a current environment until a terminal state and returns its value. 
    It selects new environments based on a selection_function. The selection_function 
    takes an environment and returns an action. A simple selection_function will return a 
    random action from all possible actions.
    '''
    def simulation(self, current_environment, selection_function):
        pass

    '''
    Expands a current_environment until all its nodes have been visited at least once.
    '''
    def expansion(self, current_environment):
        pass

    '''
    Propagates the value from a node to all of its ancesters. 
    '''
    def backpropagation(self, current_environment, value):
        pass
