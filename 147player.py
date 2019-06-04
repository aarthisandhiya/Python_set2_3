b=input().split()
a=list(b)
if len(a)==1 or len(a)==2:
    print(*a)
else:
    print(a[0],end=" ")
    for i in range(1,len(a)-1):
        s=a[i]
        print(s[::-1],end=" ")
    print(a[-1])
