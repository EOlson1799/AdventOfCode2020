acc = 0

def run_instructions(instructions):
    acc = 0
    seen = [False for x in instructions]
    
    i = 0
    while i < len(instructions):
        inst, val = instructions[i].split(" ")
        if seen[i]:
            return acc
        seen[i] = True
        if inst == 'acc':
            acc += int(val)
        elif inst == 'jmp':
            i += int(val)
            continue
        
        i += 1


if __name__ == '__main__':
    inst = []
    with open("../input/day8.txt", 'r') as f:
        line = f.readline()
        while line:
            inst.append(line.split('\n')[0])
            line = f.readline()
    
    print(run_instructions(inst))
