#!/usr/bin/env python


PUZZLE="""11111
S1X11
11111
X11E1
1111X""".split('\n')

import copy

ROWS = len(PUZZLE)
COLS = len(PUZZLE[0])


def print_puzzle(puzzle):
    for line in puzzle:
        print(''.join([ch for ch in line]))
    print('')

def find_path(puzzle, row, col, distance_so_far):
    # Find all possible paths to 'E', return solution and length tuples
    # test current location, if '1' change to 'P' and continue.
    # if 'E' we have a solution
    solutions = []
    if puzzle[row][col] == 'E':
        solution = copy.deepcopy(puzzle)
        return [(solution, distance_so_far)]
    if puzzle[row][col] not in ('1', 'S'):
        return []
    left = col == 0
    right = col == COLS - 1
    top = row == 0
    bottom = row == ROWS - 1
    orig = puzzle[row][col]
    # move in all possible directions and recurse
    if not right:
        if orig != 'S':
            puzzle[row][col] = 'P'
        solutions += find_path(puzzle, row, col + 1, distance_so_far + 1)
        puzzle[row][col] = orig
    if not left:
        if orig != 'S':
            puzzle[row][col] = 'P'
        solutions += find_path(puzzle, row, col - 1, distance_so_far + 1)
        puzzle[row][col] = orig
    if not top:
        if orig != 'S':
            puzzle[row][col] = 'P'
        solutions += find_path(puzzle, row, col + 1, distance_so_far + 1)
        puzzle[row][col] = orig
    if not left:
        if orig != 'S':
            puzzle[row][col] = 'P'
        solutions += find_path(puzzle, row, col - 1, distance_so_far + 1)
        puzzle[row][col] = orig
    if not top:
        if orig != 'S':
            puzzle[row][col] = 'P'
        solutions += find_path(puzzle, row - 1, col, distance_so_far + 1)
        puzzle[row][col] = orig
    if not bottom:
        if orig != 'S':
           puzzle[row][col] = 'P'
        solutions += find_path(puzzle, row + 1, col, distance_so_far + 1)
        puzzle[row][col] = orig
    return solutions


def solve(puzzle):
   # find start point S, find shortest path to ending
   # point, mark with P for path
   for row in range(ROWS):
       for col in range(COLS):
           if puzzle[row][col] == 'S':
               solutions = find_path(puzzle, row, col, 0)
               # find solution(s) with shortest path
               if not solutions:
                   print('No path possible')
                   return
               shortest = min([distance for _, distance in solutions])
               print ('Shortest solution length is {}'.format(shortest))
               for solution in [solution for solution, distance in  solutions if distance == shortest]:
                   print('Solution:')
                   print_puzzle(solution)


if __name__ == '__main__':
    # split each line into ch array
    puzzle = [[ch for ch in line] for line in PUZZLE]
    print ('Starting puzzle:')
    print_puzzle(puzzle)
    solve(puzzle)