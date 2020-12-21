preamble = 25

def find_invalid(numbers):
    global preamble
    num_ind = preamble
    while num_ind < len(numbers):
        valid = False
        i = num_ind - preamble 
        while not valid and i < num_ind - 1:
            while (i < num_ind - 1):
                j = i + 1
                while (j < num_ind):
                    #print(numbers[i], numbers[j], numbers[num_ind])
                    if (numbers[i] + numbers[j] == numbers[num_ind]):
                        #print('here')
                        valid = True
                    j += 1
                i += 1
        if not valid:
            return numbers[num_ind]
        num_ind += 1

def find_cont(invalid, numbers):
    for i in range(len(numbers)):
        cont_sum = numbers[i]
        min_num = numbers[i]
        max_num = numbers[i]
        j = i + 1
        while (cont_sum < invalid and j < len(numbers)):
            cont_sum += numbers[j]
            min_num = min(min_num, numbers[j])
            max_num = max(max_num, numbers[j])
            if cont_sum == invalid:
                #print(min_num, max_num)
                return min_num + max_num
            j += 1


if __name__ == '__main__':
    numbers = []
    with open('../input/day9.txt', 'r') as f:
        line = f.readline()
        while line:
            number = int(line.split('\n')[0])
            numbers.append(number)
            line = f.readline()
        
    invalid = find_invalid(numbers)

    contiguous = find_cont(invalid, numbers)

    print(invalid, contiguous)