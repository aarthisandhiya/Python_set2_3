a=int(input())
s=' '
b=[int(a) for a in input().split()]
for i in range(0,a-2):
    for j in range(i+1,a-1):
        for k in range(j+1,a):
            if b[i]+b[j]==b[k] and i<j<k:
                print(b[i],b[j],b[k])
                break
