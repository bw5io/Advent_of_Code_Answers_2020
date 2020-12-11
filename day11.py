def isEight(a,x,y):
    flag=dict()
    flag["#"],flag["L"],flag["."]=0,0,0
    if a[x][y]==".":
        return(".")
    if x!=0:
        flag[a[x-1][y]]+=1
        if y!=0:
            flag[a[x-1][y-1]]+=1
        if y!=len(a[x])-1:
            flag[a[x-1][y+1]]+=1
    if x!=len(a)-1:
        flag[a[x+1][y]]+=1
        if y!=0:
            flag[a[x+1][y-1]]+=1
        if y!=len(a[x])-1:
            flag[a[x+1][y+1]]+=1
    if y!=0:
        flag[a[x][y-1]]+=1
    if y!=len(a[x])-1:
        flag[a[x][y+1]]+=1
    # print (flag)
    if (a[x][y]=="L" and flag["#"]==0) or (a[x][y]=="#" and flag["#"]<4):
        return("#")
    else:
        return("L")

def goNuts(b,a):
    flag=0
    for x in range(len(a)):
        for y in range(len(a[x])):
            c=isEight(a,x,y)
            if c!=a[x][y]:
                flag+=1
            b[x][y]=c
            print(c,end='')
        # print(a)
        print("")
    print(flag)
    if flag!=0:
        goNuts(a,b)
    return(flag)

def countSeats(a):
    flag=0
    for x in a:
        for y in x:
            if y=="#":
                flag+=1
    return(flag)

file=open("day11.txt")
seats=[]
seatsb=[]
for line in file:
    seats+=[list(line.strip())]
    seatsb+=[list(line.strip())]
for line in seats:
    print (line)
count=goNuts(seats,seatsb)
# print(seats,count)
print(countSeats(seats))