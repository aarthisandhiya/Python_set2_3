a=int(input())
s=[]
kit=0
for i in range(2,a):
    if a%i==0:
        for j in range(2,i):
            if i%j==0:
                break 
        else:
            s.append(i)
if len(s)==0:
    print(a)
else:
    print(*s)
