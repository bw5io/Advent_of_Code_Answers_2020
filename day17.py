import copy

def readFile(fileName,outVar):
    file=open(fileName)
    for line in file:
        outVar.append(list(line.strip()))
    return None

def plusZ(inVar):
    inVar = ["."] + copy.deepcopy(inVar) + ["."]
    return inVar

def plusY(inVar, leng):
    d=[]
    for i in range(leng):
        d.append(".")
    inVar = [copy.deepcopy(d)] + copy.deepcopy(inVar) + [copy.deepcopy(d)]
    return inVar

def plusX(inVar,lenY,lenZ):
    d=[]
    for i in range(lenZ):
        d.append([])
        for j in range(lenY):
            d[i].append(".")
    inVar = [copy.deepcopy(d)] + copy.deepcopy(inVar)
    inVar=copy.deepcopy(inVar) + [copy.deepcopy(d)]
    return inVar

def suckIt(inVar):
    last_space = copy.deepcopy(inVar)
    for x in range(len(inVar)):
        for y in range(len(inVar[x])):
            for z in range(len(inVar[x][y])):
                flag = 0
                for px in range(-1,2):
                    for py in range(-1,2):
                        for pz in range(-1,2):
                            # print(x+px,y+py,z+pz)
                            if x+px in range(len(inVar)) and y+py in range(len(inVar[x])) and z+pz in range(len(inVar[x][y])) and not px==py==pz==0:
                                # print(last_space[x+px][y+py][z+pz],end="")
                                if last_space[x+px][y+py][z+pz]=="#":
                                    flag+=1
                # print(x,y,z,flag)
                if last_space[x][y][z] == ".":
                    if flag == 3:
                        inVar[x][y][z] = "#"
                    else:
                        inVar[x][y][z] = "."
                elif last_space[x][y][z] == "#":
                    if flag == 3 or flag == 2:
                        inVar[x][y][z] = "#"
                    else:
                        inVar[x][y][z] = "."
                # print(x,y,z,flag,inVar[x][y][z])
                # printer(inVar)
        # printer(inVar)

def printer(inVar):
    for x in range(len(inVar)):
        print(x,":")
        for y in range(len(inVar[x])):
            for z in range(len(inVar[x][y])):
                print(inVar[x][y][z],end="")
            print("")
        print("")



threed_space=[[]]
readFile("day17.txt",threed_space[0])
printer(threed_space)
for times in range(6):
    print(times)
    for x in range(len(threed_space)):
        for y in range(len(threed_space[x])):
            threed_space[x][y]=plusZ(threed_space[x][y])
        threed_space[x]=plusY(threed_space[x],len(threed_space[x][0]))
    threed_space = copy.deepcopy(plusX(threed_space,len(threed_space[0]),len(threed_space[0][0])))
    last_space=copy.copy(threed_space)
    suckIt(threed_space)
    printer(threed_space)

total = 0
for x in threed_space:
    for y in x:
        for z in y:
            if z=="#":
                total+=1
print(total)