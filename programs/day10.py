import math
from functools import lru_cache
total = 0
global ratings

def find_dif():
    global ratings
    counts = [0, 0, 0]
    length = len(ratings)
     
    for i, r in enumerate(ratings):
        if (i < length - 1):
            diff = ratings[i+1] - r
            counts[diff - 1] += 1

    return counts[0] * counts[2]

@lru_cache(maxsize=None)
def count_orders(index):
    global ratings
    length = len(ratings)
    count = 0
    next_ind = index + 1

    if index == len(ratings) - 1:
        return 1

    else:
        while ((next_ind < length) and ratings[next_ind] - ratings[index] <= 3):
            count += count_orders(next_ind)
            next_ind += 1
    
    return count

if __name__ == '__main__':
    with open('../input/day10.txt', 'r') as f:
        global ratings
        ratings = [0]
        line = f.readline()
        while line:
            split = line.split('\n')
            ratings.append(int(split[0]))
            line = f.readline()
    
    ratings.sort()
    ratings.append(ratings[-1] + 3)
    print(f'Difference product: {find_dif()}, Orders: {count_orders(0)}')