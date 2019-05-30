a=int(input())
b=[int(a) for a in input().split()]
s=[]
for i in range(0,len(b)):
    if b[i] not in s:
        s.append(b[i])
print(*s)
