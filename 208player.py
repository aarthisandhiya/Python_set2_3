a=int(input())
d=[]
for i in range(a):
    s=[int(a) for a in input().split()]
    d.append(s)
e=sum(d[i][i] for i in range(a))
#print(e)
f=sum(d[i][a-i-1] for i in range(a))
#print(f)
print(e*f)
