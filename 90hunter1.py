a=input()
s=[]
c=0
for i in range(0,len(a)):
    s.append(a.count(a[i]))
d=list(a)
for i in range(0,len(d)):
    f=d.count(d[i])
    if f>c:
        c=f 
        e=d[i]
print(e,c)
    
