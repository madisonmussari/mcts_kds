# mcts_kds

mcts_kds is a Python library used to apply Monte Carlo Tree Search algorithm to solve complete information two player games (eg. tictactoe, chess, othello).

To show how mcts works, I coded the game nim and created a mcts player to chose moves that would lead to a win. However, the purpose of creating this library was to allow others to apply the algorithm to games they program.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mcts_kds.

```bash
pip install mcts_kds
```

## Implementing Players

You can create and import different types of players by implementing action,a function that determines how the player will chose moves in certain environments.For nim I created a perfect player, almost perfect player, and random player.
The library gives by default a HumanPlayer and MctsPlayer, however, you could add more by implementing action.

This is an example of how you could code a new player:

```python

class Player:
    def __init__(self) -> None:
        pass

    def action(self, environment):
        """
        Determines a certain action for a player to make.

        Args:
            environment: nim.Environment

        Returns:
            int
                the action chosen
        """
        return action

```

## Importing

When you install mcts-kds, the you will gets access to the following libraries:
mcts, nim, players, test, and utils

## Usage Examples

```python

import players
from nim import str_to_action
from nim import Environment
import utils

if __name__ == "__main__":
    start_board = Environment([2, 3, 1], 0, 2)

    player1 = players.MctsPlayer(exploration_param = 0.5)
    player2 = players.HumanPlayer(str_to_action)

    # here we are training the MctsPlayer by playing it against itself for multiple rounds 
    # and determining the results of these games; here the MctsPlayer is self-playing for 10000 rounds
    for _ in range(10000):
        log = utils.play(start_board, [player1, player1])
        (last_environment, _, _) = log[-1]
        game_value = [last_environment.value(k) for k in range(last_environment.num_agents())]
        player1.cache[last_environment].backpropagation(game_value)

    log = utils.play(start_board, [player1, player2])
    print(log)

```

## Format for Your Own Game

When using mcts_kds you should format your two-player game as follows (see nim --> environment.py for more details):

```python
class Environment:
"""
Creates a new game environment.
"""
    def __init__(self):

    def turn(self):
        """
        Determines which player's turn it is. 

        Returns:
            int
                the identifier for the current player
        """
        return

    def valid_actions(self):
        """
        Finds the possible actions that could be taken by the player in the current environment. 

        Returns:
            iterator
                an iterable of valid actions
        """
        return

    def random_action(self):
        """
        Produces a valid random action.

        Returns:
            int
                a random action
        """
        return
    
    def what_if(self, action):
        """
        Produces game state/environment assuming that player moves "action". 

        Returns:
            environment
                the state which results from taking action
        """
        return

    def is_terminal(self):
        """
        Checks if the current environment represents a terminal position. 

        Returns:
            Boolean
                True if the state is terminal, False if it is not
        """
        return

    def value(self, current_player):
        """
        Determines the value of a terminal environment (last node in a branch). If the environment is not terminal, it returns None.

        Returns:
            int
                the value for this environment (1 for a win and -1 for a loss) when the environment is not terminal, it returns None.
        """
        return

    def num_agents(self):
        """
        Determines how many agents are playing in the game.
        
        Returns:
            int
                number of agents in the game
        """
        return

    def state(self):
        """
        Describes the current environment of the game.

        Returns:
            list
                the state 
        """
        return

    def __repr__(self):
    """
    Makes the current environment information into a string.

    Returns:
        str
    """
        return

    def __eq__(self):
        return
    
    def __hash__(self):
        return

def from_state(state):
"""
Creates a nim environment from the current state.

Returns:
    list
        a list of states
"""
    return

def str_to_action(action_str):
"""
Converts a string into an action for Nim.

Returns:
    str
        actions intended by action_str
 """
    return
 
```

## Documentation

Docstrings have been written for individual, methods within the code, stating the general goal for the method and what is being sent and returned from it.

## Tests

Tests have been coded for all major methods and can be used as a tool to understand the true functionality of the code.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author

Written by Madison Mussari during the Summer of 2021.