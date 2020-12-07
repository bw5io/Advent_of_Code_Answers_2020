file=open("day6.txt")
c=""
sum=0

for line in file:
    if line.strip()=="":
        sum=sum+len(c)
        print(len(c),sum,c)
        c=""
    temp = line.strip()
    temp=temp.lower()
    for i in temp:
        if i not in c:
            c=c+i

if c!="":
        sum=sum+len(c)
        print(len(c),sum,c)
        c=""
print(sum)