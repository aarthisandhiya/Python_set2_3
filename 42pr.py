y,k=map(int,input().split())
l=list(map(int,input().split()))
if k==1:
    print(min(l))
elif k==2:
    print(max(l[0],l[y-1]))
else:
    print(max(l))
