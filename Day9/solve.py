f = open("data", "r")

preamble_len = 25

preamble = []

def findSum(arr, x):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i!=j):
                if arr[i]+arr[j] == x:
                    return True
    return False


#part1
counter = 0
answer = -1
for line in f.readlines():
    if(counter < preamble_len):
        preamble.append(int(line))
        counter = counter + 1
    else:
        x = int(line)        
        if(not findSum(preamble, x)):
            print(x)
            answer = x
            break
        else:
            preamble.pop(0)
            preamble.append(x)
#part2
f.seek(0)
array = []
for line in f.readlines():
    array.append(int(line))

cater = []
for e in array:
    print(cater)
    if len(cater) < 2:
        cater.append(e)
    elif sum(cater) < answer:
        cater.append(e)
    while(sum(cater) > answer):
        cater.pop(0)
    if sum(cater) == answer:
        print(min(cater), max(cater), min(cater)+max(cater))
        break


