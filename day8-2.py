#This code is def not optimized. To be optimized later.

def getFile(C1):
    c=open(C1)
    a=[]
    for line in c:
        d=line.split()
        a.append(d)
    return(a)

def isInfinite(lijn,ina,flag):
    count=0
    point=0
    l=getFile(ina)
    tempa=[]
    if lijn!=[]:
        temp=lijn[-1]
        lijn.pop(-1)
        if l[temp][0]=="nop":
            l[temp][0]="jmp"
        else:
            l[temp][0]="nop"
    while point<=len(l)-1:
        print (l[point],point,count)
        if point not in tempa:    
            if l[point][0]=="nop":
                if flag==0:
                    lijn.append(point)
                tempa.append(point)
                point+=1
                temp=-1
            elif l[point][0]=="jmp":
                if flag==0:
                    lijn.append(point)
                tempa.append(point)
                temp=int(l[point][1])*-1
                point+=int(l[point][1])
            elif l[point][0]=="acc":
                count+=int(l[point][1])
                tempa.append(point)
                point+=1
        else:
            count=isInfinite(lijn,ina,1)
            break
    return(count)



l=getFile ("day8.txt")
l[2].append(0)
print(l)
count=isInfinite([],"day8.txt",0)
print(count)