
if __name__ == '__main__':
    valid_pp = 0
    with open("../input/day4.txt", 'r') as f:
        fields = []
        line = f.readline()
        cid = False
        while line:
            line_fields = line.split(" ")
            for field in line_fields:
                field = field.split(":")[0]
                if (field == "cid"):
                    cid = True
                fields.append(field)
            line = f.readline()
            if (not line or line == "\n"):
                if (len(fields) == 8 or (len(fields) == 7 and not cid)):
                    valid_pp += 1
                fields = []
                cid = False
                line = f.readline()
            
            
    print(valid_pp)
