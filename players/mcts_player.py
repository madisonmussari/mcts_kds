from random import choice
from mcts.tree_node import TreeNode

class MctsPlayer:
    def __init__(self, cache=dict()):
        self.cache=cache

    def action(self, environment):
        current_node=self.cache.get(environment, TreeNode(environment, self.cache))
        if not current_node.is_expanded:
            current_node.expansion()
        
        return choice(current_node.selection(0))


    def train(self, environment, rounds, exploration_param, oponent=None):
        pass
