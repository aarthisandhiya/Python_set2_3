a,b=map(str,input().split())
b=int(b)
s=[]
if len(a)==1:
    print(a)
else:
    for i in range(0,len(a)):
        if i%2==1:
            s.append(a[i])
        
    print(*s)
