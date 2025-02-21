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
        # grid2 = copy.deepcopy(grid)
        for pos in move_blank(i, j, n):
            i1, j1 = pos
            grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
            yield [i1, j1, grid]
            grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]

            """update for manhattan distance"""

    def hFunction(state):
        grid = state[2]
        goalGrid = goal_state[2]
        # for i, (row1, row2) in enumerate(zip(grid, goalGrid)):
        #     for j, (val1, val2) in enumerate(zip(row1, row2)):
        #         if val1 != val2:
        #             total = 0
        #             total += abs(row1-row2)
        #             total += abs()
        #             val1
        #
        # for i in goal_state
        distance = 0
        for num in grid:
            pos1 = []
            pos2 = []
            for i, x in enumerate(grid):
                for j, y in enumerate(x):
                    if num == y:
                        pos1.append([i, x.index(num)])
            for i, x in enumerate(goalGrid):
                for j, y in enumerate(x):
                    if num == y:
                        pos2.append([i, x.index(num)])
            distance += abs(pos1[0] - pos2[0])
            distance += abs(pos1[1] - pos2[1])

        return distance

    def idAstar(path, moves, maxDepth):
        """ """
        nonlocal numberOfNodes
        state = copy.deepcopy(path[-1])

        h = hFunction(state)
        print(state)

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
        caseNumber = 1
    elif start_state in data.case2:
        caseNumber = 2
    numberOfMoves = len(solution) - 1

    print(f"CASE NUMBER: {caseNumber}")
    print(f"NUMBER OF MOVES {numberOfMoves}")
    print(f"NUMBER OF NODES OPENED {numberOfNodes}")
    print(f"TIME TAKEN {computingTime}")
    return numberOfMoves, numberOfNodes, computingTime, solution


solve_puzzle(data.case1[0], data.goal1)
