
class HumanPlayer:
    def __init__(self, str_to_action):
        self.str_to_action = str_to_action
        pass

    def action(self, environment):
        print("Current Environment\n")
        print(environment)
        input_str = input("Enter your move: ")
        action = self.str_to_action(input_str)
        return action
