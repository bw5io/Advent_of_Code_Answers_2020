file=open("test.txt")
now = file.readline()  #read timestamp from the file
buses = file.readline() #read buses from the file
buses = buses.strip().split(",")
flag = 0
timeStamp = 0
big=0
for c in range(len(buses)):
    if buses[c].isdigit():
        buses[c]=int(buses[c])
        if buses[c]>=big:
            d=c
            big=buses[c]
    else:
        buses[c]=-1
print(buses)
while flag==0:
    flag = 1
    e=buses[d]-(timeStamp%buses[d])-d
    if e==0:
        e=buses[d]
    timeStamp+=e
    # print(timeStamp,d,buses[d],(timeStamp+d)%buses[d],e)
    # print(timeStamp)
    # if (timeStamp+d) % buses[d]!=0:
    #     print(timeStamp)
    # timeStamp+=1
    for c in range(len(buses)):
        if buses[c]>=0:
            if (timeStamp+c) % buses[c]!=0:
                flag = 0
                break
                # e=buses[c]-(timeStamp%buses[c])-c
                # if e<=0:
                #     e=buses[c]
                # timeStamp+=e
                # print(timeStamp)

print(timeStamp)
for c in range(len(buses)):
    if buses[c]>0:
        print(timeStamp % buses[c],buses[c],c)