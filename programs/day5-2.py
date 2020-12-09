import math
all_seats = {}

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


def build_seats(seats):
    global all_seats
    for seat in seats:
        row = eval_row(seat)
        seat = eval_seat(seat)
        seat_id = row * 8 + seat
        all_seats[seat_id] = 1

def find_missing():
    for seat_id in all_seats:
        if (all_seats[seat_id + 2]):
            try: 
                my_seat = all_seats[seat_id + 1]
            except:
                return seat_id + 1

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
    build_seats(seats)
    print(find_missing())