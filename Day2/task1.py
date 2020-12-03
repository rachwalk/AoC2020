f = open("data", "r")

class Policy:
    def __init__(self, min, max, c):
        self.min = min
        self.max = max
        self.c = c

    def checkCompliance(self, word):
        n = word.count(self.c)
        return (n >= self.min and n <= self.max)

    def checkComplianceTwo(self, word):
        return(word[self.min-1] == self.c) ^ (word[self.max-1] == self.c)

#    def checkComplianceTwo(self, word):
#        if(word[self.min - 1] == self.c):
#            if(word[self.max-1] == self.c):
#                return False
#            else:
#                return True
#        elif(word[self.max - 1] == self.c):
#            return True
#        else:
#            return False
count = 0


for line in f:
    tmp = line.split(':')
    policy_str = tmp[0].split()
    limits = policy_str[0].split('-')
    policy = Policy(int(limits[0]), int(limits[1]),policy_str[1].strip())
    if(policy.checkComplianceTwo(tmp[1].strip())):
        count = count + 1


print(count);
