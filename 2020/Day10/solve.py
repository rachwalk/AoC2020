f = open("data", "r")

jols = []
jols.append(0)
for line in f.readlines():
    jols.append(int(line.rstrip()))

prev = 0
one_diffs = 0
three_diffs = 1
jols.sort()
for e in jols:
    if(e - prev == 1):
        one_diffs =  one_diffs + 1
    elif(e - prev == 3):
        three_diffs = three_diffs + 1
    prev = e

print(one_diffs)
print(three_diffs)
print(one_diffs * three_diffs)
print('\n')
jols.append(max(jols) + 3)
routes = [0] * len(jols)

for i in range(len(jols)):
    if(i == 0):
        routes[i] = 1
    elif(i == 1):
        if(jols[i] <= jols[i-1] + 3):
            routes[i] = routes[i-1]
    else:
        if(jols[i] <= jols[i-1] + 3):
            routes[i] = routes[i-1]
            if(jols[i] <= jols[i-2] + 3):
                routes[i] = routes[i] + routes[i-2]
                if(jols[i] <= jols[i-3] + 3):
                    routes[i] = routes[i] + routes[i-3]

print(max(routes))

