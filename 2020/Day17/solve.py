def getNeighbourCount(x,y,z,space):
    count = 0
    for a in range(z-1,z+2):
        for b in range(y-1, y+2):
            for c in range(x-1,x+2):
                if not (a == z and b==y and c == x):
                    if (c,b,a) in space.keys():
                        count = count + 1
    return count

def printSpace(space):
    minz = min([x[2] for x in list(space.keys())])
    miny = min([x[1] for x in list(space.keys())])
    minx = min([x[0] for x in list(space.keys())])
    maxz = max([x[2] for x in list(space.keys())])
    maxy = max([x[1] for x in list(space.keys())])
    maxx = max([x[0] for x in list(space.keys())])
    for i in range(minz, maxz+1):
        print("Z =", i)
        for j in range(miny, maxy+1):
            for k in range(minx, maxx+1):
                if (k,j,i) in space.keys():
                    print('#', end='')
                else:
                    print('.', end='')
            print()
    

def evolveGoL(space):
    minz = min([x[2] for x in list(space.keys())])
    miny = min([x[1] for x in list(space.keys())])
    minx = min([x[0] for x in list(space.keys())])
    maxz = max([x[2] for x in list(space.keys())])
    maxy = max([x[1] for x in list(space.keys())])
    maxx = max([x[0] for x in list(space.keys())])
    new_space = {}
    for i in range(minz-1, maxz+2):
        for j in range(miny-1, maxy+2):
            for k in range(minx-1, maxx+2):
                count = getNeighbourCount(k,j,i, space)
                if (k,j,i) in space.keys():
                    if(count == 2 or count == 3):
                        new_space[(k,j,i)] = '#'
                else:
                    if(count == 3):
                        new_space[(k,j,i)] = '#'
    return new_space

space = {}


f = open("data", "r")

z = 0
y = 0
for line in f.readlines():
    x = 0
    for c in line:
        if c == '#':
            space[(x,y,z)] = '#'
        x = x + 1
    y = y + 1

for i in range(6):
#    print("Iter: ", i)
#    printSpace(space)
    space = evolveGoL(space)

print(len(space.keys()))
