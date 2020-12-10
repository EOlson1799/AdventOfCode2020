bag_counts = {}
total_options = set(())

def add_bags(rule):
    global bag_counts
    seen_num = False
    rule_words = rule.split(" ")
    head_bag = rule_words[0] + " " + rule_words[1]
    cur_bag = ""
    i = 3
    while i < len(rule_words):
        try:
            num = int(rule_words[i])
            seen_num = True
            i += 1
            continue
        except:
            if (rule_words[i][0:3] == "bag" and seen_num):
                cur_bag = cur_bag.strip()
                if cur_bag in bag_counts:
                    bag_counts[cur_bag].append(head_bag)
                else: 
                    bag_counts[cur_bag] = [head_bag]
                cur_bag = ""
                i += 1
                seen_num = False
                continue
            elif (rule_words[i] == "contain"):
                i += 1
                continue
            else:
                cur_bag += rule_words[i] + " "
        i += 1
        

def build_total_options(bag):
    global bag_counts
    global total_options
    for bag in bag_counts[bag]:
        total_options.add(bag)
        if bag in bag_counts:
            build_total_options(bag)

def find_total_options():
    global total_options
    length = len(total_options)
    total_options = set(())
    return length


if __name__ == '__main__':
    with open('../input/day7.txt', 'r') as f:
        line = f.readline()
        while line:
            add_bags(line.split("\n")[0])
            line = f.readline()
    
    build_total_options("shiny gold")
    print(find_total_options())