from itertools import permutations

def is_valid_assignment(assignment):
    g, o, t, u = assignment['G'], assignment['O'], assignment['T'], assignment['U']
    return g != 0 and t != 0 and u != 0 and (g * 10 + o + t * 10 + o == u * 100 + t * 10 + g)

def solve_cryptarithmetic():
    letters = ['G', 'O', 'T', 'U']
    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        if is_valid_assignment(assignment):
            print(f"Solution found: {assignment}")
            print(f"{assignment['G']} {assignment['O']}")
            print("+ {assignment['T']} {assignment['O']}")
            print("--------")
            print(f"{assignment['O']} {assignment['U']} {assignment['T']} {assignment['U']}")
            return
    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithmetic()
