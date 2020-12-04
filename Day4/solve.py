import re
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

valid_eye = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def verify(candidate):
    for item in candidate.keys():
        if(item != "cid"):
            if(candidate[item] == ""):
                return False
            elif(item == "byr"):
                if(int(candidate[item]) < 1920 or int(candidate[item]) > 2002):
                    return False
            elif(item == "iyr"):
                if(int(candidate[item]) < 2010 or int(candidate[item]) > 2020):
                    return False
            elif(item == "eyr"):
                if(int(candidate[item]) < 2020 or int(candidate[item]) > 2030):
                    return False
            elif(item == "hgt"):
                unit = candidate[item][-2:]
                if(unit == "cm"):
                    if( int(candidate[item][:-2]) < 150 or int(candidate[item][:-2]) > 193):
                        return False
                elif(unit == "in"):
                    if( int(candidate[item][:-2]) < 59 or int(candidate[item][:-2]) > 76):
                        return False
                else:
                    return False
            elif(item == "hcl"):
                res = re.search(r'^#[0-9a-f]{6}$', candidate[item])
                if(res == None):
                    return False
            elif(item == "ecl"):
                if(not candidate[item] in valid_eye ):
                    return False
            elif(item == "pid"):
                res = re.search(r'^[0-9]{9}$', candidate[item])
                if(res == None):
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
