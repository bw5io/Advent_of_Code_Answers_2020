def toBinary(num):
    bnum=""
    while num>=1:
        bnum=str(num%2)+bnum
        num=num//2
    if len(bnum)<36:
        bnum="0"*(36-len(bnum))+bnum
    return(bnum)

def toDecimal(num):
    dnum=0
    for c in range(len(num)):
        dnum+=int(num[c])*(2**(len(num)-c-1))
    return(dnum)

def getMask(num,mask):
    bnum=list(toBinary(num))
    # print(bnum,len(bnum))
    # print(mask,len(mask))
    for c in range(len(mask)):
        if mask[c] != "X":
            bnum[c]=mask[c]
    return(toDecimal(bnum))


mask=""
mem={}

file = open ("day14.txt")
for line in file:
    tline = line.strip().split("=")
    if tline[0]=="mask ":
        mask=tline[1].strip()
        # print(mask)
    if "mem" in tline[0]:
        mem[tline[0][3:].strip()]=(getMask(int(tline[1].strip()),mask))
sumNum = 0
for c in mem.values():
    # print(c)
    sumNum+=c
print(sumNum)
