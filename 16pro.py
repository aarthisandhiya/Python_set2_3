a=int(input())
c=0
b=[int(a) for a in input().split()]
s=sorted(b)
#print(s)
if s==b:
    rev=s[::-1]
    #print(rev)
    for i in range(len(rev)-1):
        for j in range(i+1,len(rev)):
            if rev[i]>rev[j] and j!=i:
                #print(rev[i])
                c=c+1
    else:
        if rev[-1]>rev[-2]:
            c=c+1 
else:
    for i in range(len(b)-1):
        for j in range(i+1,len(b)):
            if b[i]>b[j] and j!=i:
                #print(b[i])
                c=c+1
    else:
        if b[-1]>b[-2]:
            c=c+1 

print(c+a)  
