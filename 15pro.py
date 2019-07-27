a=int(input())
c=[int(a) for a in input().split()]
s=sorted(c)
d=s[::-1]
for i in range(0,len(d)):
    print(d[i])
