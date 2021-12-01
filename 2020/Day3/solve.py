f = open("data", "r")

position = 0

tree_count = 0

line_len = 31

first_line_flag = True;

for line in f.readlines():
    if(not first_line_flag): #if it's the first line do nothing
        if(line[position] == '#'):
            tree_count = tree_count + 1
    first_line_flag = False
    position = (position + 3) % line_len


print(tree_count)
