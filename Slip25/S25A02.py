from collections import deque

class PuzzleState:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))

def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i, row in enumerate(state.board) for j, val in enumerate(row) if val == 0)

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = [row[:] for row in state.board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbors.append(PuzzleState(new_board, parent=state))

    return neighbors

def reconstruct_path(goal_state):
    path = []
    while goal_state:
        path.append(goal_state.board)
        goal_state = goal_state.parent
    return path[::-1]

def solve_puzzle(initial_state):
    visited = set()
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()

        if current_state.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return reconstruct_path(current_state)

        visited.add(hash(current_state))

        for neighbor in get_neighbors(current_state):
            if hash(neighbor) not in visited:
                queue.append(neighbor)

    return None

if __name__ == "__main__":
    initial_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    initial_state = PuzzleState(initial_board)

    solution_path = solve_puzzle(initial_state)

    if solution_path:
        print("Solution Found:")
        for step, board in enumerate(solution_path):
            print(f"Step {step + 1}:")
            for row in board:
                print(row)
            print("------")
    else:
        print("No solution found.")
