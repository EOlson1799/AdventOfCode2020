
def run_instructions(instructions, swap_list, swap):

    for ind in swap_list:
        seen = [False for x in instructions]
        acc = 0
        i = 0
        while i < len(instructions):
            inst, val = instructions[i]
            if seen[i]:
                break
            seen[i] = True
            if i == ind:
                inst = swap
            if inst == 'acc':
                acc += int(val)
            elif inst == 'jmp':
                i += int(val)
                continue
            
            i += 1
        if i >= len(instructions):
            return acc

    return None

if __name__ == '__main__':
    inst = []
    nop = []
    jmp = []
    with open("../input/day8.txt", 'r') as f:
        line = f.readline()
        i = 0
        while line:
            line = line.split('\n')[0]
            split = line.split(' ')
            if split[0] == "nop":
                nop.append(i)
            elif split[0] == "jmp":
                jmp.append(i)
            inst.append(split)
            i += 1
            line = f.readline()
    
    acc = run_instructions(inst, nop, 'jmp')
    if not acc:
        acc = run_instructions(inst, jmp, 'nop')
    
    print(acc)
