a=int(input())
s=[]
b=[int(a) for a in input().split()]
for i in range(0,len(b)):
    if i%2==0 and b[i]%2==1:
        s.append(b[i])
    elif i%2==1 and b[i]%2==0:
        s.append(b[i])
w=' '        
for i in range(0,len(s)):
    w=w+str(s[i])+' '
print(w.strip())

        

