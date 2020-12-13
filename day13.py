file=open("day13.txt")
now = file.readline()  #read timestamp from the file
now = int(now.strip()) #delete /n in the end
buses = file.readline() #read buses from the file
buses = buses.strip().split(",")
busTime=dict()          
closest = now          #create a big enough temp variable
closestBus = 0
for i in buses:
    if i.isdigit()==True:
        thisBusTime = int(i)-now%int(i)
        busTime[i]=thisBusTime
        if thisBusTime < closest:
            closest = thisBusTime
            closestBus = int(i)
print(closestBus * closest)