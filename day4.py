file=open("day4.txt")
sumValid=0
sumInValid=0
flagByr=0
flagIyr=0
flagEyr=0
flagHgt=0
flagHcl=0
flagEcl=0
flagPid=0
flagCid=0

for line in file:
    if len(line.strip())==0:
        if flagByr==1 and  flagIyr==1 and flagEyr==1 and flagHgt==1 and flagHcl==1 and flagEcl==1 and flagPid==1:
            sumValid+=1
        else:
            sumInValid+=1
        print("New Line")
        flagByr=0
        flagIyr=0
        flagEyr=0
        flagHgt=0
        flagHcl=0
        flagEcl=0
        flagPid=0
        flagCid=0
    else:
        temp=line.split()
        tempc=[]
        for attr in temp:
            tempc.append(attr.split(":"))
        for attr in tempc:
            if attr[0]=="byr":
                if int(attr[1])>=1920 and int(attr[1])<=2002:
                    flagByr=1
            if attr[0]=="iyr":
                if int(attr[1])>=2010 and int(attr[1])<=2020:
                    flagIyr=1
            if attr[0]=="eyr":
                if int(attr[1])>=2020 and int(attr[1])<=2030:
                    flagEyr=1
            if attr[0]=="hgt":
                if attr[1].endswith("in"): 
                    len2=int(attr[1].strip("in"))
                    if int(len2)>=59 and int(len2)<=76:
                        flagHgt=1
                if attr[1].endswith("cm"):
                    len2=int(attr[1].strip("cm"))
                    if int(len2)>=150 and int(len2)<=193:
                        flagHgt=1
            if attr[0]=="hcl":
                flagHcls=0
                color=attr[1]
                if color[0]=="#":
                    if len(color)==7:
                        for no in range(1,7):
                            if color[no]>="0" and color[no]<="9" or color[no]>="a" or color[no]<="f":
                                flagHcls+=1
                                print("true")
                if flagHcls == 6:
                    flagHcl=1
            if attr[0]=="ecl":
                if attr[1]=="amb" or attr[1]=="brn" or attr[1]=="gry" or attr[1]=="grn" or attr[1]=="hzl" or attr[1]=="oth" or attr[1]=="blu":
                    flagEcl=1
            if attr[0]=="pid":
                if len(attr[1])==9:
                    flagPid=1
            if attr[0]=="cid":
                flagCid=1
        print(flagByr,flagIyr,flagEyr,flagHgt,flagHcl,flagEcl,flagPid,flagCid,line)

print(sumValid,sumInValid)