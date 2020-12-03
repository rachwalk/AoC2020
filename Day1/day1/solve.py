f = open("data", "r")

data = f.readlines()

for i in data:
    for j in data:
        if(i != j):
            a = int(i)
            b = int(j)
            if(a + b == 2020):
                print(a*b)

