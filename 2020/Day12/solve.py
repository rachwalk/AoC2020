f = open("data","r")

x = 0
y = 0
dir = 90


for line in f.readlines():
    act = line[0]
    if(act == 'N'):
        x = x + int(line[1:])
    elif(act == 'S'):
        x = x - int(line[1:])
    elif(act == 'E'):
        y = y + int(line[1:])
    elif(act == 'W'):
        y = y - int(line[1:])
    elif(act == 'L'):
        dir = (dir - int(line[1:]))%360
    elif(act == 'R'):
        dir = (dir + int(line[1:]))%360
    elif(act == 'F'):
        if(dir == 0):
            x = x + int(line[1:])
        if(dir == 90):
            y = y + int(line[1:])
        if(dir == 180):
            x = x - int(line[1:])
        if(dir == 270):
            y = y - int(line[1:])

print(abs(x) + abs(y))

