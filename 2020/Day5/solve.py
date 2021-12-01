f = open("data", "r")

def mapRow(c):
    if c == 'F':
        return '0'
    elif c == 'B':
        return '1'
    else:
        print("ERROR")

def mapCol(c):
    if c == 'L':
        return '0'
    elif c == 'R':
        return '1'
    else:
        print("ERROR", c)

max_id = 0
ids = []


for line in f.readlines():
    row = line[:7]
    col = line[-4:-1]
    s1 = ""
    row_id = int(s1.join(list(map(mapRow, row))), 2)
    col_id = int(s1.join(list(map(mapCol, col))), 2)
    seat_id = row_id * 8 + col_id
    ids.append(seat_id)
    if(seat_id > max_id):
        max_id = seat_id

print(max_id) 

ids.sort()

for i in range(0, len(ids) -2):
    if(ids[i] != ids[i+1] - 1):
        print(ids[i] + 1)
    
