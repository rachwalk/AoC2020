f = open("data", "r")

passport = {
        "byr": "",
        "iyr": "",
        "eyr": "",
        "hgt": "",
        "hcl": "",
        "ecl": "",
        "pid": "",
        "cid": ""
        }

def verify(candidate):
    for item in candidate.keys():
        if(item != "cid"):
            if(candidate[item] == ""):
                return False
    return True

def reset(candidate):
    for item in candidate.keys():
        candidate[item] = ""
        
count = 0

for line in f.readlines():
    if line.strip() == "":
        if(verify(passport)):
            count = count+1
        reset(passport)
    else:
        infos = line.split()
        for item in infos:
            passport[item[0:3]] = item[4:]

print(count) 
