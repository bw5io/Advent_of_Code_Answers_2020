def getRules(file):
    file=open("day7.txt")
    words=[]
    for line in file:
        temp=line.split()
        c=[]
        c.append(temp[0]+" "+temp[1])
        for i in range(len(temp)):
            if temp[i].isdigit()==True:
                c.append(temp[i+1]+" "+temp[i+2])
                c.append(temp[i])
        words+=[c]
        # print(temp)
    return(words)

def tryRule(cri,rule):
    c=[]
    for i in rule:
        if cri in i and i[0]!=cri:
            c.append(i[0])
            print(i[0])
            c=c+tryRule(i[0],rule)
    return(c)

def calBag(cri,rule):
    c=0
    for i in rule:
        if i[0]==cri:
            e=1
            while e < len(i):
                c=c+int(i[e+1])
                c=c+calBag(i[e],rule)*int(i[e+1])
                e=e+2
    return(c)

rules=getRules("day7.txt")
t=tryRule("shiny gold",rules)
lst=list(set(t))
print(len(lst))
print(rules)
print(calBag("shiny gold",rules))