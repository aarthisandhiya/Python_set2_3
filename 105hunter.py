a=int(input())
b=str(a)
c=len(b)
s=0
v=list(map(int,b))
for i in range(0,len(v)):
    s=s+v[i]**c
print(s)
