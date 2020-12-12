def isNegative(num):
    if num>0:
        return(1)
    if num<0:
        return(-1)


def openFile(path):
    file = open(path)
    instructions=[]
    for line in file:
        instructions.append([line[0],int(line[1:])])
    return instructions

instructs = openFile("day12.txt")
axisX=0        #east is positive, west is negative
axisY=0        #south is positive, north is negative
wayPointX=10
wayPointY=-1

for inst in instructs:
    if inst[0]=="E":
        wayPointX+=inst[1]
    if inst[0]=="S":
        wayPointY+=inst[1]
    if inst[0]=="W":
        wayPointX-=inst[1]    
    if inst[0]=="N":
        wayPointY-=inst[1]
    if inst[0]=="L" or inst[0]=="R":
        operate=inst[1]//90
        if inst[0]=="L":
            operate=-1*operate+4
        for i in range(operate):
            if wayPointX==0:
                wayPointX,wayPointY=-1*wayPointY,wayPointX   
            elif wayPointY==0:
                wayPointX,wayPointY=wayPointY,wayPointX
            else:
                flagX,flagY=isNegative(wayPointX),isNegative(wayPointY)
                if flagX*flagY>0:
                    flagX=flagX*-1
                else:
                    flagY=flagY*-1
                wayPointX, wayPointY=abs(wayPointY)*flagX,abs(wayPointX)*flagY
    if inst[0]=="F":
        axisX+=wayPointX*inst[1]
        axisY+=wayPointY*inst[1]
    print(wayPointX,wayPointY,inst,axisX,axisY)
print(axisX,axisY,abs(axisX)+abs(axisY))