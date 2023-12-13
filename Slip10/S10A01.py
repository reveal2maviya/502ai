"""
Cryptarithmetic Problem Solver

Question:
Write a Python program to solve the cryptarithmetic problem "TWO + TWO = FOUR".

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python cryptarithmetic_solver.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 cryptarithmetic_solver.py
"""

from itertools import permutations

def is_valid_assignment(mapping):
    # Check if there is a leading zero in any word
    if mapping['T'] == 0 or mapping['F'] == 0:
        return False

    # Evaluate the expression
    two_sum = mapping['T'] * 100 + mapping['W'] * 10 + mapping['O']
    four = mapping['F'] * 1000 + mapping['O'] * 100 + mapping['U'] * 10 + mapping['R']

    return two_sum + two_sum == four

def cryptarithmetic_solver():
    unique_letters = set("TWOFOUR")
    if len(unique_letters) != 7:
        print("Invalid cryptarithmetic problem.")
        return

    for perm in permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))
        if is_valid_assignment(mapping):
            print(f"Solution found: {mapping}")
            break
    else:
        print("No solution found.")

if __name__ == "__main__":
    cryptarithmetic_solver()
