def i_ll_play():
    print("I'll play")


class Environment:
    # Creates a new Nim environment with the current heap allocation and player.
    def __init__(self,
                 heap=[10, 10, 10],
                 current_player=0,
                 num_players=2,
                 game_play = True):
        self.heap = heap
        self.current_player = current_player
        pass

    #  Returns the identifier for the current player.
    def turn(self,current_player, num_players):
        if current_player < num_players:
            current_player += 1
        else:
            current_player = 0
        return current_player


    # Returns an iterable of all actions which can be taken from this environment.
    def valid_actions(self, heap):
        sort_heap = sorted(self.heap)
        actions = []
        stone_num = 0
        for i in len(sort_heap+1):
            stone_num = sort_heap[i]




        pass

    # Returns the state which results from taking action. Actions are of the form (heap, stones_to_take_out)
    def what_if(self, action):

        pass

    # Returns True if this state is a terminal state.
    def is_terminal(self,heap,current_player):
        if all([ i == 0 for i in heap]):
            self.value(current_player)
            return True
        return False

    # Returns the value for this environment. Values can only be calculated for terminal states.
    def value(self, current_player):
        result = 0
        last_player = current_player
        score = -1
        return last_player, score

    # Returns current state (num_players, current_player, heap)
    def state(self, num_players, current_player, heap):
        state = [num_players, current_player, heap]
        return state

# main program -  do I need this?
# while self.game_play == True:
#   self.turn()



