a,b=map(int,input().split())
c=[int(a) for a in input().split()]
lis=[]
n=[]
for i in range(0,b):
    u,v=map(int,input().split())
    lis.append(u)
    lis.append(v)
    n.append(min(lis))
for j in range(0,len(n)):
    print(n[j])
