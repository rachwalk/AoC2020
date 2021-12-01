import re
def op(o,a,b): return a+b if o=="+" else a*b
def f1(m): return str(op(m.group(2),int(m.group(1)),int(m.group(3))))
def fa(m): return "("+str(op("*",int(m.group(1)),int(m.group(2))))+" *"
def fb(m): return "* "+str(op("*",int(m.group(1)),int(m.group(2))))+")"
def s1(s):
  while(t:=re.sub(r"(\d+) ([+*]) (\d+)",f1,s,1))!=s:s=re.sub(r"\((\d+)\)",r"\1",t)
  return int(s)
def s2(s):
  while "no good 'loop' statement in python":
    if (v:=re.sub(r"(\d+) (\+) (\d+)",f1,s))!=s: s=v; continue
    if (v:=re.sub(r"\((\d+)\)",r"\1",s))!=s: s=v; continue
    if (v:=re.sub(r"\((\d+) (\*) (\d+)\)",f1,s))!=s: s=v; continue
    if (v:=re.sub(r"\((\d+) \* (\d+) \*",fa,s,1))!=s: s=v; continue
    if (v:=re.sub(r"\* (\d+) \* (\d+)\)",fb,s,1))!=s: s=v; continue
    if (v:=re.sub(r"(\d+) (\*) (\d+)",f1,s,1))!=s: s=v; continue
    break
  return int(s)
t=open("data","rt").read().splitlines()
print(sum(map(s1,t))) # 15285807527593
print(sum(map(s2,t))) # 461295257566346
