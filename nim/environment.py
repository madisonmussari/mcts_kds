


class Environment:
    def __init__(self, heap: list(int), player) -> Environment:
        self.heap = heap
        self.current_player = player
        pass

    #  Returns 1 if it is the maximizer player's turn to choose an action, or -1 for the minimiser player
    def getCurrentPlayer():
        pass 
    
    # Returns an iterable of all actions which can be taken from this environment
    def getPossibleActions():
        pass

    # Returns the state which results from taking action
    def takeAction(action: list(int)):
        pass

    # Returns True if this state is a terminal state
    def isTerminal():
        pass

    # Returns the reward for this environment. Only needed for terminal states.
    def getReward():
        pass

    

    

