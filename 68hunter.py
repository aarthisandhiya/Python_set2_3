a=int(input())
b=[int(a) for a in input().split()]
for i in range(0,len(b)):
    minn=b[0]
    if minn>b[i]:
        minn=b[i]
for j in range(0,len(b)):
    maxx=b[0]
    if maxx<b[i]:
        maxx=b[i]
#print(minn)
#print(maxx)
for i in range(0,len(b)):
    if minn==b[i]:
        print(i+1,end=" ")
    elif maxx==b[i]:
        print(i+1,end=" ")
    
