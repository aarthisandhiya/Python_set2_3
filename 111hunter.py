a=int(input())
s=[]
t=[]
for i in range(a):
    d=[]
    d=[int(a) for a in input().split()]
    s.append(d)
#print(s)
dumm=sum(s[i][i] for i in range(a))
print(dumm)
    
