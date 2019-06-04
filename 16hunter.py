a,b=map(int,input().split())
c=[int(a) for a in input().split()]
c=sorted(c)
for i in range(0,len(c)-1):
    if c[i]==b and i==0:
        if i<4:
            print(c[1],c[2],c[3])
            break
    elif c[i]==b and i==1:
        print(c[2],c[3],c[0])
        break
    elif c[i]==b and i>1:
        print(c[i-1],c[i+1],c[i-2])
        break
