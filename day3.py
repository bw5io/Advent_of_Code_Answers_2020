def goSlope(file,arrow,lines):
    point=0
    encounter=0
    flag=lines
    file.seek(0)
    for line in file:
        if flag == lines:
            flag=0
            c=line.strip()
            if point>=len(c):
                point = point - len(c)
            if line[point]=="#":
                encounter+=1
            point+=arrow
        print(line,point,encounter,flag)
        flag+=1
    return(encounter)

file=open("day3.txt")
c=1
c*=goSlope(file,3,1)
c*=goSlope(file,1,1)
c*=goSlope(file,5,1)
c*=goSlope(file,7,1)
c*=goSlope(file,1,2)
print(c)
# print(goSlope(file,3,1))
# print(goSlope(file,5,1))
# print(goSlope(file,7,1))
# print(goSlope(file,1,1))
# print(goSlope(file,1,2))