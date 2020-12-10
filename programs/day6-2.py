
def countAns(group):
    counts = {}
    total = 0
    for item in group:
        for letter in item:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

    for c in counts:
        if counts[c] == len(group):
            total += 1
    return total

if __name__ == '__main__':
    total = 0
    answers = []
    with open("../input/day6.txt", 'r') as f:
        group = []
        line = f.readline()
        while line:
            group.append(line.split('\n')[0])
            line = f.readline()
            if (not line or line == '\n'):
                total += countAns(group)
                group = []
                line = f.readline()

    print(total)