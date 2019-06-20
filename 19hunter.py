a=int(input())
s=[]
kit=0
for i in range(2,a):
    for j in range(2,i):
        if i%j!=0:
            kit=0
    else:
        kit=kit+1
if kit==0:
    print(a)
elif kit>0:
    for i in range(2,a):
        if a%i==0:
            for j in range(2,i):
                if i%j==0:
                    break 
            else:
                s.append(i)
    print(*s)


