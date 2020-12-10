file = open("day10.txt")
c=[]
s=[0,0,0,0]
for line in file:
    d=int(line.strip())
    c.append(d)
c.sort()
c.append(c[-1]+3)
c.append(0)
c.sort()
print(c)
for i in range(1,len(c)):
    f=c[i]-c[i-1]
    s[f]+=1
    print(c[i],c[i-1],i,f,s[f])

lian=[0,0,0,0,0,0,0,0,0,0,0,0]
flag=0
for i in range(1,len(c)):
    if c[i]-c[i-1]==1:
        flag+=1
    else:
        lian[flag]+=1
        flag=0
print (lian)