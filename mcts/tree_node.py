from random import choice
from math import inf, log, sqrt

from .utils import random_rollout


class TreeNode:
    """
    Executes the four steps in mcts: selection, expansion, simulation, and backpropagation for a specific node.
    """
    def __init__(self, environment, cache=dict()):
        """
        Initializes a node for montecarlo tree search.

        Args:
            environment: nim.Environment
            cache: dict
                takes a node and returns its corresponding tree_node.
        """
        self.environment = environment
        self.cache = cache
        if environment in cache:
            stored_node = cache.get(environment)
            self.num_visits = stored_node.num_visits
            self.agent_to_value = stored_node.agent_to_value
            self.is_expanded = stored_node.is_expanded
            self.children = stored_node.children
            self.parents = stored_node.parents
        else:
            self.num_visits = 0
            self.agent_to_value = [0] * self.environment.num_agents()
            self.is_expanded = False
            self.children = dict()
            self.parents = set()

        self.cache[environment] = self

    def __repr__(self) -> str:
        return f"Environment {self.environment}, Parent {self.parent}, Action {self.action} "

    def selection(self, exploration_parameter=0.5): # theoretically the exploration parameter is equal to sqrt(2)
        """
        This method returns a list of valid actions with higher ucb score (specific formula used to determine).

        Args:
            exploration_parameter: int
                keeps the balance between exploring new parts of the tree or exploiting current parts that have been explored; defaults to sqrt(2)

        Returns:
            best_actions: list
                contains actions that will lead to a desirable result for the current player.
        """
        
        total_visits = 0
        for child in self.children.values():
            total_visits += child.num_visits

        best_actions = []
        best_score = -inf
        current_player = self.environment.turn()
        for action, child in self.children.items():
            child_value = child.agent_to_value[current_player]
            child_visits = child.num_visits
            score = child_value / child_visits + sqrt( 
                exploration_parameter *
                log(total_visits) / child_visits)
            if score == best_score:
                best_actions.append(action)
                best_score = score
            elif score > best_score:
                best_actions.clear()
                best_actions.append(action)
                best_score = score

        return best_actions

    def simulation(self, exploration_param=0.5, rollout_strategy=random_rollout):
        """
        Runs a current environment until a terminal state and returns its value. 
        For expanded nodes, it chooses the next environment based on the selection function. 
        For not expanded nodes, it chooses the next environment using a rollout_strategy.
        The rollout_strategy takes an environment and returns an action. 
        The default rollout_strategy will return a random action from all possible actions.

        Args:
            rollout_strategy: environment
                takes an environment and returns an action. Defaults to random_rollout.

        Returns:
            simulation_value: list 
        """

        current_node = self
        while current_node.is_expanded and not current_node.environment.is_terminal():
            best_action = choice(current_node.selection(exploration_param))
            current_node = current_node.children[best_action]

        current_environment = current_node.environment
        while not (current_environment.is_terminal()):
            current_environment = current_environment.what_if(rollout_strategy(current_environment))
        
        simulation_value = [
            current_environment.value(k)
            for k in range(current_environment.num_agents())
        ]

        # current_node.backpropagation(simulation_value)
        return simulation_value

   
    def expansion(self):
        """
        Populates the children of a node. 
        """
        if self.is_expanded:
            return

        for action in self.environment.valid_actions():
            child_environment = self.environment.what_if(action)

            if child_environment in self.cache:
                child_node = self.cache.get(child_environment)
            else:
                child_node = TreeNode(child_environment, self.cache)

            child_node.parents.add(self.environment)
            child_node_value = child_node.simulation()
            child_node.backpropagation(child_node_value)
            self.children[action] = child_node

        self.is_expanded = True

    def backpropagation(self, value):
        """
        Propagates the value from a node to all of its ancestors. 
        
        Args:
            value: int
                the specifc value of the environment (1 for a win and -1 for a loss) 
        """
        for i in range(len(self.agent_to_value)):
            self.agent_to_value[i] += value[i]

        self.num_visits += 1

        for parent in self.parents:
            parent_node = self.cache.get(parent)
            parent_node.backpropagation(value)