"""
Monkey Banana Problem Solver

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python monkey_banana_problem.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 monkey_banana_problem.py
"""

def monkey_banana_problem(room):
    monkey_position = (0, 0)
    banana_positions = [(3, 1), (2, 2), (1, 4)]

    def heuristic(position):
        # Simple heuristic function (Manhattan distance to the closest banana)
        return min(abs(position[0] - banana[0]) + abs(position[1] - banana[1]) for banana in banana_positions)

    def move(position, action):
        x, y = position
        if action == "UP":
            return (x - 1, y)
        elif action == "DOWN":
            return (x + 1, y)
        elif action == "LEFT":
            return (x, y - 1)
        elif action == "RIGHT":
            return (x, y + 1)

    def is_valid_move(position, room):
        x, y = position
        return 0 <= x < len(room) and 0 <= y < len(room[0]) and room[x][y] != "WALL"

    def possible_moves(position, room):
        moves = ["UP", "DOWN", "LEFT", "RIGHT"]
        valid_moves = [move(position, action) for action in moves if is_valid_move(move(position, action), room)]
        return valid_moves

    initial_state = {"position": monkey_position, "remaining_bananas": set(banana_positions)}
    stack = [initial_state]

    while stack:
        current_state = stack.pop()
        if not current_state["remaining_bananas"]:
            return len(banana_positions) - len(current_state["remaining_bananas"])

        moves = possible_moves(current_state["position"], room)
        next_states = [{"position": move, "remaining_bananas": current_state["remaining_bananas"] - {move}} for move in moves]

        # Use heuristic to prioritize moves
        next_states.sort(key=lambda state: heuristic(state["position"]), reverse=True)

        stack.extend(next_states)

    return None

if __name__ == "__main__":
    # Define the room with "WALL" representing walls
    room = [
        ["", "", "", "", ""],
        ["", "", "", "WALL", ""],
        ["", "", "WALL", "", ""],
        ["", "", "", "", ""],
    ]

    bananas_eaten = monkey_banana_problem(room)
    print(f"The monkey can eat {bananas_eaten} bananas.")
