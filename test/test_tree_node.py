from context import nim
# from mcts import tree_node

# test the functions in the TreeNode class

def test_selection(): # I don't think the way we brainstormed this test will work...
    environment = nim.Environment([2, 3, 1], 0, 2)
    expected_num_visits  = 0
    expected_num_wins = 0
    expected_children = []
    expected_is_expanded = False
    pass

def test_expansion():
    environment = nim.Environment([2, 3, 1], 0, 2) # should it instead be mcts.TreeNode?
    expected_children_before_expansion = {}
    expected_children_expansion = {([1, 3, 1], 1, 2), ([3, 1], 1, 2), ([2, 2, 1], 1, 2), ([2, 1, 1], 1, 2), ([2, 1], 1, 2),  ([2, 3, 0], 1, 2)}
    assert environment == expected_children_before_expansion
    assert environment.expansion() == expected_children_expansion # why is the function not being recognized?

    environment = nim.Environment([2, 2, 2], 0, 3)
    expected_children = {([1, 2, 2], 1, 3), ([2, 2], 1, 3), ([2, 1, 2], 1, 3), ([2, 2, 1], 1, 3)}
    assert environment.expansion() == expected_children

def test_backpropogation():
    
    pass

def test_simulation():
    pass