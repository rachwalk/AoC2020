with open("input", "r") as f:
    prev_lines = []
    increase_count = 0
    for line in f:
        print(prev_lines)
        if len(prev_lines) == 3:
            prev_sum = sum(prev_lines)
            prev_lines.pop(0)
            prev_lines.append(int(line))
            cur_sum = sum(prev_lines)
            print(f"prev: {prev_sum}, cur: {cur_sum}")
            if prev_sum < cur_sum:
                increase_count += 1
        else:
            prev_lines.append(int(line))

    print(increase_count)
