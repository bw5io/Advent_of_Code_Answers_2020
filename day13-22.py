import math
file=open("test.txt")
now = file.readline()  #read timestamp from the file
buses = file.readline() #read buses from the file
buses = buses.strip().split(",")
flag = 0
timeStamp =0
big=0
step=1
for c in range(len(buses)):
    if buses[c].isdigit():
        buses[c]=int(buses[c])
        step=step*buses[c]//math.gcd(step,buses[c])
    else:
        buses[c]=-1
print(buses,timeStamp)
timeStamp=buses[0]
while flag==0:
    flag = 1
    timeStamp+=step
    print(timeStamp,step)
    for c in range(len(buses)):
        if buses[c]>=0:
            if (timeStamp+c) % buses[c]!=0:
                flag = 0
                break
print(timeStamp)
