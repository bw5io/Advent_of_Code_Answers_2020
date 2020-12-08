def getFile(C1):
    c=open(C1)
    a=[]
    for line in c:
        d=line.split()+[0]
        a.append(d)
    return(a)

l=getFile ("day8.txt")
l[2].append(0)
print(l)
count=0
point=0
while point<=len(l)+1:
    print (l[point],point,count)
    if l[point][2]==0:    
        if l[point][0]=="nop":
            l[point][2]+=1
            point+=1
        elif l[point][0]=="jmp":
            l[point][2]+=1
            point+=int(l[point][1])
        elif l[point][0]=="acc":
            count+=int(l[point][1])
            l[point][2]+=1
            point+=1
    else:
        break

print(count)