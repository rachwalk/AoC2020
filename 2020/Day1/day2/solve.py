f = open("data", "r")

data = f.readlines()

for i in data:
    for j in data:
        for k in data:
            a = int(i)
            b = int(j)
            c = int(k)
            if(a + b + c == 2020):
                print(a*b*c)

