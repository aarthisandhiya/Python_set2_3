x=int(input())
c=0
for i in range(0,x):
    if 2**i==x:
        c=c+1
        if c==1:
            print("yes")
            break
        break
else:
    print("no")
    
