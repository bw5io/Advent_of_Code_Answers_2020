def readFile(fileName,outVar):
    file=open(fileName)
    for line in file:
        outVar.append(line.strip())
    return None


def splitFile(inVar,outVar):
    n=0
    outVar.append([])
    for line in inVar:
        if line!="":
            # print(n,line)
            outVar[n].append(line)
        if line=="":
            n+=1
            outVar.append([])
    return None

def getRules(inVar,outVar):
    for line in inVar:
        c=line.split(":")
        key = c[0]
        d=c[1].split()
        group1=d[0].split("-")
        group2=d[2].split("-")
        outVar[key]=[]
        for sn in range(int(group1[0]),int(group1[1])+1):
            outVar[key].append(sn)
        for sn in range(int(group2[0]),int(group2[1])+1):
            outVar[key].append(sn)
        # print(c,key,group1,group2,outVar[key])
    return None

def getNearbyTicket(inVar,outVar):
    for line in inVar:
        if "nearby" in line:
            continue
        outVar.append(line.split(","))
    return None

def isValid(tix,rule):
    sumN=0
    flag=0
    for d in tix:
        for num in d:
            flag=0
            # print("num:",num)
            inum=int(num)
            for i in rule.values():
                if inum in i:
                    flag=1
            if flag==0:
                sumN+=inum
                # print (inum)
    return sumN

inFile=[]
inFileSplit=[]
readFile("day16.txt",inFile)
splitFile(inFile,inFileSplit)
# print(inFileSplit)
rules, ticket, nticket = dict(), [], []
getRules(inFileSplit[0],rules)
# getMyTicket(inFileSplit[1],ticket)
# print(nticket)
getNearbyTicket(inFileSplit[2],nticket)

# print(nticket)
print(rules)
print(isValid(nticket,rules))