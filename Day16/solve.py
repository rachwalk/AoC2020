
class Field:
    def __init__(self, name, ranges):
        self.name = name
        self.rules = []
        for l in ranges.split("or"):
            self.rules.append(l.lstrip().rstrip().split('-'))
    def validate(self, value):
        for rule in self.rules:
            if value >= int(rule[0]) and value <= int(rule[1]):
                return True
        return False



def isFieldValidForAny(value, fields):
    for f in fields:
        if f.validate(value):
            return True
    return False


f = open("data", "r")            

fields = []
yourticket = []
nearby = []
to_rem = []

readingFields = True
readingYou = False
readingNearby = False
for l in f.readlines():
    if readingFields:
        if l.rstrip() == "":
            readingFields = False
        else:
            tmp = l.split(':')
            fields.append(Field(tmp[0], tmp[1]))
    elif readingYou:
        if l.rstrip() == "":
            readingYou = False
        else:
            yourticket = l.rstrip().split(',')
    elif readingNearby:
        nearby.append(l.rstrip().split(','))
    if l.rstrip() == "your ticket:":
        readingYou = True
    if l.rstrip() == "nearby tickets:":
        readingNearby = True
error_rate = 0
for ticket in nearby:
    for field in ticket:
        if not isFieldValidForAny(int(field), fields):
            error_rate = error_rate + int(field)
            to_rem.append(ticket) # part2 cleanup
        
print(error_rate)
#part 2


