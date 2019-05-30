a=int(input())
b=[int(a) for a in input().split()]
s=[]
if a%2==1:
    for i in range(0,len(b)-1,2):
        if i!=len(b)-1:
            j=i+1
            b[i],b[j]=b[j],b[i]
            s.append(b[i])
            s.append(b[j])
    else:
        s.append(b[-1])
else:
    for i in range(0,len(b)-1,2):
        j=i+1 
        b[i],b[j]=b[j],b[i]
        s.append(b[i])
        s.append(b[j])
print(*s)
            
