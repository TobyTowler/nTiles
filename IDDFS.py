"""
OUTPUT

CASE NUMBER: 1.0
NUMBER OF MOVES 18
NUMBER OF NODES OPENED 231338
TIME TAKEN 0.8857522010803223
CASE NUMBER: 1.1
NUMBER OF MOVES 22
NUMBER OF NODES OPENED 2266087
TIME TAKEN 8.8618905544281
CASE NUMBER: 1.2
NUMBER OF MOVES 24
NUMBER OF NODES OPENED 6469699
TIME TAKEN 25.517180919647217
CASE NUMBER: 1.3
NUMBER OF MOVES 26
NUMBER OF NODES OPENED 25176804
TIME TAKEN 101.01597309112549
CASE NUMBER: 1.4
NUMBER OF MOVES 20
NUMBER OF NODES OPENED 561376
TIME TAKEN 2.154597043991089
CASE NUMBER: 2.0
NUMBER OF MOVES 20
NUMBER OF NODES OPENED 691985
TIME TAKEN 2.672685146331787
CASE NUMBER: 2.1
NUMBER OF MOVES 14
NUMBER OF NODES OPENED 18556
TIME TAKEN 0.06989645957946777
CASE NUMBER: 2.2
NUMBER OF MOVES 24
NUMBER OF NODES OPENED 4737774
TIME TAKEN 18.600117683410645
CASE NUMBER: 2.3
NUMBER OF MOVES 22
NUMBER OF NODES OPENED 1558377
TIME TAKEN 6.286353349685669
CASE NUMBER: 2.4
NUMBER OF MOVES 31
NUMBER OF NODES OPENED 221466926
TIME TAKEN 903.6199638843536
"""

import data
import copy
import time

"""
finds the path from the start state to the goal state of n tile puzzle

start_state : array of representing current grid poistion
goal_state : array of representing desired grid poistion

return : 
numberOfMoves : number of moves taken to get to goal state
numberOfNodes : number of nodes opened in total during search
computingTime : real world time taken to solve problem
solution : array of all states from start to goal
"""


def solve_puzzle(start_state, goal_state):
    # Global variable
    numberOfNodes = 0

    """
    move the blank tile 

    i : x coordinate of blank tile in grid
    j : y coordinate of blank tile in grid
    n : size of grid

    yield : new position of blank tile

    implementation of n assumes square grid
    """

    def move_blank(i, j, n):
        if i + 1 < n:
            yield (i + 1, j)
        if i - 1 >= 0:
            yield (i - 1, j)
        if j + 1 < n:
            yield (i, j + 1)
        if j - 1 >= 0:
            yield (i, j - 1)

    """
    produce next state of grid

    state : current state of game

    yield : new state after blank tile move
    """

    def move(state):
        nonlocal numberOfNodes
        [i, j, grid] = state
        n = len(grid)
        for pos in move_blank(i, j, n):
            i1, j1 = pos
            grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
            yield [i1, j1, grid]
            numberOfNodes = numberOfNodes + 1  # increment after each yield
            grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]

    def is_goal(state):
        return state == goal_state

    """
    iterative deepening depth first search recursive

    path : array of states to get to current state
    depth : current depth of iterative deepening
    maxDepth : maximum depth of iterative deepening

    return : array of states from beginning state to solution state
    """

    def iddfs_rec(path, depth, maxDepth):
        state = copy.deepcopy(path[-1])
        # state = path[-1]
        # print(state)

        if is_goal(state):
            return path

        if depth > maxDepth:
            return None
        else:
            for next_state in move(state):
                if next_state not in path:
                    next_path = path + [next_state]
                    solution = iddfs_rec(next_path, depth + 1, maxDepth)
                    if solution is not None:
                        return solution
        return None

    solution = None
    computingTime = 0
    startTime = time.time()
    for i in range(0, 100):
        solution = iddfs_rec([start_state], 0, i)
        if solution is not None:
            computingTime = time.time() - startTime
            break

    caseNumber = 0
    if start_state in data.case1:
        caseNumber = 1 + (data.case1.index(start_state)) * 0.1
    elif start_state in data.case2:
        caseNumber = 2 + (data.case2.index(start_state)) * 0.1
    numberOfMoves = len(solution) - 1

    print(f"CASE NUMBER: {caseNumber}")
    print(f"NUMBER OF MOVES {numberOfMoves}")
    print(f"NUMBER OF NODES OPENED {numberOfNodes}")
    print(f"TIME TAKEN {computingTime}")
    return numberOfMoves, numberOfNodes, computingTime, solution


for i in data.case1:
    solve_puzzle(i, data.goal1)

for i in data.case2:
    solve_puzzle(i, data.goal2)

# for i in data.case3:
# print(solve_puzzle(data.case3[3], data.goal3))
