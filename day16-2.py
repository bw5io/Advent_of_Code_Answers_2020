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
    for d in range(len(tix)):
        cflag=0
        for num in tix[d]:
            flag=0
            # print("num:",num)
            inum=int(num)
            for i in rule.values():
                if inum in i:
                    flag=1
            if flag==0:
                sumN+=inum
                cflag=1
                # print (inum)
        if cflag==1:
            tix[d].append("invalid")
    # print(tix)
    return sumN

def isValid2(tix,rule):
    valid=[]
    for i in range(len(tix[0])):
        valid.append([])
        for key,value in rule.items():
            if int(tix[0][i]) in value:
                valid[i].append(key)
    # print(valid)
    for i in tix:
        if "invalid" in i:
            continue
        for sn,v in enumerate(i):
            for key,value in rule.items():
                if int(v) not in value:
                    if key in valid[sn]:
                        # print(valid[sn])
                        valid[sn].remove(key)
    # print(valid)
    return valid

def cleanUp(inVar,cur):
    for i,j in enumerate(inVar):
        if len(j)==1 and i not in cur:
            cur.append(i)
            key=j[0]
            for k,l in enumerate(inVar):
                if i!=k and key in l:
                    l.remove(key)
    if len(cur)!=len(inVar):
        cleanUp(inVar,cur)
    return(inVar)

def getMyTicket(inVar):
    for i in inVar:
        print (i)
        if "your" in i:
            continue
        outVar=i.split(",")
        print(outVar)
    return(outVar)

inFile=[]
inFileSplit=[]
readFile("day16.txt",inFile)
splitFile(inFile,inFileSplit)
rules, ticket, nticket = dict(), [], []
getRules(inFileSplit[0],rules)
getNearbyTicket(inFileSplit[2],nticket)
isValid(nticket,rules)
valid=isValid2(nticket,rules)
cleanUp(valid,[])
print(valid)
outVar=getMyTicket(inFileSplit[1])
print(ticket)