f = open("data", "r")


class Instruction:
    def __init__(self, inst, val):
        self.inst = inst
        self.val = val
        self.visited = False

instructions = []


def reset(inst):
    for e in inst:
        e.visited = False


for line in f.readlines():
    x = line.rstrip().split()
    instructions.append(Instruction(x[0], int(x[1])))

def runProgram(instructions):
    accumulator = 0
    ptr = 0
    while(True):
        #check if loop
        if(ptr == len(instructions)):
            reset(instructions)
            return((accumulator, True))
        if(instructions[ptr].visited):
            reset(instructions)
            return((accumulator, False))
        else:
            instructions[ptr].visited = True
    
        if(instructions[ptr].inst == "nop"):
            ptr = ptr + 1
        elif(instructions[ptr].inst == "acc"):
            accumulator = accumulator + instructions[ptr].val
            ptr = ptr + 1
        else:
            ptr = ptr + instructions[ptr].val


for e in instructions:
    if(e.inst == "nop"):
        e.inst = "jmp"
        x = runProgram(instructions)
        if(x[1]):
            print(x[0])
        e.inst = "nop"


for e in instructions:
    if(e.inst == "jmp"):
        e.inst = "nop"
        x = runProgram(instructions)
        if(x[1]):
            print(x[0])
        e.inst = "jmp"

