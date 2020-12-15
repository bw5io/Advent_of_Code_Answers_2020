def dictadd(thedict,i,j):
    if j in thedict:
        thedict[j].append(i)
    else:
        thedict[j]=[i]
    return thedict

nums=[8,0,17,4,1,12]
count=dict()
for i,j in enumerate(nums):
    count = dictadd(count,i,j)

while len(nums)<=30000000:
    if len(count[nums[-1]])>=2:
        newnum=count[nums[-1]][-1]-count[nums[-1]][-2]
    else:
        newnum=0
    count=dictadd(count,len(nums),newnum)
    nums.append(newnum)

print(nums[2019])
print(nums[29999999])