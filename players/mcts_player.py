from random import choice
from math import sqrt
from context import mcts

class MctsPlayer:
    def __init__(self, rounds=1000, exploration_param=sqrt(2), oponent=None, cache=dict()):
        self.cache=cache

    def action(self, environment):
        current_node=self.cache.get(environment, mcts.TreeNode(environment, self.cache))
        if not current_node.is_expanded: # num_rounds vs num_visits
            current_node.expansion()
        
        return choice(current_node.selection(0))

