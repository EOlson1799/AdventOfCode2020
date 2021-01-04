occupied = 0

def run_life(grid):
    global occupied
    change = False
    cur_buffer = [None] * len(grid[0])
    other_buffer = [None] * len(grid[0])
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            cur_buffer[j] = char

            def check_empty(grid, row, col):
                for row_off in range(-1, 2):
                    row2 = row + row_off
                    for col_off in range(-1, 2):
                        col2 = col + col_off
                        if row2 >= 0 and row2 < len(grid) and col2 >= 0 and col2 < len(grid[0]):
                            if grid[row2][col2] == '#':
                                return False
                return True

            def check_occ(grid, row, col):
                count = 0
                for row_off in range(-1, 2):
                    if count >= 4:
                        break
                    row2 = row + row_off
                    for col_off in range(-1, 2):
                        col2 = col + col_off
                        if (row == row2) and (col == col2):
                            continue
                        elif row2 >= 0 and row2 < len(grid) and col2 >= 0 and col2 < len(grid[0]):
                            if grid[row2][col2] == '#':
                                count += 1
                return count >= 4

            if char == 'L':
                if check_empty(grid, i, j):
                    cur_buffer[j] = '#'
                    occupied += 1
                    change = True
            elif char == '#':
                if check_occ(grid, i, j):
                    cur_buffer[j] = 'L'
                    occupied -= 1
                    change = True
            else:
                continue
        
        if i != 0:
            grid[i-1] = other_buffer[:]
            if i == len(grid) - 1:
                grid[i] = cur_buffer[:]
                
        other_buffer = cur_buffer[:]   

    if change:
        run_life(grid)
    else:
        return

if __name__ == '__main__':
    grid = []
    with open('../input/day11.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.split('\n')[0]
            row = []
            for char in line:
                if char == '#':
                    occupied += 1
                row.append(char)
            grid.append(row)
            line = f.readline()

    run_life(grid) 
    print(occupied)