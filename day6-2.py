file=open("day6.txt")
c=""
ci=""
sum=0
flag=0

for line in file:
    if line.strip()=="":
        sum=sum+len(ci)
        print(len(ci),sum,ci)
        ci=""
        c=""
        flag=0
    else:
        temp = line.strip()
        temp=temp.lower()
        if flag == 0:
            for i in temp:
                if i not in c:
                    c=c+i
            ci=c
            flag=1
        else:
            c=""
            for i in temp:
                if i in ci and i not in c:
                    c=c+i
            ci=c

            

if ci!="":
        sum=sum+len(ci)
        print(len(ci),sum,ci)
print(sum)