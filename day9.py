def isLegal(number,asset):
    print(asset)
    for a in range(len(asset)-1):
        for b in range(a+1,len(asset)):
            if asset[a]+asset[b]==number and asset[a]!=asset[b]:
                return(True)
    return(False)

def isLegal2(number,asset):
    print(asset)
    for a in range(len(asset)):
        for b in range(a):
            for c in (range(len(asset)-a)):
                dsum=0
                nums=[]
                for d in range(b):
                    v=int(asset[c+d])
                    dsum+=v
                    nums.append(v)
                if dsum==number:
                    return(nums)
                # print(nums,dsum)
            

file=open("day9.txt")
c=[] #number collection
fake=[]
for line in file:
    if len(c)>=25:
        if isLegal(int(line.strip()),c[len(c)-25:len(c)])==False:
            print(c)
            print(line,"False")
            anotherc=isLegal2(int(line.strip()),c)
            anotherc.sort()
            print(anotherc)
            print(anotherc[-1]+anotherc[0],anotherc[0],anotherc[-1])
            break
    c.append(int(line.strip()))
    print (c[-1],len(c))
