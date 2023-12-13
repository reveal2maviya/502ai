from itertools import permutations

def is_valid_assignment(assignment):
    s, e, n, d, m, o, r, y = assignment['S'], assignment['E'], assignment['N'], assignment['D'], assignment['M'], assignment['O'], assignment['R'], assignment['Y']
    return s != 0 and m != 0 and (1000 * s + 100 * e + 10 * n + d + 1000 * m + 100 * o + 10 * r + e == 10000 * m + 1000 * o + 100 * n + 10 * e + y)

def solve_cryptarithmetic():
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        if is_valid_assignment(assignment):
            print(f"Solution found: {assignment}")
            print(f"{assignment['S']} {assignment['E']} {assignment['N']} {assignment['D']}")
            print("+ {assignment['M']} {assignment['O']} {assignment['R']} {assignment['E']}")
            print("-----------")
            print(f"{assignment['M']} {assignment['O']} {assignment['N']} {assignment['E']} {assignment['Y']}")
            return
    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithmetic()
