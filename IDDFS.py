import data
import copy
import time


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

    def is_goal(state):
        return state == goal_state

    def iddfs_rec(path, depth, maxDepth):
        nonlocal numberOfNodes
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
                    numberOfNodes = numberOfNodes + 1
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

    print()

    caseNumber = 0
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


for i in data.case1:
    print(solve_puzzle(i, data.goal1))

for i in data.case2:
    print(solve_puzzle(i, data.goal2))

# for i in data.case3:
#     print(solve_puzzle(i, data.goal3))
