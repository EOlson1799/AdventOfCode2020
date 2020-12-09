totalCount = 0

def isValid(min, max, req, password):
    letterCount = 0
    global totalCount
    if ((password[min-1] == req) != (password[max-1] == req)):
        totalCount += 1

if __name__ == '__main__':
    with open("../input/day2-1.txt", 'r') as f:
        line = f.readline()
        while line:
            linesplit = line.split(" ")
            minmax = linesplit[0].split('-')
            isValid(int(minmax[0]), int(minmax[1]), linesplit[1][0], linesplit[2])
            line = f.readline()
    f.close

    print(totalCount)