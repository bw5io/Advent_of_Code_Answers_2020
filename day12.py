def openFile(path):
    file = open(path)
    instructions=[]
    for line in file:
        instructions.append([line[0],int(line[1:])])
    return instructions

instructs = openFile("day12.txt")
axisX=0        #east is positive, west is negative
axisY=0        #south is positive, north is negative
direction=0 #east is 0 south is 90 west is 180 north is 270
for inst in instructs:
    if inst[0]=="E":
        axisX+=inst[1]
    if inst[0]=="S":
        axisY+=inst[1]
    if inst[0]=="W":
        axisX-=inst[1]    
    if inst[0]=="N":
        axisY-=inst[1]
    if inst[0]=="L":
        direction-=inst[1]
        if direction < 0:
            direction+=360
    if inst[0]=="R":
        direction+=inst[1]
        if direction >= 360:
            direction-=360
    if inst[0]=="F":
        navi=direction/90
        if navi == 0:
            axisX+=inst[1]
        if navi == 1:
            axisY+=inst[1]
        if navi == 2:
            axisX-=inst[1]
        if navi == 3:
            axisY-=inst[1]
    print(axisX,axisY,inst[0],inst[1],direction/90)
print(axisX,axisY,abs(axisX)+abs(axisY))