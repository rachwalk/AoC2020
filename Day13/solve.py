from math import prod
f = open("data", "r")

timestamp = int(f.readline())

table = f.readline().split(',')
table1 = list(filter(lambda x: x != 'x', table))
#part 1
min_diff = 999999
min_el = 0
for e in table1:
    time = int(e) - timestamp % int(e)
    if(time < min_diff):
        min_diff = time
        min_el = int(e)
print(min_diff * min_el)
print()

#part2
inputs = [(int(x), int(x) - p) for p, x in enumerate(table) if x != "x"]

def chinese_remainder(n, a):
    p = prod(n)
    total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
    return total % p

print(chinese_remainder([x[0] for x in inputs], [x[1] for x in inputs]))
