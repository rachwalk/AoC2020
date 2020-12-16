
class Field:
    def __init__(self, name, ranges):
        self.name = name
        self.rules = []
        self.index = -1
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
#cleanup for the indexfinding
for t in to_rem:
    nearby.remove(t)

ticket_len = 20

for f in fields:
    candidate_indexes = list(range(0, ticket_len))
    for ticket in nearby:
        for i in range(len(ticket)):
            if(not f.validate(int(ticket[i]))):
                candidate_indexes.remove(i)
        if(len(candidate_indexes) == 1):
            f.index = candidate_indexes[0]
            break

print("Found indexes:")
for f in fields:
    print( f.index)

#in case the last one is inferred
#candidate_indexes = list(range(0, ticket_len))
#for f in fields:
#    if f.index != -1:
#        candidate_indexes.remove(f.index)
#
#for f in fields:
#    if f.index == -1:
#        f.index = candidate_indexes[0]

