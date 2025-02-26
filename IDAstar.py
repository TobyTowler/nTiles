import data
import time
import copy


def solve_puzzle(start_state, goal_state):
    numberOfNodes = 0

    def move_blank(i, j, n):
        if i + 1 < n:
            yield (i + 1, j)
        if i - 1 >= 0:
            yield (i - 1, j)
        if j + 1 < n:
            yield (i, j + 1)
        if j - 1 >= 0:
            yield (i, j - 1)

    def move(state):
        [i, j, grid] = state
        n = len(grid)
        for pos in move_blank(i, j, n):
            i1, j1 = pos
            grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
            yield [i1, j1, grid]
            grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]

    def find_position(matrix, target):
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == target:
                    return (i, j)  # Return row and column index
        return None

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

    def idAstar(path, moves, maxDepth):
        """ """
        nonlocal numberOfNodes
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
                    numberOfNodes = numberOfNodes + 1
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
        caseNumber = -1
    numberOfMoves = len(solution) - 1

    print(f"CASE NUMBER: {caseNumber}")
    print(f"NUMBER OF MOVES {numberOfMoves}")
    print(f"NUMBER OF NODES OPENED {numberOfNodes}")
    print(f"TIME TAKEN {computingTime}")
    return numberOfMoves, numberOfNodes, computingTime, solution


for i in data.case1:
    print(solve_puzzle(i, data.goal1))
#
# for i in data.case2:
#     print(solve_puzzle(i, data.goal2))

# print(solve_puzzle(data.case3[1], data.goal3))
