from random import randrange
class PerfectPlayer:
    def __init__(self) -> None:
        self.nim_sum = 0
        pass

    def nim_sum(self, environment):
        for i in environment.heap:
            self.nim_sum = self.nim_sum ^ i

    def action(self, environment):
        """
        Returns an action that leads to a new environment with a nim-sum of zero (if that's possible).
        This strategy would produce a perfect play for environments with two players.
        """
        if self.nim_sum == 0:
            move = environment.random_action()
        else:
            






class AlmostPerfectPlayer:
    def __init__(self, weakness_positions) -> None:
        self.weakness_positions = weakness_positions

    def action(self, environment):
        """
        Acts as a perfect player unless it sees one of the weakness_positions, in which case, it returns a
        subobtimal action.
        """
        pass

class RandomPlayer:
    def __init__(self) -> None:
        pass

    def action(self, environment):
        """
        Produces random moves.
        """
        return environment.valid_actions[randrange(len(environment.valid_actions))]  # or just use random_action()