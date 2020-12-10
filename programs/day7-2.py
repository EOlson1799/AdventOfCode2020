bag_counts = {}

def add_bags(rule):
    global bag_counts
    seen_num = False
    rule_words = rule.split(" ")
    head_bag = rule_words[0] + " " + rule_words[1]
    cur_bag = [-1, ""]
    i = 3
    while i < len(rule_words):
        try:
            num = int(rule_words[i])
            cur_bag[0] = num
            i += 1
            continue
        except:
            if (rule_words[i][0:3] == "bag" and cur_bag[0] != -1):
                cur_bag[1] = cur_bag[1].strip()
                if head_bag in bag_counts:
                    bag_counts[head_bag].append(tuple(cur_bag))
                else: 
                    bag_counts[head_bag] = [tuple(cur_bag)]
                cur_bag = [-1, ""]
                i += 1
                continue
            elif (rule_words[i] == "contain"):
                i += 1
                continue
            else:
                cur_bag[1] += rule_words[i] + " "
        i += 1
        
def find_total_bags(bag):
    global bag_counts
    total = 0
    if bag in bag_counts:
        for bag in bag_counts[bag]:
            total += bag[0] + (bag[0] * find_total_bags(bag[1]))

    return total

if __name__ == '__main__':
    with open('../input/day7.txt', 'r') as f:
        line = f.readline()
        while line:
            add_bags(line.split("\n")[0])
            line = f.readline()

    print(find_total_bags("shiny gold"))