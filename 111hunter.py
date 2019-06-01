a=int(input())
s=[]
t=[]
for i in range(a):
    d=[]
    d=[int(a) for a in input().split()]
    s.append(d)
#print(s)
dumm=sum(s[a-i-1][a-i-1] for i in range(a))
print(dumm)
    
