a=int(input())
if a==2:
    print(0)
for i in range(2,a):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
