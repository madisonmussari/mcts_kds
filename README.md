# mcts_kds

mcts_kds is a Python library used to apply Monte Carlo Tree Search algorithm to two player games that allows the current player to have complete information (eg. tictactoe, chess, othello)

To show how mcts works, I coded the game nim and created a mcts player to chose moves that would lead to a win. However, the purpose of creating this library was to allow others to apply the algorithm to games they program.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mcts_kds.

```bash
pip install mcts_kds
```

## Usage Examples

```python
import mcts_kds

# this function determines which player's turn it is
mcts_kds.turn()

# this function produces the game state/environment assuming that player moves "action"
mcts_kds.what_if(action)

# excecutes the simulation step in the mcts algorithm; 
# runs a current environment until a terminal state is reached and returns its value
mcts_kds.simulation(exploration_param = 0.5, rollout_strategy=random_rollout)

```

## Format for Game

When using mcts_kds you should format your two-player game as follows (see nim --> environment.py for more details):

```python
class Environment:
"""
Creates a new game environment.
"""
    def __init__(self):

    def turn(self):
        return

    def valid_actions(self):
        return

    def random_action(self):
        return
    
    def what_if(self):
        return

    def is_terminal(self):
        return

    def value(self):
        return

    def num_agents(self):
        return

    def state(self):
        return

    def __repr__(self):
        return

    def __eq__(self):
        return
    
    def __hash__(self):
        return
 
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author

Written by Madison Mussari during the Summer of 2021, supervised by Pedro Rangel.