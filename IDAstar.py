"""
OUTPUT

CASE NUMBER: 1.0
NUMBER OF MOVES 18
NUMBER OF NODES OPENED 1331
TIME TAKEN 0.013164997100830078
CASE NUMBER: 1.1
NUMBER OF MOVES 22
NUMBER OF NODES OPENED 7866
TIME TAKEN 0.07905149459838867
CASE NUMBER: 1.2
NUMBER OF MOVES 24
NUMBER OF NODES OPENED 18021
TIME TAKEN 0.171844482421875
CASE NUMBER: 1.3
NUMBER OF MOVES 26
NUMBER OF NODES OPENED 112159
TIME TAKEN 1.0554003715515137
CASE NUMBER: 1.4
NUMBER OF MOVES 20
NUMBER OF NODES OPENED 3254
TIME TAKEN 0.031116008758544922
CASE NUMBER: 2.0
NUMBER OF MOVES 20
NUMBER OF NODES OPENED 319
TIME TAKEN 0.003477811813354492
CASE NUMBER: 2.1
NUMBER OF MOVES 14
NUMBER OF NODES OPENED 79
TIME TAKEN 0.0011582374572753906
CASE NUMBER: 2.2
NUMBER OF MOVES 24
NUMBER OF NODES OPENED 14482
TIME TAKEN 0.13693904876708984
CASE NUMBER: 2.3
NUMBER OF MOVES 22
NUMBER OF NODES OPENED 12461
TIME TAKEN 0.11735820770263672
CASE NUMBER: 2.4
NUMBER OF MOVES 31
NUMBER OF NODES OPENED 168377
TIME TAKEN 1.5987794399261475
"""

import data
import time
import copy


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
            numberOfNodes = numberOfNodes + 1
            grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]

    """
    finds elements position in grid

    matrix : grid to search
    target : element to find

    return : position of element
    """

    def find_position(matrix, target):
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == target:
                    return (i, j)  # Return row and column index
        return None

    """
    calculates cost of current state using manhattan distance - heuristic function

    state : current state of game

    return : total cost of current state
    """

    def hFunction(state):
        grid = state[2]
        goalGrid = goal_state[2]
        distance = 0

        for i in grid:
            for j in i:
                x1, y1 = find_position(grid, j)
                x2, y2 = find_position(goalGrid, j)
                distance += abs(x1 - x2)
                distance += abs(y1 - y2)

        return distance

    """
    iterative deepening, recursive A star search algorithm

    path : array of states to get to current state
    depth : current depth of iterative deepening
    maxDepth : maximum depth of iterative deepening

    return : array of states from beginning state to solution state
    """

    def idAstar(path, moves, maxDepth):
        """ """
        state = copy.deepcopy(path[-1])

        h = hFunction(state)
        # print(state)

        if h == 0:
            return path

        if moves + h > maxDepth:
            return None
        else:
            for next_state in move(state):
                if next_state not in path:
                    # numberOfNodes = numberOfNodes + 1
                    # print(next_state)
                    next_path = path + [next_state]
                    solution = idAstar(next_path, moves + 1, maxDepth)
                    if solution is not None:
                        return solution
        return None

    solution = None
    computingTime = 0
    startTime = time.time()
    for i in range(0, 100):
        solution = idAstar([start_state], 0, i)
        if solution is not None:
            computingTime = time.time() - startTime
            break

    if start_state in data.case1:
        caseNumber = 1 + (data.case1.index(start_state)) * 0.1
    elif start_state in data.case2:
        caseNumber = 2 + (data.case2.index(start_state)) * 0.1
    else:
        caseNumber = "UNKNOWN"
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


solve_puzzle(data.case3[2], data.goal3)
