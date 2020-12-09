import math
max_seat = 0

def eval_row(seat):
    top = 0
    end = 127
    for i in range(7):
        if seat[i] == "F":
            end = top + math.floor((end - top) / 2)
        elif seat[i] == "B":
            top += math.ceil((end - top) / 2)
    return end
    
def eval_seat(seat):
    top = 0
    end = 7
    for j in range(3):
        j += 7
        if seat[j] == "L":
            end = top + math.floor((end - top) / 2)
        elif seat[j] == "R":
            top += math.ceil((end - top) / 2)
    return end


def find_max(seats):
    max_seat = 0
    for seat in seats:
        row = eval_row(seat)
        seat = eval_seat(seat)
        max_seat = max(max_seat, row * 8 + seat)

    return max_seat

if __name__ == '__main__':
    with open("../input/day5.txt", 'r') as f:
        line = f.readline()
        seats = []
        while line:
            seat = line.split("\n")[0]
            seats.append(seat)
            line = f.readline()
    #print(seats)
    f.close
    print(find_max(seats))