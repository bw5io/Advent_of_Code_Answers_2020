def getHalf(a,b):
    c=int((a+b)/2)
    return(c)

def getSeatID(line):
    lower=0
    upper=127
    lowerR=0
    upperR=7
    for sn in range(0,7):
        c=getHalf(lower,upper)
        if line[sn]=="F":
            upper=c
        else:
            lower=c+1
        # print(upper,lower)
    for sn in range(7,10):
        c=getHalf(lowerR,upperR)
        if line[sn]=="L":
            upperR=c
        else:
            lowerR=c+1
        # print(upperR,lowerR)
    seatID=lower*8+lowerR
    return(seatID)

file=open("day5.txt")
m=0
seats=[]
for line in file:
    now=getSeatID(line)
    print(line.strip(),now)
    seats.append(now)
    if now >=m:
        m=now
print(m)
seats.sort()
for i in range(min(seats),max(seats)+1):
    if i not in seats:
        print(i)
        break