
def countAns(group):
    unique = set(())
    for item in group:
        for letter in item:
            unique.add(letter)
    return len(unique)

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

    #total = countAns(["abc"])
    #total += countAns(["a", "b", "c"])
    #total += countAns(["ab", "ac"])
    #total += countAns(["a", "a", "a", "a"])
    #total += countAns(["b"])

    print(total)