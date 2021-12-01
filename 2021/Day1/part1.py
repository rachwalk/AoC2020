with open("input", "r") as f:
    prev_line = "9999999"
    increase_count = 0
    for line in f:
        if(int(line) > int(prev_line)):
            increase_count += 1
        prev_line = line

    print(increase_count)
