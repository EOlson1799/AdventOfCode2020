def numTrees(grid):
    trees = 0
    xpos = 0
    for row in grid:
        if (xpos >= len(row)):
            xpos = xpos % len(row)
        if (row[xpos] == '#'):
            trees += 1
        xpos += 3

    print(trees)

if __name__ == '__main__':
    grid = []
    lineCount = 0
    with open("../input/day3.txt", 'r') as f:
        line = f.readline()
        while line:
            lineCount += 1
            grid.append(line.strip())
            line = f.readline()
    #print(len(grid[0]), lineCount)
    numTrees(grid)
