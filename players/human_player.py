
class HumanPlayer:
    """
    
    """
    def __init__(self, str_to_action):
        """
        Args:
            str_to_action ([type]): [description]
        """
        self.str_to_action = str_to_action
        pass

    def action(self, environment):
        """

        Args:
            environment: nim.Environment

        Returns:
            action(int,int): Describes the location and number of stones removed from a heap by the player
        """
        print("Current Environment\n")
        print(environment)
        input_str = input("Enter your move: ")
        action = self.str_to_action(input_str)
        return action
