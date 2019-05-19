a=int(input())
s=' '
b=[int(a) for a in input().split()]
for i in range(0,len(b)):
    for j in range(0,len(b)):
        for k in range(0,len(b)):
            if b[i]+b[j]==b[k] and i<j<k:
                print(b[i],' ',b[j],' ',b[k])
