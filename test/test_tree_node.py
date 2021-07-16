from mcts import tree_node
from nim import environment
from context import nim
from context import mcts

# test the functions in the TreeNode class

def test_selection(): # I don't think the way we brainstormed this test will work...
    
    pass

def test_expansion():
    # First example
    environment = nim.Environment([2, 3, 1], 0, 2) # should it instead be mcts.TreeNode?
    tree_node = mcts.TreeNode(environment)

    expected_children_before_expansion = {}
    real_children_before_expansion = set(tree_node.children)

    assert expected_children_before_expansion == real_children_before_expansion

    tree_node.expansion()
    expected_children_constructor = [([1, 3, 1], 1, 2), ([3, 1], 1, 2), ([2, 2, 1], 1, 2), ([2, 1, 1], 1, 2), ([2, 1], 1, 2),  ([2, 3, 0], 1, 2)]
    expected_children_after_expansion = {mcts.TreeNode(nim.Environment(a[0], a[1], a[2])) for a in expected_children_constructor}
    assert set(tree_node.children) == expected_children_after_expansion

    # Second example
    environment = nim.Environment([2, 2, 2], 2, 3)
    tree_node = mcts.TreeNode(environment)

    expected_children_before_expansion = {}
    real_children_before_expansion = set(tree_node.children)

    assert expected_children_before_expansion == real_children_before_expansion
    
    tree_node.expansion()
    expected_children_constructor = {([1, 2, 2], 0, 3), ([2, 2], 0, 3), ([2, 1, 2], 0, 3), ([2, 2, 1], 0, 3)}
    expected_children_after_expansion = {mcts.TreeNode(nim.Environment(a[0], a[1], a[2])) for a in expected_children_constructor}
    assert set(tree_node.children) == expected_children_after_expansion


def test_backpropogation():
    node_0 = mcts.TreeNode([])
    node_1 = mcts.TreeNode([], parent=node_0)
    node_2 = mcts.TreeNode([], parent=node_1)
    node_3 = mcts.TreeNode([], parent=node_2)

    assert node_0.num_visits == 0
    assert node_1.num_visits == 0
    assert node_2.num_visits == 0
    assert node_3.num_visits == 0

    assert node_0.agent_to_value == []
    assert node_1.agent_to_value == []
    assert node_2.agent_to_value == []
    assert node_3.agent_to_value == []

    node_3.backpropagation([1, 0, -1])

    assert node_0.num_visits == 1
    assert node_1.num_visits == 1
    assert node_2.num_visits == 1
    assert node_3.num_visits == 1

    assert node_0.agent_to_value == [1, 0, -1]
    assert node_1.agent_to_value == [1, 0, -1]
    assert node_2.agent_to_value == [1, 0, -1]
    assert node_3.agent_to_value == [1, 0, -1]

    node_3.backpropagation([-1, 1, 1])

    assert node_0.num_visits == 2
    assert node_1.num_visits == 2
    assert node_2.num_visits == 2
    assert node_3.num_visits == 2

    assert node_0.agent_to_value == [0, 1, 0]
    assert node_1.agent_to_value == [0, 1, 0]
    assert node_2.agent_to_value == [0, 1, 0]
    assert node_3.agent_to_value == [0, 1, 0]

    node_3.backpropagation([-1, 1, 1])

    assert node_0.num_visits == 3
    assert node_1.num_visits == 3
    assert node_2.num_visits == 3
    assert node_3.num_visits == 3

    assert node_0.agent_to_value == [-1, 2, 1]
    assert node_1.agent_to_value == [-1, 2, 1]
    assert node_2.agent_to_value == [-1, 2, 1]
    assert node_3.agent_to_value == [-1, 2, 1]
    

    pass

def test_simulation():
    # An environment that always leads to a win
    heap = [1] * 5
    environment = nim.Environment(heap, 0, 2)
    tree_node = mcts.TreeNode(environment)

    expected_value = [1, -1]
    real_value = tree_node.simulation()
    assert expected_value == real_value

    # An environment that always leads to a loss
    heap = [1] * 6
    environment = nim.Environment(heap, 0, 2)
    tree_node = mcts.TreeNode(environment)

    expected_value = [-1, 1]
    real_value = tree_node.simulation()
    assert expected_value == real_value