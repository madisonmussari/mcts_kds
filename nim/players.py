from .utils import nim_sum

class PerfectPlayer:
    """
    A PerfectPlayer choses an optimal action for the game nim.
    """
    def __init__(self) -> None:
        pass

    def action(self, environment):
        """
        Returns an action that leads to a new environment with a nim-sum of zero (if that's possible).
        This strategy would produce a perfect play for environments with two players.

        Args:
            environment: nim.Environment
                PerfectPlayer choses an action for this environment

        Returns:
            (pile,num_stones): (int,int)
                the location and number of stones removed from a heap
        """
        # a perfect player attempts to return a heap with a nim_sum of 0
        current_nim_sum = nim_sum(environment.heap)
        if current_nim_sum != 0:
            for heap_idx, current_stones in enumerate(environment.heap):
                wanted_stones = current_nim_sum ^ current_stones
                if wanted_stones <= current_stones:
                    return (heap_idx, current_stones - wanted_stones)
        
        return environment.random_action()
                       

class AlmostPerfectPlayer:
    """
    An AlmostPerfectPlayer choses an optimal action for the game nim, except when in a weakness_position.
    """
    def __init__(self, weakness_positions) -> None:
        """
        Args:
            weakness_positions: environment #CHECK
        """
        self.weakness_positions = weakness_positions
        self.perfect = PerfectPlayer()

    def action(self, environment):
        """
        Acts as a perfect player unless it sees one of the weakness_positions, in which case, it returns a
        subobtimal action.

        Args:
            environment: nim.Environment
                AlmostPerfectPlayer choses an action for this environment

        Returns:
            (pile,num_stones): (int,int)
                the location and number of stones removed from a heap
        """
        if environment.heap in self.weakness_positions:
            return environment.random_action()
        
        return self.perfect.action(environment)


class RandomPlayer:
    """
    A RandomPlayer choses random valid actions for the game nim.
    """
    def __init__(self) -> None:
        pass

    def action(self, environment):
        """[summary]

        Args:
            environment: nim.Environment
                RandomPlayer choses an action for this environment

        Returns:
            (pile,num_stones): (int,int)
                the location and number of stones removed from a heap
        """
        return environment.random_action()