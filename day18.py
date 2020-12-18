def readFile(fileName,outVar):
    file=open(fileName)
    for line in file:
        outVar.append(list(line.strip().replace(" ","")))
    return None

def solve(inVar,start):
    c=start
    while c<len(inVar):
        if inVar[c] == "(":
            solve(inVar,c+1)
        elif inVar[c] == ")":
            inVar.pop(start-1)
            return(calculate(inVar,start-1))
        c+=1
    answer=calculate(inVar,0)
    return answer

def calculate(inVar,n):
    while len(inVar)!=1 and inVar[n+1]!=")":
        c=""
        c=str(inVar[n]+inVar[n+1]+inVar[n+2])
        inVar.pop(n)
        inVar.pop(n)
        inVar[n]=str(eval(c))
    if n+1 < len(inVar):
        if inVar[n+1]==")":
            inVar.pop(n+1)
    return inVar[0]

challenges=[]
readFile("day18.txt",challenges)
sumc=0
for line in challenges:
    print (solve(line,0))
    sumc = int(line[0])+sumc
print(sumc)