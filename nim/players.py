from .utils import nim_sum

class PerfectPlayer:
    def __init__(self) -> None:
        pass

    def action(self, environment):
        """
        Returns an action that leads to a new environment with a nim-sum of zero (if that's possible).
        This strategy would produce a perfect play for environments with two players.
        """
        current_nim_sum = nim_sum(environment.heap)
        if current_nim_sum != 0:
            for heap_idx, current_stones in enumerate(environment.heap):
                wanted_stones = current_nim_sum ^ current_stones
                if wanted_stones <= current_stones:
                    return (heap_idx, current_stones - wanted_stones)
        
        return environment.random_action()
                       

class AlmostPerfectPlayer:
    def __init__(self, weakness_positions) -> None:
        self.weakness_positions = weakness_positions
        self.perfect = PerfectPlayer()

    def action(self, environment):
        """
        Acts as a perfect player unless it sees one of the weakness_positions, in which case, it returns a
        subobtimal action.
        """
        if environment.heap in self.weakness_positions:
            return environment.random_action()
        
        return self.perfect.action(environment)


class RandomPlayer:
    def __init__(self) -> None:
        pass

    def action(self, environment):
        """
        Produces random moves.
        """
        return environment.random_action()