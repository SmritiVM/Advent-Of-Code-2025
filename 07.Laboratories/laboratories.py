from collections import deque

LEFT, RIGHT, DOWN = (0, -1), (0, 1), (1, 0)

def parse_input(file):
    grid = list()
    rows = columns = 0
    for line in file:
        grid.append(list(line.strip()))
        rows += 1
    columns = len(grid[0])
    return grid, rows, columns

def find_start():
    for x in range(ROWS):
        for y in range(COLUMNS):
            if MANIFOLD[x][y] == 'S': return (x, y)

def is_in_bounds(x: int, y: int):
    return 0 <= x < ROWS and 0 <= y < COLUMNS

def add_in_bounds(x: int, y: int, offset: tuple, queue: list):
    x_, y_ = x + offset[0], y + offset[1]
    if is_in_bounds(x_, y_): queue.append((x_, y_))


def find_beam_split():
    queue = deque([START])
    visited_splinters = set()
    visited_by_beam = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited_by_beam: continue
        visited_by_beam.add((x, y))
        x_, y_ = x + DOWN[0], y + DOWN[1]
        if is_in_bounds(x_, y_):
            if MANIFOLD[x_][y_] == '^' and (x_, y_) not in visited_splinters: # Splinter so add left and right
                add_in_bounds(x_, y_, LEFT, queue)
                add_in_bounds(x_, y_, RIGHT, queue)
                visited_splinters.add((x_, y_))
            else:
                queue.append((x_, y_))
    return len(visited_splinters)

with open('./input.txt') as file:
    MANIFOLD, ROWS, COLUMNS = parse_input(file)
    START = find_start()
    print(find_beam_split())

