file=open("day2.txt")
total=0
for line in file:
    c=line.strip()
    c=c.split(" ")
    r=c[0].split("-")
    a=c[1].split(":")
    password=c[2]
    asn=0
    # print(r,a[0],password)
    for sn in range(len(password)):
        if password[sn]==a[0]:
            asn+=1
    if asn>=int(r[0]) and asn <= int(r[1]):
        total+=1
        print(password,asn,r[0],r[1],a)
print(total)