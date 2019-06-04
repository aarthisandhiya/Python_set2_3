w=int(input())
g=[int(w) for w in input().split()]
s=sorted(g)
k=s[::-1]
f=[]
for i in range(0,len(k)-1):
    #if k[i] not in f:
    if len(f)<len(k):
        f.append(k[i])
        for j in range(i,len(s)):
            if j <i+1:
                #if s[j] not in f:
                if len(f)<len(k):
                    f.append(s[j])
print(*f)
