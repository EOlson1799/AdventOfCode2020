def findnum(numbers):
    for i, number in enumerate(numbers):
        j = i + 1
        while (j < len(numbers)):
            if (int(number) + int(numbers[j]) < 2020):
                almost = (int(number) + int(numbers[j]))
                k = j + 1
                while (k < len(numbers)):
                    if (almost + int(numbers[k]) == 2020):
                        print((almost - int(number)) * int(number) * int(numbers[k]))
                    k += 1
            j += 1

if __name__ == '__main__':
    txtfile = open("./day1-1.txt", 'r')
    line = txtfile.readline()
    numbers = []
    while line:
        numbers.append(line)
        line = txtfile.readline()
    numbers = [x.strip() for x in numbers]
    findnum(numbers)
    txtfile.close