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
        nonlocal numberOfNodes
        [i, j, grid] = state
        n = len(grid)
        # grid2 = copy.deepcopy(grid)
        for pos in move_blank(i, j, n):
            i1, j1 = pos
            grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
            numberOfNodes = numberOfNodes + 1
            yield [i1, j1, grid]
            grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]

    def hFunction(state):
        grid = state[2]
        goalGrid = goal_state[2]
        moves = 0
        for i, (row1, row2) in enumerate(zip(grid, goalGrid)):
            for j, (val1, val2) in enumerate(zip(row1, row2)):
                if val1 != val2:
                    moves += 1
        return moves

    def idAstar(path, depth, maxDepth):
        """ """
        state = copy.deepcopy(path[-1])
        # print(state)

        h = hFunction(state)
        # print(h)
        if h == 0:
            return path

        if depth > maxDepth:
            return None
        else:
            scores = []
            for next_state in move(state):
                if next_state not in path:
                    scores.append([next_state, hFunction(state)])
            best = scores[0]
            for i in scores:
                if scores[i][1] < best:
                    best = scores[i]

        print(best)
        next_path = path + [best]
        solution = idAstar(next_path, depth + 1, maxDepth)
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

    return solution


solve_puzzle(data.case1[0], data.goal1)
