a=int(input())
d=[]
e=1
f=1
for i in range(a):
    s=[int(a) for a in input().split()]
    d.append(s)
for i in range(a):
    e=e*d[i][i]
#print(e)
for i in range(a):
    f=f*d[i][a-i-1] 
#print(f)
print(e+f)
