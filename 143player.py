a=int(input())
b=[int(a) for a in input().split()]
c=[int(a) for a in input().split()]

for i in range(0,len(c)):
    d=min(c)
    for l in range(0,len(c)):
        if d==c[l]:
            e=l
    for j in range(0,len(b)):
        if j==e:
            #print(j)
            print(j+1,end=" ")
    c.remove(d)
            






