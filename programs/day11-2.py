occupied = 0

def run_life(grid):
    global occupied
    change = False
    new_grid = []
    for i, row in enumerate(grid):
        new_grid.append([None] * len(grid[0]))
        for j, char in enumerate(row):
            new_grid[i][j] = char
            
            def check_empty(grid, row, col):
                for row_off in range(-1, 2):
                    for col_off in range(-1, 2):
                        row2 = row + row_off
                        col2 = col + col_off
                        if (row == row2) and (col == col2):
                            continue
                        while (row2 >= 0) and (row2 < len(grid)) and (col2 >= 0) and (col2 < len(grid[0])):
                            if grid[row2][col2] == '.':
                                row2 += row_off
                                col2 += col_off
                                continue
                            elif grid[row2][col2] == '#':
                                return False
                            else:
                                break
                return True

            def check_occ(grid, row, col):
                count = 0
                for row_off in range(-1, 2):
                    if count >= 5:
                        break
                    
                    for col_off in range(-1, 2):
                        row2 = row + row_off
                        col2 = col + col_off
                        if (row == row2) and (col == col2):
                            continue
                        while (row2 >= 0) and (row2 < len(grid)) and (col2 >= 0) and (col2 < len(grid[0])):
                            if grid[row2][col2] == '.':
                                row2 += row_off
                                col2 += col_off
                                continue
                            elif grid[row2][col2] == '#':
                                count += 1
                                break
                            else:
                                break
                return count >= 5

            if char == 'L':
                if check_empty(grid, i, j):
                    new_grid[i][j] = '#'
                    occupied += 1
                    change = True
            elif char == '#':
                if check_occ(grid, i, j):
                    new_grid[i][j] = 'L'
                    occupied -= 1
                    change = True
            else:
                continue

        
            
    if change:
        run_life(new_grid)
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