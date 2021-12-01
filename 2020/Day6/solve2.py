f = open("data", "r")


def countWords(words, group_count):
    count = 0
    for e in words.values():
        if(e == group_count):
            count = count + 1
    return count

total_count = 0




words = {};
group_count = 0
for line in f.readlines():
    if line.strip() == "":
        print(group_count)
        total_count = total_count + countWords(words, group_count)
        words = {}
        group_count = 0
    else:
        group_count = group_count + 1
        for c in line:
            if(c != '\n'):
                words[c] = words[c] + 1 if c in words else 1 

print(total_count)
