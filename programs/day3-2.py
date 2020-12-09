def numTrees(xmult, ymult, grid):
    trees = 0
    xpos = 0
    row_ind = 0
    while row_ind < len(grid):
        row = grid[row_ind]
        if (xpos >= len(row)):
            xpos = xpos % len(row)
        if (row[xpos] == '#'):
            trees += 1
        xpos += xmult
        row_ind += ymult

    return trees

if __name__ == '__main__':
    grid = []
    product = 1
    with open("../input/day3.txt", 'r') as f:
        line = f.readline()
        while line:
            grid.append(line.strip())
            line = f.readline()
    #print(len(grid[0]), lineCount)
    inputs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for tup in inputs:
        product *= numTrees(tup[0], tup[1], grid)
    print(product)
