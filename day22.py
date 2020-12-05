def isLegal(char1,char2):
    if char1==char2:
        return(1)
    return(0)
        

file=open("day2.txt")
total=0
for line in file:
    c=line.strip()
    c=c.split(" ")
    r=c[0].split("-")
    a=c[1].split(":")
    password=c[2]
    # print(password,r,a)
    flag=0
    flag+=isLegal(password[int(r[0])-1],a[0])
    flag+=isLegal(password[int(r[1])-1],a[0])
    # print(r,a[0],password)
    if flag==1:
        total+=1
        print(password,r[0],r[1],flag,a)
print(total)