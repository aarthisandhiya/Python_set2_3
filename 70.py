a=int(input())
c=0
while a:
    for i in range(1,a):
        if 2**i==a:
            c=c+1
            if c==1:
                i=i+1
                print(2**i)
    else:
        a=a+1
