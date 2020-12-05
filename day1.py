file=open("input.txt")
c=list([])

for line in file:
    c.append(int(line.strip()))
    print(c)

for i in range(len(c)):
    for j in range(i,len(c)):
        for k in range(j,len(c)):
            if c[i]+c[j]+c[k]==2020:
                print (c[i],c[j],c[k],c[i]+c[j]+c[k],c[i]*c[j]*c[k])
