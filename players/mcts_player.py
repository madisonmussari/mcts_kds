from random import choice
from context import mcts

class MctsPlayer:
    def __init__(self, rounds=1, exploration_param=0.5, opponent=None, cache=dict()):
        self.rounds=rounds
        self.exploration_param=exploration_param
        self.opponent = opponent
        self.cache=cache

    def action(self, environment):
        if environment in self.cache:
            current_node = self.cache.get(environment)
        else:
            current_node = mcts.TreeNode(environment, self.cache)

        if not current_node.is_expanded: # num_rounds vs num_visits
            current_node.expansion()
        
        for i in range(self.rounds):
            if self.opponent == None:
                current_node.simulation(self.exploration_param)
            else:
                current_node.simulation(self.exploration_param, self.opponent.action)

        return choice(current_node.selection(self.exploration_param))

