f = open("data", "r")


class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def rotate(self, deg):
        if(deg == 90):
            (self.x, self.y)= (-self.y, self.x)
        if(deg == 180):
            (self.x, self.y)= (-self.x, -self.y)
        if(deg == 270):
            (self.x, self.y)= (self.y, -self.x)

ship = Entity(0,0)
waypoint = Entity(1,10)

for line in f.readlines():
    act = line[0]
    if(act == 'N'):
        waypoint.x = waypoint.x + int(line[1:])
    elif(act == 'S'):
        waypoint.x = waypoint.x - int(line[1:])
    elif(act == 'E'):
        waypoint.y = waypoint.y + int(line[1:])
    elif(act == 'W'):
        waypoint.y = waypoint.y - int(line[1:])
    elif(act == 'R'):
        waypoint.rotate(int(line[1:]))
    elif(act == 'L'):
        waypoint.rotate((360 - int(line[1:])%360))
    elif(act == 'F'):
        mult = int(line[1:])
        ship.x = ship.x + mult * waypoint.x
        ship.y = ship.y + mult * waypoint.y
    print(line)
    print("Ship:", ship.x, ship.y)
    print("Waypoint", waypoint.x, waypoint.y)
    print('\n')

print(abs(ship.x) + abs(ship.y))
