from mcts.tree_node import TreeNode
from random import choice


class MctsPlayer:
    def __init__(self,
                 cache=dict(),
                 exploration_param=0.5,):
        self.exploration_param = exploration_param
        self.cache = cache

    def action(self, environment):
        
        turn=environment.turn()

        if environment not in self.cache:
            self.cache[environment]=TreeNode(environment, self.cache)
        
        current_node = self.cache.get(environment)
        
        if not current_node.is_expanded:
            current_node.expansion()

        action=choice(current_node.selection(self.exploration_param))

        next_node=current_node.children[action]

        if not next_node.is_expanded:
            next_node.expansion()
        
        return action






