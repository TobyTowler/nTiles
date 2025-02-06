import case


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


state = case.case1[0]
goal = case.goal1[0]


def dfs_rec(path):
    if path[-1] == goal:
        return path
    else:
        # may need a copy or deep copy of path[-1]
        for next_state in move(path[-1]):
            next_path = path + [next_state]
            solution = dfs_rec(next_path)
            if solution != None:
                return solution
    return None


# state_generator = move(state) # state_generator is a generator
# print(next(state_generator)) # the next built in function gets the next valu
# print(next(state_generator))
# alternatively, we can use a for loop
print(state)
# for next_state in move(state):
#     print(next_state)


def solve_puzzle(start_state, goal_state):
    moves = 0
    yields = 0
    time = 0
    path = []

    return moves, yields, time, path


def testGame():
    for i in case.case1:
        moves, yields, time, path = solve_puzzle(i, case.goal1)
        print(f"Goal1 case {i + 1}")
        print(f"Moves : {moves}")
        print(f"Yields : {yields}")
        print(f"Time : {time}")
        print(f"Path : {path}")

    for i in case.case2:
        moves, yields, time, path = solve_puzzle(i, case.goal2)
        print(f"Goal2 case {i + 1}")
        print(f"Moves : {moves}")
        print(f"Yields : {yields}")
        print(f"Time : {time}")
        print(f"Path : {path}")


solve_puzzle(0, 0)
