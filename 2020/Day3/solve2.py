f = open("data", "r")

class Slope:
    def __init__(self, pos, count):
        self.position = pos
        self.count = count

slope_one = Slope(0,0)
slope_two = Slope(0,0)
slope_three = Slope(0,0)
slope_four = Slope(0,0)
slope_five = Slope(0,0)


line_len = 31

line_count = 0

for line in f.readlines():
    if(not line_count == 0): #if it's the first line do nothing
        if(line[slope_one.position] == '#'):
            slope_one.count = slope_one.count+1
        if(line[slope_two.position] == '#'):
            slope_two.count = slope_two.count+1
        if(line[slope_three.position] == '#'):
            slope_three.count = slope_three.count+1
        if(line[slope_four.position] == '#'):
            slope_four.count = slope_four.count+1
        if(line_count % 2 == 0):
            if(line[slope_five.position] == '#'):
                slope_five.count = slope_five.count + 1

    slope_one.position = (slope_one.position + 1)%line_len
    slope_two.position =( slope_two.position + 3)%line_len
    slope_three.position =( slope_three.position + 5)%line_len
    slope_four.position =( slope_four.position + 7)%line_len
    if(line_count%2 == 1):
        slope_five.position =( slope_five.position + 1)%line_len
    line_count = line_count + 1

print(slope_one.count * slope_two.count * slope_three.count * slope_four.count * slope_five.count)
