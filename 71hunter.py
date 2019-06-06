a,v=map(int,input().split())
k=[]
s=[int(a) for a in input().split()]
s=s[::-1]
for i in range(0,v):
    k.append(s[i])
    #print(k)
k=k[::-1]
print(*k)
    
