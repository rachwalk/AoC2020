f = open("data", "r")


class Instruction:
    def __init__(self, inst, val):
        self.inst = inst
        self.val = val
        self.visited = False

instructions = []


for line in f.readlines():
    x = line.rstrip().split()
    instructions.append(Instruction(x[0], int(x[1])))

accumulator = 0
ptr = 0
while(True):
    #check if loop
    if(instructions[ptr].visited):
        break
    else:
        instructions[ptr].visited = True

    if(instructions[ptr].inst == "nop"):
        ptr = ptr + 1
    elif(instructions[ptr].inst == "acc"):
        accumulator = accumulator + instructions[ptr].val
        ptr = ptr + 1
    else:
        ptr = ptr + instructions[ptr].val

print(accumulator)
