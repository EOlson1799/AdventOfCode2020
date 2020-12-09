
all_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

def isValid(fields):
    field_dict = {field: None for field in all_fields}
    for field in fields:
        field_dict[field[0]] = field[1]
    for field in field_dict:
        if (field == "cid"):
            continue
        elif (not field_dict[field]):
            return 0
        else:
            val = field_dict[field].split("\n")[0]
            if field == "byr":
                if (int(val) < 1920 or int(val) > 2002):
                    return 0
            if field == "iyr":
                if (int(val) < 2010 or int(val) > 2020):
                    return 0
            if field == "eyr":
                if (int(val) < 2020 or int(val) > 2030):
                    return 0
            if field == "hgt":
                if (val[-1] == 'm'):
                    if (int(val[:-2]) < 150 or int(val[:-2]) > 193):
                        return 0
                elif (val[-1] == 'n'):
                    if (int(val[:-2]) < 59 or int(val[:-2]) > 76):
                        return 0
                else:
                    return 0
            if field == "hcl":
                if (val[0] != '#' or len(val) != 7):
                    return 0
                for letter in val:
                    try:
                        number = int(letter)
                    except:
                        if letter > 'f':
                            return 0
            if field == "ecl":
                options = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if val not in options:
                    return 0
            if field == "pid":
                if len(val) != 9:
                    return 0
                try:
                    number = int(val)
                except:
                    return 0
    return 1


if __name__ == '__main__':
    valid_pp = 0
    with open("../input/day4.txt", 'r') as f:
        fields = []
        line = f.readline()
        while line:
            line_fields = line.split(" ")
            for field in line_fields:
                field = field.split(":")
                field[1] = field[1].split("\n")[0]
                fields.append(field)
            line = f.readline()
            if (not line or line == "\n"):
                valid_pp += isValid(fields)
                fields = []
                line = f.readline()
    
    print(valid_pp)
