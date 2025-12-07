DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1)
              ,(1, -1), (1, 0), (1, 1), (0, 1)]

def parse_input(file):
    grid = list()
    rows = columns = 0
    for line in file:
        grid.append(list(line.strip()))
        rows += 1
    columns = len(grid[0])
    return grid, rows, columns

def is_in_bounds(x: int, y: int):
    return 0 <= x < ROWS and 0 <= y < COLUMNS

def find_accessible_rolls():
    total = 0
    for x in range(ROWS):
        for y in range(COLUMNS):
            if GRID[x][y] != '@': continue
            adjacent_rolls = 0
            for dx, dy in DIRECTIONS:
               x_, y_ = x + dx, y + dy
               if is_in_bounds(x_, y_) and GRID[x_][y_] == '@':
                   adjacent_rolls += 1
            if adjacent_rolls < 4: total += 1
    return total


with open('./input.txt') as file:
    GRID, ROWS, COLUMNS = parse_input(file)
    # print(GRID)
    print(find_accessible_rolls())