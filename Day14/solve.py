f = open("data", "r")


def applyMask(number, mask):
    num = list(bin(number)[2:].zfill(len(mask)))
    for i in range(len(mask)):
        if(mask[i] == '0'):
            num[i] = '0'
        elif(mask[i] == '1'):
            num[i] = '1'
    tmp = ''
    return int(tmp.join(num), 2)

def getCombinations(num):
    for i in range(len(num)):
        if i == len(num)-1:
            if(num[i] == 'X'):
                tmp = num.copy()
                tmp[i] = '1'
                num[i] = '0'
                return [int(''.join(tmp), 2),int(''.join(num),2)]
            else:
                return[int(''.join(num),2)]
        elif num[i] == 'X':
            tmp = num.copy()
            num[i] = '0'
            tmp[i] = '1'
            return getCombinations(num) + getCombinations(tmp)

def applyMaskTwo(number, mask):
    num = list(bin(number)[2:].zfill(len(mask)))
    for i in range(len(mask)):
        if(mask[i] == '1'):
            num[i] = '1'
        elif(mask[i] == 'X'):
            num[i] = 'X'
    return getCombinations(num)

mask = ''
memory = {}
memory2 = {}
for line in f.readlines():
    instr = line.split() 
    if instr[0] == "mask":
        mask = instr[-1]
    else:
        mem_val = instr[0].split('[')
        mem_val = mem_val[-1][:-1]
        memory[mem_val] = applyMask(int(instr[-1]), mask)
        #part2
        for n in applyMaskTwo(int(mem_val), mask):
            memory2[n] = int(instr[-1])

print("Part 1:", sum(memory.values()))
print("Part2: ", sum(memory2.values()))
