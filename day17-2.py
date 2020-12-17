import copy
import time
start = time.time()

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
    for j in range(leng):
        d.append(".")
    inVar = copy.deepcopy([d]) + inVar
    inVar= inVar + copy.deepcopy([d])
    return inVar

def plusX(inVar,lenY,lenZ):
    d=[]
    for i in range(lenZ):
        d.append([])
        for j in range(lenY):
            d[i].append(".")
    inVar = [copy.deepcopy(d)] + inVar
    inVar = inVar + [copy.deepcopy(d)]
    return inVar

def plusW(inVar,lenX,lenY,lenZ):
    d=[]
    for i in range(lenZ):
        d.append([])
        for j in range(lenY):
            d[i].append([])
            for k in range(lenX):
                d[i][j].append(".")
    inVar = [copy.deepcopy(d)] + copy.deepcopy(inVar)
    inVar=copy.deepcopy(inVar) + [copy.deepcopy(d)]
    return inVar

def suckIt(inVar):
    last_space = copy.deepcopy(inVar)
    for w in range(len(inVar)):
        for x in range(len(inVar[w])):
            for y in range(len(inVar[w][x])):
                for z in range(len(inVar[w][x][y])):
                    flag = 0
                    for pw in range(-1,2):
                        for px in range(-1,2):
                            for py in range(-1,2):
                                for pz in range(-1,2):
                                    # print(x+px,y+py,z+pz)
                                    if w+pw in range(len(inVar)) and x+px in range(len(inVar[w])) and y+py in range(len(inVar[w][x])) and z+pz in range(len(inVar[w][x][y])) and not pw==px==py==pz==0:
                                        # print(last_space[x+px][y+py][z+pz],end="")
                                        if last_space[w+pw][x+px][y+py][z+pz]=="#":
                                            flag+=1
                        # print(x,y,z,flag)
                    if last_space[w][x][y][z] == ".":
                        if flag == 3:
                            inVar[w][x][y][z] = "#"
                        else:
                            inVar[w][x][y][z] = "."
                    elif last_space[w][x][y][z] == "#":
                        if flag == 3 or flag == 2:
                            inVar[w][x][y][z] = "#"
                        else:
                            inVar[w][x][y][z] = "."
                    # print(w,x,y,z,flag,inVar[w][x][y][z])
                    # printer(inVar)
        # printer(inVar)

def printer(inVar):
    for w in range(len(inVar)):
        for x in range(len(inVar[w])):
            print(w,x,":")
            for y in range(len(inVar[w][x])):
                for z in range(len(inVar[w][x][y])):
                    print(inVar[w][x][y][z],end="")
                print("")
            print("")



threed_space=[[[]]]
readFile("day17.txt",threed_space[0][0])
for times in range(6):
    for w in range(len(threed_space)):
        for x in range(len(threed_space[w])):
            for y in range(len(threed_space[w][x])):
                threed_space[w][x][y]=plusZ(threed_space[w][x][y])
            threed_space[w][x]=plusY(threed_space[w][x],len(threed_space[w][x][0]))
        threed_space[w] = copy.deepcopy(plusX(threed_space[w],len(threed_space[w][0]),len(threed_space[w][0][0])))
    threed_space = copy.deepcopy(plusW(threed_space,len(threed_space[0][0][0]),len(threed_space[0][0]),len(threed_space[0])))
    last_space=copy.deepcopy(threed_space)
    suckIt(threed_space)
    printer(threed_space)

total = 0
for w in threed_space:
    for x in w:
        for y in x:
            for z in y:
                if z=="#":
                    total+=1
print(total)

print("Runtime:",time.time()-start)