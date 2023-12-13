"""
Iterative Deepening Depth-First Search (IDDFS) Algorithm

Question:
Write a program to implement Iterative Deepening DFS algorithm. [20 Marks ]
[ Goal Node = G]

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python iddfs_algorithm.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 iddfs_algorithm.py
"""

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def is_goal(node, goal_state):
    return node.state == goal_state

def generate_children(node, actions):
    return [Node(action(node.state), parent=node) for action in actions]

def depth_limited_dfs(start_node, goal_state, actions, max_depth):
    if is_goal(start_node, goal_state):
        return start_node

    if max_depth == 0:
        return None

    for child in generate_children(start_node, actions):
        result = depth_limited_dfs(child, goal_state, actions, max_depth - 1)
        if result is not None:
            return result

    return None

def iterative_deepening_dfs(start_state, goal_state, actions):
    depth = 0

    while True:
        start_node = Node(start_state)
        result = depth_limited_dfs(start_node, goal_state, actions, depth)

        if result is not None:
            return result

        depth += 1

# Example usage:
if __name__ == "__main__":
    # Define your state representation and actions
    initial_state = "A"
    goal_state = "G"
    possible_actions = {
        "A": lambda state: "B",
        "B": lambda state: "C",
        "C": lambda state: "D",
        "D": lambda state: "G"
    }

    # Run IDDFS algorithm
    result_node = iterative_deepening_dfs(initial_state, goal_state, possible_actions.values())

    # Print the path to the goal
    if result_node is not None:
        path = []
        while result_node is not None:
            path.insert(0, result_node.state)
            result_node = result_node.parent
        print("Path to Goal:", path)
    else:
        print("Goal not reachable within the given depth limit.")
