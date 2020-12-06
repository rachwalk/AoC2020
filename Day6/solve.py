f = open("data", "r")


def countWords(words):
    count = 0
    for e in words.values():
        if(e == True):
            count = count + 1
    return count

total_count = 0




words = {};
for line in f.readlines():
    if line.strip() == "":
        total_count = total_count + countWords(words)
        words = {}
    else:
        for c in line:
            if(c != '\n'):
                words[c] = True 

print(total_count)
