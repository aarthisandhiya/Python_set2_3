a,b=map(str,input().split())
b=int(b)
s=[]
if len(a)==1:
    print(a)
else:
    for i in range(0,len(a),b):
        s.append(a[i])
        
    print(*s)
