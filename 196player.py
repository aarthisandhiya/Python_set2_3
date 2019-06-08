a=int(input())
b=[int(a) for a in input().split()]
c=1
lis=[]
for i in range(0,len(b)):
    if b.count(b[i])==c:
        lis.append(b[i])
print(*lis)
